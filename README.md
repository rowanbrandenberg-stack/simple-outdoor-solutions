# Simple Outdoor Solutions — website

Hand-coded static site. No framework, no build step. Every page is a single
self-contained HTML file with its CSS and JS inline; all images live in `/images`.

## Structure

```
index.html      Homepage — cinematic canyon hero, Outsak spotlight, featured grid
story.html      Our Story — canyon origin, workbench, small batches
shop.html       Full catalog — 14 products, filterable, deep-linkable
outsak.html     Outsak product detail — gallery, specs, comparison, FAQ
contact.html    Contact form, address/phone/email, shipping & warranty
images/         All optimized JPGs + the transparent SOS logo PNG
sos-site/       Older duplicate of index/story/images — safe to delete
```

Deployed with GitHub Pages from the repo root.

## Design system

| Token | Value |
|---|---|
| sand | `#f3ebdd` |
| sand-2 | `#e9dcc6` |
| warm ink | `#211b13` |
| canyon rust | `#bf5327` |
| rust-deep | `#9a3f1c` |
| ponderosa pine | `#2f5d4e` / deep `#1e3f34` |
| gold | `#e2a44b` |
| stone | `#8a7d68` |

Type: **Bricolage Grotesque** (display), **Instrument Sans** (body),
**Space Mono** (spec numbers, eyebrows), **Instrument Serif** italic (lyrical accents).
Motifs: topographic contour lines, film-grain overlay, mono spec callouts.

Positioning: lead with place + craft + Grand Canyon origin. Never put the maker
front and centre; no portraits.

## Deep links

`shop.html` reads the URL hash as a category filter:
`#food` · `#coolers` · `#straps` · `#accessories` · `#kits`

## Review mode

Append `?review=1` to `shop.html` or `outsak.html` to highlight every value that
still needs confirming (estimated prices, the Outsak weight figure). Invisible to
customers, so it can ship as-is.

## Still to confirm with David

Prices below are estimates carried over from the old site and are marked with
`data-est` in the HTML:

| Product | Shown | Status |
|---|---|---|
| Outsak UL Kits | $64–71 | confirmed |
| Bearikade Harness (+straps $48.50–54.50) | from $37.50 | confirmed |
| Escape Pod Bearikade Cooler | $49–77 | confirmed |
| Outsak Ultralight | from $44 | **estimate** |
| Outsak Spectrum | from $59 | **estimate** |
| Escape Pod (soft cooler) | from $39 | **estimate** |
| Escape Pouch | from $18 | **estimate** |
| Canyon Strap | from $22 | **estimate** |
| FlagStrap | from $28 | **estimate** |
| Adventure Seat | from $32 | **estimate** |
| Trail Bag (Dyneema) | from $26 | **estimate** |
| Overkill Slap Bag / Slap Bag | $12–16 | **estimate** |
| Storage Sleeve | from $10 | **estimate** |

Also outstanding:

- **Outsak weight** — `outsak.html` shows "from 2.8 oz". Confirm per size.
- **Sizes and capacities** — no dimensions are published anywhere yet, because none
  were verified. Add them to the spec table on `outsak.html` once known.
- **Shipping turnaround, rates, return window** — placeholders on `contact.html`.
- **Reviews** — the three testimonials on `index.html` are still placeholders and
  are labelled as such on the page. Replace with real reviews before launch.
- **Gallery photos** — `outsak.html` currently uses the studio and macro shots.
  Swap in `5.png` (open, holding trail food), `6.png` (filled, on a canyon rock),
  `7.png` (hung from a juniper), `8.png` (beside a bear canister) when available;
  the swap targets are marked with an HTML comment in the gallery block.

## Contact form

`contact.html` composes a `mailto:` to info@simpleoutdoorstore.com, so it needs no
backend on GitHub Pages. To move to a hosted form later, point the submit handler
at a Formspree or Netlify Forms endpoint — the comment above the form marks the spot.

## Accuracy note

The Outsak is described throughout as rodent- and critter-proof, **not** as a
certified bear-resistant container, and `outsak.html` says so explicitly. Please
keep that distinction — it matters legally and for customers entering units where
a hard-sided canister is required.

The Outsak closes with a **black hook-and-loop top band**, never a drawstring.
