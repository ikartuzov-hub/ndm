T.es = {
  eyebrow: "nDm · Ficha 2",
  h1: "Primer acceso: el «Rejeitado» en rojo no es un rechazo",
  lead: "Al registrarse por primera vez, el portal marca automáticamente el estado Rejeitado. Antes incluso de que usted haga nada. Uno ve «rechazado» y se va — pero solo significa «el perfil no está completo».",
  blocks: [
    { t: "h2", v: "La historia de un registro, minuto a minuto", p: "Este es el " + P("Histórico do Registo") + " del área personal. Se lee de abajo hacia arriba." },
    { t: "fig", src: "../img/b6.jpg", cap: "Histórico do Registo en el área personal. Se lee de abajo hacia arriba." },
    { t: "fields", v: [
      P("Rejeitado") + " — 11:55. El sistema creó el perfil con los datos de Autenticação.gov y de inmediato marcó rechazo. El usuario, mientras tanto, no había hecho nada.",
      "El usuario sube el " + P("Comprovativo do IBAN") + " y escribe el " + P("IBAN") + " y el teléfono — 12:00.",
      P("Pendente") + " — 12:00. El estado cambia solo, en cuanto el perfil está completo.",
      P("Validado") + " — 13:38. Un operador real abrió el documento, lo aprobó, y el estado se puso verde. Entre el «rechazo» y la aprobación pasó una hora y cuarenta y tres minutos."
    ] },
    { t: "warn", h: "Qué hacer si ve Rejeitado",
      p: "Página principal → " + P("Aceder à Área Pessoal") + " → " + P("Alterar Dados") + ". Escriba el " + P("IBAN") + " y el teléfono, guarde. Después suba el comprobante bancario de la cuenta.",
      p2: "Después solo queda esperar: el estado lo cambia el propio portal, una vez que un operador real abra su documento. Mientras el estado no sea " + P("Validado") + ", es pronto para presentar la solicitud — el pago no se procesará." },

    { t: "h2", v: "El área personal: qué hay realmente", p: "El botón " + P("Aceder à Área Pessoal") + " está escondido al final de la página principal, bajo la tarjeta con sus datos. Detrás hay cuatro apartados de los que en gov.pt no se dice ni una línea." },
    { t: "step", h: "Qué se puede cambiar",
      p: "El botón " + P("Alterar Dados") + " abre un formulario en el que solo quedan activos tres campos: tipo de beneficiario, " + P("IBAN") + " y " + P("Telefone/Telemóvel") + ". Nombre, NIF, fecha de nacimiento, correo, código postal y localidad quedan siempre en gris.",
      src: "../img/b1.jpg", cap: "Los tres campos marcados: lo único que el portal deja cambiar." },
    { t: "step", h: "Anexos del perfil",
      p: "En el apartado " + P("Anexos") + " está el " + P("Comprovativo do IBAN") + " — el comprobante bancario de la cuenta. Sin él no se procesan los pagos, y lo aprueba un operador real, no el sistema.",
      src: "../img/b2.jpg", cap: "La etiqueta verde Aprovado la pone el operador a mano." },
    { t: "step", h: "Familia",
      p: P("Situação Familiar") + " — aquí se añaden el cónyuge, los hijos y las personas dependientes, para que sus vuelos vayan en la misma solicitud. Cómo se hace: <a class=\"lnk\" href=\"../familia/\">Familia</a>." },
    { t: "step", h: "Solicitudes",
      p: P("Histórico de Pedidos") + " — la lista de sus solicitudes con sus estados. Aquí también llegan los avisos de " + P("Correção Solicitada") + ". Qué significan los estados y cuánto esperar: <a class=\"lnk\" href=\"../#depois\">«Después de presentar» en la guía</a>." },

    { t: "h2", v: "Teléfono y correo — solo los propios", p: "El teléfono y el correo del perfil deben ser suyos, los mismos que se usaron al obtener la " + P("Chave Móvel Digital") + ". Si está ayudando a otra persona y escribe sus propios contactos en el perfil de esa persona, se rompe el acceso a su propia área. En detalle: <a class=\"lnk\" href=\"../familia/#ajudar\">si lo tramita por otra persona</a>." }
  ],
  refH: "Siga leyendo",
  refs: [
    ["../", "Instrucción", "La solicitud en cinco pasos", "Cada pantalla del portal y cada campo — con capturas reales y la factura desplegada al lado."],
    ["../dinheiro/", "Ficha 1", "Cuánto dinero y por qué", "Categorías de beneficiarios, qué se devuelve y qué no, el descuento y el techo que ya no existe."],
    ["../familia/", "Ficha 3", "Familia y tramitar por otra persona", "Cómo añadir cónyuge e hijos — y la regla número uno si tramita por otra persona."]
  ],
  shareBtn: "Enviar esta página",
  shareTitle: "Primer acceso: «Rejeitado» no es un rechazo — nDm",
  shareText: "¿El portal de la subsidio le mostró «Rejeitado»? No es un rechazo —",
  copied: "Enlace copiado"
};
