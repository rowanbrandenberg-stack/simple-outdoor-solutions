# Simple Outdoor Solutions — website

Hand-coded static site. No framework, no build step. Every page is a single
self-contained HTML file with its CSS and JS inline; all images live in `/images`.

## Structure

```
index.html               Homepage — canyon hero, Outsak spotlight, featured grid
story.html               Our Story — canyon origin, workbench, small batches
shop.html                Full catalog — 14 products, filterable, deep-linkable
contact.html             Contact form + where we are + signposts
faq.html                 Grouped FAQ — ordering, Outsak, coolers, straps, warranty
shipping.html            Rates, turnaround, international, returns
warranty.html            Terms per product, what's covered, how to claim

outsak.html              Outsak UL + Spectrum — 6-size chart, canister comparison
outsak-ul-kit.html       Kit: bag + liner + sleeve
slap-bag.html            Sil nylon liner
overkill-slap-bag.html   Dyneema liner
storage-sleeve.html      Rolled-Outsak sleeve
bearikade-harness.html   Canister harness (+ safety notice)
canyon-strap.html        Nalgene bottle holder
flagstrap.html           Crossbody bottle harness
escape-pod.html          Soft-sided Reflectix cooler
escape-pod-bearikade.html Reflectix insert for a Bearikade
escape-pouch.html        Freeze-dried meal cozy
trail-bag.html           Dyneema zippered gear bags
adventure-seat.html      Cordura sit pad (lifetime warranty)

product.css              Shared stylesheet for the generated product + policy pages
build_products.py        Product page generator — edit PRODUCTS, re-run
build_pages.py           FAQ / shipping / warranty generator (imports build_products)
images/                  All optimized JPGs + the transparent SOS logo PNG
sos-site/                Older duplicate of index/story/images — safe to delete
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

Append `?review=1` to `shop.html` or `outsak.html` for an internal banner. Every price
is now sourced, so nothing is flagged as an estimate any more — the mechanism is kept
for the next round of unverified copy. Invisible to customers either way.

## Regenerating the product pages

The 12 generated product pages come from `build_products.py`. Edit the `PRODUCTS` dict
(prices, specs, FAQ, cross-sell), then:

    python3 build_products.py

Every figure in that dict came off the old site. Keep it that way — if you add a number
you can't point at a source for, mark it in the commit message.

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

## Every price is now sourced

Nothing on the site is an estimate any more. Each figure below was read off the old
site's own product page (linked). Where a page publishes only a **range**, the range
is shown as a range — the per-size prices live inside a PayPal widget that isn't in
the page HTML, so splitting the range would have been a guess.

| Product | Price | Warranty | Source page |
|---|---|---|---|
| Outsak UL / UL micro | $39 / $43 | 3 years | /outsakul_paypal.html + /outsak.html |
| Outsak Spectrum | $40 / $44 / $50 / $55 | 3 years | /outsak_spectrum_paypal.html |
| Outsak UL Kits | $64–71 | 3 yr bag, 1 yr parts | /outsak_kits.html |
| Slap Bag | $25–29 | 1 year | /slap_bags.html |
| Overkill Slap Bag | $55–65 | 1 year | /overkill_slap_bags.html |
| Storage Sleeve | $11.50 | 1 year | /storage_sleeve.html |
| Bearikade Harness | $37.50–43.50 (+straps $48.50–54.50) | 1 year | /bearikade_harness.html |
| Canyon Strap | $23.50–25.50, or $34–37 with a bottle | 1 year | /canyon_strap_water_bottle_holder.html |
| FlagStrap | $28–30 | 1 year | /flag_strap_water_bottle_holder.html |
| Escape Pod Cooler | $25–33 | 180 days | /escape_pod_cooler.html |
| Escape Pod Bearikade Cooler | $49–77 | 180 days | /escape_pod_bearikade_cooler.html |
| Escape Pouch | $24 (Original) / $32 (v2.0) | 180 days | /escape_pouch.html |
| Trail Bags | $24–35 | 1 year | /trail_bags_dyneema.html |
| Adventure Seat | $22.50–36.50 | **Lifetime** | /adventure_seat_by_simple_outdoor_solutions.html |

### Estimates that were wrong

Six of the handoff's estimates were off, two of them badly:

| Product | Was showing | Actually |
|---|---|---|
| Overkill Slap Bag | $12–16 | **$55–65** — off by roughly 4× |
| Slap Bag | $12–16 | **$25–29** — off by about half |
| Escape Pouch | from $18 | **$24** |
| Escape Pod Cooler | from $39 | **$25–33** — we were charging too much |
| Adventure Seat | from $32 | **$22.50–36.50** |
| Storage Sleeve | from $10 | **$11.50** |

### Shipping and returns — now the real policy

From /legal.html: **free USPS Ground on orders of $100 or more**, before tax and after
discounts. Under $100 ships **$4 flat**. Priority (2–3 business days) is **$14.99** for
the whole order. Most orders ship within 24 hours; they ship six days a week, often
same day. **No international orders.** Returns within **30 calendar days** of the order
confirmation email, product new and sellable, Return Goods Authorization code required
first, customer pays return shipping.

The announcement bar now reads "Free U.S. shipping over $100 · $4 flat under", which is
accurate. The earlier "over $75" line was invented and has been removed everywhere.

### Warranty tiers

Adventure Seat® **lifetime** ("No time limit. Not ever.") · Outsak® **3 years** ·
harnesses, straps, liners, trail bags, sleeves **1 year** · Escape Pod and Escape Pouch
**180 days**. Commercial use and modified gear excluded.

### Trademarks

Outsak® and Adventure Seat® are registered. Canyon Strap, Escape Pod Cooler, Escape
Pouch, Overkill Slap Bag, Outsak UL Kits, Slap Bag and Storage Sleeve are ™. Bearikade®
is Wild Ideas, Nalgene® is Thermo Fisher, and Reflectix®, Dyneema®, Cordura®, YKK® and
Velcro® belong to their respective owners. The footer of every product page carries the
attribution.

## Still worth a look

- **Trail Bag dimensions.** The old catalogue lists Small as 8 × 4.5 × 2.0 in and Medium
  as 8 × 3.5 × 2.25 in — the Small is *wider* than the Medium. That looks like a typo in
  the original listing. We publish the figures as given and say so in the FAQ rather than
  quietly changing them. Worth confirming with David.
- **Conflicting shipping claims on the old site.** Some pages say "free shipping on all
  USA orders", others say "over $100". /legal.html is the most specific, so we followed it.
- **Per-size prices.** Only the Outsak and Escape Pouch publish exact per-variant prices.
  Everything else shows a range. When Shopify goes in, each variant will need its own price.
- **Outsak UL page copy bug on the old site**, for reference: its warranty line reads
  "Outsak Spectrum is warrantied for 3 years" on the UL page. Not carried over.
- **Adventure Seat is missing from the old site's own gear nav** — it's only reachable via
  the stale sitemap. It's on the new Shop page properly.
- **Four dead links on the old site** (bandanas, nap sack, sticker, Nat Geo maps) all 404.
  Not carried over.
- **Reviews.** See the sourced quotes below — verify wording before launch.
- **Gallery photos** — `outsak.html` still uses studio and macro shots. Swap in `5.png`
  (open, holding trail food), `6.png` (filled, on a canyon rock), `7.png` (hung from a
  juniper), `8.png` (beside a bear canister); swap targets are marked in the gallery block.
- **Positioning note.** The old About Us page says "our business is family-owned, and every
  piece of gear is family-made". Per the locked positioning, we do **not** use that framing.
  It also has no founding story and never mentions the Grand Canyon — the canyon framing is
  ours.


## Privacy / contact policy

The street address (11600 N Onika Ln) has been **removed from every page** at the
owner's request, along with the phone number and any "visit us" wording. The only
contact channel on the site is **info@simpleoutdoorstore.com**, plus the form on
contact.html which composes a mailto to that address. Footers say "Handmade in
Flagstaff, Arizona" with no street address.

## Image aspect ratios

Every product studio shot is 1100×825 (4:3) and drops straight into the 4:3 frames.
Two are square (1254×1254) and were being cropped: `outsak-macro.jpg` and
`outsak-stack.jpg`. They now have companions — `outsak-macro-4x3.jpg` and
`outsak-stack-4x3.jpg` — recomposed onto a 4:3 canvas so the whole bag is visible
and centred, with the tan backdrop extended around it rather than a letterbox bar.

Use the **4x3 files in 4:3 containers** (the Outsak gallery frame, the shop cross-sell
band, the "goes with it" cards) and the **square originals in square or portrait
containers** (the homepage spotlight, the gallery thumbnails, the story page shot).
`build_products.py` already points the cross-sell table at the 4:3 version.

## Reviews on the homepage

| Quote | Source | Note |
|---|---|---|
| "No critter slipped through this tight food security system." | Backpacker, Holiday Gift Guide 2011 | Four months of testing in OR & WA |
| "I can't stop saying good things about it." | Jacob Williams, Trailspace, 4 stars, 2009 | Price Paid: $39.99 — a real customer |
| "Security was never breached." | Gary Dunckel, Backpacking Light forum | Small/medium critters |

**Verify the exact wording** against the three linked pages before launch — the quotes
were gathered via an automated read and should be eyeballed once by a human. Note the
Backpacker article lists the 2011 price of $36, older than the current $39–43.

Available if wanted: Chad Poindexter (Stick's Blog, 2010) wrote "a great product from a
great company" — he was a beta tester, so that connection would need disclosing.

Both Trailspace listings also carry low-star reviews about customer service rather than
product quality. Business issues, not website ones.

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
