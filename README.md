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

## Confirmed from the old site (simpleoutdoorstore.com)

Outsak sizing and pricing is now **verified** against the old site's comparison
chart and product pages, and is live on `shop.html` and `outsak.html`:

| Size | Series | Capacity | Weight | Dimensions | Price |
|---|---|---|---|---|---|
| UL micro | Ultralight | 4.3 L | 2.5 oz | 10 × 13 in | $39 |
| UL | Ultralight | 7.5 L | 3.4 oz | 10 × 19 in | $43 |
| X-Small | Spectrum | 9 L | 6.5 oz | 14 × 14 in | $40 |
| Small | Spectrum | 12.15 L | 7.5 oz | 14 × 18 in | $44 |
| Medium | Spectrum | 20.5 L | 10 oz | 18 × 18 in | $50 |
| Large | Spectrum | 25.7 L | 11.5 oz | 18 × 22 in | $55 |

Also verified: **three-year warranty** on every Outsak · genuine **VELCRO®**
closure "guaranteed not to mold, mildew, or rot" · Ultralight uses 1-inch
polypropylene webbing, Spectrum uses 2-inch polyester seatbelt webbing with a UV
inhibitor · Spectrum comes in eight colours and ships with a free carry strap ·
protects against rock squirrels, rats, mice, chipmunks, raccoons, skunks, marmots.

Two earlier estimates were **wrong** and have been corrected: Outsak Ultralight
was showing "from $44" (actually $39) and Outsak Spectrum "from $59" (actually $40).

## Still to confirm with David

These prices are still estimates carried over from the handoff and are marked with
`data-est` in the HTML (visible via `?review=1`):

| Product | Shown | Status |
|---|---|---|
| Outsak UL Kits | $64–71 | confirmed, per handoff |
| Bearikade Harness (+straps $48.50–54.50) | from $37.50 | confirmed, per handoff |
| Escape Pod Bearikade Cooler | $49–77 | confirmed, per handoff |
| Escape Pod (soft cooler) | from $39 | **estimate** |
| Escape Pouch | from $18 | **estimate** |
| Canyon Strap | from $22 | **estimate** |
| FlagStrap | from $28 | **estimate** |
| Adventure Seat | from $32 | **estimate** |
| Trail Bag (Dyneema) | from $26 | **estimate** |
| Overkill Slap Bag / Slap Bag | $12–16 | **estimate** |
| Storage Sleeve | from $10 | **estimate** |

Also outstanding:

- **Phone number: removed.** (928) 637-4007 was Rowan's old home number and has been
  taken off every page. Email is now the only contact channel, which matches the old
  site's own advice that "the BEST way is by email." Add a business line later if wanted.
- **Email.** The old site's contact page gives info@simpleoutdoorstore.com and says
  email is the best way to reach them; its homepage footer shows jen@ instead.
  We use info@ throughout.
- **Free shipping.** An earlier draft advertised "Free U.S. shipping over $75" in the
  announcement bar and on the product page. Nothing on the old site supports that, so
  it has been replaced with the verified three-year warranty line. Put it back once
  David confirms the actual threshold.
- **Shipping turnaround, rates, return window** — placeholders on `contact.html`.
- **Reviews: now real and sourced.** The fabricated "verified buyer" testimonials are
  gone. The homepage now quotes three independent, linked sources:

  | Quote | Source | Note |
  |---|---|---|
  | "No critter slipped through this tight food security system." | Backpacker, Holiday Gift Guide 2011 | Four months of testing in OR & WA |
  | "I can't stop saying good things about it." | Jacob Williams, Trailspace, 4 stars, 2009 | Price Paid: $39.99 — a real customer |
  | "Security was never breached." | Gary Dunckel, Backpacking Light forum | Small/medium critters |

  **Verify the exact wording** against the three linked pages before launch — the quotes
  were gathered via an automated read and should be eyeballed once by a human.

  Note the Backpacker article lists the 2011 price of $36 and a weight of 3.7 oz, so a
  visitor who clicks through sees older figures than the site's current $39–43.

  Not used, but available if wanted: Chad Poindexter (Stick's Blog, 2010) wrote "a great
  product from a great company" — he was a beta tester, so that connection would need
  disclosing alongside the quote.

  Also worth knowing: both Trailspace listings carry a low-star review about customer
  service, not product quality (Michael, Aug 2015, refund/return dispute; and a 0.5-star
  review from May 2026 about a $7 PayPal fee kept from a refund). Those are business
  issues rather than website ones.
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
