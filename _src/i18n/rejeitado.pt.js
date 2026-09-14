T.pt = {
  eyebrow: "nDm · Ficha 2",
  h1: "Primeiro acesso: o «Rejeitado» a vermelho não é uma recusa",
  lead: "No primeiro registo, o portal atribui automaticamente o estado Rejeitado. Ainda antes de se clicar em fosse o que fosse. A pessoa vê «recusado» e desiste — mas isto significa apenas «o perfil não está preenchido».",
  blocks: [
    { t: "h2", v: "A história de um registo, minuto a minuto", p: "Eis o " + P("Histórico do Registo") + " da área pessoal. Lê-se de baixo para cima." },
    { t: "fig", src: "../img/b6.jpg", cap: "Histórico do Registo na área pessoal. Lê-se de baixo para cima." },
    { t: "fields", v: [
      P("Rejeitado") + " — 11:55. O sistema criou o perfil a partir dos dados da Autenticação.gov e atribuiu logo a recusa. O utilizador ainda não tinha feito nada.",
      "O utilizador carrega o " + P("Comprovativo do IBAN") + " e insere o " + P("IBAN") + " e o telefone — 12:00.",
      P("Pendente") + " — 12:00. O estado muda sozinho assim que o perfil fica preenchido.",
      P("Validado") + " — 13:38. Um operador abriu o documento, aprovou-o, e o estado ficou verde. Entre a «recusa» e a aprovação passou uma hora e quarenta e três minutos."
    ] },
    { t: "warn", h: "O que fazer ao ver Rejeitado",
      p: "Página principal → " + P("Aceder à Área Pessoal") + " → " + P("Alterar Dados") + ". Inserir o " + P("IBAN") + " e o telefone, guardar. Depois carregar o comprovativo bancário da conta.",
      p2: "A seguir é só esperar: o portal muda o estado sozinho, depois de um operador abrir o seu documento. Enquanto o estado não estiver " + P("Validado") + ", ainda é cedo para submeter o pedido — o pagamento não passa." },

    { t: "h2", v: "A área pessoal: o que lá existe", p: "O botão " + P("Aceder à Área Pessoal") + " está escondido em baixo, na página principal, sob o cartão com os seus dados. Atrás dele há quatro secções que o gov.pt não menciona em lado nenhum." },
    { t: "step", h: "O que se pode alterar",
      p: "O botão " + P("Alterar Dados") + " abre um formulário em que só três campos ficam ativos: tipo de beneficiário, " + P("IBAN") + " e " + P("Telefone/Telemóvel") + ". Nome, NIF, data de nascimento, email, código postal e localidade — sempre a cinzento.",
      src: "../img/b1.jpg", cap: "Os três campos assinalados — a única coisa que o portal deixa alterar." },
    { t: "step", h: "Anexos do perfil",
      p: "Na secção " + P("Anexos") + " está o " + P("Comprovativo do IBAN") + " — o comprovativo bancário da conta. Sem ele os pagamentos não passam, e é aprovado por um operador humano, não pelo sistema.",
      src: "../img/b2.jpg", cap: "A etiqueta verde Aprovado é colocada manualmente pelo operador." },
    { t: "step", h: "Família",
      p: P("Situação Familiar") + " — é aqui que se adicionam a esposa, os filhos e outros dependentes, para que as suas viagens sigam no mesmo pedido. Como se faz — <a class=\"lnk\" href=\"../familia/\">Família</a>." },
    { t: "step", h: "Pedidos",
      p: P("Histórico de Pedidos") + " — a lista dos seus pedidos com os respetivos estados. É também aqui que chegam as notificações de " + P("Correção Solicitada") + ". O que significam os estados e quanto tempo esperar — <a class=\"lnk\" href=\"../#depois\">«Depois de submeter» na instrução</a>." },

    { t: "h2", v: "Telefone e email — só os seus", p: "O telefone e o email no perfil têm de ser seus, os mesmos usados para obter a " + P("Chave Móvel Digital") + ". Se está a ajudar outra pessoa e inserir os seus próprios contactos no perfil dela, o acesso à sua própria área fica danificado. Em detalhe — <a class=\"lnk\" href=\"../familia/#ajudar\">se está a tratar do pedido de outra pessoa</a>." }
  ],
  refH: "A seguir",
  refs: [
    ["../", "Instrução", "O pedido em cinco passos", "Cada ecrã do portal e cada campo — com imagens reais e as páginas da fatura."],
    ["../dinheiro/", "Ficha 1", "Quanto dinheiro e porquê", "Categorias de beneficiários, o que devolvem e o que não, o desconto e o tecto que já não existe."],
    ["../familia/", "Ficha 3", "Família e ajudar outra pessoa", "Como adicionar a esposa e os filhos — e a regra número um se está a tratar do pedido de outra pessoa."]
  ],
  shareBtn: "Enviar esta página",
  shareTitle: "Primeiro acesso: «Rejeitado» não é recusa — nDm",
  shareText: "O portal do subsídio mostrou «Rejeitado»? Não é uma recusa —",
  copied: "Ligação copiada"
};
