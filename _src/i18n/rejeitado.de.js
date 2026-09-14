T.de = {
  eyebrow: "nDm · Merkblatt 2",
  h1: "Erster Zugang: „Rejeitado“ ist keine Ablehnung",
  lead: "Bei der ersten Registrierung setzt das Portal automatisch den Status Rejeitado. Noch bevor Sie irgendetwas angeklickt haben. Man sieht „abgelehnt“ und geht — dabei bedeutet es nur „Profil nicht ausgefüllt“.",
  blocks: [
    { t: "h2", v: "Die Geschichte einer Registrierung, Minute für Minute", p: "Hier ist die " + P("Histórico do Registo") + " aus dem persönlichen Bereich. Wird von unten nach oben gelesen." },
    { t: "fig", src: "../img/b6.jpg", cap: "Histórico do Registo im persönlichen Bereich. Wird von unten nach oben gelesen." },
    { t: "fields", v: [
      P("Rejeitado") + " — 11:55. Das System hat das Profil aus den Daten von Autenticação.gov erstellt und sofort die Ablehnung gesetzt. Der Nutzer hatte dabei noch nichts getan.",
      "Der Nutzer lädt " + P("Comprovativo do IBAN") + " hoch und trägt " + P("IBAN") + " und Telefonnummer ein — 12:00.",
      P("Pendente") + " — 12:00. Der Status ändert sich von selbst, sobald das Profil ausgefüllt ist.",
      P("Validado") + " — 13:38. Ein Sachbearbeiter öffnete das Dokument, genehmigte es, und der Status wurde grün. Zwischen der „Ablehnung“ und der Genehmigung lagen eine Stunde und dreiundvierzig Minuten."
    ] },
    { t: "warn", h: "Was zu tun ist, wenn Sie Rejeitado sehen",
      p: "Startseite → " + P("Aceder à Área Pessoal") + " → " + P("Alterar Dados") + ". " + P("IBAN") + " und Telefonnummer eintragen, speichern. Danach den Kontonachweis hochladen.",
      p2: "Danach bleibt nur warten: Der Status wechselt von selbst, sobald ein Sachbearbeiter Ihr Dokument öffnet. Solange der Status nicht " + P("Validado") + " lautet, ist es zu früh für den Antrag — die Auszahlung geht nicht durch." },

    { t: "h2", v: "Der persönliche Bereich: was es dort überhaupt gibt", p: "Die Schaltfläche " + P("Aceder à Área Pessoal") + " ist unten auf der Startseite versteckt, unter der Karte mit Ihren Daten. Dahinter liegen vier Bereiche, über die auf gov.pt keine Zeile steht." },
    { t: "step", h: "Was sich ändern lässt",
      p: "Die Schaltfläche " + P("Alterar Dados") + " öffnet ein Formular, in dem nur drei Felder aktiv bleiben: Begünstigtentyp, " + P("IBAN") + " und " + P("Telefone/Telemóvel") + ". Name, NIF, Geburtsdatum, E-Mail, Postleitzahl und Ort bleiben für immer grau.",
      src: "../img/b1.jpg", cap: "Die drei umrahmten Felder — das Einzige, was das Portal zu ändern erlaubt." },
    { t: "step", h: "Anhänge des Profils",
      p: "Im Bereich " + P("Anexos") + " liegt " + P("Comprovativo do IBAN") + " — der Kontonachweis der Bank. Ohne ihn geht keine Auszahlung durch, und genehmigt wird er von einem Sachbearbeiter, nicht vom System.",
      src: "../img/b2.jpg", cap: "Das grüne Label Aprovado setzt der Sachbearbeiter von Hand." },
    { t: "step", h: "Familie",
      p: P("Situação Familiar") + " — hier werden Ehepartner, Kinder und Angehörige hinzugefügt, damit ihre Flüge in denselben Antrag gehören. Wie das geht — <a class=\"lnk\" href=\"../familia/\">Familie</a>." },
    { t: "step", h: "Anträge",
      p: P("Histórico de Pedidos") + " — die Liste Ihrer Anträge mit Status. Hierher kommen auch die " + P("Correção Solicitada") + "-Benachrichtigungen. Was die Status bedeuten und wie lange es dauert — <a class=\"lnk\" href=\"../#depois\">Nach dem Einreichen in der Anleitung</a>." },

    { t: "h2", v: "Telefon und E-Mail — nur die eigenen", p: "Telefon und E-Mail im Profil müssen Ihre eigenen sein — dieselben, die Sie beim Erhalt der " + P("Chave Móvel Digital") + " verwendet haben. Wenn Sie einer anderen Person helfen und Ihre eigenen Kontaktdaten in deren Profil eintragen, geht der Zugang zu Ihrem eigenen Bereich kaputt. Ausführlich — <a class=\"lnk\" href=\"../familia/#ajudar\">wenn Sie für jemand anderen beantragen</a>." }
  ],
  refH: "Weiter",
  refs: [
    ["../", "Anleitung", "Der Antrag in fünf Schritten", "Jeder Bildschirm des Portals und jedes Feld — mit echten Bildschirmfotos und der Rechnung daneben."],
    ["../dinheiro/", "Merkblatt 1", "Wie viel Geld und wofür", "Empfängerkategorien, was erstattet wird und was nicht, der Rabatt und die Grenze, die es nicht mehr gibt."],
    ["../familia/", "Merkblatt 3", "Familie und für andere beantragen", "Wie Sie Ehepartner und Kinder hinzufügen — und Regel Nummer eins, wenn Sie nicht für sich selbst beantragen."]
  ],
  shareBtn: "Diese Seite senden",
  shareTitle: "Erster Zugang: „Rejeitado“ ist keine Ablehnung — nDm",
  shareText: "Das Subsidie-Portal zeigt „Rejeitado“? Das ist keine Ablehnung —",
  copied: "Link kopiert"
};
