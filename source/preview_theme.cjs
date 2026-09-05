const fs = require('fs');
const path = require('path');
const { Liquid } = require('/tmp/bea-theme-check/node_modules/liquidjs');

const root = path.resolve(__dirname, '..');
const dir = path.join(root, 'output/shopify/bea-theme');
const out = path.join(root, 'output/store-preview');
fs.mkdirSync(out, { recursive: true });

// Copy all assets
fs.cpSync(path.join(dir, 'assets'), path.join(out, 'assets'), { recursive: true });

const engine = new Liquid({
  root: [path.join(dir, 'layout'), path.join(dir, 'sections'), path.join(dir, 'snippets')],
  extname: '.liquid',
  strictFilters: false,
  strictVariables: false
});

engine.registerFilter('asset_url', v => '/assets/' + v);
engine.registerFilter('stylesheet_tag', v => `<link rel="stylesheet" href="${v}">`);
engine.registerFilter('script_tag', v => `<script src="${v}"></script>`);
engine.registerFilter('money_with_currency', v => '$' + (v / 100).toFixed(2) + ' USD');
engine.registerFilter('money', v => '$' + (v / 100).toFixed(2));
engine.registerFilter('structured_data', v => JSON.stringify({ '@context': 'https://schema.org', '@type': 'Product', name: v.title }));
engine.registerFilter('default_errors', () => '');
engine.registerFilter('default_pagination', () => '');

function expandTags(content) {
  // Remove schema blocks
  let s = content.replace(/{% schema %}[\s\S]*?{% endschema %}/g, '');
  
  // Replace sections
  s = s.replace(/{% section '([^']+)' %}/g, (m, name) => {
    const f = path.join(dir, 'sections', name + '.liquid');
    if (fs.existsSync(f)) {
      return expandTags(fs.readFileSync(f, 'utf8'));
    }
    return '';
  });

  // Replace snippets
  s = s.replace(/{% render '([^']+)'(?:,\s*[^%]*)?%}/g, (m, name) => {
    const f = path.join(dir, 'snippets', name + '.liquid');
    if (fs.existsSync(f)) {
      return expandTags(fs.readFileSync(f, 'utf8'));
    }
    return '';
  });

  // Replace forms
  s = s.replace(/{% form [^%]*%}/g, '<form data-preview-form>');
  s = s.replace(/{% endform %}/g, '</form>');
  s = s.replace(/{%[-\s]*paginate[\s\S]*?%}/g, '');
  s = s.replace(/{%[-\s]*endpaginate[\s\S]*?%}/g, '');

  return s;
}

const mockProduct = {
  id: 15973890589003,
  title: "Bea's Calm-Alone Kit",
  url: '/product.html',
  price: 2900,
  compare_at_price: 3900,
  available: true,
  has_only_default_variant: true,
  selected_or_first_available_variant: { id: 1, price: 2900, available: true },
  variants: [{ id: 1, price: 2900, available: true, title: 'Complete Kit' }],
  description: '<p>A thoughtful guide and workbook for the small steps around alone time.</p><ul><li>16-page practical guide</li><li>5-page workbook with 25 fillable fields</li><li>One-page quick reference</li></ul><p>3 English PDF files, 22 pages in total. Owner-created educational support, not a personalised treatment plan.</p>'
};

const mockCart = {
  item_count: 1,
  total_price: 2900,
  items: [
    {
      product: mockProduct,
      title: "Bea's Calm-Alone Kit",
      image: '/assets/guide-cover.png',
      final_price: 2900,
      final_line_price: 2900,
      quantity: 1,
      variant: { title: 'Digital Edition' }
    }
  ]
};

const ctx = {
  shop: { name: 'Bea & Co.', policies: [], url: 'https://bea-co.it' },
  settings: { color_bg: '#F8F5EE', color_ink: '#1C2B25', color_caramel: '#9E5B32', enable_cart_drawer: true },
  section: {
    settings: {
      show_announcement: true,
      text: "✦ Launch edition: Instant download includes all 3 digital PDFs & 25 interactive fields.",
      link_text: "Explore the Kit →",
      link_url: "#the-kit",
      eyebrow: "FOR THE DOG YOU LOVE. AND THE LIFE YOU SHARE.",
      title: "Small steps.<br>A little more<br><em>peace of mind.</em>",
      description: "When alone time feels difficult, knowing what to notice is a place to start. A thoughtful, practical guide and fillable workbook created for you and your dog.",
      cta_text: "Meet your calm-alone kit",
      cta_url: "#the-kit",
      product: mockProduct
    },
    blocks: []
  },
  all_products: { 'beas-calm-alone-kit': mockProduct },
  product: mockProduct,
  cart: mockCart,
  routes: { root_url: '/', cart_url: '/cart.html', cart_change_url: '/cart' },
  request: { locale: { iso_code: 'en' }, page_type: 'index' },
  content_for_header: '',
  page_title: 'Bea & Co. | Small steps. Thoughtful care.',
  page_description: 'A thoughtful guide and fillable workbook for the small steps around alone time. Meet Bea & Co.',
  canonical_url: 'https://bea-co.it'
};

