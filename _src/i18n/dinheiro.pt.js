T.pt = {
  eyebrow: "nDm · Ficha 1",
  h1: "Quanto dinheiro e porquê",
  lead: "O portal decide sozinho se tem direito ao subsídio, e calcula sozinho o valor. Mas o que devolve e o que não devolve está escondido atrás de um pequeno ícone ⓘ no quarto passo — e é por causa dele que os valores mais frequentemente não batem certo.",
  blocks: [
    { t: "h2", v: "Um exemplo real", p: "Um pedido real: Funchal → Lisboa → Funchal, TAP, residente da Madeira. Aprovado e pago. Cada um dos cinco números de cima foi copiado da fatura da companhia aérea — o ficheiro " + P("AIE APXIE026_….pdf") + ", que a TAP envia a pedido. De que linha vem cada um — no <a class=\"lnk\" href=\"../#passo4\">passo 4 da instrução</a>." },
    { t: "calc", head: "Como se calcula o reembolso",
      rows: [
        ["Tarifa de ida · 202,00 − 5,00 de desconto", "197,00 €"],
        ["Tarifa de regresso", "90,00 €"],
        ["Taxa de passageiro · YP", "35,03 €"],
        ["Sobretaxa de combustível · YQ", "115,00 €"],
        ["Sobretaxa de segurança · PT", "7,12 €"],
        ["Custo", "444,15 €", "sum"],
        ["Copagamento", "− 79,00 €", "sum"],
        ["Reembolso", "365,15 €", "sum big"]
      ],
      note: P("Copagamento") + " de 79 € — a parte que o passageiro paga do seu bolso; é sempre descontada, em qualquer pedido. Para estudantes é 59 €." },

    { t: "h2", v: "Quem tem direito", p: "O portal decide isto a partir dos dados da Autenticação.gov, das Finanças e da Segurança Social. Não é possível influenciar isto, mas ajuda saber em que categoria foi colocado: dela depende o valor da sua parte. Verificação rápida em três perguntas — <a class=\"lnk\" href=\"/?p=check\">na primeira página</a>." },
    { t: "who", v: [
      ["Residente", "Domiciliado na região autónoma. O portal verifica automaticamente que reside aqui há pelo menos seis meses."],
      ["Residente Equiparado na RA Madeira", "Mudou-se há menos de meio ano e trabalha na região num cargo público."],
      ["Estudante na RA Açores", "Estudante que estuda nos Açores."],
      ["Estudante no Continente/Estrangeiro", "Estudante das ilhas que estuda no continente ou no estrangeiro."]
    ] },
    { t: "p", v: "Um estrangeiro precisa de um " + P("título de residência") + " válido — o portal avisa disso numa janela à parte ao entrar. A esposa, os filhos e outros dependentes adicionam-se ao perfil com antecedência, e assim as suas viagens seguem no mesmo pedido: <a class=\"lnk\" href=\"../familia/\">Família</a>." },

    { t: "h2", v: "O que devolvem e o que não", p: "A lista está por trás desse mesmo ícone ⓘ. Tudo na coluna da esquerda copia-se da fatura para os campos do quarto passo; tudo na da direita não, mesmo que conste da fatura." },
    { t: "cols", yesH: "Devolvem",
      yes: [
        "Tarifa de classe económica",
        "Taxas de aeroporto",
        "Emissão do bilhete · " + P("XP") + " ou " + P("OB"),
        "Sobretaxa de combustível · " + P("YQ"),
        "Taxa de passageiro · " + P("YP"),
        "Taxa de carbono · " + P("J9"),
        "Sobretaxa de segurança · " + P("PT"),
        "Bagagem incluída na tarifa",
        "Escolha de lugar, check-in e embarque prioritário — se incluídos na tarifa"
      ],
      noH: "Não devolvem",
      no: [
        "Seguro de viagem",
        "Excesso de bagagem",
        "Comissões bancárias",
        "Suplementos depois de comprado o bilhete",
        "Quaisquer opções que não entrem no preço base",
        "Bagagem, escolha de lugar, check-in e prioridade — se compradas à parte"
      ] },
    { t: "warn", h: "Duas regras fáceis de esquecer",
      p: "A taxa de emissão do bilhete é aceite no máximo até 35 € numa direção e 70 € ida e volta. Na fatura pode chamar-se " + P("XP") + ", " + P("YR") + ", " + P("OB") + " ou " + P("DV") + ".",
      p2: "Se voou com milhas ou com um certificado-oferta, só se deve inscrever os euros que saíram mesmo do cartão." },

    { t: "h2", v: "Desconto e conferência", p: "Os campos das taxas no portal não têm asterisco: passam vazios sem erro, e num bilhete normal isso são cerca de 157 € — mais de um terço do reembolso. Por isso a conferência é a única proteção." },
    { t: "warn", h: "O desconto subtrai-se da tarifa de «ida»",
      p: "Na nossa fatura, a linha do cálculo dá uma tarifa de ida de <b>202,00</b>, e na primeira página está o " + P("DESCONTO") + " de <b>5,00</b>. No portal escreveu-se <b>197,00</b> — 202,00 menos o desconto. O " + P("Custo") + " ficou em 444,15, exatamente como o " + P("TOTAL") + " da fatura, e o pedido foi aprovado.",
      p2: "A verificação é simples: some as duas tarifas e todas as taxas. Tem de dar exatamente o " + P("TOTAL") + " da primeira página da fatura. Se der mais, é porque o desconto não foi subtraído." },

    { t: "h2", v: "Já não há tecto", p: "Até 6 de junho de 2026 o reembolso estava limitado a 400 € por viagem. A Lei n.º 23/2026 eliminou esse tecto, mas a página oficial do serviço continua a indicar 400 € — e dois dos nossos pedidos, mais caros do que esse valor, foram pagos na íntegra, menos o " + P("Copagamento") + ". Em detalhe, com uma calculadora da diferença — <a class=\"lnk\" href=\"/?p=news\">O que mudou na lei</a>." }
  ],
  refH: "A seguir",
  refs: [
    ["../", "Instrução", "O pedido em cinco passos", "Cada ecrã do portal e cada campo — com imagens reais e as páginas da fatura."],
    ["../rejeitado/", "Ficha 2", "Primeiro acesso: «Rejeitado» não é recusa", "Porque é que o portal marca recusa logo no registo e o que há na área pessoal."],
    ["../familia/", "Ficha 3", "Família e ajudar outra pessoa", "Como adicionar a esposa e os filhos — e a regra número um se está a tratar do pedido de outra pessoa."]
  ],
  shareBtn: "Enviar esta página",
  shareTitle: "Quanto dinheiro e porquê — nDm",
  shareText: "Subsídio de voos: o que devolvem e o que não —",
  copied: "Ligação copiada"
};
