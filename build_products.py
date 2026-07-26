#!/usr/bin/env python3
"""
Generates the individual product pages for the Simple Outdoor Solutions site.

Every price, weight, dimension, capacity, material, colour and warranty length in
PRODUCTS below was read off the old site (simpleoutdoorstore.com) — see README.md
for the source URL of each. Nothing here is estimated. Where the old site publishes
only a price range (because the per-size prices live inside a PayPal widget that
isn't in the page HTML), the range is shown as a range rather than being split.

Run:  python3 build_products.py
"""

ANNOUNCE = ('Handmade in Flagstaff, Arizona since 2008 · '
            '<b>Free U.S. shipping over $100</b> · $4 flat under')

FOOT_TM = ('Outsak<sup>&reg;</sup> and Adventure Seat<sup>&reg;</sup> are registered trademarks of '
           'Simple Outdoor Solutions, LLC. Canyon Strap, Escape Pod Cooler, Escape Pouch, '
           'Overkill Slap Bag, Outsak UL Kits, Slap Bag and Storage Sleeve are trademarks of '
           'Simple Outdoor Solutions, LLC. Bearikade<sup>&reg;</sup> is a trademark of Wild Ideas. '
           'Nalgene<sup>&reg;</sup> is a trademark of Thermo Fisher Scientific. '
           'Reflectix<sup>&reg;</sup>, Dyneema<sup>&reg;</sup>, Cordura<sup>&reg;</sup>, '
           'YKK<sup>&reg;</sup> and Velcro<sup>&reg;</sup> are trademarks of their respective owners.')

WARNING = ('Some aspects of outdoor activities are potentially hazardous. Anyone using this '
           'equipment is personally responsible for their own safety in the outdoors.')

# ---------------------------------------------------------------- product data

