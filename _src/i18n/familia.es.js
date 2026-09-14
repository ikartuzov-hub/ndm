T.es = {
  eyebrow: "nDm · Ficha 3",
  h1: "Familia y tramitar por otra persona",
  lead: "El cónyuge, los hijos y las personas dependientes tienen el mismo derecho a la subsidio. Pero para que sus vuelos entren en la solicitud hay que añadirlos una vez al perfil — y el portal no lo dice en ningún sitio. Y si tramita la solicitud no para usted mismo, hay una regla que pesa más que todas las demás.",
  blocks: [
    { t: "h2", v: "Cómo añadir a la familia", p: "Se hace una sola vez, en el área personal, antes de presentar la solicitud. Mientras la lista esté vacía, no se pueden presentar vuelos familiares — en el cuarto paso del asistente simplemente no habrá campos para ellos." },
    { t: "step", h: "El apartado Situação Familiar",
      p: "Página principal → " + P("Aceder à Área Pessoal") + " → " + P("Situação Familiar") + ". Aquí se sube el " + P("Prova de Agregado Familiar") + " — el certificado de composición familiar — y hay un botón " + P("Adicionar Membro") + ". Es la única manera de conseguir la subsidio por los vuelos del cónyuge y los hijos.",
      src: "../img/b3.jpg", cap: "Mientras la lista esté vacía, no se pueden presentar vuelos familiares." },
    { t: "step", h: "La ficha de un familiar",
      p: "En la ficha se elige el " + P("Parentesco") + ": " + P("Cônjuge") + ", " + P("Filho") + " o " + P("Dependente") + ", y se adjunta el " + P("Comprovativo de Parentesco") + " — el certificado de matrimonio o de nacimiento. El tipo de beneficiario de un hijo o del cónyuge puede ser distinto del suyo: un estudiante, por ejemplo, tiene su propia aportación, 59 € en vez de 79 €.",
      src: "../img/b4.jpg", cap: "El Comprovativo de Parentesco es obligatorio: campo con asterisco." },
    { t: "fields", v: [
      "A juzgar por cómo comprueba el portal el " + P("Comprovativo do IBAN") + ", los documentos de la familia también los abre un operador real — cuente con uno o dos días antes de presentar.",
      "Para ser honestos: todavía no hemos presentado una solicitud familiar. Cómo se ve el cuarto paso con varios pasajeros y adónde llega el dinero — lo añadiremos después de la primera solicitud real.",
      "Por cada pasajero, TAP emite una factura aparte. Al pedir los documentos, elija datos fiscales separados para que cada uno tenga su propio archivo — cómo se hace se muestra en <a class=\"lnk\" href=\"../../tap/\">Documentos TAP</a>.",
      "Si el cónyuge o un hijo mayor de edad están registrados en el portal por su cuenta, es más sencillo presentar dos solicitudes separadas, cada uno con su propia " + P("Chave Móvel Digital") + "."
    ] },

    { t: "rule" },
    { t: "h2", id: "ajudar", v: "Si tramita la solicitud por otra persona", p: "Es habitual ayudar a padres mayores, vecinos, conocidos — y el portal lo permite. Pero hay una regla que pesa más que todas las demás." },
    { t: "warn", h: "El teléfono y el correo deben ser los suyos, de la persona ayudada",
      p: "En el perfil y en la solicitud de la persona a la que ayuda deben figurar <b>su</b> teléfono y <b>su</b> correo — los mismos que se usaron al obtener <b>su</b> " + P("Chave Móvel Digital") + ". No los de usted.",
      p2: "Un caso real: una persona escribió su propio teléfono y correo en la solicitud de su hermana. La hermana recibió la subsidio, pero a la ayudante se le rompió el acceso a su propia área, y ahora está cambiando el correo a través de la Loja do Cidadão. Si la persona no tiene un correo propio, créele uno nuevo: veinte minutos ahora ahorran meses de trámites." },
    { t: "fields", v: [
      "El acceso al portal es solo con la " + P("Chave Móvel Digital") + " o el carné de ciudadano de esa persona. El código de confirmación llega a su teléfono, así que es más cómodo tramitarlo juntos que «después, solo».",
      "El IBAN — el suyo, de la persona ayudada. El dinero solo se ingresa en la cuenta del beneficiario de la subsidio; no se puede poner el propio para «pasarlo después».",
      "Todo lo demás de la solicitud son las mismas cinco pantallas que para uno mismo: <a class=\"lnk\" href=\"../\">La solicitud en cinco pasos</a>."
    ] }
  ],
  refH: "Siga leyendo",
  refs: [
    ["../", "Instrucción", "La solicitud en cinco pasos", "Cada pantalla del portal y cada campo — con capturas reales y la factura desplegada al lado."],
    ["../dinheiro/", "Ficha 1", "Cuánto dinero y por qué", "Categorías de beneficiarios, qué se devuelve y qué no, el descuento y el techo que ya no existe."],
    ["../rejeitado/", "Ficha 2", "Primer acceso: «Rejeitado» no es un rechazo", "Por qué el portal marca rechazo nada más registrarse y qué hay realmente en el área personal."]
  ],
  shareBtn: "Enviar esta página",
  shareTitle: "Familia y tramitar por otra persona — nDm",
  shareText: "Subsidio por vuelos para la familia y si tramita por otra persona —",
  copied: "Enlace copiado"
};
