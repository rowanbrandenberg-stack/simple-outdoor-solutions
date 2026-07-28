#!/usr/bin/env python3
"""
Generates the standalone policy / FAQ pages: faq.html, shipping.html, warranty.html.

Reuses the header, footer and announcement bar from build_products.py so all pages
stay identical. Every figure below is the real published policy from the old site's
/legal.html and product pages — see README.md.

Run:  python3 build_pages.py
"""
import build_products as bp

EMAIL = 'info@simpleoutdoorstore.com'


def page(slug, name, title, meta, h1, lede, toc, body):
    out = [bp.HEAD.format(title=title, meta=bp.esc_attr(meta), announce=bp.ANNOUNCE, name=name)]
    out.append(f'''
  <section class="pagehead">
    <div class="topo"></div>
    <div class="inner">
      <h1>{h1}</h1>
      <p class="lede">{lede}</p>''')
    if toc:
        out.append('\n      <nav class="toc">')
        out.append(''.join(f'<a href="#{i}">{t}</a>' for i, t in toc))
        out.append('</nav>')
    out.append('\n    </div>\n  </section>\n\n  <div class="doc">\n')
    out.append(body)
    out.append('\n  </div>\n')
    out.append(bp.FOOTER)
    with open(slug, 'w', encoding='utf-8') as f:
        f.write(''.join(out))
    print(f'wrote {slug}')


def faq_block(title, anchor, items):
    s = [f'    <section id="{anchor}">\n      <h2>{title}</h2>']
    for q, a in items:
        s.append(f'\n      <details><summary>{q}</summary>\n        <p>{a}</p></details>')
    s.append('\n    </section>\n')
    return ''.join(s)


# ----------------------------------------------------------------- shipping
shipping_body = f'''    <section id="rates">
      <h2>What shipping <em>costs</em></h2>
      <table class="terms">
        <thead><tr><th>Order</th><th>Service</th><th>Cost</th></tr></thead>
        <tbody>
          <tr><td>$100 and over</td><td>USPS Ground</td><td>Free</td></tr>
          <tr><td>Under $100</td><td>USPS Ground</td><td>$4 flat</td></tr>
          <tr><td>Any order</td><td>Priority, 2–3 business days</td><td>$14.99</td></tr>
        </tbody>
      </table>
      <p>The free-shipping threshold is calculated before tax and after any discounts.
      Priority is a flat $14.99 for the whole order, however many pieces are in it.</p>
    </section>

    <div class="rule"></div>

    <section id="turnaround">
      <h2>How fast it <em>goes out</em></h2>
      <p>Orders are usually processed within 24 hours. We ship six days a week, and most
      orders leave the same day — everything is made and packed in Flagstaff, so there's
      no warehouse in the middle slowing things down.</p>
      <p>If a size or colour is between batches we'll tell you when you order rather than
      let you wonder where it is.</p>
    </section>

    <div class="rule"></div>

    <section id="international">
      <h2>International orders</h2>
      <p>We don't ship outside the United States at this time. If you're overseas and want
      something, <a href="mailto:{EMAIL}">write to us</a> — we can at least tell you whether
      a retailer near you carries it.</p>
    </section>

    <div class="rule"></div>

    <section id="returns">
      <h2>Returns</h2>
      <p>You can return a product for a refund of the full purchase price, provided:</p>
      <ul>
        <li>It's within <b>30 calendar days</b> of your order confirmation email.</li>
        <li>The product is <b>new, unused, undamaged and in sellable condition</b>.</li>
        <li>You've asked us for a <b>Return Goods Authorization code</b> before sending
        anything back.</li>
      </ul>
      <p>Return shipping is on you — though the gear is light, so it rarely costs much.
      To start a return, email <a href="mailto:{EMAIL}">{EMAIL}</a> with your order details
      and we'll send the code and the address.</p>
      <h3>Something arrived wrong or broken?</h3>
      <p>That's not a return, that's our problem. Write to us and we'll sort it out.
      If it's a fault rather than a change of mind, see the
      <a href="warranty.html">warranty page</a>.</p>
    </section>
'''

