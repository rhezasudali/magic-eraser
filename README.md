# magic-eraser

This repository contains two independent projects:

1. **Magic Background Eraser** — a Streamlit app (`app.py`) that removes image
   backgrounds with AI.
2. **Meridian Textiles landing page** — a static marketing site
   (`index.html`, `styles.css`, `script.js`). See below.

---

## Magic Background Eraser (Streamlit)

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Meridian Textiles — Landing Page

A responsive, single-page marketing site for a fictional textile manufacturing
company. Built with plain HTML, CSS, and vanilla JavaScript — no build step.

### Sections

- **Hero** — headline, key stats, and primary calls to action
- **Trusted by** — brand logo strip
- **Capabilities** — vertically integrated manufacturing stages
- **Products** — fabric categories with woven-texture swatches
- **Sustainability** — environmental commitments and metrics
- **Process** — four-step workflow from sample to shipment
- **About** — company story, certifications, and a customer quote
- **Contact** — quote-request form with client-side validation
- **Footer** — navigation, contact links, and legal

### Run locally

It's fully static — open `index.html` directly, or serve it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

### Files

| File         | Purpose                                  |
|--------------|------------------------------------------|
| `index.html` | Page markup and content                  |
| `styles.css` | Design system, layout, and responsive UI |
| `script.js`  | Mobile nav, footer year, form handling   |

### Customizing

- **Brand colors** live as CSS custom properties in `:root` (`styles.css`).
- **Fonts** are Fraunces (display) and Inter (body), from Google Fonts.
- The contact form is a front-end simulation. To make it real, replace the
  `setTimeout` in `script.js` with a `fetch()` POST to your backend or a form
  service (Formspree, Netlify Forms, etc.).

> Company name, stats, certifications, and contact details are placeholder copy
> and should be replaced with real information before going live.