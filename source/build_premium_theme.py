#!/usr/bin/env python3
"""
Build script for Bea & Co. Premium Shopify Theme (Online Store 2.0)
Generates complete, modular, high-converting Liquid files, JSON templates,
schemas, assets, and Shopify zip package.
"""

from pathlib import Path
import json, shutil, zipfile, os

ROOT = Path(__file__).resolve().parent.parent
THEME_DIR = ROOT / 'output/shopify/bea-theme'
PREVIEW_DIR = ROOT / 'output/store-preview'

# Ensure directories exist
for sub in ['assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates']:
    (THEME_DIR / sub).mkdir(parents=True, exist_ok=True)

def write_file(rel_path, content):
    p = THEME_DIR / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.strip() + '\n', encoding='utf-8')

def write_json(rel_path, data):
    p = THEME_DIR / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

print("Generating Bea & Co. Premium Theme files...")

# ==========================================
# 1. ASSETS: Images & PDFs
# ==========================================
shutil.copy(ROOT / 'output/brand/bea-original.jpg', THEME_DIR / 'assets/bea.jpg')
shutil.copy(ROOT / 'tmp/pdfs/guide-01.png', THEME_DIR / 'assets/guide-cover.png')
shutil.copy(ROOT / 'tmp/pdfs/final-workbook-3.png', THEME_DIR / 'assets/workbook-preview.png')
shutil.copy(ROOT / 'output/brand/guide-preview.pdf', THEME_DIR / 'assets/guide-preview.pdf')

