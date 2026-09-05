# Bea & Co. — Premium Shopify Theme (Online Store 2.0)

> **A quiet-luxury, high-converting Shopify OS 2.0 theme crafted for digital educational products and gentle companion care.**

Live Store: [https://bea-co.it](https://bea-co.it)  
Store Product: [Bea's Calm-Alone Kit](https://bea-co.it/products/beas-calm-alone-kit)

---

## ✦ Overview

**Bea & Co. Premium** is an Online Store 2.0 boutique theme engineered for digital creators, educators, and pet care brands. Built from the ground up to reflect a warm, organic "quiet luxury" aesthetic (`#F8F5EE` cream, `#1C2B25` deep forest ink, `#9E5B32` warm caramel, and `#DDE5D7` soft sage), it combines editorial typography (*Cormorant Garamond* & *Plus Jakarta Sans*) with modern e-commerce conversion mechanisms.

---

## ✦ Key Features

### 1. Online Store 2.0 Architecture ("Sections Everywhere")
- Fully modular JSON templates (`index.json`, `product.json`, `cart.json`, `page.json`, `collection.json`, `404.liquid`, `search.liquid`).
- Every homepage and product page section can be reordered, duplicated, customized, or hidden directly within the **Shopify Theme Customizer**.
- Rich schema presets for easy one-click setup.

### 2. High-Converting E-Commerce Components
- **Slide-out Ajax Cart Drawer**:
  - Instant slide-out animation with backdrop blur.
  - Interactive quantity steppers and one-click item removal.
  - Dynamic free shipping / digital bonus progress meter.
  - Direct checkout button bypass.
- **Sticky Add-to-Cart Bar**:
  - Automatically slides in when the user scrolls past the main buy button.
  - Keeps purchase intent visible on both mobile and desktop.
- **Featured Product Showcase**:
  - Dual product art composite (Guide cover + angled fillable worksheet preview).
  - Launch pricing display ($29 USD vs $39 compare-at price) with "Save $10" badge.
  - 5-Star verified rating badge.
  - Trust guarantee grid (Instant Delivery, 25 Fillable Fields, SSL Protection, Lifetime Access).
  - Collapsible accordion tabs for delivery details, fillable PDF guide, and veterinary disclaimer.

### 3. Editorial & Storytelling Sections
- **Hero Banner**: Architectural arched portrait frame with rotating badge (*"Meet Bea. Made with dogs in mind ✦"*), editorial headline with italic accents, and sample preview button.
- **Values Marquee / Ticker**: Infinite trust strip highlighting ethical boundaries, fillable features, and calm pace.
- **Inside the Kit (3 Pillars)**: Deep-dive visual cards highlighting the 16-page guide, the 5-page interactive workbook (25 form fields), and the 1-page quick reference sheet.
- **Gentle 3-Step Rhythm**: *"Read. Notice. Reflect."* structured framework.
- **Editorial Brand Story ("Meet Bea")**: Large companion portrait, authentic founder story, and handwritten signature.
- **Community Testimonials**: Customer review cards with 5-star ratings, dog breed tags, and verified buyer badges.
- **FAQ Accordion**: Native accessible `<details>` accordions with smooth animations.
- **Contact & Support Form**: Clean dual-column layout with status alerts.

### 4. Customizer Settings & Global Design System
- **Brand Colors**: Customizable background, text, and accent colors via `config/settings_schema.json`.
- **Drawer Cart Toggle**: Switch between Slide-out Drawer Cart and standard Cart Page with a single toggle.
- **Multilingual / Locales**: Complete localized dictionary strings in `locales/en.default.json` and `locales/it.json`.

---

## ✦ Repository Structure

```
├── output/
│   ├── shopify/
│   │   ├── Bea-Calm-Shopify.zip      # 📦 Production-ready theme zip for Shopify upload
│   │   ├── bea-theme/                # Unpacked theme directory (Online Store 2.0)
│   │   │   ├── assets/               # CSS, JS, images, PDF sample
│   │   │   ├── config/               # settings_schema.json & settings_data.json
│   │   │   ├── layout/               # theme.liquid
│   │   │   ├── locales/              # en.default.json & it.json
│   │   │   ├── sections/             # Modular OS 2.0 sections
│   │   │   ├── snippets/             # UI components, icons, badges, cart drawer
│   │   │   └── templates/            # JSON & Liquid page templates
│   │   ├── INSTALLAZIONE.md          # Italian setup notes & live store audit
│   │   └── ISTRUZIONI.md             # Merchant instructions
│   ├── store-preview/                # Static HTML preview (index, product, cart)
│   ├── pdf/                          # Master product PDFs (Guide, Workbook, Quick Ref)
│   └── brand/                        # Brand assets & original photography
├── source/
│   ├── build_premium_theme.py        # Python build script for OS 2.0 theme
│   ├── preview_theme.cjs             # LiquidJS preview builder & syntax validator
│   ├── build_product.py              # PDF generator script
│   └── guide-content.json            # Content model
└── README.md
```

---

## ✦ Installation Guide (Shopify Admin)

1. Log in to your **Shopify Admin** (e.g. `https://admin.shopify.com/store/u21aen-nm`).
2. Navigate to **Online Store > Themes** (`Canali di vendita > Negozio online > Temi`).
3. Under **Theme library** (*Libreria dei temi*), click **Add theme > Upload zip file** (*Aggiungi tema > Carica file zip*).
4. Select the file:
   ```
   output/shopify/Bea-Calm-Shopify.zip
   ```
5. Click **Upload file**.
6. Once uploaded, click **Customize** (*Personalizza*) to adjust colors, announcements, or section order.
7. When ready, click **Publish** (*Pubblica*).

---

## ✦ Local Development & Validation

To re-build the theme, validate Liquid syntax, and regenerate the local browser preview:

```bash
# Generate theme files and package zip
python3 source/build_premium_theme.py

# Validate all Liquid files and compile preview HTML
node source/preview_theme.cjs

# Serve local preview
npx serve output/store-preview -p 8768
```

---

## ✦ License & Ownership

© 2026 **Bea & Co.** All rights reserved.  
Owner-created educational companion care.
