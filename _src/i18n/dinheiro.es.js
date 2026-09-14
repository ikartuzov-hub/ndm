T.es = {
  eyebrow: "nDm · Ficha 1",
  h1: "Cuánto dinero y por qué",
  lead: "El portal decide por su cuenta si le corresponde la subsidio y calcula el importe él solo. Pero qué devuelve exactamente y qué no queda escondido tras un pequeño icono ⓘ en el cuarto paso — y es por eso por lo que las sumas más a menudo no cuadran.",
  blocks: [
    { t: "h2", v: "Un ejemplo real", p: "Una solicitud real: Funchal → Lisboa → Funchal, TAP, residente de Madeira. Aprobada y pagada. Cada una de las cinco cifras de arriba está copiada de la factura de la aerolínea — el archivo " + P("AIE APXIE026_….pdf") + " que TAP envía a petición. De qué línea sale cada una, en el <a class=\"lnk\" href=\"../#passo4\">paso 4 de la guía</a>." },
    { t: "calc", head: "Cómo se calcula el reembolso",
      rows: [
        ["Tarifa de ida · 202,00 − 5,00 de descuento", "197,00 €"],
        ["Tarifa de vuelta", "90,00 €"],
        ["Tasa de pasajero · YP", "35,03 €"],
        ["Recargo de combustible · YQ", "115,00 €"],
        ["Tasa de seguridad · PT", "7,12 €"],
        ["Custo", "444,15 €", "sum"],
        ["Copagamento", "− 79,00 €", "sum"],
        ["Reembolso", "365,15 €", "sum big"]
      ],
      note: P("Copagamento") + " 79 € — la parte que paga el propio pasajero; se descuenta siempre, en cualquier solicitud. En los estudiantes son 59 €." },

    { t: "h2", v: "A quién le corresponde", p: "El portal lo decide con datos de Autenticação.gov, Hacienda y la Seguridad Social. No se puede influir en esto, pero conviene saber en qué categoría le han clasificado: de eso depende el importe de su aportación propia. Comprobación rápida en tres preguntas: <a class=\"lnk\" href=\"/?p=check\">en la primera página</a>." },
    { t: "who", v: [
      ["Residente", "Empadronado en la región autónoma. El portal comprueba automáticamente que ha vivido aquí al menos seis meses."],
      ["Residente Equiparado na RA Madeira", "Se trasladó hace menos de medio año y trabaja en la región en un puesto público."],
      ["Estudante na RA Açores", "Estudiante que estudia en las Azores."],
      ["Estudante no Continente/Estrangeiro", "Estudiante de las islas que estudia en el continente o en el extranjero."]
    ] },
    { t: "p", v: "El extranjero necesita un " + P("título de residência") + " en vigor — el portal lo recuerda con una ventana aparte al entrar. El cónyuge, los hijos y las personas dependientes se añaden en el perfil de antemano, y entonces sus vuelos van en la misma solicitud: <a class=\"lnk\" href=\"../familia/\">Familia</a>." },

    { t: "h2", v: "Qué se devuelve y qué no", p: "La lista del mismo icono ⓘ. Todo lo de la columna izquierda se copia de la factura a los campos del cuarto paso; todo lo de la derecha, no, aunque figure en la factura." },
    { t: "cols", yesH: "Se devuelve",
      yes: [
        "Tarifa de clase turista",
        "Tasas de aeropuerto",
        "Emisión de billete · " + P("XP") + " u " + P("OB"),
        "Recargo de combustible · " + P("YQ"),
        "Tasa de pasajero · " + P("YP"),
        "Tasa de carbono · " + P("J9"),
        "Tasa de seguridad · " + P("PT"),
        "Equipaje incluido en la tarifa",
        "Selección de asiento, facturación y embarque prioritario — si van incluidos en la tarifa"
      ],
      noH: "No se devuelve",
      no: [
        "Seguro de viaje",
        "Exceso de equipaje",
        "Comisiones bancarias",
        "Suplementos posteriores a la compra del billete",
        "Cualquier opción que no esté en el precio base",
        "Equipaje, selección de asiento, facturación y prioridad, si se compraron aparte"
      ] },
    { t: "warn", h: "Dos reglas fáciles de pasar por alto",
      p: "La tasa de emisión del billete se reconoce como máximo 35 € por trayecto y 70 € ida y vuelta. En la factura puede llamarse " + P("XP") + ", " + P("YR") + ", " + P("OB") + " o " + P("DV") + ".",
      p2: "Si voló con millas o con un vale de regalo, solo hay que anotar los euros que de verdad salieron de la tarjeta." },

    { t: "h2", v: "El descuento y la comprobación", p: "Los campos de tasas del portal no llevan asterisco: pasan vacíos sin error, y en un billete normal son unos 157 € — más de un tercio del reembolso. Por eso la comprobación es la única protección." },
    { t: "warn", h: "El descuento se resta de la tarifa de «ida»",
      p: "En nuestra factura, la línea de cálculo da una tarifa de ida de <b>202,00</b>, y en la primera página figura " + P("DESCONTO") + " <b>5,00</b>. En el portal se escribió <b>197,00</b> — 202,00 menos el descuento. El " + P("Custo") + " salió en 444,15, exactamente como el " + P("TOTAL") + " de la factura, y la solicitud se aprobó.",
      p2: "La comprobación es simple: sume las dos tarifas y todas las tasas. Debe dar exactamente el " + P("TOTAL") + " de la primera página de la factura. Si sale más, es que no se restó el descuento." },

    { t: "h2", v: "Ya no hay techo", p: "Hasta el 6 de junio de 2026 el reembolso estaba limitado a 400 € por viaje. La Lei n.º 23/2026 eliminó ese techo, pero la página oficial del servicio sigue diciendo 400 € — y dos de nuestras solicitudes por encima de esa cifra se pagaron íntegras, menos el " + P("Copagamento") + ". En detalle, con una calculadora de la diferencia: <a class=\"lnk\" href=\"/?p=news\">Qué cambió en la ley</a>." }
  ],
  refH: "Siga leyendo",
  refs: [
    ["../", "Instrucción", "La solicitud en cinco pasos", "Cada pantalla del portal y cada campo — con capturas reales y la factura desplegada al lado."],
    ["../rejeitado/", "Ficha 2", "Primer acceso: «Rejeitado» no es un rechazo", "Por qué el portal marca rechazo nada más registrarse y qué hay realmente en el área personal."],
    ["../familia/", "Ficha 3", "Familia y tramitar por otra persona", "Cómo añadir cónyuge e hijos — y la regla número uno si tramita por otra persona."]
  ],
  shareBtn: "Enviar esta página",
  shareTitle: "Cuánto dinero y por qué — nDm",
  shareText: "Subsidio por vuelos: qué se devuelve y qué no —",
  copied: "Enlace copiado"
};