# ----------------------------------------------------------------- warranty
warranty_body = f'''    <section id="terms">
      <h2>How long each piece is <em>covered</em></h2>
      <table class="terms">
        <thead><tr><th>Product</th><th>What it covers</th><th>Term</th></tr></thead>
        <tbody>
          <tr><td>Adventure Seat<sup>&reg;</sup></td><td>Stitching, materials, workmanship</td><td>Lifetime</td></tr>
          <tr><td>Outsak<sup>&reg;</sup> bags — UL, UL micro, Spectrum</td><td>Stitching, mesh, closure</td><td>3 years</td></tr>
          <tr><td>Bearikade Harness, Canyon Strap, FlagStrap</td><td>Stitching, webbing, hardware</td><td>1 year</td></tr>
          <tr><td>Slap Bag, Overkill Slap Bag, Trail Bags, Storage Sleeve</td><td>Stitching, fabric, closure</td><td>1 year</td></tr>
          <tr><td>Escape Pod Cooler, Escape Pod Bearikade Cooler, Escape Pouch</td><td>Stitching, insulation, closure</td><td>180 days</td></tr>
        </tbody>
      </table>
      <p>The Adventure Seat's term is not a figure of speech. The wording on the original
      catalogue is <b>"No time limit. Not ever."</b> and we're keeping it.</p>
    </section>

    <div class="rule"></div>

    <section id="covered">
      <h2>What's covered</h2>
      <p>Defects in <b>stitching, materials and workmanship</b>. Every piece leaves one
      bench having been checked by hand, so if a seam lets go, a strap pulls, or a
      hook-and-loop band stops holding in normal use, that's on us.</p>
      <p>Where a repair is the better answer than a replacement, we'll repair it. That's
      how gear should work, and it's how this gear has been handled since 2008.</p>

      <h3>What isn't covered</h3>
      <ul>
        <li><b>Commercial use.</b> These terms are for individual owners.</li>
        <li><b>Modified gear.</b> If it's been altered, we can't stand behind it.</li>
        <li><b>Ordinary wear, accidents and animals.</b> A bear, a rockfall, or a mule
        standing on it isn't a defect — but write to us anyway. We've seen worse, and we
        can usually do something.</li>
      </ul>
    </section>

    <div class="rule"></div>

    <section id="claim">
      <h2>Making a claim</h2>
      <p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with:</p>
      <ul>
        <li>What the product is, and roughly when you bought it</li>
        <li>A photograph or two of the problem</li>
        <li>A sentence on what happened</li>
      </ul>
      <p>There's no registration to complete and no form to hunt down. A person reads it
      and writes back.</p>
    </section>
'''

# ---------------------------------------------------------------------- FAQ
faq_body = (
    faq_block('Ordering, shipping &amp; returns', 'ordering', [
        ('How much is shipping?',
         f'Free USPS Ground on orders of $100 or more, $4 flat under that, and $14.99 for Priority (2–3 business days) on any order. Full detail on the <a href="shipping.html">shipping page</a>.'),
        ('How quickly do orders ship?',
         'Most orders leave within 24 hours, and we ship six days a week — often the same day. Everything is made and packed here in Flagstaff.'),
        ('Do you ship internationally?',
         'Not at this time. U.S. addresses only.'),
        ('Can I return something?',
         'Yes — within 30 calendar days of your order confirmation email, provided the product is new, unused and in sellable condition, and you ask us for a Return Goods Authorization code first. See the <a href="shipping.html#returns">returns section</a>.'),
        ('How do I reach a person?',
         f'Email <a href="mailto:{EMAIL}">{EMAIL}</a>, or use the form on the <a href="contact.html">contact page</a>. It goes to the same bench the gear is made on.'),
    ])
    + '\n    <div class="rule"></div>\n\n'
    + faq_block('The Outsak', 'outsak', [
        ('Will it stop a bear?',
         'No — and we won\'t pretend otherwise. The Outsak is designed for rodents and small animals: mice, squirrels, chipmunks, marmots, raccoons, skunks and ravens. Those are what get into food on the overwhelming majority of trips. Where a certified bear-resistant canister is required by regulation, carry one.'),
        ('Does it close with a drawstring?',
         'No. It closes with a black hook-and-loop top band — genuine Velcro&reg;, guaranteed not to mould, mildew or rot. There\'s no cord to fray, no cord lock to break, and nothing loose for an animal to chew at.'),
        ('Which size do I need?',
         'Go by volume. The Ultralight covers 4.3 L and 7.5 L at 2.5–3.4 oz, for solo and weekend trips. The Spectrum runs 9, 12.15, 20.5 and 25.7 L for groups and longer stretches. The <a href="outsak.html#sizes">full size chart</a> lists every dimension.'),
        ('How do I hang it, or stash it?',
         'In country without bears you can tuck it into a rock crevice or leave it under a tree. In bear country, hang it using proper technique. One thing not to do: <b>don\'t stake it to the ground</b> — that gives an animal leverage to work against. And never store it, or anything scented, in your tent or near where you sleep.'),
        ('Does it keep smells in?',
         'No, and it isn\'t meant to. Mesh isn\'t an odour barrier. If you want scent control, put an odour-proof liner bag inside it.'),
        ('Won\'t the mesh crush my food?',
         'The mesh is flexible, so it forms around what\'s inside rather than forcing a shape on it. For crumbs and powdered dinners, add a <a href="slap-bag.html">Slap Bag</a> liner.'),
        ('How do I clean it?',
         'Rinse and air dry. Stainless steel doesn\'t rot, rust out or hold odour, so the mesh tends to outlive the gear around it. Fold it flat in a <a href="storage-sleeve.html">Storage Sleeve</a> between trips.'),
    ])
    + '\n    <div class="rule"></div>\n\n'
    + faq_block('Coolers &amp; cozies', 'coolers', [
        ('Can I put ice straight in?',
         'Better not to. Use capped frozen bottles or sealed ice blocks. The <a href="escape-pod.html">Escape Pod</a> insulates but isn\'t waterproof — if you want loose ice, line it with a waterproof bag first. The <a href="escape-pod-bearikade.html">Bearikade Cooler</a> should not have ice in it at all.'),
        ('Do they work on hot food as well as cold?',
         'Yes. Reflectix&reg; reflects radiant heat in both directions, so it slows heat leaving as readily as heat arriving.'),
        ('Which cooler fits inside a Bearikade?',
         'The <a href="escape-pod-bearikade.html">Escape Pod Bearikade Cooler</a>, in four sizes matched to the Scout, Weekender, Blazer and Expedition. The standard Escape Pod is made for backpacking and isn\'t cut for canister fitment.'),
        ('Does the Escape Pouch come with food?',
         'No. Mountain House&reg; meals are sold separately. The Small is sized for Pro Paks and breakfasts, the Large for entrees and wraps.'),
    ])
    + '\n    <div class="rule"></div>\n\n'
    + faq_block('Straps &amp; harnesses', 'straps', [
        ('Should I leave the Bearikade Harness on overnight?',
         '<b>No.</b> Take it off before you store food for the night, before you leave food unattended, and any time the canister is out of arm\'s reach. Webbing left on gives a bear something to grip and may make it easier for one to carry the canister away.'),
        ('Does the harness come with a canister?',
         'No. Bearikade canisters are made by Wild Ideas and sold separately.'),
        ('Canyon Strap or FlagStrap?',
         'The <a href="canyon-strap.html">Canyon Strap</a> holds a bottle on your pack or a carabiner. The <a href="flagstrap.html">FlagStrap</a> is a crossbody or over-the-shoulder harness for carrying it on your body, hands free.'),
        ('What bottles do they fit?',
         'Wide-mouth Nalgene-style bottles in 1.0 L / 32 oz or 1.5 L / 48 oz. The Canyon Strap can be bought with a bottle included.'),
    ])
    + '\n    <div class="rule"></div>\n\n'
    + faq_block('Warranty &amp; care', 'warranty', [
        ('How long is the warranty?',
         'It depends on the piece: the Adventure Seat is covered for life, Outsak bags for three years, straps and liners for one year, and the Escape Pod and Escape Pouch for 180 days. Full terms on the <a href="warranty.html">warranty page</a>.'),
        ('How do I make a claim?',
         f'Email <a href="mailto:{EMAIL}">{EMAIL}</a> with the product, roughly when you bought it, a photo or two, and a sentence on what happened. No registration, no form.'),
        ('Do you repair gear?',
         'Where a repair is the better answer than a replacement, yes. That\'s usually the outcome we prefer too.'),
    ])
    + '\n    <div class="rule"></div>\n\n'
    + faq_block('Custom orders &amp; wholesale', 'custom', [
        ('Do you take custom orders?',
         'Sometimes. Custom sizes are noted as available on several products — the Bearikade Harness and the Bearikade Cooler among them. If you need something we don\'t list, describe it in a note and we\'ll tell you honestly whether we can make it.'),
        ('Do you sell wholesale?',
         'We work with a small number of shops. Use the form on the <a href="contact.html">contact page</a>, pick "Wholesale or retail inquiry", and tell us about your store.'),
        ('Where is the gear made?',
         'Cut, sewn and checked by hand in Flagstaff, Arizona, in small batches, since 2008. Made in the USA.'),
    ])
)