async function buildPreview() {
  console.log('Rendering preview pages with Liquid engine...');

  // 1. Index / Homepage
  const indexJson = JSON.parse(fs.readFileSync(path.join(dir, 'templates/index.json'), 'utf8'));
  let indexSectionsHtml = '';
  for (const key of indexJson.order) {
    const secType = indexJson.sections[key].type;
    const secFile = path.join(dir, 'sections', secType + '.liquid');
    if (fs.existsSync(secFile)) {
      const rawSec = fs.readFileSync(secFile, 'utf8');
      indexSectionsHtml += await engine.parseAndRender(expandTags(rawSec), ctx);
    }
  }

  ctx.content_for_layout = indexSectionsHtml;
  ctx.request.page_type = 'index';
  let layoutHtml = await engine.parseAndRender(expandTags(fs.readFileSync(path.join(dir, 'layout/theme.liquid'), 'utf8')), ctx);
  layoutHtml = layoutHtml.replace('<body>', '<body><div style="text-align:center;background:#1C2B25;color:#F8F5EE;padding:8px;font-size:12px;letter-spacing:0.04em;">✦ ANTEPRIMA TEMA PREMIUM BEA & CO. (ONLINE STORE 2.0) · Design boutique & conversion-ready</div>');
  fs.writeFileSync(path.join(out, 'index.html'), layoutHtml);

  // 2. Product Page
  ctx.request.page_type = 'product';
  const productSecFile = path.join(dir, 'sections/featured-product.liquid');
  const breakdownSecFile = path.join(dir, 'sections/kit-breakdown.liquid');
  const stepsSecFile = path.join(dir, 'sections/steps-process.liquid');
  const testSecFile = path.join(dir, 'sections/testimonials.liquid');
  const faqSecFile = path.join(dir, 'sections/faq-accordion.liquid');

  let prodContent = await engine.parseAndRender(expandTags(fs.readFileSync(productSecFile, 'utf8')), ctx);
  prodContent += await engine.parseAndRender(expandTags(fs.readFileSync(breakdownSecFile, 'utf8')), ctx);
  prodContent += await engine.parseAndRender(expandTags(fs.readFileSync(stepsSecFile, 'utf8')), ctx);
  prodContent += await engine.parseAndRender(expandTags(fs.readFileSync(testSecFile, 'utf8')), ctx);
  prodContent += await engine.parseAndRender(expandTags(fs.readFileSync(faqSecFile, 'utf8')), ctx);

  ctx.content_for_layout = prodContent;
  let prodLayout = await engine.parseAndRender(expandTags(fs.readFileSync(path.join(dir, 'layout/theme.liquid'), 'utf8')), ctx);
  prodLayout = prodLayout.replace('<body>', '<body><div style="text-align:center;background:#1C2B25;color:#F8F5EE;padding:8px;font-size:12px;letter-spacing:0.04em;">✦ ANTEPRIMA TEMA PREMIUM BEA & CO. (ONLINE STORE 2.0) · Scheda Prodotto Premium</div>');
  fs.writeFileSync(path.join(out, 'product.html'), prodLayout);

  // 3. Cart Page
  ctx.request.page_type = 'cart';
  const cartSec = fs.readFileSync(path.join(dir, 'sections/main-cart.liquid'), 'utf8');
  ctx.content_for_layout = await engine.parseAndRender(expandTags(cartSec), ctx);
  let cartLayout = await engine.parseAndRender(expandTags(fs.readFileSync(path.join(dir, 'layout/theme.liquid'), 'utf8')), ctx);
  cartLayout = cartLayout.replace('<body>', '<body><div style="text-align:center;background:#1C2B25;color:#F8F5EE;padding:8px;font-size:12px;letter-spacing:0.04em;">✦ ANTEPRIMA TEMA PREMIUM BEA & CO. (ONLINE STORE 2.0) · Pagina Carrello</div>');
  fs.writeFileSync(path.join(out, 'cart.html'), cartLayout);

  console.log('✓ Successfully rendered index.html, product.html, and cart.html in output/store-preview');

  // Syntax check all liquid files
  let count = 0;
  for (const d of ['sections', 'snippets', 'templates', 'layout']) {
    const fullDir = path.join(dir, d);
    if (!fs.existsSync(fullDir)) continue;
    for (const f of fs.readdirSync(fullDir)) {
      if (f.endsWith('.liquid')) {
        engine.parse(expandTags(fs.readFileSync(path.join(fullDir, f), 'utf8')));
        count++;
      }
    }
  }
  console.log(`✓ Liquid syntax checked: ${count} liquid files validated without errors.`);
}

buildPreview().catch(err => {
  console.error('Error generating preview:', err);
  process.exit(1);
});