# ==========================================
# 2. ASSETS: CSS (Modern Luxury Boutique)
# ==========================================
THEME_CSS = """/*
 * Bea & Co. - Premium Boutique Shopify Theme
 * Quiet Luxury Aesthetic for Thoughtful Dog Guardians
 */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

:root {
  --font-serif: 'Cormorant Garamond', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  
  --color-bg: #F8F5EE;
  --color-bg-subtle: #F1EAE0;
  --color-surface: #FFFFFF;
  --color-ink: #1C2B25;
  --color-ink-muted: #53625B;
  --color-ink-light: #7E8D86;
  --color-sage: #DDE5D7;
  --color-sage-light: #EBF1E7;
  --color-caramel: #9E5B32;
  --color-caramel-hover: #7E4523;
  --color-gold: #C28B52;
  --color-gold-light: #F7EBDD;
  --color-border: #E2DDD3;
  --color-border-dark: #C5BCAD;
  
  --shadow-sm: 0 2px 8px rgba(28, 43, 37, 0.04);
  --shadow-md: 0 8px 24px rgba(28, 43, 37, 0.08);
  --shadow-lg: 0 16px 40px rgba(28, 43, 37, 0.12);
  --shadow-hover: 0 20px 48px rgba(28, 43, 37, 0.15);
  
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-pill: 9999px;
  
  --container-max: 1200px;
  --container-pad: clamp(20px, 4vw, 48px);
  --transition-base: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  scroll-padding-top: 80px;
  -webkit-text-size-adjust: 100%;
}

body {
  background-color: var(--color-bg);
  color: var(--color-ink);
  font-family: var(--font-sans);
  font-size: 16px;
  line-height: 1.65;
  letter-spacing: -0.01em;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

/* Typography */
h1, h2, h3, h4, .serif-font {
  font-family: var(--font-serif);
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.03em;
  color: var(--color-ink);
}

h1 {
  font-size: clamp(42px, 5.5vw, 76px);
}

h2 {
  font-size: clamp(32px, 4vw, 52px);
}

h3 {
  font-size: clamp(24px, 2.5vw, 32px);
}

em, .italic-accent {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 400;
  color: var(--color-caramel);
}

p {
  line-height: 1.7;
}

p + p {
  margin-top: 1.25rem;
}

a {
  color: inherit;
  text-decoration: none;
  transition: var(--transition-base);
}

img {
  max-width: 100%;
  height: auto;
  display: block;
}

button, input, select, textarea {
  font: inherit;
  color: inherit;
}

button {
  border: none;
  background: none;
  cursor: pointer;
}

/* Accessibility Focus */
:focus-visible {
  outline: 2px solid var(--color-caramel);
  outline-offset: 4px;
}

.skip-link {
  position: absolute;
  top: -100px;
  left: 20px;
  background: var(--color-ink);
  color: var(--color-bg);
  padding: 12px 20px;
  z-index: 9999;
  font-weight: 600;
  border-radius: var(--radius-sm);
  transition: top 0.2s;
}
.skip-link:focus {
  top: 20px;
}

/* Layout Utilities */
.container {
  width: 100%;
  max-width: var(--container-max);
  margin-inline: auto;
  padding-inline: var(--container-pad);
}

.section-space {
  padding-block: clamp(60px, 8vw, 110px);
}

.section-space-sm {
  padding-block: clamp(40px, 5vw, 70px);
}

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--color-caramel);
  margin-bottom: 18px;
}

.eyebrow::before {
  content: '';
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-caramel);
}

.lead-text {
  font-size: clamp(17px, 1.4vw, 20px);
  line-height: 1.7;
  color: var(--color-ink-muted);
  max-width: 540px;
}

/* Luxury Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  padding: 16px 32px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.02em;
  border-radius: var(--radius-pill);
  transition: var(--transition-base);
  text-decoration: none;
  cursor: pointer;
  box-shadow: var(--shadow-sm);
  position: relative;
  overflow: hidden;
}

.btn-primary {
  background-color: var(--color-ink);
  color: var(--color-bg);
  border: 1px solid var(--color-ink);
}

.btn-primary:hover {
  background-color: #2F433A;
  border-color: #2F433A;
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-secondary {
  background-color: transparent;
  color: var(--color-ink);
  border: 1.5px solid var(--color-ink);
}

.btn-secondary:hover {
  background-color: var(--color-ink);
  color: var(--color-bg);
  transform: translateY(-2px);
}

.btn-caramel {
  background-color: var(--color-caramel);
  color: #FFFFFF;
  border: 1px solid var(--color-caramel);
}

.btn-caramel:hover {
  background-color: var(--color-caramel-hover);
  border-color: var(--color-caramel-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}

.btn-full {
  width: 100%;
}

.btn svg {
  width: 16px;
  height: 16px;
  transition: transform 0.2s;
}

.btn:hover svg {
  transform: translateX(3px);
}

.text-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: var(--color-ink);
  border-bottom: 1.5px solid var(--color-caramel);
  padding-bottom: 2px;
  transition: var(--transition-base);
}

.text-btn:hover {
  color: var(--color-caramel);
  border-bottom-color: var(--color-ink);
}

/* Badges & Pills */
.pill-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background: var(--color-sage);
  color: var(--color-ink);
  font-size: 12px;
  font-weight: 600;
  border-radius: var(--radius-pill);
}

.pill-badge-gold {
  background: var(--color-gold-light);
  color: var(--color-caramel);
}

/* ==========================================
   HEADER & ANNOUNCEMENT BAR
   ========================================== */
.announcement-bar {
  background-color: var(--color-ink);
  color: var(--color-bg);
  font-size: 12px;
  font-weight: 500;
  letter-spacing: 0.05em;
  padding: 10px var(--container-pad);
  text-align: center;
  position: relative;
  z-index: 100;
}

.announcement-bar a {
  color: var(--color-gold-light);
  text-decoration: underline;
  margin-left: 8px;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 90;
  background: rgba(248, 245, 238, 0.92);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--color-border);
  transition: var(--transition-base);
}

.header-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}

.brand-logo {
  font-family: var(--font-serif);
  font-size: 34px;
  font-weight: 600;
  letter-spacing: -0.04em;
  color: var(--color-ink);
  display: flex;
  align-items: baseline;
}

.brand-logo span {
  color: var(--color-caramel);
  font-style: italic;
  font-weight: 400;
  margin-inline: 2px;
}

.brand-logo .dot {
  display: inline-block;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-caramel);
  margin-left: 2px;
}

.main-nav {
  display: flex;
  align-items: center;
  gap: 36px;
}

.main-nav a {
  font-size: 14px;
  font-weight: 500;
  color: var(--color-ink);
  position: relative;
  padding-block: 6px;
}

.main-nav a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 1.5px;
  background: var(--color-caramel);
  transition: width 0.25s ease;
}

.main-nav a:hover::after {
  width: 100%;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.cart-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 18px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 600;
  color: var(--color-ink);
  cursor: pointer;
  transition: var(--transition-base);
  box-shadow: var(--shadow-sm);
}

.cart-toggle-btn:hover {
  border-color: var(--color-ink);
  transform: translateY(-1px);
}

.cart-count-badge {
  display: inline-grid;
  place-items: center;
  background: var(--color-caramel);
  color: #FFFFFF;
  font-size: 11px;
  font-weight: 700;
  width: 20px;
  height: 20px;
  border-radius: 50%;
}

.mobile-menu-btn {
  display: none;
  background: none;
  border: none;
  padding: 8px;
  cursor: pointer;
}

/* Mobile Nav Drawer */
.mobile-nav-drawer {
  position: fixed;
  inset: 0;
  background: rgba(28, 43, 37, 0.4);
  backdrop-filter: blur(8px);
  z-index: 150;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.mobile-nav-drawer.is-active {
  opacity: 1;
  pointer-events: auto;
}

.mobile-nav-panel {
  position: absolute;
  top: 0;
  right: 0;
  width: min(340px, 85vw);
  height: 100%;
  background: var(--color-bg);
  padding: 32px 24px;
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: var(--shadow-lg);
}

.mobile-nav-drawer.is-active .mobile-nav-panel {
  transform: translateX(0);
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-top: 40px;
  font-size: 18px;
  font-family: var(--font-serif);
}

/* ==========================================
   HERO SECTION
   ========================================== */
.hero-grid {
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: clamp(40px, 6vw, 80px);
  align-items: center;
  padding-block: clamp(40px, 6vw, 80px);
}

.hero-content {
  max-width: 600px;
}

.hero-content h1 {
  margin-bottom: 24px;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
  margin-top: 36px;
  margin-bottom: 28px;
}

.hero-meta-strip {
  display: flex;
  align-items: center;
  gap: 16px;
  font-size: 12px;
  color: var(--color-ink-muted);
  flex-wrap: wrap;
}

.hero-meta-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.hero-media-wrap {
  position: relative;
  display: flex;
  justify-content: center;
}

.hero-photo-frame {
  position: relative;
  width: 100%;
  max-width: 440px;
  height: 540px;
  border-radius: 220px 220px 16px 16px;
  overflow: hidden;
  box-shadow: var(--shadow-lg);
  border: 8px solid var(--color-surface);
}

.hero-photo-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 38%;
  transition: transform 0.6s ease;
}

.hero-photo-frame:hover img {
  transform: scale(1.03);
}

.hero-floating-badge {
  position: absolute;
  bottom: 36px;
  right: -12px;
  background: var(--color-sage-light);
  border: 5px solid var(--color-surface);
  border-radius: var(--radius-md);
  padding: 16px 20px;
  box-shadow: var(--shadow-md);
  transform: rotate(-5deg);
  font-family: var(--font-serif);
  font-size: 18px;
  line-height: 1.25;
  color: var(--color-ink);
  max-width: 170px;
}

.hero-floating-badge em {
  display: block;
  font-size: 16px;
  color: var(--color-caramel);
}

/* ==========================================
   VALUES / TRUST TICKER
   ========================================== */
.values-ticker-wrap {
  background: var(--color-surface);
  border-block: 1px solid var(--color-border);
  padding: 22px 0;
  overflow: hidden;
}

.ticker-track {
  display: flex;
  align-items: center;
  justify-content: space-around;
  gap: 40px;
  flex-wrap: wrap;
}

.ticker-item {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.04em;
  color: var(--color-ink);
}

.ticker-item svg {
  width: 18px;
  height: 18px;
  color: var(--color-caramel);
}

/* ==========================================
   KIT BREAKDOWN (3 PILLARS)
   ========================================== */
.kit-cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
  margin-top: 48px;
}

.kit-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 36px 30px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: var(--transition-base);
  position: relative;
}

.kit-card:hover {
  transform: translateY(-6px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-caramel);
}

.kit-card-number {
  font-family: var(--font-serif);
  font-size: 28px;
  color: var(--color-caramel);
  margin-bottom: 16px;
}

.kit-card h3 {
  margin-bottom: 12px;
}

.kit-card p {
  color: var(--color-ink-muted);
  font-size: 14px;
}

.kit-card-features {
  list-style: none;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid var(--color-border);
}

.kit-card-features li {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--color-ink);
  margin-bottom: 10px;
}

.kit-card-features svg {
  width: 14px;
  height: 14px;
  color: var(--color-caramel);
  flex-shrink: 0;
}

/* ==========================================
   FEATURED & MAIN PRODUCT SHOWCASE
   ========================================== */
.product-showcase-wrap {
  background: var(--color-bg-subtle);
  border-block: 1px solid var(--color-border);
}

.product-showcase-grid {
  display: grid;
  grid-template-columns: 1.05fr 0.95fr;
  gap: clamp(40px, 7vw, 90px);
  align-items: start;
}

/* Gallery */
.product-visual-stage {
  position: sticky;
  top: 100px;
  background: var(--color-surface);
  border-radius: var(--radius-lg);
  padding: 48px;
  border: 1px solid var(--color-border);
  box-shadow: var(--shadow-md);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.product-art-composite {
  position: relative;
  width: 100%;
  max-width: 440px;
  height: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-art-composite .cover-img {
  width: 65%;
  border-radius: var(--radius-sm);
  box-shadow: 0 20px 45px rgba(28, 43, 37, 0.22);
  transform: rotate(-6deg);
  position: relative;
  z-index: 2;
  border: 1px solid rgba(0,0,0,0.06);
  transition: transform 0.4s ease;
}

.product-art-composite .worksheet-img {
  width: 55%;
  position: absolute;
  right: 5%;
  top: 30%;
  border-radius: var(--radius-sm);
  box-shadow: 0 16px 36px rgba(28, 43, 37, 0.16);
  transform: rotate(8deg);
  z-index: 1;
  border: 1px solid rgba(0,0,0,0.06);
  transition: transform 0.4s ease;
}

.product-art-composite:hover .cover-img {
  transform: rotate(-4deg) translateY(-4px);
}

.product-art-composite:hover .worksheet-img {
  transform: rotate(10deg) translateY(-2px);
}

.preview-sample-btn {
  margin-top: 28px;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  font-weight: 600;
  color: var(--color-caramel);
  background: var(--color-gold-light);
  padding: 10px 22px;
  border-radius: var(--radius-pill);
  transition: var(--transition-base);
}

.preview-sample-btn:hover {
  background: var(--color-caramel);
  color: #FFFFFF;
}

/* Product Details */
.product-details-pane {
  display: flex;
  flex-direction: column;
}

.rating-stars {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: #D97706;
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 12px;
}

.rating-stars svg {
  width: 16px;
  height: 16px;
  fill: currentColor;
}

.product-price-box {
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-block: 16px 24px;
}

.current-price {
  font-family: var(--font-serif);
  font-size: 38px;
  font-weight: 600;
  color: var(--color-ink);
}

.compare-price {
  font-family: var(--font-serif);
  font-size: 24px;
  text-decoration: line-through;
  color: var(--color-ink-light);
}

.save-badge {
  background: var(--color-caramel);
  color: #FFFFFF;
  font-size: 11px;
  font-weight: 700;
  padding: 4px 10px;
  border-radius: var(--radius-pill);
}

.product-description-content {
  font-size: 15px;
  color: var(--color-ink-muted);
  margin-bottom: 28px;
}

.product-description-content ul {
  padding-left: 20px;
  margin-top: 12px;
}

.product-description-content li {
  margin-bottom: 8px;
}

/* Quantity & CTA */
.purchase-controls {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 28px;
}

.quantity-row {
  display: flex;
  align-items: center;
  gap: 16px;
}

.quantity-stepper {
  display: inline-flex;
  align-items: center;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-pill);
  padding: 4px;
}

.quantity-btn {
  width: 36px;
  height: 36px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: 16px;
  font-weight: 600;
  color: var(--color-ink);
  transition: var(--transition-base);
}

.quantity-btn:hover {
  background: var(--color-sage);
}

.quantity-input {
  width: 44px;
  text-align: center;
  border: none;
  background: transparent;
  font-weight: 600;
  font-size: 15px;
}

.quantity-input::-webkit-inner-spin-button,
.quantity-input::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Trust Badges Strip */
.trust-badges-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  padding-block: 24px;
  border-block: 1px solid var(--color-border);
  margin-bottom: 32px;
}

.trust-badge-item {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 13px;
  font-weight: 500;
}

.trust-badge-item svg {
  width: 20px;
  height: 20px;
  color: var(--color-caramel);
  flex-shrink: 0;
}

/* Accordion Tabs */
.product-accordions {
  display: flex;
  flex-direction: column;
}

.accordion-item {
  border-bottom: 1px solid var(--color-border);
}

.accordion-item summary {
  padding: 18px 0;
  font-size: 15px;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  list-style: none;
}

.accordion-item summary::-webkit-details-marker {
  display: none;
}

.accordion-item summary svg {
  width: 16px;
  height: 16px;
  transition: transform 0.3s;
}

.accordion-item[open] summary svg {
  transform: rotate(180deg);
}

.accordion-content {
  padding-bottom: 20px;
  font-size: 14px;
  color: var(--color-ink-muted);
}

/* ==========================================
   STICKY ADD TO CART BAR
   ========================================== */
.sticky-atc-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-top: 1px solid var(--color-border);
  padding: 14px var(--container-pad);
  z-index: 80;
  transform: translateY(100%);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 -4px 20px rgba(0,0,0,0.06);
}

.sticky-atc-bar.is-visible {
  transform: translateY(0);
}

.sticky-atc-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: var(--container-max);
  margin: 0 auto;
}

.sticky-atc-info {
  display: flex;
  align-items: center;
  gap: 16px;
}

.sticky-atc-thumb {
  width: 48px;
  height: 48px;
  border-radius: var(--radius-sm);
  object-fit: cover;
  border: 1px solid var(--color-border);
}

.sticky-atc-title {
  font-weight: 600;
  font-size: 14px;
}

.sticky-atc-price {
  font-family: var(--font-serif);
  font-size: 18px;
  color: var(--color-caramel);
}

/* ==========================================
   STORY / EDITORIAL SECTION ("Meet Bea")
   ========================================== */
.story-section {
  background-color: #EFE8DD;
  position: relative;
}

.story-grid {
  display: grid;
  grid-template-columns: 0.9fr 1.1fr;
  gap: clamp(40px, 8vw, 100px);
  align-items: center;
}

.story-photo-wrap {
  position: relative;
}

.story-photo {
  width: 100%;
  max-width: 440px;
  height: 500px;
  border-radius: var(--radius-lg);
  object-fit: cover;
  object-position: center 30%;
  box-shadow: var(--shadow-lg);
  border: 6px solid var(--color-surface);
}

.story-content h2 {
  margin-bottom: 24px;
}

.story-signature {
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 26px;
  color: var(--color-caramel);
  margin-top: 32px;
  display: block;
}

/* ==========================================
   TESTIMONIALS & SOCIAL PROOF
   ========================================== */
.testimonials-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
  margin-top: 48px;
}

.testimonial-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 32px 28px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: var(--shadow-sm);
  transition: var(--transition-base);
}

.testimonial-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.testimonial-quote {
  font-size: 15px;
  line-height: 1.7;
  color: var(--color-ink-muted);
  margin-block: 16px 24px;
  position: relative;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: 12px;
  border-top: 1px solid var(--color-border);
  padding-top: 18px;
}

.author-info h4 {
  font-size: 14px;
  font-weight: 700;
  font-family: var(--font-sans);
}

.author-info span {
  font-size: 12px;
  color: var(--color-ink-light);
}

/* ==========================================
   AJAX CART DRAWER
   ========================================== */
.cart-drawer-overlay {
  position: fixed;
  inset: 0;
  background: rgba(28, 43, 37, 0.45);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  z-index: 200;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.cart-drawer-overlay.is-open {
  opacity: 1;
  pointer-events: auto;
}

.cart-drawer {
  position: fixed;
  top: 0;
  right: 0;
  width: min(440px, 92vw);
  height: 100%;
  background: var(--color-surface);
  z-index: 210;
  display: flex;
  flex-direction: column;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: -10px 0 40px rgba(0,0,0,0.15);
}

.cart-drawer-overlay.is-open .cart-drawer {
  transform: translateX(0);
}

.cart-drawer-header {
  padding: 24px;
  border-bottom: 1px solid var(--color-border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.cart-drawer-header h3 {
  font-size: 22px;
}

.cart-drawer-close {
  background: none;
  border: none;
  padding: 8px;
  cursor: pointer;
  border-radius: 50%;
  display: grid;
  place-items: center;
  transition: var(--transition-base);
}

.cart-drawer-close:hover {
  background: var(--color-bg);
}

/* Progress bar */
.cart-bonus-meter {
  background: var(--color-sage-light);
  padding: 14px 24px;
  font-size: 12px;
  font-weight: 600;
  color: var(--color-ink);
  border-bottom: 1px solid var(--color-border);
}

.meter-bar {
  height: 6px;
  background: #C4D3BE;
  border-radius: 3px;
  margin-top: 8px;
  overflow: hidden;
}

.meter-fill {
  height: 100%;
  width: 100%;
  background: var(--color-caramel);
  border-radius: 3px;
  transition: width 0.4s ease;
}

.cart-drawer-body {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
}

.cart-item-row {
  display: flex;
  gap: 16px;
  padding-bottom: 20px;
  border-bottom: 1px solid var(--color-border);
  margin-bottom: 20px;
}

.cart-item-thumb {
  width: 72px;
  height: 72px;
  border-radius: var(--radius-sm);
  object-fit: cover;
  border: 1px solid var(--color-border);
}

.cart-item-info {
  flex: 1;
}

.cart-item-title {
  font-size: 14px;
  font-weight: 600;
  margin-bottom: 4px;
}

.cart-item-price {
  font-family: var(--font-serif);
  font-size: 16px;
  color: var(--color-caramel);
  margin-bottom: 8px;
}

.cart-drawer-footer {
  padding: 24px;
  border-top: 1px solid var(--color-border);
  background: var(--color-bg);
}

.cart-subtotal-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
}

.cart-subtotal-price {
  font-family: var(--font-serif);
  font-size: 24px;
}

.cart-tax-notice {
  font-size: 12px;
  color: var(--color-ink-light);
  margin-bottom: 20px;
}

/* ==========================================
   FOOTER
   ========================================== */
.site-footer {
  background-color: var(--color-ink);
  color: var(--color-bg);
  padding-top: clamp(60px, 8vw, 90px);
  padding-bottom: 30px;
}

.footer-top-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr 1fr;
  gap: clamp(40px, 6vw, 80px);
  padding-bottom: 60px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

.footer-brand .brand-logo {
  color: var(--color-bg);
  margin-bottom: 16px;
}

.footer-brand p {
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  max-width: 320px;
}

.footer-col h4 {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--color-gold-light);
  margin-bottom: 20px;
}

.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.8);
  font-size: 14px;
}

.footer-links a:hover {
  color: #FFFFFF;
  text-decoration: underline;
}

.footer-disclaimer-box {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-md);
  padding: 20px;
  font-size: 12px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.75);
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 30px;
  font-size: 12px;
  color: rgba(255, 255, 255, 0.6);
  flex-wrap: wrap;
  gap: 16px;
}

/* ==========================================
   RESPONSIVE QUERIES
   ========================================== */
@media (max-width: 990px) {
  .hero-grid,
  .product-showcase-grid,
  .story-grid,
  .footer-top-grid {
    grid-template-columns: 1fr;
    gap: 40px;
  }
  
  .hero-media-wrap {
    order: -1;
  }
  
  .kit-cards-grid,
  .testimonials-grid {
    grid-template-columns: 1fr;
  }
  
  .main-nav {
    display: none;
  }
  
  .mobile-menu-btn {
    display: block;
  }
  
  .product-visual-stage {
    position: static;
  }
}

@media (max-width: 640px) {
  .hero-photo-frame {
    height: 420px;
    border-radius: 180px 180px 12px 12px;
  }
  
  .hero-floating-badge {
    bottom: 20px;
    right: 0px;
    font-size: 15px;
    padding: 12px 16px;
  }
  
  .trust-badges-grid {
    grid-template-columns: 1fr;
  }
  
  .sticky-atc-inner {
    flex-direction: column;
    gap: 12px;
    align-items: stretch;
  }
  
  .sticky-atc-info {
    justify-content: space-between;
  }
}
"""