PRODUCTS = [
  dict(
    slug='outsak-ul-kit', cat='kits',
    name='Outsak UL Kit', h1='The <em>UL Kit</em>.', tm='',
    title='Outsak UL Kit — Bag, Liner and Sleeve Together',
    meta='The Outsak UL Kit bundles an Outsak stainless wire-mesh bag, a Slap Bag liner and a matching Storage Sleeve. $64–71, handmade in Flagstaff, Arizona.',
    eyebrow='Everything together', img='outsak-ul-kit.jpg',
    cap='Bag, liner and sleeve',
    sub='One Outsak interlocking stainless-steel wire-mesh bag, one Slap Bag liner to keep crumbs off the mesh, and one matching Storage Sleeve for the off-season. Buying the three together costs less than buying them apart.',
    price='$64–71', pricenote='Choose your bag size and two colours',
    opts=[('Bag size', 'One of', [('UL micro', '4.3 L · 2.5 oz'), ('UL', '7.5 L · 3.4 oz')])],
    colors=('Liner &amp; sleeve colours', ['Brown', 'Tan', 'White']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'Three-year warranty on the Outsak; one year on the liner and sleeve',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('Why the kit', 'Bought separately the three pieces come to roughly <b>$75.50–$83.50</b>. '
             'The kit is <b>$64–71</b>. Same gear, same bench, less money.'),
    specs=[('Includes', 'One Outsak UL or UL micro, one Slap Bag liner, one Storage Sleeve'),
           ('Bag body', 'Flexible interlocking stainless-steel wire mesh'),
           ('Bag closure', 'Genuine Velcro&reg; — guaranteed not to mould, mildew or rot'),
           ('Liner', '30-denier silicone nylon with a Velcro&reg; slap top and Dyneema&reg; pull loops'),
           ('Sleeve', '30-denier silicone nylon, drawstring with a cord lock'),
           ('Liner &amp; sleeve colours', 'Brown, tan or white'),
           ('Warranty', 'Outsak 3 years · liner and sleeve 1 year each'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=None,
    feat=('What you get', 'Three pieces that were <em>designed together</em>.',
          [('The bag', 'The Outsak itself — steel mesh a rodent can chew at all night and never get through.'),
           ('The liner', 'A Slap Bag sized exactly to the bag, so crumbs and powdered dinners stay inside it.'),
           ('The sleeve', 'Roll the Outsak, slide it in, and the mesh stays true between trips.')]),
    faq=[('Which bag size should I pick?',
          'The UL micro holds 4.3 litres at 2.5 oz — solo and overnight. The UL holds 7.5 litres at 3.4 oz — longer solo trips or two people. The <a href="outsak.html#sizes">full size chart</a> has every dimension.'),
         ('Do the liner and sleeve have to match?',
          'They come in the same three colours — brown, tan and white — and you pick each one. Matching is optional.'),
         ('Is the liner necessary?',
          'Not strictly. The mesh works without it. The liner is there so crumbs, wrappers and powdered dinners stay on the inside of the mesh instead of falling through it.'),
         ('Is this bear-proof?',
          'No. The Outsak is built for rodents and small animals. It is not a certified bear-resistant container. Where a hard-sided canister is required by regulation, carry one.')],
    pairs=['outsak', 'bearikade-harness', 'adventure-seat'],
  ),

  dict(
    slug='slap-bag', cat='food',
    name='Slap Bag', h1='The <em>Slap Bag</em>.', tm='',
    title='Slap Bag — Liner Sack for the Outsak UL',
    meta='A 30-denier silicone nylon liner sack for the Outsak UL and UL micro, with a Velcro slap top and Dyneema pull loops. $25–29, handmade in Flagstaff, Arizona.',
    eyebrow='Keeps crumbs off the mesh', img='slap-bag.jpg',
    cap='30-denier sil nylon · Velcro slap top',
    sub='A liner sack cut to fit inside an Outsak UL exactly. Your dinner stays in the bag instead of falling through the mesh, and the mesh stays clean.',
    price='$25–29', pricenote='Two sizes · three colours',
    opts=[('Size', 'Fits', [('Small', 'Outsak UL micro · 0.4 oz'), ('Large', 'Outsak UL · 0.6 oz')])],
    colors=('Colours', ['Brown', 'Tan', 'White']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('Sizing is exact', 'The <b>Small</b> fits the Outsak <b>UL micro</b>. The <b>Large</b> fits the Outsak <b>UL</b>. '
             'These are liners for the Ultralight series only — they are not cut for the Outsak Spectrum.'),
    specs=[('Body', '30-denier silicone nylon'),
           ('Closure', 'Slap top with a genuine Velcro&reg; closure'),
           ('Pull loops', 'Dyneema&reg; side-pull loops and thumb tabs'),
           ('Weights', 'Small 0.4 oz · Large 0.6 oz, empty'),
           ('Dimensions', 'Small 10 &times; 12.5 in · Large 10 &times; 18.5 in'),
           ('Colours', 'Brown, tan, white'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Fits', 'Weight', 'Dimensions'],
               rows=[['Small', 'Outsak UL micro', '0.4 oz', '10 &times; 12.5 in'],
                     ['Large', 'Outsak UL', '0.6 oz', '10 &times; 18.5 in']],
               title='Two sizes, <em>one job each</em>.',
               intro='Pick the one that matches the Outsak you own. Weights are for the empty bag.'),
    feat=('Small details', 'The bits that make it <em>worth having</em>.',
          [('Slap it shut', 'A genuine Velcro&reg; slap top — one motion, no cord, nothing to freeze up.'),
           ('Dyneema pulls', 'Side-pull loops and thumb tabs in Dyneema&reg;, where the abrasion actually happens.'),
           ('Sil nylon body', '30-denier silicone nylon: light, slick, and easy to shake clean.')]),
    faq=[('Does it fit the Outsak Spectrum?',
          'No. Slap Bags are cut for the Outsak UL and UL micro. Nothing on the old catalogue claims Spectrum compatibility, so we won\'t either.'),
         ('Is it animal-proof on its own?',
          'No — it is a liner. The steel mesh of the Outsak is what stops animals. The Slap Bag keeps your food tidy inside it.'),
         ('How is this different from the Overkill Slap Bag?',
          'Same idea, much tougher materials. The <a href="overkill-slap-bag.html">Overkill</a> uses a full Dyneema&reg; body instead of sil nylon, in ten colours, for long-term caches and abusive loads.'),
         ('Can I get it as part of a kit?',
          'Yes — the <a href="outsak-ul-kit.html">Outsak UL Kit</a> bundles the bag, a liner and a sleeve for less than buying the three separately.')],
    pairs=['outsak', 'storage-sleeve', 'overkill-slap-bag'],
  ),

  dict(
    slug='overkill-slap-bag', cat='food',
    name='Overkill Slap Bag', h1='The <em>Overkill</em>.', tm='',
    title='Overkill Slap Bag — Dyneema Liner for the Outsak UL',
    meta='A full Dyneema liner sack for the Outsak UL and UL micro, with a 3/4-inch Velcro slap top. Ten colours, $55–65, handmade in Flagstaff, Arizona.',
    eyebrow='A Slap Bag on steroids', img='overkill-slap-bag.jpg',
    cap='Dyneema&reg; body · &frac34;-inch Velcro top',
    sub='The same liner, built out of Dyneema&reg; — the fabric backpackers reach for when abrasion resistance matters more than money. For long-term food caches and loads that punish a bag.',
    price='$55–65', pricenote='Two sizes · ten colours',
    opts=[('Size', 'Fits', [('Small', 'Outsak UL micro · 0.7 oz'), ('Large', 'Outsak UL · 1 oz')])],
    colors=('Colours', ['Gray', 'Black', 'White', 'Blaze Orange', 'Sunflower', 'Cranberry',
                        'Purple Haze', 'Frost Blue', 'Moroccan Blue', 'Camel']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('What the Overkill is <b>not</b>', 'It is <b>not bear resistant</b>. It is <b>not</b> intended as a stand-alone '
             'animal-resistant bag, and it is <b>not</b> meant to be hung on its own. It goes '
             '<i>inside</i> an Outsak — that is the bag doing the protecting.', True),
    specs=[('Body', 'Genuine Dyneema&reg; composite fabric hybrid'),
           ('Closure', 'Genuine &frac34;-inch Velcro&reg; brand hook-and-loop slap top'),
           ('Pull loops', 'Dyneema&reg; side-pull loops'),
           ('Weights', 'Small 0.7 oz · Large 1 oz, empty'),
           ('Dimensions', 'Small 10 &times; 12.5 in · Large 10 &times; 18.5 in'),
           ('Colours', 'Ten — gray, black, white, blaze orange, sunflower, cranberry, purple haze, frost blue, Moroccan blue, camel'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Fits', 'Weight', 'Dimensions'],
               rows=[['Small', 'Outsak UL micro', '0.7 oz', '10 &times; 12.5 in'],
                     ['Large', 'Outsak UL', '1 oz', '10 &times; 18.5 in']],
               title='Two sizes, <em>matched to the bag</em>.',
               intro='Same footprint as the standard Slap Bag; the difference is entirely in the fabric.'),
    feat=('How to use it', 'Food inside the liner, liner <em>inside the Outsak</em>.',
          [('01 &nbsp;Load it', 'Put the food in the Overkill Slap Bag and slap the Velcro&reg; top shut.'),
           ('02 &nbsp;Sleeve it', 'Put the whole liner inside an Outsak UL or UL micro — sold separately.'),
           ('03 &nbsp;Hang or hide it', 'Hang the Outsak, or conceal it. The steel mesh is what animals meet first.')]),
    faq=[('Is it worth more than double the standard Slap Bag?',
          'Only if you need it. Dyneema&reg; resists abrasion far better than sil nylon, which matters for long-term caches and rough loads. For a weekend with a freeze-dried dinner in it, the <a href="slap-bag.html">standard Slap Bag</a> is the sensible buy.'),
         ('Can I hang it by itself?',
          'No. It isn\'t built for that and it isn\'t animal resistant on its own. It belongs inside an Outsak.'),
         ('Does it fit the Outsak Spectrum?',
          'No — Small fits the UL micro, Large fits the UL. Ultralight series only.'),
         ('What is Dyneema, exactly?',
          'A composite fabric, formerly sold as Cuben Fiber, built around one of the strongest fibres available by weight. It is prized for abrasion and water resistance at almost no weight penalty.')],
    pairs=['outsak', 'slap-bag', 'trail-bag'],
  ),

  dict(
    slug='storage-sleeve', cat='accessories',
    name='Storage Sleeve', h1='The <em>Storage Sleeve</em>.', tm='',
    title='Storage Sleeve — Keeps a Rolled Outsak Tidy',
    meta='A 0.3 oz silicone nylon sleeve that holds a rolled Outsak UL or UL micro between trips. $11.50, three colours, handmade in Flagstaff, Arizona.',
    eyebrow='For the other fifty weeks', img='storage-sleeve.jpg',
    cap='0.3 oz · 30-denier sil nylon',
    sub='Roll the Outsak, slide it in, pull the drawstring. The mesh keeps its shape, the bag stays clean, and it takes up almost no room in a gear bin.',
    price='$11.50', pricenote='One size · three colours',
    opts=None,
    colors=('Colours', ['Brown', 'Tan', 'White']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('One size, two bags', 'The sleeve fits a rolled Outsak <b>UL</b> or <b>UL micro</b>. '
             'The Outsak itself is sold separately.'),
    specs=[('Body', '30-denier silicone nylon'),
           ('Closure', 'Drawstring with a cord lock'),
           ('Weight', '0.3 oz, empty'),
           ('Dimensions', '4 &times; 12.5 in'),
           ('Fits', 'A rolled Outsak UL or UL micro'),
           ('Colours', 'Brown, tan, white'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=None,
    feat=('Why bother', 'Steel mesh keeps its shape if you <em>let it</em>.',
          [('Holds the roll', 'Rolled and sleeved, the mesh doesn\'t get crushed flat under everything else in the bin.'),
           ('Keeps it clean', 'Out of the dust between trips, so you aren\'t rinsing it before you pack.'),
           ('Weighs nothing', 'Three-tenths of an ounce. You can carry it on the trip too if you want.')]),
    faq=[('Does the sleeve close with a drawstring?',
          'Yes — the sleeve does, with a cord lock. Note that the <a href="outsak.html">Outsak itself</a> does not: that closes with a Velcro&reg; top band, deliberately, so there is no cord for an animal to work at.'),
         ('Will it fit an Outsak Spectrum?',
          'It is specified for a rolled UL or UL micro. Nothing on the old catalogue claims Spectrum fitment.'),
         ('Can I get it in a kit?',
          'Yes — the <a href="outsak-ul-kit.html">Outsak UL Kit</a> includes a bag, a liner and a matching sleeve for less than buying all three separately.')],
    pairs=['outsak', 'outsak-ul-kit', 'slap-bag'],
  ),

  dict(
    slug='bearikade-harness', cat='straps',
    name='Bearikade Harness', h1='Bearikade <em>Harness</em>.', tm='',
    title='Bearikade Harness — Straps a Bearikade to Your Pack',
    meta='A two-piece polypropylene webbing harness that straps a Bearikade bear canister to a backpack. Four sizes, from $37.50, handmade in Flagstaff, Arizona.',
    eyebrow='For the trips that require a canister', img='bearikade-harness.jpg',
    cap='&frac34;-inch polypropylene webbing',
    sub='Two pieces slide over a Bearikade, clip together and cinch tight. Four D-rings, a carry handle, and dual side-release buckles — so the canister rides on the outside of your pack and the space stays on the inside.',
    price='$37.50–43.50', pricenote='With optional attachment straps $48.50–54.50',
    opts=[('Size', 'Fits', [('Small', 'Scout · 2.2 oz'), ('Medium', 'Weekender · 2.3 oz'),
                            ('Large', 'Blazer · 2.3 oz'), ('X-Large', 'Expedition · 2.4 oz')])],
    colors=None,
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty · custom sizes available on request',
              'Bearikade canisters by Wild Ideas sold separately'],
    callout=('Safety — please read', 'Take the harness <b>off</b> whenever you are storing food while you sleep, '
             'whenever your food is unattended, and whenever the canister is out of arm\'s reach. '
             'Left on, the webbing gives a bear something to grab, and it may make it easier for one to carry the canister away.', True),
    specs=[('Webbing', '&frac34;-inch polypropylene webbing'),
           ('Construction', 'Two pieces — slide over the canister, clip together, cinch tight'),
           ('Adjustment', 'Adjustable in four places; dual side-release buckles'),
           ('Attachment points', 'Four D-rings, usable as anchor points or strap guides'),
           ('Weights', 'Small 2.2 oz · Medium 2.3 oz · Large 2.3 oz · X-Large 2.4 oz'),
           ('Optional straps', '45 in long, &frac34; in wide, 1.4 oz the pair — sold in pairs'),
           ('Mould &amp; mildew', 'No growth'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Fits Bearikade', 'Weight'],
               rows=[['Small', 'Scout', '2.2 oz'], ['Medium', 'Weekender', '2.3 oz'],
                     ['Large', 'Blazer', '2.3 oz'], ['X-Large', 'Expedition', '2.4 oz'],
                     ['Custom', 'Custom Bearikade', 'Ask us']],
               title='Sized to the <em>canister</em>, not the pack.',
               intro='Match the harness to your Bearikade model. Need a size that isn\'t here? We make custom ones — get in touch.'),
    feat=('What it does', 'Bulky item outside means <em>more space inside</em>.',
          [('Easy on, easy off', 'Two pieces, dual side-release buckles. On and off without unpacking anything.'),
           ('Four D-rings', 'Use them as attachment points, or as guides for the optional 45-inch straps.'),
           ('A real handle', 'Comfortable in the hand for the walk from the car, or from camp to the hang.')]),
    faq=[('Does it come with a canister?',
          'No. Bearikade canisters are made by Wild Ideas and sold separately. This is the harness only.'),
         ('What are the optional attachment straps for?',
          'They lash the harnessed canister to a pack that has no obvious anchor points. They are 45 inches long, &frac34; inch wide, 1.4 oz for the pair, and sold in pairs.'),
         ('Should I leave the harness on overnight?',
          'No. Take it off before you store food for the night, before you leave food unattended, and any time the canister is out of arm\'s reach. Webbing left on gives a bear something to grip.'),
         ('Can I also cool the inside of the canister?',
          'Yes — the <a href="escape-pod-bearikade.html">Escape Pod Bearikade Cooler</a> is a Reflectix&reg; insert that fits inside a Scout, Weekender, Blazer or Expedition.')],
    pairs=['escape-pod-bearikade', 'outsak', 'adventure-seat'],
  ),

  dict(
    slug='canyon-strap', cat='straps',
    name='Canyon Strap', h1='Canyon <em>Strap</em>.', tm='',
    title='Canyon Strap — Nalgene Water Bottle Holder',
    meta='A reflective polypropylene webbing bottle holder for wide-mouth Nalgene-style bottles. Two sizes, five colours, from $23.50. Handmade in Flagstaff, Arizona.',
    eyebrow='Durable. Light. Minimal.', img='canyon-strap.jpg',
    cap='Dual reflective panels',
    sub='A webbing holder for a wide-mouth Nalgene, with a locking buckle and a 1.5-inch loop that takes a pack buckle or a carabiner. Carry more than one bottle without wrecking the plastic loop on the lid.',
    price='$23.50–25.50', pricenote='Or $34–37 with a Nalgene&reg; bottle included',
    opts=[('Size', 'Fits', [('1.0 L', '32 oz wide-mouth · 0.8 oz'), ('1.5 L', '48 oz wide-mouth · 0.9 oz')])],
    colors=('Colours', ['Slate', 'Clear', 'Glow-in-the-Dark', 'Gray', 'Spring Green']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty',
              'Available with or without a Nalgene&reg; bottle'],
    callout=('Two ways to buy', 'Strap only: <b>$23.50–25.50</b>. With a wide-mouth Nalgene&reg; bottle included: '
             '<b>$34–37</b>. Bottles are Nalgene-branded and made by Thermo Fisher Scientific.'),
    specs=[('Webbing', '&frac34;-inch polypropylene webbing'),
           ('Closure', 'Adjustable locking buckle'),
           ('Loop', '1.5-inch loop — takes a pack buckle or a carabiner'),
           ('Reflectivity', 'Dual reflective panels'),
           ('Weights', '1.0 L 0.8 oz · 1.5 L 0.9 oz'),
           ('Fits', 'Wide-mouth Nalgene-style bottles, 1.0 L / 32 oz or 1.5 L / 48 oz'),
           ('Colours', 'Slate, clear, glow-in-the-dark, gray, spring green'),
           ('Mould &amp; mildew', 'No growth'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Fits', 'Weight'],
               rows=[['1.0 L', '1 litre / 32 oz wide-mouth Nalgene-style', '0.8 oz'],
                     ['1.5 L', '1.5 litre / 48 oz wide-mouth Nalgene-style', '0.9 oz']],
               title='Two sizes, <em>two bottles</em>.',
               intro='Match the strap to the bottle you already carry.'),
    feat=('Details', 'Small things that stop <em>small annoyances</em>.',
          [('Locking buckle', 'Adjustable and locking, so the bottle stays put on rough ground.'),
           ('Reflective panels', 'Two of them — you can find your bottle at night without a headlamp hunt.'),
           ('Kind to your lid', 'Carry several bottles without hanging them off the moulded plastic loop until it snaps.')]),
    faq=[('Will it fit a narrow-mouth bottle?',
          'It is specified for wide-mouth Nalgene-style bottles in 1.0 and 1.5 litre. Narrow-mouth fitment isn\'t claimed.'),
         ('What is the difference from the FlagStrap?',
          'The Canyon Strap holds a bottle on your pack or a carabiner. The <a href="flagstrap.html">FlagStrap</a> is a full crossbody or over-the-shoulder harness for carrying the bottle on your body, hands free.'),
         ('Does glow-in-the-dark actually glow?',
          'It is one of the five webbing colours offered. It is a colour choice rather than a substitute for the reflective panels, which is what makes it findable by headlamp.')],
    pairs=['flagstrap', 'trail-bag', 'adventure-seat'],
  ),

  dict(
    slug='flagstrap', cat='straps',
    name='FlagStrap', h1='The <em>FlagStrap</em>.', tm='',
    title='FlagStrap — Hands-Free Crossbody Bottle Harness',
    meta='A crossbody or over-the-shoulder harness for wide-mouth Nalgene bottles, adjustable 33 to 63 inches, with dual reflective panels. $28–30, handmade in Flagstaff, Arizona.',
    eyebrow='Hands free', img='flagstrap.jpg',
    cap='Adjustable 33–63 inches',
    sub='Carry your water on your body instead of digging it out of a pack. Across the body or over one shoulder, adjustable from 33 to 63 inches, with reflective panels so you can find it after dark.',
    price='$28–30', pricenote='Nalgene&reg; bottles sold separately',
    opts=[('Size', 'Fits', [('1.0 L', '32 oz wide-mouth · 1.3 oz'), ('1.5 L', '48 oz wide-mouth · 1.4 oz')])],
    colors=None,
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('Bottle not included', 'The FlagStrap is the harness. Wide-mouth Nalgene&reg; bottles are sold separately. '
             'If you\'d rather buy the two together, the <a href="canyon-strap.html">Canyon Strap</a> has a with-bottle option.'),
    specs=[('Webbing', '&frac34;-inch polypropylene webbing'),
           ('Carry', 'Across the body or over the shoulder'),
           ('Adjustment', '33 to 63 inches'),
           ('Reflectivity', 'Dual reflective panels'),
           ('Weights', '1.0 L 1.3 oz · 1.5 L 1.4 oz'),
           ('Fits', 'Wide-mouth Nalgene-style bottles, 1.0 L / 32 oz or 1.5 L / 48 oz'),
           ('Mould &amp; mildew', 'No growth'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Fits', 'Weight', 'Adjustable'],
               rows=[['FlagStrap 1.0', '1 litre / 32 oz wide-mouth Nalgene-style', '1.3 oz', '33–63 in'],
                     ['FlagStrap 1.5', '1.5 litre / 48 oz wide-mouth Nalgene-style', '1.4 oz', '33–63 in']],
               title='Two sizes, <em>one long range of fit</em>.',
               intro='Thirty inches of adjustment covers a light shirt in August and a puffy in October.'),
    feat=('Why crossbody', 'Water you don\'t have to <em>stop for</em>.',
          [('No stopping', 'Reach down, drink, keep walking. The pack stays on your back and shut.'),
           ('Two ways to wear it', 'Across the body when you\'re moving, over one shoulder around camp.'),
           ('Findable at night', 'Dual reflective panels. Sweep a headlamp and there it is.')]),
    faq=[('Which size do I need?',
          'Match the bottle: FlagStrap 1.0 for a 1 litre / 32 oz wide-mouth Nalgene, FlagStrap 1.5 for a 1.5 litre / 48 oz.'),
         ('Will it fit over a jacket?',
          'It adjusts from 33 to 63 inches, so yes — that range is meant to cover everything from a t-shirt to an insulated layer.'),
         ('Canyon Strap or FlagStrap?',
          'FlagStrap if you want the bottle on your body, hands free. <a href="canyon-strap.html">Canyon Strap</a> if you want it clipped to your pack or a carabiner.')],
    pairs=['canyon-strap', 'adventure-seat', 'trail-bag'],
  ),

  dict(
    slug='escape-pod', cat='coolers',
    name='Escape Pod Cooler', h1='Escape Pod <em>Cooler</em>.', tm='&trade;',
    title='Escape Pod Cooler — Ultralight Soft-Sided Backpacking Cooler',
    meta='A double-walled Reflectix cooler that blocks 96% of radiant heat at 2.4 to 3.4 ounces. Three sizes, $25–33, handmade in Flagstaff, Arizona.',
    eyebrow='Hot or cold, both directions', img='escape-pod.jpg',
    cap='Reflectix&reg; · 96% reflective',
    sub='Double-walled Reflectix&reg; that blocks 96% of radiant heat, weighing between 2.4 and 3.4 ounces. Soft-sided, so it packs down to nothing when it\'s empty — and it works on hot food as well as cold.',
    price='$25–33', pricenote='Three sizes · optional Tyvek&reg; bag',
    opts=[('Size', 'Holds', [('Small', 'Two 12 oz cans · 2.4 oz'), ('Medium', 'Four 12 oz cans · 2.8 oz'),
                             ('Large', 'Six 12 oz cans · 3.4 oz')])],
    colors=None,
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              '180-day warranty',
              'The Large includes a bottle-protecting insert'],
    callout=('How to keep it cold', 'Cool it with <b>capped frozen bottles or sealed ice blocks</b>. '
             'If you want to use loose ice cubes, put a waterproof liner bag in first — the Pod is an '
             'insulator, not a waterproof tub.'),
    specs=[('Material', 'Reflectix&reg; — layers of 96% reflective metalised aluminium separated by a 5/16-inch enclosed air space'),
           ('Insulation', 'Double-walled; insulates from heat and cold'),
           ('Weights, pod only', 'Small 2.4 oz · Medium 2.8 oz · Large 3.4 oz'),
           ('Outside dimensions', 'Small 7.25 in dia &times; 4.5 in · Medium 7.25 &times; 6 in · Large 7.25 &times; 8.5 in'),
           ('Pack impact', 'Small 3 L · Medium 4 L · Large 5.7 L'),
           ('Storage capacity', 'Small 1.9 L · Medium 2.8 L · Large 4.25 L'),
           ('Optional Tyvek&reg; bag', 'High-density polyethylene fibres — tear resistant, water resistant, UV protected. 0.6–0.8 oz'),
           ('Puncture resistance', '60 lb/in'),
           ('Mould &amp; mildew', 'No growth'),
           ('Warranty', '180 days'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Best use', 'Outside', 'Storage', 'Weight'],
               rows=[['Small', 'Two 12 oz cans, or a solo day hike', '7.25 in dia &times; 4.5 in', '1.9 L', '2.4 oz'],
                     ['Medium', 'Four 12 oz cans, or a medium picnic', '7.25 in dia &times; 6 in', '2.8 L', '2.8 oz'],
                     ['Large', 'Six 12 oz cans, four bottles, or a small picnic', '7.25 in dia &times; 8.5 in', '4.25 L', '3.4 oz']],
               title='Three sizes, <em>measured in cans</em>.',
               intro='Weights are the pod alone. Add roughly 0.6–0.8 oz if you add the optional Tyvek&reg; bag.'),
    feat=('How it works', 'Ninety-six per cent of the radiant heat, <em>turned around</em>.',
          [('Reflectix core', 'Metalised aluminium either side of a 5/16-inch air gap. It reflects rather than absorbs.'),
           ('Works both ways', 'Keeps cold things cold and hot things hot. Same physics, either direction.'),
           ('Packs flat-ish', 'Soft-sided and pliable, so an empty Pod isn\'t carrying a fixed volume for you.')]),
    faq=[('Can I put ice cubes straight in?',
          'Better not to. Use capped frozen bottles or sealed ice blocks. If you do want loose ice, line it with a waterproof bag first — the Pod insulates but it isn\'t a waterproof container.'),
         ('Will it keep coffee hot?',
          'It insulates in both directions, so yes — it slows heat moving out as readily as heat moving in.'),
         ('What is the Tyvek bag for?',
          'It is an optional outer bag: tear resistant, water resistant and UV protected, adding roughly 0.6 to 0.8 oz depending on size.'),
         ('Will it fit inside a Bearikade?',
          'Not properly. The standard Escape Pod is made for backpacking, not for canister fitment — the <a href="escape-pod-bearikade.html">Escape Pod Bearikade Cooler</a> is the one cut to fit inside a Bearikade.')],
    pairs=['escape-pouch', 'escape-pod-bearikade', 'adventure-seat'],
  ),

  dict(
    slug='escape-pod-bearikade', cat='coolers',
    name='Escape Pod Bearikade Cooler', h1='Bearikade <em>Cooler</em>.', tm='&trade;',
    title='Escape Pod Bearikade Cooler — Reflectix Insert for a Bearikade',
    meta='A three-piece Reflectix cooler that fits inside a Scout, Weekender, Blazer or Expedition Bearikade. Four sizes, $49–77, handmade in Flagstaff, Arizona.',
    eyebrow='Made for the Bearikade', img='escape-pod-bearikade.jpg',
    cap='Shell, liner and lid',
    sub='Three pieces — shell, liner and lid — that turn the canister you are already required to carry into a cooler. It fits <i>inside</i> the Bearikade, uses very little of the space, and adds only a few ounces.',
    price='$49–77', pricenote='Four sizes · custom sizes on request',
    opts=[('Size', 'Fits', [('Small', 'Scout · 4.8 oz'), ('Medium', 'Weekender · 5.6 oz'),
                            ('Large', 'Blazer · 6.0 oz'), ('X-Large', 'Expedition · 7.0 oz')])],
    colors=None,
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              '180-day warranty · custom sizes available on request',
              'Bearikade canisters by Wild Ideas sold separately'],
    callout=('Dry cooler — no ice', 'This is an insulator against temperature change, not a waterproof tub. '
             'Use <b>frozen items</b> to hold the cold longer. <b>Don\'t use ice</b> — the cooler is not waterproof.', True),
    specs=[('Material', 'Reflectix&reg; — layers of 96% reflective metalised aluminium separated by a 5/16-inch enclosed air space'),
           ('Construction', 'Three pieces: shell, liner and lid'),
           ('Fitment', 'Fits <i>inside</i> a Scout, Weekender, Blazer or Expedition Bearikade'),
           ('Weights', 'Small 4.8 oz · Medium 5.6 oz · Large 6.0 oz · X-Large 7.0 oz'),
           ('Puncture resistance', '60 lb/in'),
           ('Mould &amp; mildew', 'No growth'),
           ('Warranty', '180 days'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Cooler size', 'Fits Bearikade', 'Weight'],
               rows=[['Small', 'Scout', '4.8 oz'], ['Medium', 'Weekender', '5.6 oz'],
                     ['Large', 'Blazer', '6.0 oz'], ['X-Large', 'Expedition', '7.0 oz'],
                     ['Custom', 'Custom Bearikade', 'Ask us']],
               title='Matched to <em>your canister</em>.',
               intro='Pick by Bearikade model. If yours is a custom size, get in touch and we\'ll cut one to fit.'),
    feat=('The idea', 'You\'re carrying the canister <em>anyway</em>.',
          [('Free space', 'Bulky item outside, more space inside — and now the inside is insulated too.'),
           ('Three pieces', 'Shell, liner and lid, so the whole interior is wrapped rather than just the base.'),
           ('A few ounces', 'Between 4.8 and 7.0 oz depending on size. Against a canister measured in pounds.')]),
    faq=[('Does it come with a Bearikade?',
          'No. Bearikade canisters are made by Wild Ideas and sold separately. This is the cooler insert only.'),
         ('Can I use ice?',
          'No. It isn\'t waterproof. Use frozen items — a capped frozen bottle, a sealed block — to hold the cold.'),
         ('Will the standard Escape Pod fit my Bearikade?',
          'Not properly. The <a href="escape-pod.html">original Escape Pod</a> is great for backpacking but is not cut to fit a Bearikade. This one is.'),
         ('How do I carry the canister on my pack?',
          'The <a href="bearikade-harness.html">Bearikade Harness</a> straps it to any pack — just take the harness off before you store food for the night.')],
    pairs=['bearikade-harness', 'escape-pod', 'outsak'],
  ),

  dict(
    slug='escape-pouch', cat='coolers',
    name='Escape Pouch', h1='Escape <em>Pouch</em>.', tm='&trade;',
    title='Escape Pouch — Freeze-Dried Meal Cozy',
    meta='A 1.1 oz Reflectix cozy for Mountain House freeze-dried meals, with a fold-back handle and a tight sealing flap. Original $24, v2.0 gusseted $32.',
    eyebrow='Eat hot food', img='escape-pouch.jpg',
    cap='Reflectix&reg; · fold-back handle',
    sub='Pour the water, seal the flap, walk away for a few minutes, and come back to a dinner that is actually hot and actually rehydrated. Possibly the lightest food-warming pouch made — 1.1 ounces.',
    price='$24 each', pricenote='v2.0 gusseted $32 each · one of each $42 / $57',
    opts=[('Design', 'Two varieties', [('Original', '$24 each'), ('v2.0 gusseted', '$32 each — stands up')]),
          ('Size', 'Fits', [('Small', 'Pro Paks &amp; breakfasts · 1.1 oz'), ('Large', 'Entrees &amp; wraps · 1.3–1.4 oz')])],
    colors=None,
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              '180-day warranty',
              'Mountain House&reg; meals sold separately'],
    callout=('Two designs', 'The <b>Original</b> is $24 each. <b>v2.0</b> adds a gusseted bottom so the pouch '
             'stands up on its own, at $32 each. Buy one of each size for <b>$42</b> (Original) or '
             '<b>$57</b> (v2.0).'),
    specs=[('Material', 'Reflectix&reg; with a hook-and-loop closure'),
           ('Original weights', 'Small 1.1 oz · Large 1.4 oz'),
           ('Original dimensions', 'Small 7 &times; 7&frac12; in · Large 8 &times; 7&frac34; in'),
           ('v2.0 weights', 'Small 1.1 oz · Large 1.3 oz'),
           ('v2.0 dimensions', 'Small 7 in top, 4&frac34; in bottom, 5&frac34; in high, 2&frac34; in gusset · Large 8 in top, 5&frac12; in bottom, 7&frac34; in high, 3&frac14; in gusset'),
           ('Small fits', 'Mountain House&reg; Pro Paks and breakfasts, or a quart Ziplock'),
           ('Large fits', 'Mountain House&reg; entrees and wraps, or two 12 oz cans'),
           ('Handle', 'Fold-back handle keeps your hand off the hot pouch'),
           ('Warranty', '180 days'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Design', 'Size', 'Fits', 'Weight', 'Price'],
               rows=[['Original', 'Small', 'Pro Paks &amp; breakfasts', '1.1 oz', '$24'],
                     ['Original', 'Large', 'Entrees &amp; wraps', '1.4 oz', '$24'],
                     ['v2.0', 'Small', 'Pro Paks &amp; breakfasts', '1.1 oz', '$32'],
                     ['v2.0', 'Large', 'Entrees &amp; wraps', '1.3 oz', '$32']],
               title='Two sizes, <em>two varieties</em>.',
               intro='v2.0 costs more because of the gusseted bottom — it stands up on its own while it steeps.'),
    feat=('Why it works', 'Heat that stays <em>in the bag</em>.',
          [('Tight seal', 'The sealing flap holds heat in until you\'re ready, instead of letting it out at the top.'),
           ('Fold-back handle', 'Both designs have one, so you can hold the thing when the food is at its hottest.'),
           ('v2.0 stands up', 'The gusseted bottom means it doesn\'t need a rock, a knee or a third hand.')]),
    faq=[('Does it come with food?',
          'No. Mountain House&reg; meals are made by Oregon Freeze Dry and sold separately. Small fits Pro Paks and breakfasts; Large fits entrees and wraps.'),
         ('Original or v2.0?',
          'v2.0 has a gusseted bottom and stands on its own, for $32 against $24. If you always have somewhere to prop a pouch, the Original does the same insulating job.'),
         ('Will it fit a non-Mountain House meal?',
          'The Small is also sized for a quart Ziplock bag, and the Large will take two 12 oz cans, so other pouches of similar size generally work.'),
         ('How long does it keep food hot?',
          'The old catalogue says "a lot longer" without publishing a figure, so we won\'t invent one. It is Reflectix&reg; with a sealing flap — the same material as the coolers.')],
    pairs=['escape-pod', 'adventure-seat', 'outsak'],
  ),

  dict(
    slug='trail-bag', cat='accessories',
    name='Trail Bag', h1='Trail <em>Bags</em>.', tm='',
    title='Trail Bags — Dyneema Zippered Gear Bags',
    meta='Dyneema composite gear bags with full-length YKK zippers, from half an ounce. Three sizes, ten colours, $24–35. Handmade in Flagstaff, Arizona.',
    eyebrow='Organise like a guide', img='trail-bag.jpg',
    cap='Dyneema&reg; body · YKK&reg; zipper',
    sub='Dyneema&reg; composite fabric and a full-length YKK&reg; zipper, from half an ounce empty. For kitchen kits, toiletries, cables, and the million other things that rattle loose in a pack.',
    price='$24–35', pricenote='Three sizes · ten colours',
    opts=[('Size', 'Empty weight', [('Small', '0.5 oz'), ('Medium', '0.7 oz'), ('Large', '1.0 oz')])],
    colors=('Colours', ['Gray', 'Black', 'White', 'Blaze Orange', 'Sunflower', 'Cranberry',
                        'Purple Haze', 'Frost Blue', 'Moroccan Blue', 'Camel']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'One-year warranty',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('Colour-code it', 'Ten colours, so the kitchen kit doesn\'t look like the first-aid kit at '
             'the bottom of a pack at dusk. The grabber handle means you can pull the right one out '
             'without unpacking the rest.'),
    specs=[('Body', 'Genuine Dyneema&reg; composite fabric hybrid'),
           ('Zipper', 'Genuine YKK&reg; full-length zipper with a metal slider'),
           ('Handle', 'Lightweight polypropylene grabber handle, water resistant'),
           ('Weights', 'Small 0.5 oz · Medium 0.7 oz · Large 1.0 oz, empty'),
           ('Water resistance', 'Dyneema&reg; is abrasion and water resistant'),
           ('Colours', 'Ten — gray, black, white, blaze orange, sunflower, cranberry, purple haze, frost blue, Moroccan blue, camel'),
           ('Warranty', 'One year'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Dimensions', 'Empty weight'],
               rows=[['Small', '8 &times; 4.5 &times; 2.0 in', '0.5 oz'],
                     ['Medium', '8 &times; 3.5 &times; 2.25 in', '0.7 oz'],
                     ['Large', '9.25 &times; 4.25 &times; 3.0 in', '1.0 oz']],
               title='Three sizes, <em>all featherweight</em>.',
               intro='Dimensions are as published on the old catalogue. If the size you want sits between two of these, ask us.'),
    feat=('Materials', 'The strongest fibre available, <em>by weight</em>.',
          [('Dyneema composite', 'Formerly sold as Cuben Fiber. Abrasion resistant, water resistant, and almost weightless.'),
           ('YKK zipper', 'Full length, metal slider, no fuss. The part that usually fails, chosen carefully.'),
           ('Grabber handle', 'Hook a finger and the bag comes out of a stuffed pack in one motion.')]),
    faq=[('Is it waterproof?',
          'Water resistant, not waterproof. Dyneema&reg; shrugs off rain and damp ground; it isn\'t a dry bag rated for submersion.'),
         ('Why is the Small listed as wider than the Medium?',
          'Because that is what the old catalogue publishes — Small at 8 &times; 4.5 &times; 2.0 in and Medium at 8 &times; 3.5 &times; 2.25 in. It looks like a typo in the original listing, and we are checking it rather than quietly changing the numbers.'),
         ('What do people use them for?',
          'Kitchen kits, toiletries, first aid, electronics and cables, repair kits. Anything you want to find in one grab.')],
    pairs=['overkill-slap-bag', 'adventure-seat', 'canyon-strap'],
  ),

  dict(
    slug='adventure-seat', cat='accessories',
    name='Adventure Seat', h1='Adventure <em>Seat</em>.', tm='&reg;',
    title='Adventure Seat — Insulated Cordura Sit Pad, Lifetime Warranty',
    meta='A half-inch closed-cell foam sit pad in a Cordura nylon shell, R-value 4, from 2.3 ounces. Four sizes, five colours, $22.50–36.50, lifetime warranty.',
    eyebrow='A nice place to sit', img='adventure-seat.jpg',
    cap='Cordura&reg; shell · R-value 4',
    sub='Half an inch of closed-cell foam in a Cordura&reg; nylon shell, with a DWR coating and a reflective strip so you can find it in the dark. Cold rock, wet log, gravel bar — it does not care.',
    price='$22.50–36.50', pricenote='Four sizes · five colours · lifetime warranty',
    opts=[('Size', 'Dimensions', [('Youth', '7 &times; 11 in · 2.30 oz'), ('Small', '9 &times; 12 in · 3.10 oz'),
                                  ('Medium', '10 &times; 14 in · 3.75 oz'), ('Large', '11 &times; 16 in · 4.9 oz')])],
    colors=('Colours', ['Yellow', 'Orange', 'Green', 'Clay', 'Black']),
    reassure=['Sewn by hand in Flagstaff, Arizona — made in the USA',
              'Lifetime warranty — no time limit, not ever',
              'Free U.S. shipping over $100 · $4 flat under'],
    callout=('Lifetime warranty', 'Not a decade, not "lifetime of the product". <b>No time limit. Not ever.</b> '
             'It covers defects in stitching, materials and workmanship — commercial use and '
             'modifications excepted.'),
    specs=[('Shell', '100% Cordura&reg; nylon — abrasion, tear and scuff resistant'),
           ('Core', 'Polyethylene closed-cell foam — won\'t rot, mould or mildew'),
           ('Thickness', '&frac12; inch'),
           ('Thermal resistance', 'R-value 4 — highly insulative'),
           ('Weather', 'Durable water repellent (DWR) coating'),
           ('Reflectivity', 'Reflective strip, so it\'s easier to find in the dark'),
           ('Weights', 'Youth 2.30 oz · Small 3.10 oz · Medium 3.75 oz · Large 4.9 oz (&plusmn;0.2 oz)'),
           ('Colours', 'Yellow, orange, green, clay, black'),
           ('Warranty', 'Lifetime'),
           ('Made', 'Cut and sewn by hand in Flagstaff, Arizona')],
    sizes=dict(head=['Size', 'Dimensions', 'Weight'],
               rows=[['Youth', '7 &times; 11 in', '2.30 oz'], ['Small', '9 &times; 12 in', '3.10 oz'],
                     ['Medium', '10 &times; 14 in', '3.75 oz'], ['Large', '11 &times; 16 in', '4.9 oz']],
               title='Four sizes, <em>half an inch thick</em>.',
               intro='All weights &plusmn;0.2 oz. Every size is the same half-inch of closed-cell foam and the same R-value 4.'),
    feat=('Why it lasts', 'Cordura&reg; outside, closed-cell foam <em>inside</em>.',
          [('Nearly indestructible', 'Cordura&reg; is the fabric used where abrasion and tearing are expected, not feared.'),
           ('Won\'t rot', 'Polyethylene closed-cell foam doesn\'t absorb water, so it can\'t rot, mould or mildew.'),
           ('R-value 4', 'Enough insulation that a cold rock stops being the reason you stand back up.')]),
    faq=[('Is the lifetime warranty real?',
          'The old catalogue\'s wording is "No time limit. Not ever." It covers defects in stitching, materials and workmanship. Commercial use and modifications are excluded.'),
         ('Which size should I get?',
          'Youth 7 &times; 11 in and Small 9 &times; 12 in are the packable end. Medium 10 &times; 14 in is the common choice for adults. Large 11 &times; 16 in is a proper camp seat at 4.9 oz.'),
         ('Can I use it as a sleeping pad?',
          'It is a sit pad — half an inch thick at R-value 4. Some people use one under their shoulders or hips as part of an ultralight sleep system, but it isn\'t sold as a sleeping pad.'),
         ('What is the reflective strip for?',
          'Finding it. Set a dark sit pad down at dusk and it disappears; a headlamp picks up the strip.')],
    pairs=['trail-bag', 'escape-pod', 'canyon-strap'],
  ),
]

# ------------------------------------------------------------------ cross-sell

CROSS = {
  'outsak':               ('The Outsak',            'outsak.html',               'outsak-macro.jpg',      'from $39',      'Animal-proof stainless wire mesh.'),
  'outsak-ul-kit':        ('Outsak UL Kit',         'outsak-ul-kit.html',        'outsak-ul-kit.jpg',     '$64–71',        'Bag, liner and sleeve together.'),
  'slap-bag':             ('Slap Bag',              'slap-bag.html',             'slap-bag.jpg',          '$25–29',        'Sil nylon liner for the Outsak UL.'),
  'overkill-slap-bag':    ('Overkill Slap Bag',     'overkill-slap-bag.html',    'overkill-slap-bag.jpg', '$55–65',        'Dyneema liner, ten colours.'),
  'storage-sleeve':       ('Storage Sleeve',        'storage-sleeve.html',       'storage-sleeve.jpg',    '$11.50',        'Holds a rolled Outsak, 0.3 oz.'),
  'bearikade-harness':    ('Bearikade Harness',     'bearikade-harness.html',    'bearikade-harness.jpg', 'from $37.50',   'Straps a canister to any pack.'),
  'canyon-strap':         ('Canyon Strap',          'canyon-strap.html',         'canyon-strap.jpg',      'from $23.50',   'Reflective Nalgene holder.'),
  'flagstrap':            ('FlagStrap',             'flagstrap.html',            'flagstrap.jpg',         '$28–30',        'Hands-free crossbody carry.'),
  'escape-pod':           ('Escape Pod Cooler',     'escape-pod.html',           'escape-pod.jpg',        '$25–33',        'Reflectix, hot or cold, 2.4 oz.'),
  'escape-pod-bearikade': ('Bearikade Cooler',      'escape-pod-bearikade.html', 'escape-pod-bearikade.jpg','$49–77',      'Fits inside a Bearikade.'),
  'escape-pouch':         ('Escape Pouch',          'escape-pouch.html',         'escape-pouch.jpg',      'from $24',      'Freeze-dried meal cozy, 1.1 oz.'),
  'trail-bag':            ('Trail Bag',             'trail-bag.html',            'trail-bag.jpg',         '$24–35',        'Dyneema, YKK zipper, 0.5 oz.'),
  'adventure-seat':       ('Adventure Seat',        'adventure-seat.html',       'adventure-seat.jpg',    '$22.50–36.50',  'Cordura sit pad, lifetime warranty.'),
}

# -------------------------------------------------------------------- template

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Simple Outdoor Solutions</title>
<meta name="description" content="{meta}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@10..48,300..800&family=Instrument+Sans:ital,wght@0,400..600;1,400&family=Instrument+Serif:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="product.css">
</head>
<body>
  <div class="announce">{announce}</div>

  <header>
    <nav class="nav">
      <a href="index.html" class="logo">
        <span class="sos"><img src="images/sos-logo.png" alt="Simple Outdoor Solutions"></span>
        <span class="full">Simple Outdoor Solutions<small>Flagstaff, AZ · est. 2008</small></span>
      </a>
      <div class="menu">
        <a href="shop.html">Shop</a>
        <a href="outsak.html">The Outsak</a>
        <a href="story.html">Our Story</a>
        <a href="contact.html">Contact</a>
      </div>
      <button class="cart" type="button">Cart <span class="badge">0</span></button>
    </nav>
  </header>

  <nav class="crumb"><a href="index.html">Home</a><span>/</span><a href="shop.html">Shop</a><span>/</span>{name}</nav>
"""

FOOTER = """
  <footer>
    <div class="foot">
      <div>
        <div class="brand"><span class="sos"><img src="images/sos-logo.png" alt="Simple Outdoor Solutions"></span> Simple Outdoor Solutions</div>
        <p>Handmade ultralight backpacking gear, sewn by hand in the high pines of Flagstaff, Arizona. Born in the Grand Canyon, made by hand since 2008.</p>
      </div>
      <div>
        <h4>Shop</h4>
        <a href="outsak.html">The Outsak</a><a href="shop.html#coolers">Coolers &amp; Cozies</a><a href="shop.html#straps">Straps &amp; Harnesses</a><a href="shop.html#accessories">Accessories</a><a href="shop.html#kits">Kits &amp; Bundles</a>
      </div>
      <div>
        <h4>Company</h4>
        <a href="story.html">Our Story</a><a href="contact.html#warranty">Warranty</a><a href="contact.html#shipping">Shipping &amp; Returns</a><a href="contact.html">Contact</a>
      </div>
      <div class="contact">
        <h4>Visit / Reach us</h4>
        <span>11600 N Onika Ln<br>Flagstaff, AZ</span>
        <a href="mailto:info@simpleoutdoorstore.com">info@simpleoutdoorstore.com</a>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Simple Outdoor Solutions, LLC</span>
      <span class="made">✦ Handmade in Flagstaff, AZ · Made in USA</span>
    </div>
    <p class="tm">""" + WARNING + """</p>
    <p class="tm">""" + FOOT_TM + """</p>
  </footer>

<script>
  const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('is-vis');io.unobserve(e.target)}})},{threshold:.12});
  document.querySelectorAll('.rev').forEach((el,i)=>{el.style.transitionDelay=((i%3)*70)+'ms';io.observe(el)});

  document.querySelectorAll('.swatches').forEach(group=>{
    const btns=[...group.querySelectorAll('button')];
    btns.forEach(b=>b.addEventListener('click',()=>{
      btns.forEach(o=>o.classList.remove('active'));
      b.classList.add('active');
      const out=group.parentElement.querySelector('.lab b');
      if(out) out.textContent=b.dataset.label||b.textContent.trim().split('\\n')[0];
    }));
  });

  let q=1;const qEl=document.getElementById('q');
  const plus=document.getElementById('plus'),minus=document.getElementById('minus');
  if(plus) plus.onclick=()=>{q=Math.min(q+1,20);qEl.textContent=q};
  if(minus) minus.onclick=()=>{q=Math.max(q-1,1);qEl.textContent=q};

  let n=0;const badge=document.querySelector('.cart .badge'),addBtn=document.getElementById('addBtn');
  if(addBtn) addBtn.addEventListener('click',()=>{
    n+=q;badge.textContent=n;
    addBtn.textContent='Added ✓';addBtn.style.background='var(--pine)';
    setTimeout(()=>{addBtn.textContent='Add to cart';addBtn.style.background=''},1100);
  });
</script>
</body>
</html>
"""


def esc_attr(s):
    return s.replace('&', '&amp;').replace('"', '&quot;')


def render(p):
    out = [HEAD.format(title=p['title'], meta=esc_attr(p['meta']),
                       announce=ANNOUNCE, name=p['name'])]

    # ---- pdp
    out.append('\n  <section class="pdp">\n    <div class="gallery">\n      <div class="frame">')
    out.append(f'<img src="images/{p["img"]}" alt="{esc_attr(p["name"])}">')
    out.append(f'<span class="cap">{p["cap"]}</span></div>\n    </div>\n')

    out.append('    <div class="buy">')
    out.append(f'\n      <div class="eyebrow">{p["eyebrow"]}</div>')
    h1 = p['h1']
    if p['tm']:
        mark = '<sup>' + p['tm'] + '</sup>'
        # the trademark mark belongs on the name, not after the full stop
        h1 = (h1[:-1] + mark + '.') if h1.endswith('.') else (h1 + mark)
    out.append(f'\n      <h1>{h1}</h1>')
    out.append(f'\n      <p class="sub">{p["sub"]}</p>')
    out.append('\n      <div class="priceline">'
               f'<span class="p">{p["price"]}</span>'
               f'<span class="note">{p["pricenote"]}</span></div>')

    if p['opts']:
        out.append('\n      <div class="opt">')
        for i, (label, sublabel, items) in enumerate(p['opts']):
            first = items[0][0]
            style = ' style="margin-top:1.3rem"' if i else ''
            out.append(f'\n        <div class="lab"{style}>{label} <b>{first}</b></div>'
                       '\n        <div class="swatches">')
            for j, (nm, sub) in enumerate(items):
                cls = ' class="active"' if j == 0 else ''
                out.append(f'<button{cls} data-label="{esc_attr(nm)}">{nm}<small>{sub}</small></button>')
            out.append('</div>')
        out.append('\n      </div>')

    if p['colors']:
        label, cols = p['colors']
        out.append(f'\n      <div class="opt">\n        <div class="lab">{label} <b>{len(cols)} available</b></div>'
                   '\n        <div class="colors">')
        out.append(''.join(f'<span>{c}</span>' for c in cols))
        out.append('</div>\n      </div>')

    out.append('''
      <div class="buyrow">
        <div class="qty">
          <button type="button" id="minus" aria-label="Decrease quantity">&minus;</button>
          <span id="q">1</span>
          <button type="button" id="plus" aria-label="Increase quantity">+</button>
        </div>
        <button class="btn btn-primary" id="addBtn">Add to cart</button>
      </div>''')

    out.append('\n      <ul class="reassure">')
    out.append(''.join(f'\n        <li>{r}</li>' for r in p['reassure']))
    out.append('\n      </ul>')

    if p['callout']:
        c = p['callout']
        warn = ' warn' if len(c) > 2 and c[2] else ''
        out.append(f'\n      <div class="callout{warn}">\n        <h3>{c[0]}</h3>\n        <p>{c[1]}</p>\n      </div>')

    out.append('\n    </div>\n  </section>\n')

    # ---- specs
    out.append('''
  <section class="specs">
    <div class="topo"></div>
    <div class="in">
      <div class="rev">
        <div class="kick">The numbers</div>
        <h2>Every figure <em>published</em>.</h2>
        <p class="blurb">Weights, dimensions, materials and warranty exactly as Simple Outdoor Solutions has always listed them. Nothing here is estimated.</p>
      </div>
      <div class="rev">
        <table class="spec">''')
    for th, td in p['specs']:
        out.append(f'\n          <tr><th>{th}</th><td>{td}</td></tr>')
    out.append('\n        </table>\n      </div>\n    </div>\n  </section>\n')

    # ---- size table
    if p['sizes']:
        s = p['sizes']
        out.append(f'''
  <section class="sizes" id="sizes">
    <div class="rev">
      <div class="kick">Pick a size</div>
      <h2>{s["title"]}</h2>
      <p class="intro">{s["intro"]}</p>
    </div>
    <div class="tablewrap rev">
      <table class="cmp">
        <thead><tr>''')
        for i, h in enumerate(s['head']):
            cls = ' class="us"' if h == 'Price' else ''
            out.append(f'<th{cls}>{h}</th>')
        out.append('</tr></thead>\n        <tbody>')
        for row in s['rows']:
            out.append('\n          <tr>')
            for i, cell in enumerate(row):
                if i == 0:
                    out.append(f'<th>{cell}</th>')
                elif s['head'][i] == 'Price':
                    out.append(f'<td class="us">{cell}</td>')
                else:
                    out.append(f'<td>{cell}</td>')
            out.append('</tr>')
        out.append('\n        </tbody>\n      </table>\n    </div>'
                   '\n    <p class="scrollhint">Scroll the table sideways for every column →</p>\n  </section>\n')

    # ---- feature band
    title, head, cols = p['feat']
    out.append(f'''
  <section class="feat">
    <div class="topo"></div>
    <div class="fb">
      <div class="rev"><div class="kick">{title}</div><h2>{head}</h2></div>
      <div class="fgrid">''')
    for i, (h, body) in enumerate(cols):
        no = '' if h[:2].isdigit() else f'<span class="no">{i+1:02d}</span> '
        out.append(f'\n        <div class="fcol rev"><h3>{no}{h}</h3><p>{body}</p></div>')
    out.append('\n      </div>\n    </div>\n  </section>\n')

    # ---- faq
    out.append('\n  <section class="faq">\n    <div class="rev"><div class="kick">Common questions</div>'
               '<h2>Before you buy.</h2></div>\n')
    for q, a in p['faq']:
        out.append(f'\n    <details class="rev"><summary>{q}</summary>\n      <p>{a}</p></details>')
    out.append('\n  </section>\n')

    # ---- pairs
    out.append('\n  <section class="pairs">\n    <div class="pw">'
               '\n      <div class="rev"><div class="kick">Goes with it</div></div>'
               '\n      <div class="pgrid">')
    for key in p['pairs']:
        nm, href, img, price, desc = CROSS[key]
        out.append(f'''
        <a class="pcard rev" href="{href}">
          <div class="ph"><img src="images/{img}" alt="{esc_attr(nm)}" loading="lazy"></div>
          <div class="i"><div class="n">{nm} <span class="pr">{price}</span></div><div class="d">{desc}</div></div>
        </a>''')
    out.append('\n      </div>\n    </div>\n  </section>\n')

    # ---- cta
    out.append('''
  <section class="cta">
    <div class="rev">
      <div class="kick" style="justify-content:center">Ounces matter</div>
      <h2>Carry less. <em>Go deeper.</em></h2>
      <p>Everything we make exists to give you more trail, more quiet, and more days out there.</p>
      <a href="shop.html" class="btn btn-primary">See the full catalog →</a>
    </div>
  </section>
''')

    out.append(FOOTER)
    return ''.join(out)


if __name__ == '__main__':
    for p in PRODUCTS:
        path = f'{p["slug"]}.html'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(render(p))
        print(f'wrote {path}')
    print(f'\n{len(PRODUCTS)} product pages generated')
