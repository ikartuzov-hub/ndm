T.en = {
  eyebrow: "nDm · Subsídio de Mobilidade",
  h1: "The claim in five steps",
  lead: "The State refunds island residents most of the ticket price. The money lands in your bank account — if you get through five portal screens and correctly copy seven figures from the airline invoice. Here is every screen and every field — and where people lose the money.",
  by: "Free, no registration. We do not file anything for you — we show you how to file it yourself.",
  facts: ["5 screens", "7 figures from the invoice", "≈ 15 days to the money"],

  needH: "What to prepare before you start",
  needP: "The form will not let you go further without these, and you cannot go back and add something mid-claim — the draft loses fields. So gather everything first, then start.",
  need: [
    "Two PDFs from TAP: the <b>invoice</b> " + P("AIE APXIE026_….pdf") + " (with the Declaração para efeitos de Subsídio de Mobilidade attachment) and the <b>travel proof</b> " + P("BoardingProofTAP_….pdf") + ". How to request both — <a class=\"lnk\" href=\"../tap/\">Documentos TAP</a>.",
    P("IBAN") + " and phone number entered in the portal profile, and a " + P("Comprovativo do IBAN") + " approved by an operator. If red " + P("Rejeitado") + " appeared on your first login — that is not a refusal: <a class=\"lnk\" href=\"./rejeitado/\">First login</a>.",
    P("Chave Móvel Digital") + " or a citizen card with a card reader — there is no other way into the portal.",
    "If your spouse or children flew with you, they must be added to the profile beforehand: <a class=\"lnk\" href=\"./familia/\">Family</a>."
  ],
  needNote: "Whether you are eligible at all — <a class=\"lnk\" href=\"/?p=check\">three questions</a>, half a minute. What exactly is refunded and how much — <a class=\"lnk\" href=\"./dinheiro/\">How much money and what for</a>.",

  exH: "Following one real example",
  exP: "Below is a real claim: Funchal → Lisbon → Funchal, TAP, Madeira resident. Approved and paid. Every figure in the steps is taken from its invoice, and we show which line each one comes from.",
  calcHead: "How the portal calculated the refund",
  calc: [
    ["Outbound fare · 202.00 − 5.00 discount", "197.00 €"],
    ["Return fare", "90.00 €"],
    ["Passenger fee · YP", "35.03 €"],
    ["Fuel surcharge · YQ", "115.00 €"],
    ["Security fee · PT", "7.12 €"],
    ["Custo", "444.15 €", "sum"],
    ["Copagamento", "− 79.00 €", "sum"],
    ["Reembolso", "365.15 €", "sum big"]
  ],
  calcNote: P("Copagamento") + " of €79 is the share the passenger pays themselves; it is always deducted. Where the other figures come from, and what is never refunded — <a class=\"lnk\" href=\"./dinheiro/\">How much money and what for</a>.",

  openBtn: "Open the portal",
  copyBtn: "Copy the address",
  copiedLink: "Address copied",
  openHint: "On a computer the portal opens in a separate window on the right — the instructions stay on the left. Login only via " + P("Chave Móvel Digital") + " or a citizen card. On the portal home page, click " + P("Submeter Pedido") + ".",

  stepsH: "The five wizard screens",
  stepsP: "The list of steps is visible on the left of the portal. You cannot click through it — you can only go back with the " + P("Anterior") + " button, one step at a time. Worth knowing in advance.",
  steps: [
    {
      h: "Dados Gerais do Beneficiário",
      p: "The first screen asks nothing. All six fields are grey — name, NIF, postcode, town, email and phone come from Autenticação.gov, and cannot be changed here. There is only one live element.",
      imgs: [{ src: "img/c1.jpg", cap: "The only thing you can click on the first step." }],
      fields: [
        P("Residente Equiparado há menos de 6 meses a exercer funções públicas na Região Autónoma?") + " — ticked only if you moved to the region less than six months ago and work here in a public-sector role. In every other case, leave it alone."
      ],
      after: "There is no “back” button on the first step — only " + P("Seguinte") + ".",
      warn: {
        h: "The postcode and town stay blank",
        p: P("Código Postal") + " and " + P("Localidade") + " cannot be filled in here or in the personal area — the portal shows the fields but does not let you edit them.",
        p2: "This does not affect eligibility: in our claim the postcode is blank and the status is " + P("Validado") + "."
      }
    },
    {
      h: "Informação bancária",
      p: "One field. It too is grey: the portal fills in whatever is in the profile.",
      imgs: [{ src: "img/c2.jpg", cap: "The whole step — one read-only field." }],
      fields: [
        P("IBAN") + " — read-only. Changed in " + P("Área Pessoal") + " → " + P("Alterar Dados") + " (what that looks like and how — <a class=\"lnk\" href=\"./rejeitado/\">First login</a>)."
      ],
      warn: {
        h: "Stop if the account is not yours or the field is blank",
        p: "The money will go to this exact IBAN. Go back to the home page, open " + P("Área Pessoal") + ", fix the account — and only then start the claim."
      }
    },
    {
      h: "Dados da Viagem",
      p: "The longest screen. It splits into three parts: the invoice, the route and two files. We go through each part, and show where every figure in the invoice comes from.",
      imgs: [{ src: "img/c3.jpg", cap: "Part one: the invoice." }],
      fields: [
        P("NIF da Entidade Emissora") + " — the tax number of whoever issued the invoice. For TAP this is " + P("500278725") + ". If a foreign travel agency issued the invoice, the portal asks for " + P("000000000") + ".",
        P("Data de Emissão do Bilhete") + " — the ticket issue date. The portal warns: not earlier than " + P("15/01/2026") + ".",
        P("Número da Fatura") + " — the full invoice number, including the letter prefix: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — the date of the invoice itself. Not the ticket issue date, and not the departure date."
      ],
      imgs2: [{ src: "img/f1.jpg", cap: "Page one of the invoice, AIE APXIE026_….pdf, which TAP sends on request. This is where the number, dates and airline NIF come from." }],
      fields2: [
        P("Número da Fatura") + " — the full number, with the letters: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — the date to the right of the number. In this example, " + P("2026-08-22") + ".",
        P("NIF da Entidade Emissora") + " — " + P("500278725") + ". No need to look it up: it is printed in the invoice header, in the line “Matriculada na CRC de Lisboa e NIPC”.",
        P("Data de Emissão do Bilhete") + " — column " + P("DT.EMISSÃO") + ". Here " + P("2026-07-31") + ": the ticket was issued on 31 July, and the invoice on 22 August. Different dates, and the portal asks for both.",
        P("E-Ticket") + " — column " + P("NR. DOC.") + ", thirteen digits, starting with " + P("047") + ". Needed at step four.",
        "The " + P("TOTAL") + " column is not entered into the portal, but it is what you check against: the " + P("Custo") + " the portal calculates itself must match this figure.",
        "The " + P("DESCONTO") + " column — if there is a discount here, note it. At step four you will have to subtract it from the fare, or the total will not add up."
      ],
      imgs3: [{ src: "img/c4.jpg", cap: "Part two: the route. Below is an identical Volta block." }],
      fields3: [
        P("Origem Inicial da Viagem") + " and " + P("Destino Final da Viagem") + " — these are regions, not airports: " + P("Madeira") + ", " + P("Lisboa") + ".",
        P("Data de Partida") + " and " + P("Hora de Partida") + " are required. " + P("Data de Chegada") + " and " + P("Hora de Chegada") + " carry no asterisk, but fill them in: the operator checks them against the boarding pass. Dates and times come from the segments on page two of the invoice (shown at step 4).",
        P("Companhia Aérea") + " and " + P("Número de Reserva") + " — the six-letter booking code, the portal suggests " + P("EX: WAAXYI") + ". This is not the ticket number.",
        P("Acrescentar Escala?") + " — " + P("Sim") + " only if there was a connection within a single ticket."
      ],
      imgs4: [{ src: "img/c5.jpg", cap: "Part three: two files. They must not be mixed up." }],
      fields4: [
        P("Fatura(s) de Viagem emitidas por Companhia Aérea ou intermediário") + " — this is where the <b>invoice</b> goes: for TAP, the file " + P("AIE APXIE026_….pdf") + ".",
        P("Título(s) de Viagem: Bilhete ou Confirmação de Reserva") + " — this is where the <b>travel proof</b> goes: " + P("BoardingProofTAP_….pdf") + ".",
        P("Adquiriu a sua viagem através de agência ou outro intermediário de viagens?") + " — " + P("Não") + " if the ticket was bought directly from the airline."
      ],
      warn: {
        h: "This is what people mix up most",
        p: "The two documents are not interchangeable. And an extra document is also an error: a real correction notice reads " + P("O documento submetido não é necessário") + " — “the attached document is not needed”.",
        p2: "How to request both documents from TAP is shown in <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a> — opens in a new tab."
      }
    },
    {
      h: "Dados dos passageiros",
      p: "This is where the money appears. Seven figures, all seven copied from the invoice — the file " + P("AIE APXIE026_….pdf") + " that TAP sends on request (how to request it — <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>). Which fees are refunded and which are not — <a class=\"lnk\" href=\"./dinheiro/\">How much money and what for</a>.",
      imgs: [{ src: "img/c6.jpg", cap: "Ticket numbers. The screenshot shows what a saved draft can end up like." }],
      fields: [
        P("Vai participar na viagem?") + " — must be set to " + P("Sim") + ". While it is set to " + P("Não") + ", there are no amount fields on the screen at all, and the refund shows as €0.",
        P("E-Ticket (Ida)") + " and " + P("E-Ticket (Volta)") + " — ticket numbers, thirteen digits, starting with " + P("047") + " for TAP.",
        "In this screenshot, " + P("E-Ticket (Volta)") + " is blank and " + P("Valor da Tarifa (Volta)") + " is zero. This is what a draft looks like after being saved and reopened."
      ],
      imgs2: [{ src: "img/c7.jpg", cap: "Seven figures. The fee codes are the same as on the TAP invoice." }],
      fields2: [
        P("Valor da Tarifa (Ida)") + " and " + P("(Volta)") + " — the bare fare, before fees.",
        P("Taxa de Emissão de Bilhete - XP") + " — on the invoice it may appear as " + P("YR") + ", " + P("OB") + " or " + P("DV") + ". Capped at €35 one way and €70 return.",
        P("Taxa de Serviço a Passageiros - YP") + ", " + P("Sobretaxa de Combustível - YQ") + ", " + P("Taxa de Carbono - J9") + " and " + P("Sobretaxa de Segurança - PT") + " — copied from the invoice line by line, by code. The fee fields carry no asterisk: they go through blank without an error, and on a normal ticket that is about €157 — over a third of the refund.",
        "Use a comma, not a full stop. Where there is no value, enter 0."
      ],
      imgs3: [{ src: "img/f2.jpg", cap: "Page two of the invoice — Declaração para efeitos de Subsídio de Mobilidade. All seven figures are here." }],
      fields3: [
        "<b>Fare calculation line</b> — the only place in any document where the fare is split into “outbound” and “return”. " + P("FNC TP LIS202.00TP FNC90.00EUR292.00END") + " reads left to right: from FNC on flight TP to LIS — <b>202.00</b>; then flight TP to FNC — <b>90.00</b>; total 292.00. The first figure goes into " + P("Valor da Tarifa (Ida)") + ", the second into " + P("Valor da Tarifa (Volta)") + ".",
        "<b>Fees by code.</b> " + P("YQ") + " 115.00 → " + P("Sobretaxa de Combustível - YQ") + "; " + P("PT") + " 7.12 → " + P("Sobretaxa de Segurança - PT") + "; " + P("YP") + " 35.03 → " + P("Taxa de Serviço a Passageiros - YP") + ". The " + P("FARE") + " line is the sum of the fares and is not entered into the portal. If a code is missing from the list, the portal field stays zero.",
        "The " + P("Tarifa") + " column on page one of the invoice already includes YQ — that figure is not entered into the fare field, or the fuel surcharge is doubled and the claim is sent back for correction.",
        P("XVYV7W/1A") + " — the booking code. The first six characters go into " + P("Número de Reserva") + " at step three.",
        "Segments: flight number, date, airports. This is where the departure and arrival dates for step three come from, and it also shows which leg is outbound and which is return."
      ],
      imgs4: [{ src: "img/c9.jpg", cap: "The portal does the sum itself. You still have to check it." }],
      fields4: [
        "At the bottom the portal adds up " + P("Custo") + ", subtracts " + P("Copagamento") + " and shows " + P("Reembolso Total") + ". If the total looks odd, a field has almost always been missed — the portal is rarely wrong."
      ],
      warn: {
        h: "Trap: Guardar Rascunho on a return trip",
        p: "We saved a draft at €208, left and came back — the return leg had vanished: " + P("E-Ticket (Volta)") + " blank, " + P("Valor da Tarifa (Volta)") + " zero, the total down to €118.",
        p2: "And it was not a display glitch: after leaving, the claims list also showed €118. Fill it in and submit in one sitting."
      },
      warn2: {
        h: "The discount is deducted from the outbound fare",
        p: "In our invoice, the fare calculation line gives an outbound fare of <b>202.00</b>, and page one shows a " + P("DESCONTO") + " of <b>5.00</b>. What went into the portal was <b>197.00</b> — that is, 202.00 minus the discount. " + P("Custo") + " came out at 444.15, exactly matching the invoice's " + P("TOTAL") + ", and the claim was approved.",
        p2: "The check is simple: add up both fares and all the fees. It should come to exactly the " + P("TOTAL") + " on page one. If it comes to more, the discount was not deducted."
      }
    },
    {
      h: "Próximos Passos",
      p: "The fifth screen appears only after clicking " + P("Submeter") + ". We do not have a screenshot yet — we have not submitted a real claim just for the picture. We will go through it on the next real flight and add it here. To be honest: this step is not shown yet. What happens after submission — <a class=\"lnk\" href=\"#depois\">below, “How long to wait”</a>.",
      imgs: []
    }
  ],

  mapH: "Summary: where everything sits on the invoice",
  mapP: "Short, to keep in view while filling in the form. The invoice is the file " + P("AIE APXIE026_….pdf") + " from TAP, two pages; page two is called " + P("Declaração para efeitos de Subsídio de Mobilidade") + ". How to request it — <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>.",
  mapHead: ["Portal field", "Where on the invoice", "What to watch for"],
  map: [
    [P("Valor da Tarifa (Ida)") + "<br>" + P("Valor da Tarifa (Volta)"), "P. 2, fare calculation line", "Two figures in a row: …LIS<b>202.00</b>TP FNC<b>90.00</b>"],
    [P("Taxa de Emissão de Bilhete - XP"), "P. 2, fees block", "May appear as YR, OB or DV. Capped at €35 / €70"],
    [P("Taxa de Serviço a Passageiros - YP"), "P. 2, YP line", "Airport fee per passenger"],
    [P("Sobretaxa de Combustível - YQ"), "P. 2, YQ line", "Usually the largest fee"],
    [P("Taxa de Carbono - J9"), "P. 2, J9 line", "Often missing from the list — means zero"],
    [P("Sobretaxa de Segurança - PT"), "P. 2, PT line", "Shown simply as PT on the invoice"],
    [P("Número de Reserva"), "P. 2, above the fare line", "Six characters before the slash"],
    [P("Número da Fatura"), "P. 1, top right", "With the letters: AIE APXIE026/…"],
    [P("Data da Fatura"), "P. 1, next to the number", "Invoice date, not departure date"],
    [P("Data de Emissão do Bilhete"), "P. 1, DT.EMISSÃO column", "A different date — when the ticket was issued"],
    [P("E-Ticket"), "P. 1, NR. DOC. column", "13 digits, starting with 047"],
    [P("NIF da Entidade Emissora"), "P. 1, top left", "500278725 — in the NIPC line"],
    ["<b>Check</b>", "P. 1, TOTAL and DESCONTO columns", "Sum of all portal fields = TOTAL. Deduct the discount from the outbound fare"]
  ],
  outK: "Issue 1",
  outT: "Documentos TAP",
  outD: "How to request both documents from the airline — the invoice and the travel proof. Eight screens, three traps.",

  timeH: "After submitting: how long to wait",
  timeP: "The claim goes through a human operator: they open every attached file and approve it separately. That is what takes the time.",
  timeHead: ["Event", "When", "What happens"],
  times: [
    [P("Submeter Pedido"), "0", "The claim is sent"],
    [P("Em Análise"), "immediately", "The status changes automatically"],
    [P("Aprovar") + " of the documents", "from an hour", "The operator opens each file separately"],
    [P("Aprovado"), "2–11 days", "The six-month residence criterion is checked"],
    [P("Pagamento Efetuado"), "+2–4 days", "The money is sent to the IBAN"]
  ],
  timeNote: "Across three real claims, filing to payment took 15, 12 and 2 days. The spread is wide, and depends on how quickly the operator gets to the last attached file. Track a claim under " + P("Histórico de Pedidos") + " on the portal home page.",
  statH: "Statuses",
  stats: [
    [P("Rascunho"), "Draft. Not submitted and not looked at by anyone."],
    [P("Em Análise"), "Under review."],
    [P("Correção Solicitada"), "A correction is requested. Not a refusal — the claim will be reviewed again."],
    [P("Aprovado"), "Approved, the money is queued for payment."],
    [P("Pago"), "Paid."],
    [P("Compareceu / Não Compareceu"), "A separate check that you actually took the flight. A paid claim can still show " + P("Não Verificado") + " — that is normal."]
  ],

  corrH: "If you receive Correção Solicitada",
  corrP: "This is not a refusal. The claim is sent back for correction, then reviewed again. Here is a real notice — and both reasons in it are exactly about what this page covers.",
  corrCap: "Análise de Pedido de Subsídio — the notice arrives in the personal area.",
  corrQuote: [
    "“Your claim could not be confirmed for the reasons listed below. The claim will be reviewed again once the following has been corrected:",
    "— " + P("Fatura de voo ou escala marítima - 01") + ": the attached document is not required.",
    "— The values in the fields “valor da tarifa” and the fees do not match the submitted documents. Please update the data on the platform (should be: Valor da Tarifa €45.50, Valor da Tarifa de Retorno €3.50, XP €0.00, YP €35.60, YQ €39.00, J9 €0.00, PT €7.12).”"
  ],
  corrDo: "What to do: open " + P("Histórico de Pedidos") + ", go into the claim and correct exactly what is listed. The operator usually writes the correct figures themselves — but the letter arrives two weeks after submission. Easier to copy the figures from the invoice correctly the first time.",

  refH: "Related pages",
  refP: "What this page covers in one line is set out separately elsewhere.",
  refs: [
    ["./dinheiro/", "Note 1", "How much money and what for", "Categories of recipients, what is refunded and what is not, the cap on the ticketing fee, the discount, and the cap that no longer exists."],
    ["./rejeitado/", "Note 2", "First login: “Rejeitado” is not a refusal", "Why the portal marks a refusal right at registration, what to do, and what the personal area holds."],
    ["./familia/", "Note 3", "Family and helping someone else", "How to add a spouse and children so their flights go into the same claim — and rule number one if you are filing for someone else."],
    ["../tap/", "Issue 1", "Documentos TAP", "How to request the invoice and the travel proof from the airline. Eight screens, three traps."]
  ],

  endH: "If you get stuck",
  endP: "The only contact on the whole portal is " + P("infossm@ctt.pt") + ". No phone, no chat, no feedback form. Write in Portuguese and always include the " + P("Número de Pedido") + ".",
  lawP: "Since 6 June 2026, Lei n.º 23/2026 has been in force: the subsidy was renamed Mecanismo de Continuidade Territorial, the reimbursement cap was removed, and the portal has not yet been updated to match. What this changes for you — <a class=\"lnk\" href=\"/?p=news\">What changed in the law</a>.",
  shareBtn: "Send this guide",
  shareTitle: "The claim in five steps — nDm",
  shareText: "Flight subsidy: how to file and not lose money —",
  copied: "Link copied"
};
