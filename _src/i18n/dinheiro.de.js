T.de = {
  eyebrow: "nDm · Merkblatt 1",
  h1: "Wie viel Geld und wofür",
  lead: "Das Portal entscheidet selbst, ob Ihnen die Subsidie zusteht, und berechnet selbst den Betrag. Was es aber genau erstattet und was nicht, versteckt sich hinter einem kleinen ⓘ-Symbol im vierten Schritt — und wegen genau dieses Symbols stimmen die Summen am häufigsten nicht.",
  blocks: [
    { t: "h2", v: "Ein echtes Beispiel", p: "Ein echter Antrag: Funchal → Lissabon → Funchal, TAP, Ansässiger von Madeira. Genehmigt und ausgezahlt. Jede der fünf oberen Zahlen ist aus der Rechnung der Fluggesellschaft übertragen — der Datei " + P("AIE APXIE026_….pdf") + ", die TAP auf Anfrage zusendet. Aus welcher Zeile jede stammt — in <a class=\"lnk\" href=\"../#passo4\">Schritt 4 der Anleitung</a>." },
    { t: "calc", head: "Wie die Erstattung berechnet wird",
      rows: [
        ["Tarif hin · 202,00 − 5,00 Rabatt", "197,00 €"],
        ["Tarif zurück", "90,00 €"],
        ["Passagiergebühr · YP", "35,03 €"],
        ["Treibstoffzuschlag · YQ", "115,00 €"],
        ["Sicherheitsgebühr · PT", "7,12 €"],
        ["Custo", "444,15 €", "sum"],
        ["Copagamento", "− 79,00 €", "sum"],
        ["Reembolso", "365,15 €", "sum big"]
      ],
      note: P("Copagamento") + " 79 € — der Anteil, den der Passagier selbst trägt; er wird immer abgezogen, bei jedem Antrag. Bei Studierenden sind es 59 €." },

    { t: "h2", v: "Wem es zusteht", p: "Das Portal entscheidet das anhand der Daten von Autenticação.gov, der Finanzverwaltung und der Sozialversicherung. Beeinflussen lässt sich das nicht, aber es hilft zu wissen, welcher Kategorie Sie zugeordnet wurden: Davon hängt die Höhe Ihres Eigenanteils ab. Eine schnelle Prüfung mit drei Fragen — <a class=\"lnk\" href=\"/?p=check\">auf der ersten Seite</a>." },
    { t: "who", v: [
      ["Residente", "Im autonomen Gebiet gemeldet. Das Portal prüft automatisch, dass Sie hier mindestens sechs Monate gelebt haben."],
      ["Residente Equiparado na RA Madeira", "Vor weniger als sechs Monaten zugezogen und übt hier einen öffentlichen Dienst aus."],
      ["Estudante na RA Açores", "Studierender, der auf den Azoren studiert."],
      ["Estudante no Continente/Estrangeiro", "Studierender von den Inseln, der auf dem Festland oder im Ausland studiert."]
    ] },
    { t: "p", v: "Ausländer benötigen einen gültigen " + P("título de residência") + " — das Portal erinnert beim Zugang mit einem eigenen Fenster daran. Ehepartner, Kinder und Angehörige werden vorab im Profil hinzugefügt, dann gehören ihre Flüge in denselben Antrag: <a class=\"lnk\" href=\"../familia/\">Familie</a>." },

    { t: "h2", v: "Was erstattet wird und was nicht", p: "Die Liste hinter genau diesem ⓘ-Symbol. Alles aus der linken Spalte wird aus der Rechnung in die Felder des vierten Schritts übertragen; alles aus der rechten — nicht, auch wenn es in der Rechnung steht." },
    { t: "cols", yesH: "Wird erstattet",
      yes: [
        "Tarif der Economy-Klasse",
        "Flughafengebühren",
        "Ausstellungsgebühr · " + P("XP") + " oder " + P("OB"),
        "Treibstoffzuschlag · " + P("YQ"),
        "Passagiergebühr · " + P("YP"),
        "CO2-Abgabe · " + P("J9"),
        "Sicherheitsgebühr · " + P("PT"),
        "Gepäck, wenn im Tarif enthalten",
        "Sitzplatzwahl, Check-in und Priority Boarding — wenn im Tarif enthalten"
      ],
      noH: "Wird nicht erstattet",
      no: [
        "Reiseversicherung",
        "Gepäcküberzug",
        "Bankgebühren",
        "Zuzahlungen nach dem Ticketkauf",
        "Jede Option, die nicht im Grundpreis enthalten ist",
        "Gepäck, Sitzplatzwahl, Check-in und Priority — wenn separat gekauft"
      ] },
    { t: "warn", h: "Zwei Regeln, die leicht übersehen werden",
      p: "Die Ausstellungsgebühr wird höchstens mit 35 € pro Richtung und 70 € für Hin- und Rückflug angerechnet. In der Rechnung kann sie " + P("XP") + ", " + P("YR") + ", " + P("OB") + " oder " + P("DV") + " heißen.",
      p2: "Wenn Sie mit Meilen oder einem Geschenkgutschein geflogen sind — einzutragen sind nur die Euro, die tatsächlich von der Karte abgebucht wurden." },

    { t: "h2", v: "Rabatt und Kontrolle", p: "Die Gebührenfelder im Portal haben kein Sternchen: leer gehen sie ohne Fehlermeldung durch, und bei einem normalen Ticket sind das rund 157 € — über ein Drittel der Erstattung. Die Kontrolle ist deshalb der einzige Schutz." },
    { t: "warn", h: "Der Rabatt wird vom Tarif „hin“ abgezogen",
      p: "In unserer Rechnung ergibt die Berechnungszeile für den Tarif hin <b>202,00</b>, und auf der ersten Seite steht " + P("DESCONTO") + " <b>5,00</b>. Ins Portal wurde <b>197,00</b> eingetragen — 202,00 minus Rabatt. " + P("Custo") + " ergab 444,15, genau wie das " + P("TOTAL") + " der Rechnung, und der Antrag wurde genehmigt.",
      p2: "Die Kontrolle ist einfach: Addieren Sie beide Tarife und alle Gebühren. Es muss genau das " + P("TOTAL") + " von der ersten Seite der Rechnung ergeben. Kommt mehr heraus — dann wurde der Rabatt nicht abgezogen." },

    { t: "h2", v: "Es gibt keine Obergrenze mehr", p: "Bis zum 6. Juni 2026 war die Erstattung auf 400 € pro Reise begrenzt. Das Lei n.º 23/2026 hat diese Grenze aufgehoben, aber die offizielle Seite des Dienstes nennt weiterhin 400 € — und zwei unserer Anträge über diesem Betrag wurden voll ausgezahlt, abzüglich " + P("Copagamento") + ". Ausführlich, mit Differenzrechner — <a class=\"lnk\" href=\"/?p=news\">Was sich im Gesetz geändert hat</a>." }
  ],
  refH: "Weiter",
  refs: [
    ["../", "Anleitung", "Der Antrag in fünf Schritten", "Jeder Bildschirm des Portals und jedes Feld — mit echten Bildschirmfotos und der Rechnung daneben."],
    ["../rejeitado/", "Merkblatt 2", "Erster Zugang: „Rejeitado“ ist keine Ablehnung", "Warum das Portal schon bei der Registrierung ablehnt und was der persönliche Bereich überhaupt enthält."],
    ["../familia/", "Merkblatt 3", "Familie und für andere beantragen", "Wie Sie Ehepartner und Kinder hinzufügen — und Regel Nummer eins, wenn Sie nicht für sich selbst beantragen."]
  ],
  shareBtn: "Diese Seite senden",
  shareTitle: "Wie viel Geld und wofür — nDm",
  shareText: "Subsidie für Flüge: was erstattet wird und was nicht —",
  copied: "Link kopiert"
};
