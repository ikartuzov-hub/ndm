T.en = {
  eyebrow: "nDm · Note 3",
  h1: "Family and helping someone else",
  lead: "A spouse, children and dependants have the same right to the subsidy. But for their flights to go into the claim, they must be added to the profile once — and the portal says nothing about this anywhere. And if you are filing on behalf of someone else, one rule matters more than all the others.",
  blocks: [
    { t: "h2", v: "How to add family", p: "Done once, in the personal area, before submitting a claim. While the list is empty, family flights cannot be filed — at step four of the wizard their fields simply will not be there." },
    { t: "step", h: "The Situação Familiar section",
      p: "Home page → " + P("Aceder à Área Pessoal") + " → " + P("Situação Familiar") + ". This is where you upload the " + P("Prova de Agregado Familiar") + " — the certificate of household composition — and there is an " + P("Adicionar Membro") + " button. This is the only way to get the subsidy for a spouse's or children's flights.",
      src: "../img/b3.jpg", cap: "While the list is empty, family flights cannot be filed." },
    { t: "step", h: "The family member card",
      p: "The card lets you pick " + P("Parentesco") + ": " + P("Cônjuge") + ", " + P("Filho") + " or " + P("Dependente") + ", and attach the " + P("Comprovativo de Parentesco") + " — a marriage or birth certificate. A child's or spouse's beneficiary type can differ from your own: a student, for example, has their own share — €59 instead of €79.",
      src: "../img/b4.jpg", cap: "Comprovativo de Parentesco is required — the field carries an asterisk." },
    { t: "fields", v: [
      "Judging by how the portal checks the " + P("Comprovativo do IBAN") + ", family documents are also opened by a human operator — allow a day or two before submitting.",
      "To be honest: we have not yet submitted a family claim. What step four looks like with several passengers, and where the money goes — we will add this after the first real claim.",
      "TAP issues a separate invoice for each passenger. When requesting the documents, choose separate fiscal details so each person has their own file — how this is done is shown in <a class=\"lnk\" href=\"../../tap/\">Documentos TAP</a>.",
      "If a spouse or adult child is registered on the portal themselves, it is simpler to file two separate claims — each with their own " + P("Chave Móvel Digital") + "."
    ] },

    { t: "rule" },
    { t: "h2", id: "ajudar", v: "If you are filing for someone else", p: "Elderly parents, neighbours and acquaintances are often helped this way — and the portal allows it. But one rule matters more than all the others." },
    { t: "warn", h: "The phone and email must be their own",
      p: "In the profile and in the claim of the person you are helping, <b>their</b> phone number and <b>their</b> email must appear — the same ones used to obtain their " + P("Chave Móvel Digital") + ". Not yours.",
      p2: "A real case: a helper entered her own phone number and email into her sister's claim. The sister received the subsidy — but the helper's access to her own account broke, and she is now changing her email through Loja do Cidadão. If a person has no working email, set up a new one for them: twenty minutes now saves months of running around." },
    { t: "fields", v: [
      "Logging into the portal requires only their own " + P("Chave Móvel Digital") + " or their own citizen card. The confirmation code goes to their phone, so it is easier to do this together than to leave it for “later, on their own”.",
      "The IBAN — theirs. The money only goes to the account of the subsidy recipient; entering your own to “pass it on later” is not possible.",
      "Everything else in the claim is the same five screens as for yourself: <a class=\"lnk\" href=\"../\">The claim in five steps</a>."
    ] }
  ],
  refH: "More",
  refs: [
    ["../", "Instruction", "The claim in five steps", "Every portal screen and every field — with real screenshots and the invoice alongside."],
    ["../dinheiro/", "Note 1", "How much money and what for", "Categories of recipients, what is refunded and what is not, the discount and the cap that no longer exists."],
    ["../rejeitado/", "Note 2", "First login: “Rejeitado” is not a refusal", "Why the portal marks a refusal right at registration, and what the personal area holds."]
  ],
  shareBtn: "Send this page",
  shareTitle: "Family and helping someone else — nDm",
  shareText: "Flight subsidy for family, and if you are filing for someone else —",
  copied: "Link copied"
};
