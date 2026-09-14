T.en = {
  eyebrow: "nDm · Note 2",
  h1: "First login: red “Rejeitado” is not a refusal",
  lead: "On first registration the portal automatically sets the status to Rejeitado. Before you have clicked anything. People see “refused” and give up — but it only means “profile not filled in”.",
  blocks: [
    { t: "h2", v: "One registration, minute by minute", p: "This is the " + P("Histórico do Registo") + " from the personal area. It reads bottom to top." },
    { t: "fig", src: "../img/b6.jpg", cap: "Histórico do Registo in the personal area. Reads bottom to top." },
    { t: "fields", v: [
      P("Rejeitado") + " — 11:55. The system created the profile from Autenticação.gov data and immediately set it to refused. The user had done nothing at this point.",
      "The user uploads the " + P("Comprovativo do IBAN") + " and enters " + P("IBAN") + " and phone number — 12:00.",
      P("Pendente") + " — 12:00. The status changes itself, as soon as the profile is complete.",
      P("Validado") + " — 13:38. A human operator opened the document, approved it, and the status turned green. An hour and forty-three minutes passed between “refused” and approval."
    ] },
    { t: "warn", h: "What to do if you see Rejeitado",
      p: "Home page → " + P("Aceder à Área Pessoal") + " → " + P("Alterar Dados") + ". Enter the " + P("IBAN") + " and phone number, save. Then upload the bank confirmation of the account.",
      p2: "After that, wait: the portal switches the status itself once a human operator opens your document. Until the status is " + P("Validado") + ", it is too early to submit a claim — the payment will not go through." },

    { t: "h2", v: "The personal area: what is actually there", p: "The " + P("Aceder à Área Pessoal") + " button is tucked away at the bottom of the home page, under the card with your details. Behind it are four sections that gov.pt does not describe anywhere." },
    { t: "step", h: "What can be changed",
      p: "The " + P("Alterar Dados") + " button opens a form where only three fields are editable: beneficiary type, " + P("IBAN") + " and " + P("Telefone/Telemóvel") + ". Name, NIF, date of birth, email, postcode and town are permanently grey.",
      src: "../img/b1.jpg", cap: "The three boxed fields are the only things the portal lets you change." },
    { t: "step", h: "Profile attachments",
      p: "The " + P("Anexos") + " section holds the " + P("Comprovativo do IBAN") + " — the bank confirmation of the account. Without it, payments do not go through, and it is approved by a human operator, not the system.",
      src: "../img/b2.jpg", cap: "The green Aprovado tag is set by an operator by hand." },
    { t: "step", h: "Family",
      p: P("Situação Familiar") + " — this is where a spouse, children and dependants are added, so that their flights go into the same claim. How this is done — <a class=\"lnk\" href=\"../familia/\">Family</a>." },
    { t: "step", h: "Claims",
      p: P("Histórico de Pedidos") + " — a list of your claims with their statuses. This is also where " + P("Correção Solicitada") + " notices appear. What the statuses mean and how long to wait — <a class=\"lnk\" href=\"../#depois\">“After submitting” in the guide</a>." },

    { t: "h2", v: "Phone and email — your own only", p: "The phone number and email in the profile must be your own — the same ones used to obtain " + P("Chave Móvel Digital") + ". If you are helping someone else and enter your own contact details into their profile, access to your own account breaks. In detail — <a class=\"lnk\" href=\"../familia/#ajudar\">if you are filing for someone else</a>." }
  ],
  refH: "More",
  refs: [
    ["../", "Instruction", "The claim in five steps", "Every portal screen and every field — with real screenshots and the invoice alongside."],
    ["../dinheiro/", "Note 1", "How much money and what for", "Categories of recipients, what is refunded and what is not, the discount and the cap that no longer exists."],
    ["../familia/", "Note 3", "Family and helping someone else", "How to add a spouse and children — and rule number one if you are filing for someone else."]
  ],
  shareBtn: "Send this page",
  shareTitle: "First login: “Rejeitado” is not a refusal — nDm",
  shareText: "The subsidy portal showed “Rejeitado”? That is not a refusal —",
  copied: "Link copied"
};