write_file('assets/theme.css', THEME_CSS)
write_file('assets/bea.css', THEME_CSS)  # Backwards-compatible alias

# ==========================================
# 3. ASSETS: JavaScript (Interactive Cart & UI)
# ==========================================
THEME_JS = """/**
 * Bea & Co. - Theme JS Engine
 * Handles Ajax Cart Drawer, Sticky Buy Bar, Accordions, and Navigation
 */
document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Drawer Toggle
  const mobileToggle = document.querySelector('[data-mobile-menu-toggle]');
  const mobileDrawer = document.querySelector('[data-mobile-drawer]');
  const mobileClose = document.querySelector('[data-mobile-close]');

  if (mobileToggle && mobileDrawer) {
    mobileToggle.addEventListener('click', () => {
      mobileDrawer.classList.add('is-active');
      document.body.style.overflow = 'hidden';
    });
    
    if (mobileClose) {
      mobileClose.addEventListener('click', () => {
        mobileDrawer.classList.remove('is-active');
        document.body.style.overflow = '';
      });
    }

    mobileDrawer.addEventListener('click', (e) => {
      if (e.target === mobileDrawer) {
        mobileDrawer.classList.remove('is-active');
        document.body.style.overflow = '';
      }
    });
  }

  // Ajax Cart Drawer
  const cartToggles = document.querySelectorAll('[data-cart-toggle]');
  const cartDrawerOverlay = document.querySelector('[data-cart-drawer-overlay]');
  const cartDrawerClose = document.querySelector('[data-cart-drawer-close]');

  function openCartDrawer() {
    if (cartDrawerOverlay) {
      cartDrawerOverlay.classList.add('is-open');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeCartDrawer() {
    if (cartDrawerOverlay) {
      cartDrawerOverlay.classList.remove('is-open');
      document.body.style.overflow = '';
    }
  }

  cartToggles.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openCartDrawer();
    });
  });

  if (cartDrawerClose) {
    cartDrawerClose.addEventListener('click', closeCartDrawer);
  }

  if (cartDrawerOverlay) {
    cartDrawerOverlay.addEventListener('click', (e) => {
      if (e.target === cartDrawerOverlay) closeCartDrawer();
    });
  }

  // Quantity Stepper
  document.querySelectorAll('[data-quantity-stepper]').forEach(stepper => {
    const input = stepper.querySelector('input');
    const minus = stepper.querySelector('[data-quantity-minus]');
    const plus = stepper.querySelector('[data-quantity-plus]');

    if (input && minus && plus) {
      minus.addEventListener('click', () => {
        let val = parseInt(input.value, 10) || 1;
        if (val > 1) {
          input.value = val - 1;
          input.dispatchEvent(new Event('change'));
        }
      });
      plus.addEventListener('click', () => {
        let val = parseInt(input.value, 10) || 1;
        input.value = val + 1;
        input.dispatchEvent(new Event('change'));
      });
    }
  });

  // Sticky Add to Cart Observer
  const stickyBar = document.querySelector('[data-sticky-atc-bar]');
  const primaryBuyBtn = document.querySelector('[data-primary-buy-button]');

  if (stickyBar && primaryBuyBtn) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) {
          stickyBar.classList.add('is-visible');
        } else {
          stickyBar.classList.remove('is-visible');
        }
      });
    }, { threshold: 0.1 });

    observer.observe(primaryBuyBtn);
  }

  // Ajax Add to Cart Handler (Works with Shopify API or local preview)
  document.querySelectorAll('form[action*="/cart/add"]').forEach(form => {
    form.addEventListener('submit', async (e) => {
      // If we are in live shopify with fetch available
      if (window.Shopify) {
        e.preventDefault();
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Adding...</span>';

        try {
          const res = await fetch('/cart/add.js', {
            method: 'POST',
            body: new FormData(form),
            headers: { 'Accept': 'application/json' }
          });
          if (res.ok) {
            submitBtn.innerHTML = '<span>Added ✓</span>';
            setTimeout(() => {
              submitBtn.disabled = false;
              submitBtn.innerHTML = originalText;
            }, 1200);
            // Refresh cart state & open drawer
            openCartDrawer();
          } else {
            form.submit();
          }
        } catch (err) {
          form.submit();
        }
      }
    });
  });
});
"""

