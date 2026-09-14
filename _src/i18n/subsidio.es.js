T.es = {
  eyebrow: "nDm · Subsídio de Mobilidade",
  h1: "La solicitud en cinco pasos",
  lead: "El Estado le devuelve a los residentes de las islas la mayor parte del precio del billete. El dinero llega a la cuenta bancaria si supera las cinco pantallas del portal y copia correctamente siete cifras de la factura de la aerolínea. Aquí se muestra cada pantalla y cada campo — y dónde se pierde el dinero.",
  by: "Gratis, sin registro. No tramitamos nada por usted: le mostramos cómo hacerlo usted mismo.",
  facts: ["5 pantallas", "7 cifras de la factura", "≈ 15 días hasta el pago"],

  needH: "Qué tener listo antes de entrar",
  needP: "El formulario no le deja avanzar sin estas cosas, y no se puede volver atrás a mitad de la solicitud para añadir algo: el borrador pierde campos. Así que primero se reúne todo, después se entra.",
  need: [
    "Dos PDF de TAP: la <b>factura</b> " + P("AIE APXIE026_….pdf") + " (con el anexo Declaração para efeitos de Subsídio de Mobilidade) y el <b>comprobante de viaje</b> " + P("BoardingProofTAP_….pdf") + ". Cómo pedir ambos: <a class=\"lnk\" href=\"../tap/\">Documentos TAP</a>.",
    P("IBAN") + " y teléfono cumplimentados en el perfil del portal, y el " + P("Comprovativo do IBAN") + " aprobado por el operador. Si en el primer acceso vio el rojo " + P("Rejeitado") + ", no es un rechazo: <a class=\"lnk\" href=\"./rejeitado/\">Primer acceso</a>.",
    P("Chave Móvel Digital") + " o carné de ciudadano con lector — no hay otra forma de entrar en el portal.",
    "Si voló con su cónyuge o hijos, deben estar añadidos al perfil de antemano: <a class=\"lnk\" href=\"./familia/\">Familia</a>."
  ],
  needNote: "Si le corresponde o no la subsidio, en <a class=\"lnk\" href=\"/?p=check\">tres preguntas</a>, medio minuto. Qué se devuelve exactamente y cuánto: <a class=\"lnk\" href=\"./dinheiro/\">Cuánto dinero y por qué</a>.",

  exH: "Lo explicamos con este ejemplo",
  exP: "Abajo, una solicitud real: Funchal → Lisboa → Funchal, TAP, residente de Madeira. Aprobada y pagada. Todas las cifras de los pasos vienen de su factura, y se indica de qué línea exacta.",
  calcHead: "Cómo calcula el portal el reembolso",
  calc: [
    ["Tarifa de ida · 202,00 − 5,00 de descuento", "197,00 €"],
    ["Tarifa de vuelta", "90,00 €"],
    ["Tasa de pasajero · YP", "35,03 €"],
    ["Recargo de combustible · YQ", "115,00 €"],
    ["Tasa de seguridad · PT", "7,12 €"],
    ["Custo", "444,15 €", "sum"],
    ["Copagamento", "− 79,00 €", "sum"],
    ["Reembolso", "365,15 €", "sum big"]
  ],
  calcNote: P("Copagamento") + " 79 € — la parte que paga el propio pasajero; se descuenta siempre. De dónde salen las demás cifras y qué no se devuelve nunca: <a class=\"lnk\" href=\"./dinheiro/\">Cuánto dinero y por qué</a>.",

  openBtn: "Abrir el portal",
  copyBtn: "Copiar la dirección",
  copiedLink: "Dirección copiada",
  openHint: "En el ordenador el portal se abre en una ventana aparte a la derecha; la guía queda a la izquierda. Solo se entra con " + P("Chave Móvel Digital") + " o carné de ciudadano. En la página principal del portal, pulse " + P("Submeter Pedido") + ".",

  stepsH: "Las cinco pantallas del asistente",
  stepsP: "A la izquierda del portal se ve la lista de pasos. No se puede hacer clic sobre ella: solo se retrocede con el botón " + P("Anterior") + ", paso a paso. Conviene saberlo de antemano.",
  steps: [
    {
      h: "Dados Gerais do Beneficiário",
      p: "La primera pantalla no pregunta nada. Los seis campos están en gris — nombre, NIF, código postal, localidad, correo y teléfono llegan de Autenticação.gov y no se pueden cambiar aquí. Solo hay un elemento activo.",
      imgs: [{ src: "img/c1.jpg", cap: "Lo único que se puede pulsar en el primer paso." }],
      fields: [
        P("Residente Equiparado há menos de 6 meses a exercer funções públicas na Região Autónoma?") + " — se marca solo si se ha trasladado a la región hace menos de seis meses y trabaja aquí en un puesto público. En cualquier otro caso, no tocar."
      ],
      after: "En el primer paso no hay botón «atrás», solo " + P("Seguinte") + ".",
      warn: {
        h: "El código postal y la localidad quedan vacíos",
        p: "No se puede rellenar " + P("Código Postal") + " ni " + P("Localidade") + " ni aquí ni en el área personal — el portal muestra los campos pero no permite editarlos.",
        p2: "Esto no afecta al derecho a la subsidio: en nuestra solicitud el código postal está vacío y el estado es " + P("Validado") + "."
      }
    },
    {
      h: "Informação bancária",
      p: "Un solo campo. También en gris: el portal introduce lo que hay en el perfil.",
      imgs: [{ src: "img/c2.jpg", cap: "El paso entero: un campo de solo lectura." }],
      fields: [
        P("IBAN") + " — solo lectura. Se cambia en " + P("Área Pessoal") + " → " + P("Alterar Dados") + " (dónde y cómo: <a class=\"lnk\" href=\"./rejeitado/\">Primer acceso</a>)."
      ],
      warn: {
        h: "Deténgase si la cuenta no es suya o el campo está vacío",
        p: "El dinero se ingresará en ese IBAN exactamente. Vuelva a la página principal, abra " + P("Área Pessoal") + ", corrija la cuenta, y solo entonces empiece la solicitud."
      }
    },
    {
      h: "Dados da Viagem",
      p: "La pantalla más larga. Se divide en tres partes: factura, itinerario y dos archivos. Vamos por partes — y mostramos de dónde sale cada número de la factura.",
      imgs: [{ src: "img/c3.jpg", cap: "Primera parte: la factura." }],
      fields: [
        P("NIF da Entidade Emissora") + " — el NIF de quien emitió la factura. En TAP es " + P("500278725") + ". Si la factura la emitió una agencia extranjera, el portal pide escribir " + P("000000000") + ".",
        P("Data de Emissão do Bilhete") + " — fecha de emisión del billete. El portal avisa: no antes del " + P("15/01/2026") + ".",
        P("Número da Fatura") + " — el número completo de la factura, con el prefijo de letras: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — la fecha de la propia factura. No es la fecha de emisión del billete ni la fecha de salida."
      ],
      imgs2: [{ src: "img/f1.jpg", cap: "Primera página de la factura AIE APXIE026_….pdf que TAP envía a petición. De aquí salen el número, las fechas y el NIF de la aerolínea." }],
      fields2: [
        P("Número da Fatura") + " — el número completo, con letras: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — la fecha a la derecha del número. En este ejemplo, " + P("2026-08-22") + ".",
        P("NIF da Entidade Emissora") + " — " + P("500278725") + ". No hay que buscarlo: está impreso en la cabecera de la factura, en la línea «Matriculada na CRC de Lisboa e NIPC».",
        P("Data de Emissão do Bilhete") + " — columna " + P("DT.EMISSÃO") + ". Aquí " + P("2026-07-31") + ": el billete se emitió el 31 de julio y la factura se emitió el 22 de agosto. Son fechas distintas, y el portal pide las dos.",
        P("E-Ticket") + " — columna " + P("NR. DOC.") + ", trece cifras, empieza por " + P("047") + ". Hará falta en el cuarto paso.",
        "La columna " + P("TOTAL") + " no se copia al portal, pero sirve para comprobar: el " + P("Custo") + " que calcula el portal debe coincidir con ese número.",
        "La columna " + P("DESCONTO") + " — si hay un descuento, anótelo. En el cuarto paso habrá que restarlo de la tarifa, o la suma no cuadrará."
      ],
      imgs3: [{ src: "img/c4.jpg", cap: "Segunda parte: el itinerario. Debajo hay un bloque idéntico, Volta." }],
      fields3: [
        P("Origem Inicial da Viagem") + " y " + P("Destino Final da Viagem") + " — aquí van regiones, no aeropuertos: " + P("Madeira") + ", " + P("Lisboa") + ".",
        P("Data de Partida") + " y " + P("Hora de Partida") + " son obligatorios. " + P("Data de Chegada") + " y " + P("Hora de Chegada") + " — sin asterisco, pero rellénelos: el operador los coteja con la tarjeta de embarque. Fechas y horas salen de los segmentos de la segunda página de la factura (se muestra en el paso 4).",
        P("Companhia Aérea") + " y " + P("Número de Reserva") + " — el código de reserva de seis letras; el portal sugiere " + P("EX: WAAXYI") + ". No es el número del billete.",
        P("Acrescentar Escala?") + " — " + P("Sim") + " solo si hubo escala dentro del mismo billete."
      ],
      imgs4: [{ src: "img/c5.jpg", cap: "Tercera parte: dos archivos. No se pueden confundir." }],
      fields4: [
        P("Fatura(s) de Viagem emitidas por Companhia Aérea ou intermediário") + " — aquí va la <b>factura</b>: en TAP es el archivo " + P("AIE APXIE026_….pdf") + ".",
        P("Título(s) de Viagem: Bilhete ou Confirmação de Reserva") + " — aquí va el <b>comprobante de viaje</b>: " + P("BoardingProofTAP_….pdf") + ".",
        P("Adquiriu a sua viagem através de agência ou outro intermediário de viagens?") + " — " + P("Não") + ", si el billete se compró directamente a la aerolínea."
      ],
      warn: {
        h: "Aquí es donde más se confunden",
        p: "Los dos documentos no son intercambiables. Y un documento de más también es un error: en un aviso de corrección real se lee " + P("O documento submetido não é necessário") + " — «el documento adjunto no hace falta».",
        p2: "Cómo pedir a TAP los dos documentos se muestra en <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a> — se abre en otra pestaña."
      }
    },
    {
      h: "Dados dos passageiros",
      p: "Aquí aparece el dinero. Siete campos con cifras, y las siete se copian de la factura — el archivo " + P("AIE APXIE026_….pdf") + " que TAP envía a petición (cómo pedirlo: <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>). Qué tasas se devuelven y cuáles no: <a class=\"lnk\" href=\"./dinheiro/\">Cuánto dinero y por qué</a>.",
      imgs: [{ src: "img/c6.jpg", cap: "Números de billete. En la captura se ve cómo queda un borrador guardado." }],
      fields: [
        P("Vai participar na viagem?") + " — debe estar en " + P("Sim") + ". Mientras esté en " + P("Não") + ", no hay ningún campo de importes en la pantalla, y el reembolso se muestra como 0 €.",
        P("E-Ticket (Ida)") + " y " + P("E-Ticket (Volta)") + " — números de billete, trece cifras, en TAP empiezan por " + P("047") + ".",
        "En esta captura, " + P("E-Ticket (Volta)") + " está vacío y " + P("Valor da Tarifa (Volta)") + " es cero. Así queda un borrador después de guardarlo y volver a abrirlo."
      ],
      imgs2: [{ src: "img/c7.jpg", cap: "Siete cifras. Los códigos de las tasas son los mismos que en la factura de TAP." }],
      fields2: [
        P("Valor da Tarifa (Ida)") + " y " + P("(Volta)") + " — la tarifa neta, sin tasas.",
        P("Taxa de Emissão de Bilhete - XP") + " — en la factura puede aparecer como " + P("YR") + ", " + P("OB") + " o " + P("DV") + ". Se reconocen como máximo 35 € por trayecto y 70 € ida y vuelta.",
        P("Taxa de Serviço a Passageiros - YP") + ", " + P("Sobretaxa de Combustível - YQ") + ", " + P("Taxa de Carbono - J9") + " y " + P("Sobretaxa de Segurança - PT") + " — se copian de la factura línea por línea, por código. Los campos de tasas no llevan asterisco: pasan vacíos sin error, y en un billete normal son unos 157 € — más de un tercio del reembolso.",
        "Escriba coma, no punto. Donde no haya valor, ponga 0."
      ],
      imgs3: [{ src: "img/f2.jpg", cap: "Segunda página de la factura — Declaração para efeitos de Subsídio de Mobilidade. Las siete cifras están aquí." }],
      fields3: [
        "<b>Línea de cálculo de la tarifa</b> — el único lugar de todos los documentos donde la tarifa se desglosa en «ida» y «vuelta». " + P("FNC TP LIS202.00TP FNC90.00EUR292.00END") + " se lee de izquierda a derecha: de FNC con el vuelo TP a LIS, <b>202,00</b>; luego con el vuelo TP a FNC, <b>90,00</b>; total 292,00. El primer número va a " + P("Valor da Tarifa (Ida)") + ", el segundo a " + P("Valor da Tarifa (Volta)") + ".",
        "<b>Tasas por código.</b> " + P("YQ") + " 115,00 → " + P("Sobretaxa de Combustível - YQ") + "; " + P("PT") + " 7,12 → " + P("Sobretaxa de Segurança - PT") + "; " + P("YP") + " 35,03 → " + P("Taxa de Serviço a Passageiros - YP") + ". La línea " + P("FARE") + " es la suma de las tarifas y no se copia al portal. Si un código no aparece en la lista, en el portal queda en cero.",
        "La columna " + P("Tarifa") + " de la primera página de la factura ya incluye el YQ; ese número no se copia al campo de tarifa, o el recargo de combustible se duplicaría y la solicitud volvería para corrección.",
        P("XVYV7W/1A") + " — código de reserva. Los primeros seis caracteres van a " + P("Número de Reserva") + " en el tercer paso.",
        "Segmentos: número de vuelo, fecha, aeropuertos. De aquí salen las fechas de salida y llegada para el tercer paso, y también se ve cuál es el trayecto de «ida» y cuál el de «vuelta»."
      ],
      imgs4: [{ src: "img/c9.jpg", cap: "El portal calcula solo. Comprobar sigue siendo cosa suya." }],
      fields4: [
        "Al final, el portal suma el " + P("Custo") + ", resta el " + P("Copagamento") + " y muestra el " + P("Reembolso Total") + ". Si la suma parece rara, casi siempre falta un campo, no un fallo del portal."
      ],
      warn: {
        h: "Trampa: Guardar Rascunho en un itinerario de ida y vuelta",
        p: "Guardamos un borrador con 208 €, salimos y volvimos, y el segmento de vuelta había desaparecido: " + P("E-Ticket (Volta)") + " vacío, " + P("Valor da Tarifa (Volta)") + " en cero, la suma bajó a 118 €.",
        p2: "Y no es un fallo de pantalla: al salir, en la lista de solicitudes también quedó en 118 €. Rellene y envíe de una vez."
      },
      warn2: {
        h: "El descuento se resta de la tarifa de «ida»",
        p: "En nuestra factura, la línea de cálculo da una tarifa de ida de <b>202,00</b>, y en la primera página figura " + P("DESCONTO") + " <b>5,00</b>. En el portal se escribió <b>197,00</b> — es decir, 202,00 menos el descuento. El " + P("Custo") + " salió en 444,15, exactamente como el " + P("TOTAL") + " de la factura, y la solicitud se aprobó.",
        p2: "La comprobación es simple: sume las dos tarifas y todas las tasas. Debe dar exactamente el " + P("TOTAL") + " de la primera página. Si sale más, es que no se restó el descuento."
      }
    },
    {
      h: "Próximos Passos",
      p: "La quinta pantalla solo aparece después de pulsar " + P("Submeter") + ". Todavía no tenemos captura — no hemos enviado una solicitud real solo para la foto. Haremos la subida en el próximo vuelo real y la añadiremos aquí. Para ser honestos: este paso no está mostrado. Qué pasa después de enviar: <a class=\"lnk\" href=\"#depois\">más abajo, «Cuánto esperar»</a>.",
      imgs: []
    }
  ],

  mapH: "Resumen: qué está dónde en la factura",
  mapP: "Breve, para tener a la vista mientras rellena. La factura es el archivo " + P("AIE APXIE026_….pdf") + " de TAP, dos páginas; la segunda se llama " + P("Declaração para efeitos de Subsídio de Mobilidade") + ". Cómo pedirla: <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>.",
  mapHead: ["Campo del portal", "Dónde está en la factura", "Qué tener en cuenta"],
  map: [
    [P("Valor da Tarifa (Ida)") + "<br>" + P("Valor da Tarifa (Volta)"), "Pág. 2, línea de cálculo de la tarifa", "Dos números seguidos: …LIS<b>202.00</b>TP FNC<b>90.00</b>"],
    [P("Taxa de Emissão de Bilhete - XP"), "Pág. 2, bloque de tasas", "Puede aparecer como YR, OB o DV. Máximo 35 € / 70 €"],
    [P("Taxa de Serviço a Passageiros - YP"), "Pág. 2, línea YP", "Tasa de aeropuerto por pasajero"],
    [P("Sobretaxa de Combustível - YQ"), "Pág. 2, línea YQ", "Normalmente la tasa más alta"],
    [P("Taxa de Carbono - J9"), "Pág. 2, línea J9", "A menudo no aparece en la lista: significa cero"],
    [P("Sobretaxa de Segurança - PT"), "Pág. 2, línea PT", "En la factura, simplemente PT"],
    [P("Número de Reserva"), "Pág. 2, encima de la línea de tarifa", "Seis caracteres antes de la barra"],
    [P("Número da Fatura"), "Pág. 1, cabecera derecha", "Con las letras: AIE APXIE026/…"],
    [P("Data da Fatura"), "Pág. 1, junto al número", "Fecha de la factura, no de la salida"],
    [P("Data de Emissão do Bilhete"), "Pág. 1, columna DT.EMISSÃO", "Otra fecha: cuándo se emitió el billete"],
    [P("E-Ticket"), "Pág. 1, columna NR. DOC.", "13 cifras, empieza por 047"],
    [P("NIF da Entidade Emissora"), "Pág. 1, cabecera izquierda", "500278725 — en la línea sobre el NIPC"],
    ["<b>Comprobación</b>", "Pág. 1, columnas TOTAL y DESCONTO", "La suma de todos los campos del portal = TOTAL. Restar el descuento de la tarifa de «ida»"]
  ],
  outK: "Edición 1",
  outT: "Documentos TAP",
  outD: "Cómo pedir a la aerolínea los dos documentos: la factura y el comprobante de viaje. Ocho pantallas, tres trampas.",

  timeH: "Después de presentar: cuánto esperar",
  timeP: "La solicitud pasa por un operador real: abre cada archivo adjunto y lo aprueba por separado. Eso es lo que lleva tiempo.",
  timeHead: ["Evento", "Cuándo", "Qué ocurre"],
  times: [
    [P("Submeter Pedido"), "0", "La solicitud se envía"],
    [P("Em Análise"), "de inmediato", "El estado cambia automáticamente"],
    [P("Aprovar") + " documentos", "desde una hora", "El operador abre cada archivo por separado"],
    [P("Aprovado"), "2–11 días", "Se comprueba el criterio de seis meses de residencia"],
    [P("Pagamento Efetuado"), "+2–4 días", "El dinero se ingresa en el IBAN"]
  ],
  timeNote: "En tres solicitudes reales, desde presentar hasta cobrar pasaron 15, 12 y 2 días. La diferencia es grande y depende de lo rápido que el operador llegue al último archivo adjunto. Seguir la solicitud, en " + P("Histórico de Pedidos") + " de la página principal del portal.",
  statH: "Estados",
  stats: [
    [P("Rascunho"), "Borrador. No enviado, nadie lo revisa."],
    [P("Em Análise"), "En revisión."],
    [P("Correção Solicitada"), "Piden corregir. No es un rechazo: la solicitud se volverá a revisar."],
    [P("Aprovado"), "Aprobado, el dinero está en cola de pago."],
    [P("Pago"), "Pagado."],
    [P("Compareceu / Não Compareceu"), "Comprobación aparte de si realmente voló. Una solicitud ya pagada puede tener " + P("Não Verificado") + " — es normal."]
  ],

  corrH: "Si llega Correção Solicitada",
  corrP: "No es un rechazo. La solicitud se devuelve para corregirla, y tras la corrección se vuelve a revisar. Este es un aviso real — y las dos razones que da tratan exactamente de lo que explica esta página.",
  corrCap: "Análise de Pedido de Subsídio — el aviso llega al área personal.",
  corrQuote: [
    "«No se ha podido validar su solicitud por los motivos indicados a continuación. La solicitud se volverá a revisar tras corregir lo siguiente:",
    "— " + P("Fatura de voo ou escala marítima - 01") + ": el documento adjunto no es necesario.",
    "— Los valores de los campos «valor da tarifa» y de las tasas no coinciden con los documentos presentados. Le pedimos que actualice los datos en la plataforma (deben ser: Valor da Tarifa 45,50 €, Valor da Tarifa de Retorno 3,50 €, XP 0,00 €, YP 35,60 €, YQ 39,00 €, J9 0,00 €, PT 7,12 €).»"
  ],
  corrDo: "Qué hacer: abrir " + P("Histórico de Pedidos") + ", entrar en la solicitud y corregir exactamente lo que se indica. El operador suele escribir él mismo los valores correctos, pero el aviso llega dos semanas después de presentar. Es más sencillo reescribir las cifras de la factura una sola vez.",

  refH: "Para consultar aparte",
  refP: "Lo que en esta página se menciona en una línea está tratado por separado.",
  refs: [
    ["./dinheiro/", "Ficha 1", "Cuánto dinero y por qué", "Categorías de beneficiarios, lista de lo que se devuelve y lo que no, límite en la tasa de emisión, el descuento y el techo que ya no existe."],
    ["./rejeitado/", "Ficha 2", "Primer acceso: «Rejeitado» no es un rechazo", "Por qué el portal marca rechazo nada más registrarse, qué hacer, y qué hay realmente en el área personal."],
    ["./familia/", "Ficha 3", "Familia y tramitar por otra persona", "Cómo añadir cónyuge e hijos para que sus vuelos vayan en la misma solicitud — y la regla número uno si tramita por otra persona."],
    ["../tap/", "Edición 1", "Documentos TAP", "Cómo pedir a la aerolínea la factura y el comprobante de viaje. Ocho pantallas, tres trampas."]
  ],

  endH: "Si se queda atascado",
  endP: "El único contacto de todo el portal es " + P("infossm@ctt.pt") + ". Ni teléfono, ni chat, ni formulario de contacto. Escriba en portugués e indique siempre el " + P("Número de Pedido") + ".",
  lawP: "Desde el 6 de junio de 2026 está en vigor la Lei n.º 23/2026: la subsidio pasó a llamarse Mecanismo de Continuidade Territorial, se eliminó el techo del reembolso, y el portal todavía no se ha adaptado a las reglas nuevas. Qué cambia esto para usted: <a class=\"lnk\" href=\"/?p=news\">Qué cambió en la ley</a>.",
  shareBtn: "Enviar esta guía",
  shareTitle: "La solicitud en cinco pasos — nDm",
  shareText: "Subsidio por vuelos: cómo solicitarla sin perder dinero —",
  copied: "Enlace copiado"
};