if __name__ == '__main__':
    page('shipping.html', 'Shipping &amp; Returns',
         'Shipping &amp; Returns',
         'Free USPS Ground shipping on orders over $100, $4 flat under that, and Priority for $14.99. Most orders ship within 24 hours from Flagstaff, Arizona. 30-day returns.',
         'Shipping &amp; <em>returns</em>.',
         'Everything is made and packed in Flagstaff, so orders leave from here — not from a warehouse three time zones away.',
         [('rates', 'Rates'), ('turnaround', 'Turnaround'), ('international', 'International'), ('returns', 'Returns')],
         shipping_body)

    page('warranty.html', 'Warranty',
         'Warranty',
         'Adventure Seat lifetime, Outsak bags three years, straps and liners one year, Escape Pod and Pouch 180 days. Defects in stitching, materials and workmanship.',
         'We stand behind <em>every stitch</em>.',
         'Every piece leaves one bench, checked by hand. If something fails in normal use, tell us and we will make it right.',
         [('terms', 'Terms'), ('covered', "What's covered"), ('claim', 'Making a claim')],
         warranty_body)

    page('faq.html', 'FAQ',
         'Frequently Asked Questions',
         'Answers on the Outsak, sizing, bears versus rodents, coolers, harness safety, shipping, returns and warranty — Simple Outdoor Solutions, Flagstaff, Arizona.',
         'Questions, <em>answered</em>.',
         'The ones we get asked most, grouped so you can find yours. If it is not here, write to us and it probably will be.',
         [('ordering', 'Ordering'), ('outsak', 'The Outsak'), ('coolers', 'Coolers'),
          ('straps', 'Straps'), ('warranty', 'Warranty'), ('custom', 'Custom')],
         faq_body)