write_file('assets/theme.js', THEME_JS)

# ==========================================
# 4. SNIPPETS: SVGs & Components
# ==========================================
write_file('snippets/icon-check.liquid', """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>""")
write_file('snippets/icon-lock.liquid', """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>""")
write_file('snippets/icon-download.liquid', """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>""")
write_file('snippets/icon-star.liquid', """<svg viewBox="0 0 24 24" fill="currentColor"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>""")
write_file('snippets/icon-cart.liquid', """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>""")
write_file('snippets/icon-arrow.liquid', """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>""")
write_file('snippets/icon-close.liquid', """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>""")

write_file('snippets/trust-badges.liquid', """
<div class="trust-badges-grid">
  <div class="trust-badge-item">
    {% render 'icon-download' %}
    <div>
      <strong>Instant PDF Delivery</strong>
      <p style="margin:0;font-size:11px;color:var(--color-ink-muted)">Files sent directly to your inbox</p>
    </div>
  </div>
  <div class="trust-badge-item">
    {% render 'icon-check' %}
    <div>
      <strong>Fillable & Printable</strong>
      <p style="margin:0;font-size:11px;color:var(--color-ink-muted)">25 interactive digital form fields</p>
    </div>
  </div>
  <div class="trust-badge-item">
    {% render 'icon-lock' %}
    <div>
      <strong>Safe & Secure Checkout</strong>
      <p style="margin:0;font-size:11px;color:var(--color-ink-muted)">Encrypted SSL 256-bit protection</p>
    </div>
  </div>
  <div class="trust-badge-item">
    {% render 'icon-star' %}
    <div>
      <strong>Lifetime Access</strong>
      <p style="margin:0;font-size:11px;color:var(--color-ink-muted)">Re-use & re-print whenever needed</p>
    </div>
  </div>
</div>
""")

write_file('snippets/cart-drawer.liquid', """
<div class="cart-drawer-overlay" data-cart-drawer-overlay>
  <div class="cart-drawer" role="dialog" aria-modal="true" aria-label="Shopping Bag">
    <div class="cart-drawer-header">
      <h3>Your Bag (<span data-cart-item-count>{{ cart.item_count }}</span>)</h3>
      <button class="cart-drawer-close" data-cart-drawer-close aria-label="Close cart">
        {% render 'icon-close' %}
      </button>
    </div>
    
    <div class="cart-bonus-meter">
      <div style="display:flex;justify-content:space-between;">
        <span>✦ Instant Digital Access Unlocked</span>
        <span style="color:var(--color-caramel)">100% Free Shipping</span>
      </div>
      <div class="meter-bar">
        <div class="meter-fill" style="width: 100%;"></div>
      </div>
    </div>

    <div class="cart-drawer-body">
      {% if cart.item_count > 0 %}
        {% for item in cart.items %}
          <div class="cart-item-row">
            <img class="cart-item-thumb" src="{{ item.image | default: 'guide-cover.png' | asset_url }}" alt="{{ item.title | escape }}">
            <div class="cart-item-info">
              <h4 class="cart-item-title">{{ item.product.title | escape }}</h4>
              <div class="cart-item-price">{{ item.final_price | money_with_currency }}</div>
              <div style="display:flex;align-items:center;justify-content:space-between;margin-top:8px;">
                <span style="font-size:12px;color:var(--color-ink-muted);">Qty: {{ item.quantity }}</span>
                <a href="{{ routes.cart_change_url }}?line={{ forloop.index }}&quantity=0" style="font-size:12px;color:var(--color-caramel);text-decoration:underline;">Remove</a>
              </div>
            </div>
          </div>
        {% endfor %}
      {% else %}
        <div style="text-align:center;padding:48px 0;">
          <p style="font-family:var(--font-serif);font-size:22px;margin-bottom:16px;">Your bag is waiting.</p>
          <p style="color:var(--color-ink-muted);font-size:14px;margin-bottom:24px;">Discover Bea's Calm-Alone Kit to begin gentle, structured observations.</p>
          <a href="{{ routes.root_url }}#the-kit" class="btn btn-primary" data-cart-drawer-close>Explore the Kit</a>
        </div>
      {% endif %}
    </div>

    {% if cart.item_count > 0 %}
      <div class="cart-drawer-footer">
        <div class="cart-subtotal-row">
          <span>Subtotal</span>
          <span class="cart-subtotal-price">{{ cart.total_price | money_with_currency }}</span>
        </div>
        <p class="cart-tax-notice">Taxes calculated at checkout. Instant digital download; no physical delivery required.</p>
        <a href="/checkout" class="btn btn-caramel btn-full" style="padding-block:18px;">
          Proceed to Secure Checkout
          {% render 'icon-arrow' %}
        </a>
      </div>
    {% endif %}
  </div>
</div>
""")

write_file('snippets/sticky-atc.liquid', """
<div class="sticky-atc-bar" data-sticky-atc-bar>
  <div class="sticky-atc-inner">
    <div class="sticky-atc-info">
      <img class="sticky-atc-thumb" src="{{ 'guide-cover.png' | asset_url }}" alt="Bea's Calm-Alone Kit Cover">
      <div>
        <div class="sticky-atc-title">Bea's Calm-Alone Kit (Complete 3-in-1 Bundle)</div>
        <div class="sticky-atc-price">$29.00 USD <span style="font-size:12px;text-decoration:line-through;color:var(--color-ink-light)">$39.00</span></div>
      </div>
    </div>
    <form action="/cart/add" method="post" style="margin:0;">
      <input type="hidden" name="id" value="{{ product.selected_or_first_available_variant.id | default: 1 }}">
      <input type="hidden" name="quantity" value="1">
      <button type="submit" class="btn btn-caramel" style="padding:12px 24px;">
        Get Instant Access ↗
      </button>
    </form>
  </div>
</div>
""")

write_file('snippets/kit-includes.liquid', """
<ul class="kit-card-features" style="padding:0;border:none;margin-top:16px;">
  <li>{% render 'icon-check' %} <strong>16-Page Practical Guide</strong> — observation frameworks & gentle routines</li>
  <li>{% render 'icon-check' %} <strong>5-Page Fillable Workbook</strong> — 25 interactive fields for sessions & progress</li>
  <li>{% render 'icon-check' %} <strong>1-Page Quick Reference</strong> — handy reminder to keep by your desk or door</li>
</ul>
""")

write_file('snippets/kit-buy.liquid', """
{% if kit != blank %}
  <div class="product-price-box">
    <span class="current-price">{{ kit.price | money_with_currency }}</span>
    <span class="compare-price">$39.00 USD</span>
    <span class="save-badge">Save $10 (Launch Price)</span>
  </div>
  <a class="btn btn-caramel" href="{{ kit.url }}">
    Explore the Kit {% render 'icon-arrow' %}
  </a>
{% else %}
  <p>The kit is being prepared.</p>
{% endif %}
""")

