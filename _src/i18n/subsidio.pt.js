T.pt = {
  eyebrow: "nDm · Subsídio de Mobilidade",
  h1: "O pedido em cinco passos",
  lead: "O Estado devolve aos residentes das ilhas a maior parte do preço do bilhete. O dinheiro chega à conta bancária — desde que se passe pelos cinco ecrãs do portal e se copiem corretamente sete números da fatura da companhia aérea. Aqui mostra-se cada ecrã e cada campo — e onde as pessoas costumam perder esse dinheiro.",
  by: "Gratuito, sem registo. Não tratamos do pedido por si — mostramos como o fazer sozinho.",
  facts: ["5 ecrãs", "7 números da fatura", "≈ 15 dias até ao dinheiro"],

  needH: "O que preparar antes de entrar",
  needP: "O formulário não avança sem estas coisas, e não é possível voltar atrás a meio do pedido para acrescentar algo — o rascunho perde campos. Por isso, reúna tudo primeiro e só depois entre.",
  need: [
    "Dois PDF da TAP: a <b>fatura</b> " + P("AIE APXIE026_….pdf") + " (com o anexo Declaração para efeitos de Subsídio de Mobilidade) e o <b>comprovativo de viagem</b> " + P("BoardingProofTAP_….pdf") + ". Como pedir os dois — <a class=\"lnk\" href=\"../tap/\">Documentos TAP</a>.",
    P("IBAN") + " e o telemóvel inscritos no perfil do portal, e o " + P("Comprovativo do IBAN") + " aprovado pelo operador. Se ao entrar pela primeira vez viu o «" + P("Rejeitado") + "» a vermelho — não é uma recusa: <a class=\"lnk\" href=\"./rejeitado/\">Primeiro acesso</a>.",
    P("Chave Móvel Digital") + " ou Cartão de Cidadão com leitor — não há outra forma de entrar no portal.",
    "Se viajou com a esposa ou com os filhos, têm de ser adicionados ao perfil com antecedência: <a class=\"lnk\" href=\"./familia/\">Família</a>."
  ],
  needNote: "Se tem ou não direito ao subsídio — <a class=\"lnk\" href=\"/?p=check\">três perguntas</a>, meio minuto. O que exatamente devolvem e quanto — <a class=\"lnk\" href=\"./dinheiro/\">Quanto dinheiro e porquê</a>.",

  exH: "Vamos ver este exemplo",
  exP: "Abaixo está um pedido real: Funchal → Lisboa → Funchal, TAP, residente da Madeira. Aprovado e pago. Todos os números dos passos vêm da sua fatura, e ao longo do texto mostra-se de que linha exata.",
  calcHead: "Como o portal calculou o reembolso",
  calc: [
    ["Tarifa de ida · 202,00 − 5,00 de desconto", "197,00 €"],
    ["Tarifa de regresso", "90,00 €"],
    ["Taxa de passageiro · YP", "35,03 €"],
    ["Sobretaxa de combustível · YQ", "115,00 €"],
    ["Sobretaxa de segurança · PT", "7,12 €"],
    ["Custo", "444,15 €", "sum"],
    ["Copagamento", "− 79,00 €", "sum"],
    ["Reembolso", "365,15 €", "sum big"]
  ],
  calcNote: P("Copagamento") + " de 79 € — a parte que o passageiro paga do seu bolso; é sempre descontada. De onde vêm os outros números e o que nunca é devolvido — <a class=\"lnk\" href=\"./dinheiro/\">Quanto dinheiro e porquê</a>.",

  openBtn: "Abrir o portal",
  copyBtn: "Copiar o endereço",
  copiedLink: "Endereço copiado",
  openHint: "No computador, o portal abre numa janela à parte, à direita — a instrução fica à esquerda. A entrada é só com " + P("Chave Móvel Digital") + " ou Cartão de Cidadão. Na página principal do portal, clique em " + P("Submeter Pedido") + ".",

  stepsH: "Os cinco ecrãs do assistente",
  stepsP: "À esquerda, no portal, vê-se a lista de passos. Não se pode clicar nela — só se pode voltar atrás com o botão " + P("Anterior") + ", passo a passo. Vale a pena saber isto de antemão.",
  steps: [
    {
      h: "Dados Gerais do Beneficiário",
      p: "O primeiro ecrã não pergunta nada. Os seis campos estão a cinzento — nome, NIF, código postal, localidade, email e telefone vêm da Autenticação.gov, e não podem ser alterados aqui. Só há um elemento ativo.",
      imgs: [{ src: "img/c1.jpg", cap: "A única coisa em que se pode clicar no primeiro passo." }],
      fields: [
        P("Residente Equiparado há menos de 6 meses a exercer funções públicas na Região Autónoma?") + " — só se assinala se se mudou para a região há menos de seis meses e trabalha aqui num cargo público. Em todos os outros casos — não tocar."
      ],
      after: "No primeiro passo não há botão «anterior» — só " + P("Seguinte") + ".",
      warn: {
        h: "O código postal e a localidade ficam vazios",
        p: "Não é possível preencher o " + P("Código Postal") + " e a " + P("Localidade") + ", nem aqui nem na área pessoal — o portal mostra os campos mas não permite editá-los.",
        p2: "Isto não afeta o direito ao subsídio: no nosso pedido o código postal ficou vazio, e o estado é " + P("Validado") + "."
      }
    },
    {
      h: "Informação bancária",
      p: "Um único campo. Também está a cinzento: o portal preenche o que está guardado no perfil.",
      imgs: [{ src: "img/c2.jpg", cap: "O passo inteiro — um único campo, só de leitura." }],
      fields: [
        P("IBAN") + " — só de leitura. Altera-se em " + P("Área Pessoal") + " → " + P("Alterar Dados") + " (onde e como isto se faz — <a class=\"lnk\" href=\"./rejeitado/\">Primeiro acesso</a>)."
      ],
      warn: {
        h: "Pare se a conta não é sua ou o campo está vazio",
        p: "O dinheiro é enviado exatamente para este IBAN. Volte à página principal, abra a " + P("Área Pessoal") + ", corrija a conta — e só depois comece o pedido."
      }
    },
    {
      h: "Dados da Viagem",
      p: "O ecrã mais longo. Divide-se em três partes: a fatura, o itinerário e os dois ficheiros. Vamos vê-las uma a uma — e mostrar de onde vem, na fatura, cada número.",
      imgs: [{ src: "img/c3.jpg", cap: "Parte um: a fatura." }],
      fields: [
        P("NIF da Entidade Emissora") + " — o número fiscal de quem emitiu a fatura. No caso da TAP é " + P("500278725") + ". Se a fatura foi emitida por uma agência de viagens estrangeira, o portal pede que se escreva " + P("000000000") + ".",
        P("Data de Emissão do Bilhete") + " — a data de emissão do bilhete. O portal avisa: não antes de " + P("15/01/2026") + ".",
        P("Número da Fatura") + " — o número da fatura por inteiro, com o prefixo de letras: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — a data da própria fatura. Não é a data de emissão do bilhete nem a data do voo."
      ],
      imgs2: [{ src: "img/f1.jpg", cap: "Primeira página da fatura AIE APXIE026_….pdf, que a TAP envia a pedido. Daqui vêm o número, as datas e o NIF da companhia." }],
      fields2: [
        P("Número da Fatura") + " — o número por inteiro, com as letras: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — a data à direita do número. Neste exemplo, " + P("2026-08-22") + ".",
        P("NIF da Entidade Emissora") + " — " + P("500278725") + ". Não é preciso procurá-lo: está impresso no cabeçalho da fatura, na linha «Matriculada na CRC de Lisboa e NIPC».",
        P("Data de Emissão do Bilhete") + " — coluna " + P("DT.EMISSÃO") + ". Aqui, " + P("2026-07-31") + ": o bilhete foi emitido a 31 de julho, e a fatura a 22 de agosto. São datas diferentes, e o portal pede as duas.",
        P("E-Ticket") + " — coluna " + P("NR. DOC.") + ", treze algarismos, começa por " + P("047") + ". Vai ser preciso no quarto passo.",
        "A coluna " + P("TOTAL") + " não se transcreve para o portal, mas serve para conferir: o " + P("Custo") + ", que o portal calcula sozinho, tem de coincidir com este número.",
        "A coluna " + P("DESCONTO") + " — se aparecer um desconto, guarde o valor. No quarto passo vai ser preciso subtraí-lo da tarifa, senão a soma não bate certo."
      ],
      imgs3: [{ src: "img/c4.jpg", cap: "Parte dois: o itinerário. Abaixo está o mesmo bloco, Volta." }],
      fields3: [
        P("Origem Inicial da Viagem") + " e " + P("Destino Final da Viagem") + " — aqui são regiões, não aeroportos: " + P("Madeira") + ", " + P("Lisboa") + ".",
        P("Data de Partida") + " e " + P("Hora de Partida") + " são obrigatórias. " + P("Data de Chegada") + " e " + P("Hora de Chegada") + " — sem asterisco, mas preencha-as: o operador confere-as com o comprovativo de embarque. Datas e horas — vêm dos segmentos na segunda página da fatura (mostrada no passo 4).",
        P("Companhia Aérea") + " e " + P("Número de Reserva") + " — código de reserva de seis letras, o portal sugere " + P("EX: WAAXYI") + ". Não é o número do bilhete.",
        P("Acrescentar Escala?") + " — " + P("Sim") + " só se houve escala dentro do mesmo bilhete."
      ],
      imgs4: [{ src: "img/c5.jpg", cap: "Parte três: os dois ficheiros. Não podem ser trocados." }],
      fields4: [
        P("Fatura(s) de Viagem emitidas por Companhia Aérea ou intermediário") + " — aqui vai a <b>fatura</b>: na TAP é o ficheiro " + P("AIE APXIE026_….pdf") + ".",
        P("Título(s) de Viagem: Bilhete ou Confirmação de Reserva") + " — aqui vai o <b>comprovativo de viagem</b>: " + P("BoardingProofTAP_….pdf") + ".",
        P("Adquiriu a sua viagem através de agência ou outro intermediário de viagens?") + " — " + P("Não") + ", se o bilhete foi comprado diretamente à companhia aérea."
      ],
      warn: {
        h: "É aqui que mais se erra",
        p: "Os dois documentos não são intermutáveis. E um documento a mais também é erro: num aviso de correção real lê-se " + P("O documento submetido não é necessário") + ".",
        p2: "Como pedir à TAP os dois documentos é mostrado na edição <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a> — abre num separador ao lado."
      }
    },
    {
      h: "Dados dos passageiros",
      p: "Aqui aparece o dinheiro. Sete campos com números, e todos os sete copiam-se da fatura — o ficheiro " + P("AIE APXIE026_….pdf") + ", que a TAP envia a pedido (como o pedir — <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>). Que taxas são devolvidas e quais não — <a class=\"lnk\" href=\"./dinheiro/\">Quanto dinheiro e porquê</a>.",
      imgs: [{ src: "img/c6.jpg", cap: "Números dos bilhetes. Na imagem vê-se como fica um rascunho guardado." }],
      fields: [
        P("Vai participar na viagem?") + " — tem de estar em " + P("Sim") + ". Enquanto estiver em " + P("Não") + ", os campos com valores nem aparecem no ecrã, e o reembolso mostra 0 €.",
        P("E-Ticket (Ida)") + " e " + P("E-Ticket (Volta)") + " — números dos bilhetes, treze algarismos, na TAP começam por " + P("047") + ".",
        "Nesta imagem, " + P("E-Ticket (Volta)") + " está vazio, e " + P("Valor da Tarifa (Volta)") + " é zero. É assim que fica um rascunho depois de ser guardado e reaberto."
      ],
      imgs2: [{ src: "img/c7.jpg", cap: "Sete números. Os códigos das taxas são os mesmos da fatura da TAP." }],
      fields2: [
        P("Valor da Tarifa (Ida)") + " e " + P("(Volta)") + " — tarifa líquida, sem taxas.",
        P("Taxa de Emissão de Bilhete - XP") + " — na fatura pode aparecer como " + P("YR") + ", " + P("OB") + " ou " + P("DV") + ". São aceites no máximo 35 € numa direção e 70 € ida e volta.",
        P("Taxa de Serviço a Passageiros - YP") + ", " + P("Sobretaxa de Combustível - YQ") + ", " + P("Taxa de Carbono - J9") + " e " + P("Sobretaxa de Segurança - PT") + " — copiam-se da fatura linha a linha, pelos códigos. Os campos das taxas não têm asterisco: passam vazios sem erro, e num bilhete normal isso são cerca de 157 € — mais de um terço do reembolso.",
        "Escreva vírgula, não ponto. Onde não há valor, ponha 0."
      ],
      imgs3: [{ src: "img/f2.jpg", cap: "Segunda página da fatura — Declaração para efeitos de Subsídio de Mobilidade. Os sete números estão todos aqui." }],
      fields3: [
        "<b>Linha do cálculo da tarifa</b> — o único sítio em todos os documentos onde a tarifa aparece dividida em «ida» e «volta». " + P("FNC TP LIS202.00TP FNC90.00EUR292.00END") + " lê-se da esquerda para a direita: de FNC pelo voo TP até LIS — <b>202,00</b>; depois, pelo voo TP até FNC — <b>90,00</b>; total 292,00. O primeiro número vai para " + P("Valor da Tarifa (Ida)") + ", o segundo para " + P("Valor da Tarifa (Volta)") + ".",
        "<b>Taxas por código.</b> " + P("YQ") + " 115,00 → " + P("Sobretaxa de Combustível - YQ") + "; " + P("PT") + " 7,12 → " + P("Sobretaxa de Segurança - PT") + "; " + P("YP") + " 35,03 → " + P("Taxa de Serviço a Passageiros - YP") + ". A linha " + P("FARE") + " é a soma das tarifas e não se transcreve para o portal. Se um código não estiver na lista, o campo fica em zero.",
        "A coluna " + P("Tarifa") + " na primeira página da fatura já inclui o YQ — o seu número não se transcreve para o campo da tarifa, senão a sobretaxa de combustível fica duplicada e o pedido é devolvido para correção.",
        P("XVYV7W/1A") + " — código de reserva. Os primeiros seis caracteres vão para " + P("Número de Reserva") + " no terceiro passo.",
        "Segmentos: número do voo, data, aeroportos. Daqui vêm as datas de partida e chegada para o terceiro passo, e é aqui que se vê qual é a «ida» e qual é a «volta»."
      ],
      imgs4: [{ src: "img/c9.jpg", cap: "O portal calcula sozinho. Ainda assim, tem de conferir." }],
      fields4: [
        "Em baixo, o portal soma o " + P("Custo") + ", subtrai o " + P("Copagamento") + " e mostra o " + P("Reembolso Total") + ". Se a soma parece estranha, quase sempre é um campo em falta, não um erro do portal."
      ],
      warn: {
        h: "Armadilha: Guardar Rascunho num trajeto de ida e volta",
        p: "Guardámos um rascunho com 208 €, saímos e voltámos — o segmento de regresso desapareceu: " + P("E-Ticket (Volta)") + " ficou vazio, " + P("Valor da Tarifa (Volta)") + " a zero, a soma caiu para 118 €.",
        p2: "E não é um erro de visualização: depois de sair, na lista de pedidos também ficaram 118 €. Preencha e submeta tudo de uma só vez."
      },
      warn2: {
        h: "O desconto subtrai-se da tarifa de «ida»",
        p: "Na nossa fatura, a linha do cálculo dá uma tarifa de ida de <b>202,00</b>, e na primeira página está o " + P("DESCONTO") + " de <b>5,00</b>. No portal escreveu-se <b>197,00</b> — ou seja, 202,00 menos o desconto. O " + P("Custo") + " ficou em 444,15, exatamente como o " + P("TOTAL") + " da fatura, e o pedido foi aprovado.",
        p2: "A verificação é simples: some as duas tarifas e todas as taxas. Tem de dar exatamente o " + P("TOTAL") + " da primeira página. Se der mais, é porque o desconto não foi subtraído."
      }
    },
    {
      h: "Próximos Passos",
      p: "O quinto ecrã só aparece depois de clicar em " + P("Submeter") + ". Ainda não temos uma imagem — não submetemos um pedido real só para tirar a fotografia. Faremos o pedido no próximo voo real e acrescentamos aqui. Para ser honesto: este passo ainda não está mostrado. O que acontece depois de submeter — <a class=\"lnk\" href=\"#depois\">mais abaixo, «Quanto tempo esperar»</a>.",
      imgs: []
    }
  ],

  mapH: "Resumo: onde está cada coisa na fatura",
  mapP: "Curto, para ter à vista enquanto preenche. A fatura é o ficheiro " + P("AIE APXIE026_….pdf") + " da TAP, duas páginas; a segunda chama-se " + P("Declaração para efeitos de Subsídio de Mobilidade") + ". Como pedi-la — <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>.",
  mapHead: ["Campo do portal", "Onde está na fatura", "O que ter em conta"],
  map: [
    [P("Valor da Tarifa (Ida)") + "<br>" + P("Valor da Tarifa (Volta)"), "Pág. 2, linha do cálculo da tarifa", "Dois números seguidos: …LIS<b>202.00</b>TP FNC<b>90.00</b>"],
    [P("Taxa de Emissão de Bilhete - XP"), "Pág. 2, bloco de taxas", "Pode aparecer como YR, OB ou DV. Máximo 35 € / 70 €"],
    [P("Taxa de Serviço a Passageiros - YP"), "Pág. 2, linha YP", "Taxa de aeroporto por passageiro"],
    [P("Sobretaxa de Combustível - YQ"), "Pág. 2, linha YQ", "Normalmente a maior taxa"],
    [P("Taxa de Carbono - J9"), "Pág. 2, linha J9", "Muitas vezes não consta na lista — ou seja, zero"],
    [P("Sobretaxa de Segurança - PT"), "Pág. 2, linha PT", "Na fatura, apenas PT"],
    [P("Número de Reserva"), "Pág. 2, acima da linha da tarifa", "Seis caracteres antes da barra"],
    [P("Número da Fatura"), "Pág. 1, cabeçalho à direita", "Com as letras: AIE APXIE026/…"],
    [P("Data da Fatura"), "Pág. 1, junto ao número", "Data da fatura, não do voo"],
    [P("Data de Emissão do Bilhete"), "Pág. 1, coluna DT.EMISSÃO", "Outra data — quando o bilhete foi emitido"],
    [P("E-Ticket"), "Pág. 1, coluna NR. DOC.", "13 algarismos, começa por 047"],
    [P("NIF da Entidade Emissora"), "Pág. 1, cabeçalho à esquerda", "500278725 — na linha sobre o NIPC"],
    ["<b>Conferência</b>", "Pág. 1, colunas TOTAL e DESCONTO", "A soma de todos os campos do portal = TOTAL. Subtrair o desconto da tarifa de «ida»"]
  ],
  outK: "Edição 1",
  outT: "Documentos TAP",
  outD: "Como pedir à companhia aérea os dois documentos — a fatura e o comprovativo de viagem. Oito ecrãs, três armadilhas.",

  timeH: "Depois de submeter: quanto tempo esperar",
  timeP: "O pedido passa por um operador humano: ele abre cada ficheiro anexado e aprova-o separadamente. É isso que demora.",
  timeHead: ["Evento", "Quando", "O que acontece"],
  times: [
    [P("Submeter Pedido"), "0", "O pedido é enviado"],
    [P("Em Análise"), "logo a seguir", "O estado muda automaticamente"],
    [P("Aprovar") + " dos documentos", "a partir de uma hora", "O operador abre cada ficheiro separadamente"],
    [P("Aprovado"), "2–11 dias", "É verificado o critério dos seis meses de residência"],
    [P("Pagamento Efetuado"), "+2–4 dias", "O dinheiro é enviado para o IBAN"]
  ],
  timeNote: "Em três pedidos reais, do envio até ao dinheiro passaram 15, 12 e 2 dias. A diferença é grande e depende da rapidez com que o operador chega ao último ficheiro anexado. Para acompanhar o pedido — " + P("Histórico de Pedidos") + " na página principal do portal.",
  statH: "Estados",
  stats: [
    [P("Rascunho"), "Rascunho. Não foi enviado e ninguém o vê."],
    [P("Em Análise"), "Em análise."],
    [P("Correção Solicitada"), "Pedem uma correção. Não é uma recusa — o pedido será reanalisado."],
    [P("Aprovado"), "Aprovado, o dinheiro está em fila para pagamento."],
    [P("Pago"), "Pago."],
    [P("Compareceu / Não Compareceu"), "Verificação à parte de se o passageiro voou mesmo. Num pedido já pago pode aparecer " + P("Não Verificado") + " — isso é normal."]
  ],

  corrH: "Se chegou um Correção Solicitada",
  corrP: "Não é uma recusa. O pedido é devolvido para se corrigir, e depois de corrigido é reanalisado. Eis um aviso real — e as duas razões falam exatamente do que esta página trata.",
  corrCap: "Análise de Pedido de Subsídio — o aviso chega à área pessoal.",
  corrQuote: [
    "«Não foi possível validar o seu pedido pelos motivos abaixo indicados. O pedido será reanalisado após a correção do seguinte:",
    "— " + P("Fatura de voo ou escala marítima - 01") + ": o documento submetido não é necessário.",
    "— Os valores nos campos «valor da tarifa» e taxas não coincidem com os documentos apresentados. Solicitamos a atualização dos dados na plataforma (deve ser: Valor da Tarifa 45,50 €, Valor da Tarifa de Retorno 3,50 €, XP 0,00 €, YP 35,60 €, YQ 39,00 €, J9 0,00 €, PT 7,12 €).»"
  ],
  corrDo: "O que fazer: abrir " + P("Histórico de Pedidos") + ", entrar no pedido e corrigir exatamente o que está indicado. O operador costuma escrever os valores corretos — mas a carta chega cerca de duas semanas depois do envio. É mais simples reescrever de uma vez os números da fatura.",

  refH: "Fichas de apoio",
  refP: "O que nesta página está referido numa linha é desenvolvido em separado.",
  refs: [
    ["./dinheiro/", "Ficha 1", "Quanto dinheiro e porquê", "Categorias de beneficiários, o que devolvem e o que não, o limite da taxa de emissão, o desconto e o tecto que já não existe."],
    ["./rejeitado/", "Ficha 2", "Primeiro acesso: «Rejeitado» não é recusa", "Porque é que o portal marca recusa logo no registo, o que fazer, e o que há na área pessoal."],
    ["./familia/", "Ficha 3", "Família e ajudar outra pessoa", "Como adicionar a esposa e os filhos, para que as suas viagens sigam no mesmo pedido — e a regra número um se está a tratar do pedido de outra pessoa."],
    ["../tap/", "Edição 1", "Documentos TAP", "Como pedir à companhia aérea a fatura e o comprovativo de viagem. Oito ecrãs, três armadilhas."]
  ],

  endH: "Se ficou preso",
  endP: "O único contacto em todo o portal é " + P("infossm@ctt.pt") + ". Nem telefone, nem chat, nem formulário de contacto. Escreva em português e indique sempre o " + P("Número de Pedido") + ".",
  lawP: "Desde 6 de junho de 2026 está em vigor a Lei n.º 23/2026: o subsídio passou a chamar-se Mecanismo de Continuidade Territorial, o tecto de reembolso foi eliminado, e o portal ainda não foi atualizado às novas regras. O que isto muda para si — <a class=\"lnk\" href=\"/?p=news\">O que mudou na lei</a>.",
  shareBtn: "Enviar esta instrução",
  shareTitle: "O pedido em cinco passos — nDm",
  shareText: "Subsídio de voos: como submeter o pedido sem perder dinheiro —",
  copied: "Ligação copiada"
};
