T.en = {
  eyebrow: "nDm · Note 1",
  h1: "How much money and what for",
  lead: "The portal decides on its own whether you are eligible, and calculates the amount itself. But what exactly it refunds and what it does not is hidden behind a small ⓘ icon at step four — and that is usually why the totals do not add up.",
  blocks: [
    { t: "h2", v: "A real example", p: "A real claim: Funchal → Lisbon → Funchal, TAP, Madeira resident. Approved and paid. Each of the five figures above is copied from the airline invoice — the file " + P("AIE APXIE026_….pdf") + " that TAP sends on request. Which line each one comes from — in <a class=\"lnk\" href=\"../#passo4\">step 4 of the guide</a>." },
    { t: "calc", head: "How the refund is calculated",
      rows: [
        ["Outbound fare · 202.00 − 5.00 discount", "197.00 €"],
        ["Return fare", "90.00 €"],
        ["Passenger fee · YP", "35.03 €"],
        ["Fuel surcharge · YQ", "115.00 €"],
        ["Security fee · PT", "7.12 €"],
        ["Custo", "444.15 €", "sum"],
        ["Copagamento", "− 79.00 €", "sum"],
        ["Reembolso", "365.15 €", "sum big"]
      ],
      note: P("Copagamento") + " of €79 is the share the passenger pays themselves; it is deducted always, from every claim. For students it is €59." },

    { t: "h2", v: "Who is eligible", p: "The portal decides this from data held by Autenticação.gov, the tax office and social security. You cannot influence it, but it helps to understand which category you have been placed in: it determines the size of your share. A quick check in three questions — <a class=\"lnk\" href=\"/?p=check\">on the first page</a>." },
    { t: "who", v: [
      ["Residente", "Registered in the autonomous region. The portal automatically checks that you have lived here for at least six months."],
      ["Residente Equiparado na RA Madeira", "Moved less than six months ago and works in the region in a public-sector role."],
      ["Estudante na RA Açores", "A student studying in the Azores."],
      ["Estudante no Continente/Estrangeiro", "A student from the islands studying on the mainland or abroad."]
    ] },
    { t: "p", v: "A foreign national needs a valid " + P("título de residência") + " — the portal reminds you of this in a separate pop-up at login. A spouse, children and dependants are added to the profile beforehand, and their flights then go into the same claim: <a class=\"lnk\" href=\"../familia/\">Family</a>." },

    { t: "h2", v: "What is refunded and what is not", p: "The list from that ⓘ icon. Everything in the left column is copied from the invoice into the step-four fields; everything in the right column is not, even if it appears on the invoice." },
    { t: "cols", yesH: "Refunded",
      yes: [
        "Economy-class fare",
        "Airport fees",
        "Ticketing fee · " + P("XP") + " or " + P("OB"),
        "Fuel surcharge · " + P("YQ"),
        "Passenger fee · " + P("YP"),
        "Carbon fee · " + P("J9"),
        "Security fee · " + P("PT"),
        "Baggage included in the fare",
        "Seat selection, check-in and priority boarding — if included in the fare"
      ],
      noH: "Not refunded",
      no: [
        "Travel insurance",
        "Excess baggage",
        "Bank charges",
        "Add-ons purchased after the ticket",
        "Any option not included in the base price",
        "Baggage, seat selection, check-in and priority — if bought separately"
      ] },
    { t: "warn", h: "Two rules that are easy to miss",
      p: "The ticketing fee is capped at €35 one way and €70 return. On the invoice it may be labelled " + P("XP") + ", " + P("YR") + ", " + P("OB") + " or " + P("DV") + ".",
      p2: "If you flew on miles or a gift voucher, enter only the euros that actually left your card." },

    { t: "h2", v: "The discount and the check", p: "The fee fields on the portal carry no asterisk: they go through blank without an error, and on a normal ticket that is about €157 — over a third of the refund. So checking your own figures is the only safeguard." },
    { t: "warn", h: "The discount is deducted from the outbound fare",
      p: "In our invoice, the fare calculation line gives an outbound fare of <b>202.00</b>, and page one shows a " + P("DESCONTO") + " of <b>5.00</b>. What went into the portal was <b>197.00</b> — 202.00 minus the discount. " + P("Custo") + " came out at 444.15, exactly matching the invoice's " + P("TOTAL") + ", and the claim was approved.",
      p2: "The check is simple: add up both fares and all the fees. It should come to exactly the " + P("TOTAL") + " on page one of the invoice. If it comes to more, the discount was not deducted." },

    { t: "h2", v: "The cap is gone", p: "Until 6 June 2026 the refund was capped at €400 per trip. Lei n.º 23/2026 removed that cap, but the official service page still says €400 — and two of our own claims, above that figure, were paid in full, minus " + P("Copagamento") + ". In detail, with a difference calculator — <a class=\"lnk\" href=\"/?p=news\">What changed in the law</a>." }
  ],
  refH: "More",
  refs: [
    ["../", "Instruction", "The claim in five steps", "Every portal screen and every field — with real screenshots and the invoice alongside."],
    ["../rejeitado/", "Note 2", "First login: “Rejeitado” is not a refusal", "Why the portal marks a refusal right at registration, and what the personal area holds."],
    ["../familia/", "Note 3", "Family and helping someone else", "How to add a spouse and children — and rule number one if you are filing for someone else."]
  ],
  shareBtn: "Send this page",
  shareTitle: "How much money and what for — nDm",
  shareText: "Flight subsidy: what is refunded and what is not —",
  copied: "Link copied"
};