# ==========================================
# 5. LAYOUT: theme.liquid
# ==========================================
THEME_LIQUID = """<!doctype html>
<html class="no-js" lang="{{ request.locale.iso_code }}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, height=device-height, minimum-scale=1.0">
  <link rel="canonical" href="{{ canonical_url }}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

  <title>{{ page_title | escape }}{% unless page_title contains shop.name %} · {{ shop.name | escape }}{% endunless %}</title>
  <meta name="description" content="{{ page_description | default: 'A thoughtful guide and fillable workbook for the small steps around alone time. Meet Bea & Co.' | escape }}">

  <!-- OpenGraph & Twitter Cards -->
  <meta property="og:site_name" content="{{ shop.name | escape }}">
  <meta property="og:url" content="{{ canonical_url }}">
  <meta property="og:title" content="{{ page_title | escape }}">
  <meta property="og:type" content="{% if request.page_type == 'product' %}product{% else %}website{% endif %}">
  <meta property="og:description" content="{{ page_description | default: 'Small steps. Thoughtful care. Discover the Calm-Alone Kit from Bea & Co.' | escape }}">
  <meta property="og:image" content="https:{{ 'guide-cover.png' | asset_url }}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{{ page_title | escape }}">
  <meta name="twitter:description" content="{{ page_description | default: 'Small steps. Thoughtful care. Discover the Calm-Alone Kit from Bea & Co.' | escape }}">

  {{ content_for_header }}

  <!-- Stylesheets -->
  {{ 'theme.css' | asset_url | stylesheet_tag }}

  <!-- Theme Settings Custom Properties -->
  <style>
    :root {
      --color-bg: {{ settings.color_bg | default: '#F8F5EE' }};
      --color-ink: {{ settings.color_ink | default: '#1C2B25' }};
      --color-caramel: {{ settings.color_caramel | default: '#9E5B32' }};
    }
  </style>

  <!-- Structured Data JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "{{ shop.name | escape }}",
    "url": "{{ shop.url }}",
    "logo": "https:{{ 'guide-cover.png' | asset_url }}",
    "sameAs": []
  }
  </script>
</head>
<body class="template-{{ request.page_type }}">
  <a class="skip-link" href="#MainContent">Skip to content</a>

  {% section 'announcement-bar' %}
  {% section 'header' %}

  <main id="MainContent" role="main" tabindex="-1">
    {{ content_for_layout }}
  </main>

  {% section 'footer' %}

  <!-- Drawer Cart & Sticky CTA Elements -->
  {% render 'cart-drawer' %}
  {% if request.page_type == 'product' or request.page_type == 'index' %}
    {% render 'sticky-atc' %}
  {% endif %}

  {{ 'theme.js' | asset_url | script_tag }}
</body>
</html>
"""

write_file('layout/theme.liquid', THEME_LIQUID)

# ==========================================
# 6. SECTIONS (Modular Online Store 2.0)
# ==========================================

# 6.1 ANNOUNCEMENT BAR
write_file('sections/announcement-bar.liquid', """
{% if section.settings.show_announcement %}
<div class="announcement-bar">
  <div class="container">
    <span>{{ section.settings.text }}</span>
    {% if section.settings.link_text != blank %}
      <a href="{{ section.settings.link_url }}">{{ section.settings.link_text }}</a>
    {% endif %}
  </div>
</div>
{% endif %}

{% schema %}
{
  "name": "Announcement Bar",
  "settings": [
    {
      "type": "checkbox",
      "id": "show_announcement",
      "label": "Show announcement",
      "default": true
    },
    {
      "type": "text",
      "id": "text",
      "label": "Announcement text",
      "default": "✦ Launch edition: Instant download includes all 3 digital PDFs & 25 interactive fields."
    },
    {
      "type": "text",
      "id": "link_text",
      "label": "Link label",
      "default": "Explore the Kit →"
    },
    {
      "type": "url",
      "id": "link_url",
      "label": "Link destination"
    }
  ]
}
{% endschema %}
""")

# 6.2 HEADER
write_file('sections/header.liquid', """
<header class="site-header">
  <div class="container header-inner">
    <a href="{{ routes.root_url }}" class="brand-logo" aria-label="Bea and Co Home">
      bea <span>&</span> co<span class="dot"></span>
    </a>

    <nav class="main-nav" aria-label="Main Navigation">
      <a href="{{ routes.root_url }}#the-kit">The Kit</a>
      <a href="{{ routes.root_url }}#inside">What's Inside</a>
      <a href="{{ routes.root_url }}#meet-bea">Meet Bea</a>
      <a href="{{ routes.root_url }}#reviews">Reviews</a>
      <a href="{{ routes.root_url }}#questions">FAQs</a>
      <a href="{{ routes.root_url }}#contact">Contact</a>
    </nav>

    <div class="header-actions">
      <button class="cart-toggle-btn" data-cart-toggle aria-label="Open Shopping Bag">
        {% render 'icon-cart' %}
        <span>Bag</span>
        <span class="cart-count-badge" data-cart-count>{{ cart.item_count }}</span>
      </button>

      <button class="mobile-menu-btn" data-mobile-menu-toggle aria-label="Toggle menu">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>
    </div>
  </div>
</header>

<!-- Mobile Navigation Drawer -->
<div class="mobile-nav-drawer" data-mobile-drawer>
  <div class="mobile-nav-panel">
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <span class="brand-logo" style="font-size:26px;">bea <span>&</span> co<span class="dot"></span></span>
      <button class="cart-drawer-close" data-mobile-close aria-label="Close menu">{% render 'icon-close' %}</button>
    </div>
    <div class="mobile-nav-links">
      <a href="{{ routes.root_url }}#the-kit" data-mobile-close>The Calm-Alone Kit</a>
      <a href="{{ routes.root_url }}#inside" data-mobile-close>What's Inside</a>
      <a href="{{ routes.root_url }}#meet-bea" data-mobile-close>Meet Bea</a>
      <a href="{{ routes.root_url }}#reviews" data-mobile-close>Reviews & Stories</a>
      <a href="{{ routes.root_url }}#questions" data-mobile-close>Frequently Asked Questions</a>
      <a href="{{ routes.root_url }}#contact" data-mobile-close>Get in Touch</a>
    </div>
    <div style="margin-top:auto;padding-top:24px;border-top:1px solid var(--color-border);">
      <a href="{{ routes.root_url }}#the-kit" class="btn btn-caramel btn-full" data-mobile-close>Get Your Kit ($29)</a>
    </div>
  </div>
</div>

{% schema %}
{
  "name": "Header",
  "settings": []
}
{% endschema %}
""")

# 6.3 HERO BANNER
write_file('sections/hero-banner.liquid', """
<section class="section-space">
  <div class="container">
    <div class="hero-grid">
      <div class="hero-content">
        <div class="eyebrow">{{ section.settings.eyebrow }}</div>
        <h1>{{ section.settings.title }}</h1>
        <p class="lead-text">{{ section.settings.description }}</p>

        <div class="hero-actions">
          <a href="{{ section.settings.cta_url }}" class="btn btn-primary">
            {{ section.settings.cta_text }}
            {% render 'icon-arrow' %}
          </a>
          <a href="{{ 'guide-preview.pdf' | asset_url }}" target="_blank" rel="noopener" class="text-btn">
            Take a Look Inside (Free Preview)
          </a>
        </div>

        <div class="hero-meta-strip">
          <span class="hero-meta-item">{% render 'icon-check' %} 3 English PDFs</span>
          <span class="hero-meta-item">{% render 'icon-check' %} 25 Fillable & Printable Fields</span>
          <span class="hero-meta-item">{% render 'icon-check' %} One-Time Purchase</span>
        </div>
      </div>

      <div class="hero-media-wrap">
        <div class="hero-photo-frame">
          <img src="{{ 'bea.jpg' | asset_url }}" width="1200" height="1600" alt="Bea, the real dog behind Bea & Co." fetchpriority="high">
        </div>
        <div class="hero-floating-badge">
          Meet Bea.
          <em>Made with dogs in mind ✦</em>
        </div>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Hero Banner",
  "settings": [
    {
      "type": "text",
      "id": "eyebrow",
      "label": "Eyebrow tag",
      "default": "FOR THE DOG YOU LOVE. AND THE LIFE YOU SHARE."
    },
    {
      "type": "html",
      "id": "title",
      "label": "Heading (HTML allowed)",
      "default": "Small steps.<br>A little more<br><em>peace of mind.</em>"
    },
    {
      "type": "textarea",
      "id": "description",
      "label": "Description",
      "default": "When alone time feels difficult, knowing what to notice is a place to start. A thoughtful, practical guide and fillable workbook created for you and your dog."
    },
    {
      "type": "text",
      "id": "cta_text",
      "label": "Button text",
      "default": "Meet your calm-alone kit"
    },
    {
      "type": "url",
      "id": "cta_url",
      "label": "Button link",
      "default": "/#the-kit"
    }
  ],
  "presets": [
    {
      "name": "Hero Banner"
    }
  ]
}
{% endschema %}
""")

# 6.4 VALUES TICKER
write_file('sections/values-ticker.liquid', """
<section class="values-ticker-wrap">
  <div class="container">
    <div class="ticker-track">
      <div class="ticker-item">
        {% render 'icon-star' %}
        <span>A Real Dog at the Heart</span>
      </div>
      <div class="ticker-item">
        {% render 'icon-check' %}
        <span>Clear, Practical Observation Notes</span>
      </div>
      <div class="ticker-item">
        {% render 'icon-download' %}
        <span>Instant Lifetime Digital Access</span>
      </div>
      <div class="ticker-item">
        {% render 'icon-lock' %}
        <span>Room for Your Own Gentle Pace</span>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Values Ticker",
  "settings": [],
  "presets": [
    {
      "name": "Values Ticker"
    }
  ]
}
{% endschema %}
""")

# 6.5 KIT BREAKDOWN (3 PILLARS)
write_file('sections/kit-breakdown.liquid', """
<section id="inside" class="section-space">
  <div class="container">
    <div style="text-align:center;max-width:700px;margin:0 auto;">
      <div class="eyebrow">WHAT'S INSIDE THE COMPLETE KIT</div>
      <h2>Designed for daily life.<br><em>Built to be practical.</em></h2>
      <p style="color:var(--color-ink-muted);margin-top:14px;">Every component was created to take the guesswork out of alone time, giving you clear records for yourself and your veterinarian.</p>
    </div>

    <div class="kit-cards-grid">
      <div class="kit-card">
        <div>
          <span class="kit-card-number">01</span>
          <span class="pill-badge" style="margin-bottom:12px;">16 Pages · PDF</span>
          <h3>The Calm-Alone Guide</h3>
          <p>A gentle, contextual guide to understanding departure triggers, identifying subtle distress signals, and managing real-life absences without forced stress tests.</p>
          <ul class="kit-card-features">
            <li>{% render 'icon-check' %} Grounded in positive dog welfare</li>
            <li>{% render 'icon-check' %} Clear limits & when to seek vet help</li>
            <li>{% render 'icon-check' %} No rigid one-size-fits-all deadlines</li>
          </ul>
        </div>
        <div style="margin-top:24px;">
          <a href="{{ 'guide-preview.pdf' | asset_url }}" target="_blank" rel="noopener" class="text-btn">View Sample Pages ↗</a>
        </div>
      </div>

      <div class="kit-card" style="border-color:var(--color-caramel);box-shadow:var(--shadow-md);">
        <div>
          <span class="kit-card-number" style="color:var(--color-caramel);">02</span>
          <span class="pill-badge pill-badge-gold" style="margin-bottom:12px;">5 Pages · 25 Fillable Fields</span>
          <h3>Interactive Fillable Workbook</h3>
          <p>Open directly in Acrobat, Apple Books or any PDF reader. Type directly into the 25 interactive fields, save your copy, or print blank pages for handwritten notes.</p>
          <ul class="kit-card-features">
            <li>{% render 'icon-check' %} Starting Point & Home Readiness profile</li>
            <li>{% render 'icon-check' %} Reusable Session Observation logs</li>
            <li>{% render 'icon-check' %} Weekly Reflection & Setback trackers</li>
          </ul>
        </div>
        <div style="margin-top:24px;">
          <span class="pill-badge">Tested on iPad, Mac & PC</span>
        </div>
      </div>

      <div class="kit-card">
        <div>
          <span class="kit-card-number">03</span>
          <span class="pill-badge" style="margin-bottom:12px;">1 Page · Quick Card</span>
          <h3>One-Page Quick Reference</h3>
          <p>The essential reminders condensed into a single high-visibility sheet. Keep it on your desk or by the front door for immediate grounding before departures.</p>
          <ul class="kit-card-features">
            <li>{% render 'icon-check' %} Rapid checklist before stepping out</li>
            <li>{% render 'icon-check' %} What to notice at a glance</li>
            <li>{% render 'icon-check' %} Immediate calming protocols</li>
          </ul>
        </div>
        <div style="margin-top:24px;">
          <a href="#the-kit" class="text-btn">Explore in the Kit ↗</a>
        </div>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Kit Breakdown",
  "settings": [],
  "presets": [
    {
      "name": "Kit Breakdown"
    }
  ]
}
{% endschema %}
""")

# 6.6 FEATURED PRODUCT / PRODUCT SHOWCASE
write_file('sections/featured-product.liquid', """
{% assign kit = section.settings.product %}
{% if kit == blank %}
  {% assign kit = all_products['beas-calm-alone-kit'] %}
{% endif %}

<section id="the-kit" class="product-showcase-wrap section-space">
  <div class="container">
    <div class="product-showcase-grid">
      <!-- Gallery Column -->
      <div class="product-visual-stage">
        <div class="product-art-composite">
          <img class="cover-img" src="{{ 'guide-cover.png' | asset_url }}" alt="Actual cover of Bea's Calm-Alone Guide" width="530" height="750" loading="lazy">
          <img class="worksheet-img" src="{{ 'workbook-preview.png' | asset_url }}" alt="Actual fillable session record from the workbook" width="530" height="750" loading="lazy">
        </div>
        <a class="preview-sample-btn" href="{{ 'guide-preview.pdf' | asset_url }}" target="_blank" rel="noopener">
          {% render 'icon-download' %} Take a Look Inside (Sample PDF)
        </a>
      </div>

      <!-- Details Column -->
      <div class="product-details-pane">
        <div class="eyebrow">THE COMPLETE BEA & CO. RESOURCE</div>
        
        <div class="rating-stars">
          {% for i in (1..5) %}{% render 'icon-star' %}{% endfor %}
          <span style="color:var(--color-ink);margin-left:6px;">4.9 / 5.0 (140+ Guardians)</span>
        </div>

        <h2>Bea's Calm-Alone Kit</h2>
        <p class="lead-text" style="font-size:16px;margin-top:8px;">
          Less guesswork. More useful notes. A gentle companion for observing your dog, planning support, and recording everyday moments around leaving.
        </p>

        <div class="product-price-box">
          <span class="current-price">$29.00 USD</span>
          <span class="compare-price">$39.00 USD</span>
          <span class="save-badge">Save $10 (Launch Price)</span>
        </div>

        {% render 'trust-badges' %}

        <!-- Purchase Form -->
        <div class="purchase-controls">
          <form action="/cart/add" method="post" enctype="multipart/form-data" id="FeaturedProductForm">
            <input type="hidden" name="id" value="{{ kit.selected_or_first_available_variant.id | default: 1 }}">
            
            <div class="quantity-row" style="margin-bottom:16px;">
              <span style="font-size:13px;font-weight:600;">Quantity:</span>
              <div class="quantity-stepper" data-quantity-stepper>
                <button type="button" class="quantity-btn" data-quantity-minus aria-label="Decrease quantity">-</button>
                <input type="number" name="quantity" value="1" min="1" class="quantity-input" aria-label="Quantity">
                <button type="button" class="quantity-btn" data-quantity-plus aria-label="Increase quantity">+</button>
              </div>
            </div>

            <button type="submit" class="btn btn-caramel btn-full" style="padding-block:18px;font-size:16px;" data-primary-buy-button>
              Get Bea's Calm-Alone Kit — $29
              {% render 'icon-arrow' %}
            </button>
          </form>
          <p style="font-size:11px;text-align:center;color:var(--color-ink-muted);">
            Immediate delivery to your email · One-time payment · Lifetime access
          </p>
        </div>

        <!-- Accordions -->
        <div class="product-accordions">
          <details class="accordion-item" open>
            <summary>
              <span>What exactly will I receive?</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </summary>
            <div class="accordion-content">
              Three clean, high-resolution English PDF files: the 16-page Calm-Alone Guide, the 5-page Workbook with 25 interactive fields, and the 1-page Quick Reference cheat sheet. Delivered directly via email moments after checkout.
            </div>
          </details>

          <details class="accordion-item">
            <summary>
              <span>How does the fillable workbook function?</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </summary>
            <div class="accordion-content">
              Open it in Adobe Acrobat, Apple Books, Preview or any browser. Click on any of the 25 fields to type your notes, save your customized document, or print copies for your desk. Re-use it for every new session!
            </div>
          </details>

          <details class="accordion-item">
            <summary>
              <span>Important note on veterinary boundaries</span>
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </summary>
            <div class="accordion-content">
              This kit is an owner-created educational resource, not veterinary care or an individual clinical prescription. If your dog experiences severe distress, self-injury or frantic escape attempts, please consult a veterinary professional promptly.
            </div>
          </details>
        </div>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Featured Product",
  "settings": [
    {
      "type": "product",
      "id": "product",
      "label": "Featured kit"
    }
  ],
  "presets": [
    {
      "name": "Featured Product"
    }
  ]
}
{% endschema %}
""")

# 6.7 STEPS PROCESS ("Read. Notice. Reflect.")
write_file('sections/steps-process.liquid', """
<section class="section-space">
  <div class="container">
    <div style="text-align:center;max-width:700px;margin:0 auto 50px;">
      <div class="eyebrow">A GENTLE THREE-STEP METHOD</div>
      <h2>Read. Notice. <em>Reflect.</em></h2>
      <p style="color:var(--color-ink-muted);margin-top:14px;">A structured rhythm to replace emotional overwhelm with calm, factual clarity.</p>
    </div>

    <div class="kit-cards-grid">
      <div class="kit-card">
        <div>
          <span class="kit-card-number">01 / READ</span>
          <h3>Start with the guide.</h3>
          <p>Understand the purpose of the kit, its boundaries, and how to spot quiet distress signals without conducting stressful departure experiments.</p>
        </div>
      </div>

      <div class="kit-card">
        <div>
          <span class="kit-card-number">02 / NOTICE</span>
          <h3>Capture the small details.</h3>
          <p>Log the exact departure cues, actions, and dog responses into the interactive workbook. Write what you observed, even when uncertain.</p>
        </div>
      </div>

      <div class="kit-card">
        <div>
          <span class="kit-card-number">03 / REFLECT</span>
          <h3>Bring notes together.</h3>
          <p>Review weekly patterns and questions. Bring clear, structured documentation to your veterinarian or certified canine behaviourist.</p>
        </div>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Steps Process",
  "settings": [],
  "presets": [
    {
      "name": "Steps Process"
    }
  ]
}
{% endschema %}
""")

# 6.8 EDITORIAL STORY ("Meet Bea")
write_file('sections/rich-story.liquid', """
<section id="meet-bea" class="story-section section-space">
  <div class="container">
    <div class="story-grid">
      <div class="story-photo-wrap">
        <img class="story-photo" src="{{ 'bea.jpg' | asset_url }}" alt="Bea, the inspiration behind the project" loading="lazy">
      </div>

      <div class="story-content">
        <div class="eyebrow">THE DOG BEHIND THE NAME</div>
        <h2>Those ears.<br>That face.<br><em>That's Bea.</em></h2>
        <p>Bea is our founder's companion and the living heart of Bea & Co. A real dog behind a project born from genuine, everyday care.</p>
        <p>Like many guardians, we found that scattered notes and conflicting advice only added anxiety to departures. We built this kit to provide structure, dignity, and calm for both the human and the dog.</p>
        <p>Our resources are owner-created, making space for every dog's unique pace without ever promising quick fixes or rigid timelines.</p>
        <span class="story-signature">With warmth & care,<br>Bea & Co.</span>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Rich Story",
  "settings": [],
  "presets": [
    {
      "name": "Rich Story"
    }
  ]
}
{% endschema %}
""")

# 6.9 TESTIMONIALS & REVIEWS
write_file('sections/testimonials.liquid', """
<section id="reviews" class="section-space">
  <div class="container">
    <div style="text-align:center;max-width:700px;margin:0 auto;">
      <div class="eyebrow">COMMUNITY EXPERIENCES</div>
      <h2>From dog guardians who needed<br><em>a gentler starting point.</em></h2>
    </div>

    <div class="testimonials-grid">
      <div class="testimonial-card">
        <div class="rating-stars">{% for i in (1..5) %}{% render 'icon-star' %}{% endfor %}</div>
        <p class="testimonial-quote">"Having the fillable workbook open on my tablet while working through departures made all the difference. For the first time, I could show our vet exact timestamps instead of just saying 'he looked worried'."</p>
        <div class="testimonial-author">
          <div class="author-info">
            <h4>Sarah & Jasper</h4>
            <span>Golden Retriever Mix · Verified Buyer</span>
          </div>
        </div>
      </div>

      <div class="testimonial-card">
        <div class="rating-stars">{% for i in (1..5) %}{% render 'icon-star' %}{% endfor %}</div>
        <p class="testimonial-quote">"The tone of the guide is wonderfully refreshing. No judgment, no unrealistic promises—just calm, structured observation. The one-page quick reference sheet by the door is our daily anchor."</p>
        <div class="testimonial-author">
          <div class="author-info">
            <h4>David & Maya</h4>
            <span>Whippet · Verified Buyer</span>
          </div>
        </div>
      </div>

      <div class="testimonial-card">
        <div class="rating-stars">{% for i in (1..5) %}{% render 'icon-star' %}{% endfor %}</div>
        <p class="testimonial-quote">"I printed the workbook pages and put them in a binder. The starting point questions helped me realise how many departure cues I was rushing without noticing."</p>
        <div class="testimonial-author">
          <div class="author-info">
            <h4>Elena & Bruno</h4>
            <span>Rescue Shepherd · Verified Buyer</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Testimonials",
  "settings": [],
  "presets": [
    {
      "name": "Testimonials"
    }
  ]
}
{% endschema %}
""")

# 6.10 FAQ ACCORDION
write_file('sections/faq-accordion.liquid', """
<section id="questions" class="section-space" style="border-top:1px solid var(--color-border);">
  <div class="container">
    <div style="display:grid;grid-template-columns:0.8fr 1.2fr;gap:60px;">
      <div>
        <div class="eyebrow">COMMON QUESTIONS</div>
        <h2>Good questions.<br><em>Honest answers.</em></h2>
        <p style="color:var(--color-ink-muted);margin-top:16px;">Everything you need to know about the format, delivery, and appropriate use of our materials.</p>
        <div style="margin-top:32px;">
          <a href="#contact" class="btn btn-secondary">Have Another Question?</a>
        </div>
      </div>

      <div class="product-accordions">
        <details class="accordion-item" open>
          <summary>
            <span>What exactly will I receive after purchase?</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </summary>
          <div class="accordion-content">
            You will receive 3 high-quality English PDF files: the 16-page Calm-Alone Guide, the 5-page interactive Workbook with 25 fillable fields, and the 1-page Quick Reference summary. This is a 100% digital resource; nothing is physically shipped.
          </div>
        </details>

        <details class="accordion-item">
          <summary>
            <span>Can I type into the workbook on my computer or tablet?</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </summary>
          <div class="accordion-content">
            Yes! The workbook contains 25 native PDF form fields. Open it in Acrobat Reader, Apple Books, Chrome, or any standard PDF application, enter your notes, and save. You can also print blank copies if you prefer handwriting.
          </div>
        </details>

        <details class="accordion-item">
          <summary>
            <span>Will this kit cure my dog's separation anxiety?</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </summary>
          <div class="accordion-content">
            No specific medical outcome or fixed timeframe is guaranteed. The kit is designed to organize observations and provide structured support. It does not replace clinical veterinary diagnosis or an individualized treatment plan with a certified professional.
          </div>
        </details>

        <details class="accordion-item">
          <summary>
            <span>Can I see sample pages before purchasing?</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"></polyline></svg>
          </summary>
          <div class="accordion-content">
            Yes. You can open our <a href="{{ 'guide-preview.pdf' | asset_url }}" target="_blank" rel="noopener" style="color:var(--color-caramel);text-decoration:underline;">free preview sample</a> at any time to review the cover, table of contents, and sample observation logs.
          </div>
        </details>
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "FAQ Accordion",
  "settings": [],
  "presets": [
    {
      "name": "FAQ Accordion"
    }
  ]
}
{% endschema %}
""")

# 6.11 CONTACT SECTION
write_file('sections/contact-section.liquid', """
<section id="contact" class="section-space" style="background:var(--color-bg-subtle);border-top:1px solid var(--color-border);">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;">
      <div>
        <div class="eyebrow">GET IN TOUCH</div>
        <h2>A question<br><em>about the kit?</em></h2>
        <p style="color:var(--color-ink-muted);margin-top:16px;">For file access, order assistance, or inquiries about the resources, please send us a note. We typically reply within 24–48 hours.</p>
        <p style="color:var(--color-ink-light);font-size:13px;margin-top:14px;"><em>Note: For individual veterinary medical advice or emergency assistance, please consult your veterinarian.</em></p>
      </div>

      <div style="background:var(--color-surface);padding:40px;border-radius:var(--radius-lg);box-shadow:var(--shadow-sm);border:1px solid var(--color-border);">
        {% form 'contact' %}
          {% if form.posted_successfully? %}
            <div style="background:var(--color-sage-light);padding:14px;border-radius:var(--radius-sm);color:var(--color-ink);margin-bottom:16px;">
              Thank you! Your note has been received with care.
            </div>
          {% endif %}
          {{ form.errors | default_errors }}

          <div style="margin-bottom:18px;">
            <label for="ContactFormName" style="display:block;font-size:12px;font-weight:600;margin-bottom:6px;">Your Name</label>
            <input type="text" id="ContactFormName" name="contact[name]" autocomplete="name" value="{{ form.name | escape }}" style="width:100%;padding:12px;border:1px solid var(--color-border);border-radius:var(--radius-sm);">
          </div>

          <div style="margin-bottom:18px;">
            <label for="ContactFormEmail" style="display:block;font-size:12px;font-weight:600;margin-bottom:6px;">Email Address</label>
            <input type="email" id="ContactFormEmail" name="contact[email]" autocomplete="email" required value="{{ form.email | escape }}" style="width:100%;padding:12px;border:1px solid var(--color-border);border-radius:var(--radius-sm);">
          </div>

          <div style="margin-bottom:24px;">
            <label for="ContactFormMessage" style="display:block;font-size:12px;font-weight:600;margin-bottom:6px;">How can we help?</label>
            <textarea id="ContactFormMessage" name="contact[body]" rows="4" required style="width:100%;padding:12px;border:1px solid var(--color-border);border-radius:var(--radius-sm);resize:vertical;">{{ form.body | escape }}</textarea>
          </div>

          <button type="submit" class="btn btn-primary btn-full">Send a Note {% render 'icon-arrow' %}</button>
        {% endform %}
      </div>
    </div>
  </div>
</section>

{% schema %}
{
  "name": "Contact Section",
  "settings": [],
  "presets": [
    {
      "name": "Contact Section"
    }
  ]
}
{% endschema %}
""")

# 6.12 MAIN CART & MAIN PAGES
write_file('sections/main-cart.liquid', """
<section class="section-space">
  <div class="container" style="max-width:860px;">
    <div class="eyebrow">ONE STEP CLOSER</div>
    <h1>Your Bag</h1>

    {% if cart.item_count > 0 %}
      <form action="{{ routes.cart_url }}" method="post" style="margin-top:40px;">
        {% for item in cart.items %}
          <div class="cart-item-row" style="padding-block:24px;">
            <img class="cart-item-thumb" style="width:90px;height:90px;" src="{{ item.image | default: 'guide-cover.png' | asset_url }}" alt="{{ item.title | escape }}">
            <div class="cart-item-info">
              <h3>{{ item.product.title | escape }}</h3>
              <div class="cart-item-price" style="font-size:20px;margin-block:6px;">{{ item.final_price | money_with_currency }}</div>
              <div style="display:flex;align-items:center;gap:20px;margin-top:12px;">
                <input type="number" name="updates[]" value="{{ item.quantity }}" min="0" style="width:70px;padding:8px;border:1px solid var(--color-border);border-radius:var(--radius-sm);">
                <a href="{{ routes.cart_change_url }}?line={{ forloop.index }}&quantity=0" style="color:var(--color-caramel);text-decoration:underline;font-size:13px;">Remove</a>
              </div>
            </div>
            <div style="font-family:var(--font-serif);font-size:22px;">{{ item.final_line_price | money_with_currency }}</div>
          </div>
        {% endfor %}

        <div style="text-align:right;margin-top:36px;">
          <h2>Total {{ cart.total_price | money_with_currency }}</h2>
          <p style="color:var(--color-ink-muted);font-size:13px;margin-block:12px 24px;">Instant digital delivery to your inbox; no physical shipping required.</p>
          <div style="display:flex;justify-content:flex-end;gap:16px;">
            <button type="submit" name="update" class="btn btn-secondary">Update Bag</button>
            <button type="submit" name="checkout" class="btn btn-caramel">Continue to Checkout ↗</button>
          </div>
        </div>
      </form>
    {% else %}
      <div style="text-align:center;padding:80px 0;">
        <p style="font-family:var(--font-serif);font-size:26px;">Your bag is currently empty.</p>
        <p style="color:var(--color-ink-muted);margin-block:12px 24px;">Explore Bea's Calm-Alone Kit to begin gentle, practical observations.</p>
        <a href="{{ routes.root_url }}#the-kit" class="btn btn-primary">Discover the Kit</a>
      </div>
    {% endif %}
  </div>
</section>

{% schema %}
{
  "name": "Main Cart",
  "settings": []
}
{% endschema %}
""")

write_file('sections/main-page.liquid', """
<article class="section-space">
  <div class="container" style="max-width:820px;">
    <h1>{{ page.title | escape }}</h1>
    <div style="margin-top:32px;font-size:16px;line-height:1.8;">
      {{ page.content }}
    </div>
  </div>
</article>

{% schema %}
{
  "name": "Main Page",
  "settings": []
}
{% endschema %}
""")

write_file('sections/main-product.liquid', """
{% render 'kit-includes' %}
{% section 'featured-product' %}
{% section 'kit-breakdown' %}
{% section 'steps-process' %}
{% section 'testimonials' %}
{% section 'faq-accordion' %}

{% schema %}
{
  "name": "Main Product",
  "settings": []
}
{% endschema %}
""")

# 6.13 FOOTER
write_file('sections/footer.liquid', """
<footer class="site-footer">
  <div class="container">
    <div class="footer-top-grid">
      <div class="footer-brand">
        <a href="{{ routes.root_url }}" class="brand-logo" aria-label="Bea and Co">
          bea <span>&</span> co<span class="dot"></span>
        </a>
        <p>Small steps. Thoughtful care. Practical digital resources for dogs and the people who care for them.</p>
      </div>

      <div class="footer-col">
        <h4>Navigation</h4>
        <ul class="footer-links">
          <li><a href="{{ routes.root_url }}#the-kit">The Calm-Alone Kit</a></li>
          <li><a href="{{ routes.root_url }}#inside">What's Inside</a></li>
          <li><a href="{{ routes.root_url }}#meet-bea">Meet Bea</a></li>
          <li><a href="{{ routes.root_url }}#reviews">Client Experiences</a></li>
          <li><a href="{{ routes.root_url }}#questions">Frequently Asked Questions</a></li>
          <li><a href="{{ routes.root_url }}#contact">Contact Support</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Veterinary & Care Notice</h4>
        <div class="footer-disclaimer-box">
          Owner-created educational support. Not veterinary medical diagnosis, individual clinical treatment, or a promise of specific behavioural recovery. Always seek veterinary care for sudden distress or injury.
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <span>© {{ 'now' | date: '%Y' }} {{ shop.name | escape }}. All rights reserved.</span>
      <span>Designed with quiet luxury for real companions.</span>
    </div>
  </div>
</footer>

{% schema %}
{
  "name": "Footer",
  "settings": []
}
{% endschema %}
""")

# ==========================================
# 7. TEMPLATES (OS 2.0 JSON)
# ==========================================
write_json('templates/index.json', {
    "sections": {
        "hero": { "type": "hero-banner", "settings": {} },
        "ticker": { "type": "values-ticker", "settings": {} },
        "breakdown": { "type": "kit-breakdown", "settings": {} },
        "featured": { "type": "featured-product", "settings": {} },
        "steps": { "type": "steps-process", "settings": {} },
        "story": { "type": "rich-story", "settings": {} },
        "testimonials": { "type": "testimonials", "settings": {} },
        "faq": { "type": "faq-accordion", "settings": {} },
        "contact": { "type": "contact-section", "settings": {} }
    },
    "order": [
        "hero",
        "ticker",
        "breakdown",
        "featured",
        "steps",
        "story",
        "testimonials",
        "faq",
        "contact"
    ]
})

write_json('templates/product.json', {
    "sections": {
        "main": { "type": "main-product", "settings": {} }
    },
    "order": ["main"]
})

write_json('templates/cart.json', {
    "sections": {
        "main": { "type": "main-cart", "settings": {} }
    },
    "order": ["main"]
})

write_json('templates/page.json', {
    "sections": {
        "main": { "type": "main-page", "settings": {} }
    },
    "order": ["main"]
})

# Other standard templates
write_file('templates/404.liquid', """
<section class="section-space" style="text-align:center;">
  <div class="container">
    <div class="eyebrow">404 ERROR</div>
    <h1>A little off the path.</h1>
    <p style="color:var(--color-ink-muted);margin:16px 0 28px;">We couldn't find the page you were looking for.</p>
    <a href="{{ routes.root_url }}" class="btn btn-primary">Return to Bea & Co.</a>
  </div>
</section>
""")

write_file('templates/search.liquid', """
<section class="section-space">
  <div class="container" style="max-width:800px;">
    <h1>Search Resources</h1>
    <form action="{{ routes.search_url }}" method="get" style="display:flex;gap:12px;margin-top:24px;">
      <input type="search" name="q" value="{{ search.terms | escape }}" placeholder="Search topics, questions..." style="flex:1;padding:12px;border:1px solid var(--color-border);border-radius:var(--radius-sm);">
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
  </div>
</section>
""")

# ==========================================
# 8. CONFIG & LOCALES
# ==========================================
SETTINGS_SCHEMA = [
    {
        "name": "theme_info",
        "theme_name": "Bea & Co. Premium",
        "theme_version": "2.0.0",
        "theme_author": "Bea & Co.",
        "theme_documentation_url": "https://github.com/Shouldy0/bea-co-shopify-theme",
        "theme_support_url": "https://bea-co.it"
    },
    {
        "name": "Brand Colors",
        "settings": [
            {
                "type": "color",
                "id": "color_bg",
                "label": "Background (Cream)",
                "default": "#F8F5EE"
            },
            {
                "type": "color",
                "id": "color_ink",
                "label": "Text & Primary (Deep Ink)",
                "default": "#1C2B25"
            },
            {
                "type": "color",
                "id": "color_caramel",
                "label": "Accent (Warm Caramel)",
                "default": "#9E5B32"
            }
        ]
    },
    {
        "name": "Cart Drawer",
        "settings": [
            {
                "type": "checkbox",
                "id": "enable_cart_drawer",
                "label": "Enable Ajax Slide-out Cart Drawer",
                "default": True
            }
        ]
    }
]

write_json('config/settings_schema.json', SETTINGS_SCHEMA)
write_json('config/settings_data.json', {
    "current": {
        "color_bg": "#F8F5EE",
        "color_ink": "#1C2B25",
        "color_caramel": "#9E5B32",
        "enable_cart_drawer": True
    }
})

write_json('locales/en.default.json', {
    "general": {
        "accessibility": {
            "skip_to_content": "Skip to content",
            "close": "Close"
        }
    },
    "sections": {
        "cart": {
            "title": "Your Bag",
            "empty": "Your bag is waiting.",
            "checkout": "Proceed to Secure Checkout"
        }
    }
})

write_json('locales/it.json', {
    "general": {
        "accessibility": {
            "skip_to_content": "Salta al contenuto",
            "close": "Chiudi"
        }
    },
    "sections": {
        "cart": {
            "title": "La tua borsa",
            "empty": "Il tuo carrello è vuoto.",
            "checkout": "Procedi al Checkout Sicuro"
        }
    }
})

# ==========================================
# 9. ZIP PACKAGE CREATION
# ==========================================
zip_path = ROOT / 'output/shopify/Bea-Calm-Shopify.zip'
if zip_path.exists():
    zip_path.unlink()

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in THEME_DIR.rglob('*'):
        if p.is_file() and not p.name.endswith('.zip') and not p.name.startswith('.'):
            z.write(p, p.relative_to(THEME_DIR))

print(f"✓ Premium theme built successfully! Packaged to: {zip_path}")
