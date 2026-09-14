T.de = {
  eyebrow: "nDm · Subsídio de Mobilidade",
  h1: "Der Antrag in fünf Schritten",
  lead: "Der Staat erstattet den Inselbewohnern den größten Teil des Ticketpreises. Das Geld kommt auf das Bankkonto — wenn Sie die fünf Bildschirme des Portals durchlaufen und sieben Zahlen korrekt aus der Rechnung der Fluggesellschaft übertragen. Hier wird jeder Bildschirm und jedes Feld gezeigt — und dort, wo Menschen dieses Geld verlieren.",
  by: "Kostenlos, ohne Registrierung. Wir erledigen nichts für Sie — wir zeigen, wie Sie es selbst erledigen.",
  facts: ["5 Bildschirme", "7 Zahlen aus der Rechnung", "≈ 15 Tage bis zum Geld"],

  needH: "Was Sie vor dem Einstieg bereithalten müssen",
  needP: "Ohne diese Dinge lässt das Formular Sie nicht weiter, und mitten im Antrag zurückzugehen und etwas nachzutragen geht nicht — der Entwurf verliert Felder. Deshalb erst alles zusammenstellen, dann einsteigen.",
  need: [
    "Zwei PDFs von TAP: <b>die Rechnung</b> " + P("AIE APXIE026_….pdf") + " (mit dem Anhang Declaração para efeitos de Subsídio de Mobilidade) und der <b>Reisenachweis</b> " + P("BoardingProofTAP_….pdf") + ". Wie Sie beide bestellen — <a class=\"lnk\" href=\"../tap/\">Documentos TAP</a>.",
    P("IBAN") + " und Telefonnummer, im Portalprofil eingetragen, sowie ein vom Sachbearbeiter genehmigtes " + P("Comprovativo do IBAN") + ". Wenn beim ersten Zugang ein rotes " + P("Rejeitado") + " erscheint — das ist keine Ablehnung: <a class=\"lnk\" href=\"./rejeitado/\">Erster Zugang</a>.",
    P("Chave Móvel Digital") + " oder Cartão de Cidadão mit Lesegerät — einen anderen Zugang zum Portal gibt es nicht.",
    "Wenn Sie mit Ehepartner oder Kindern geflogen sind — sie müssen vorher im Profil hinzugefügt werden: <a class=\"lnk\" href=\"./familia/\">Familie</a>."
  ],
  needNote: "Ob Ihnen die Subsidie überhaupt zusteht — <a class=\"lnk\" href=\"/?p=check\">drei Fragen</a>, eine halbe Minute. Was genau erstattet wird und wie viel — <a class=\"lnk\" href=\"./dinheiro/\">Wie viel Geld und wofür</a>.",

  exH: "So sehen wir es an diesem Beispiel",
  exP: "Unten steht ein echter Antrag: Funchal → Lissabon → Funchal, TAP, Ansässiger von Madeira. Genehmigt und ausgezahlt. Alle Zahlen in den Schritten stammen aus seiner Rechnung, und es wird jeweils gezeigt, aus welcher Zeile genau.",
  calcHead: "Wie das Portal die Erstattung berechnet hat",
  calc: [
    ["Tarif hin · 202,00 − 5,00 Rabatt", "197,00 €"],
    ["Tarif zurück", "90,00 €"],
    ["Passagiergebühr · YP", "35,03 €"],
    ["Treibstoffzuschlag · YQ", "115,00 €"],
    ["Sicherheitsgebühr · PT", "7,12 €"],
    ["Custo", "444,15 €", "sum"],
    ["Copagamento", "− 79,00 €", "sum"],
    ["Reembolso", "365,15 €", "sum big"]
  ],
  calcNote: P("Copagamento") + " 79 € — der Anteil, den der Passagier selbst trägt; er wird immer abgezogen. Woher die übrigen Zahlen stammen und was gar nicht erstattet wird — <a class=\"lnk\" href=\"./dinheiro/\">Wie viel Geld und wofür</a>.",

  openBtn: "Portal öffnen",
  copyBtn: "Adresse kopieren",
  copiedLink: "Adresse kopiert",
  openHint: "Am Computer öffnet sich das Portal in einem eigenen Fenster rechts — die Anleitung bleibt links. Zugang nur mit " + P("Chave Móvel Digital") + " oder Cartão de Cidadão. Klicken Sie auf der Startseite des Portals auf " + P("Submeter Pedido") + ".",

  stepsH: "Fünf Bildschirme des Assistenten",
  stepsP: "Links im Portal sehen Sie die Liste der Schritte. Anklicken können Sie sie nicht — zurück geht es nur über die Schaltfläche " + P("Anterior") + ", Schritt für Schritt. Das sollten Sie vorher wissen.",
  steps: [
    {
      h: "Dados Gerais do Beneficiário",
      p: "Der erste Bildschirm fragt nichts ab. Alle sechs Felder sind grau — Name, NIF, Postleitzahl, Ort, E-Mail und Telefon kommen von Autenticação.gov und lassen sich hier nicht ändern. Es gibt genau ein aktives Element.",
      imgs: [{ src: "img/c1.jpg", cap: "Das Einzige, was sich im ersten Schritt anklicken lässt." }],
      fields: [
        P("Residente Equiparado há menos de 6 meses a exercer funções públicas na Região Autónoma?") + " — wird nur gesetzt, wenn Sie vor weniger als sechs Monaten in die Region gezogen sind und hier einen öffentlichen Dienst ausüben. In allen anderen Fällen — nicht anrühren."
      ],
      after: "Eine „Zurück“-Schaltfläche gibt es im ersten Schritt nicht — nur " + P("Seguinte") + ".",
      warn: {
        h: "Postleitzahl und Ort bleiben leer",
        p: P("Código Postal") + " und " + P("Localidade") + " lassen sich weder hier noch im persönlichen Bereich ausfüllen — das Portal zeigt die Felder, gibt sie aber nicht zur Bearbeitung frei.",
        p2: "Auf den Anspruch auf die Subsidie hat das keinen Einfluss: In unserem Antrag ist die Postleitzahl leer, und der Status lautet " + P("Validado") + "."
      }
    },
    {
      h: "Informação bancária",
      p: "Ein einziges Feld. Auch es ist grau: Das Portal übernimmt, was im Profil hinterlegt ist.",
      imgs: [{ src: "img/c2.jpg", cap: "Der ganze Schritt — ein einziges Feld, nur lesbar." }],
      fields: [
        P("IBAN") + " — nur lesbar. Geändert wird er in " + P("Área Pessoal") + " → " + P("Alterar Dados") + " (wo das ist und wie es aussieht — <a class=\"lnk\" href=\"./rejeitado/\">Erster Zugang</a>)."
      ],
      warn: {
        h: "Halten Sie inne, wenn das Konto nicht Ihres ist oder das Feld leer ist",
        p: "Das Geld geht genau auf diese IBAN. Kehren Sie zur Startseite zurück, öffnen Sie " + P("Área Pessoal") + ", korrigieren Sie das Konto — und beginnen Sie erst danach den Antrag."
      }
    },
    {
      h: "Dados da Viagem",
      p: "Der längste Bildschirm. Er gliedert sich in drei Teile: Rechnung, Reiseroute und zwei Dateien. Wir gehen ihn teilweise durch — und zeigen, woher in der Rechnung jede Zahl stammt.",
      imgs: [{ src: "img/c3.jpg", cap: "Teil eins: die Rechnung." }],
      fields: [
        P("NIF da Entidade Emissora") + " — die Steuernummer dessen, der die Rechnung ausgestellt hat. Bei TAP ist das " + P("500278725") + ". Hat ein ausländisches Reisebüro die Rechnung ausgestellt, verlangt das Portal die Eingabe von " + P("000000000") + ".",
        P("Data de Emissão do Bilhete") + " — das Ausstellungsdatum des Tickets. Das Portal warnt: nicht vor dem " + P("15/01/2026") + ".",
        P("Número da Fatura") + " — die vollständige Rechnungsnummer, mitsamt dem Buchstabenpräfix: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — das Datum der Rechnung selbst. Das ist weder das Ausstellungsdatum des Tickets noch das Abflugdatum."
      ],
      imgs2: [{ src: "img/f1.jpg", cap: "Die erste Seite der Rechnung AIE APXIE026_….pdf, die TAP auf Anfrage zusendet. Von hier stammen Nummer, Daten und die NIF der Fluggesellschaft." }],
      fields2: [
        P("Número da Fatura") + " — die vollständige Nummer, mitsamt den Buchstaben: " + P("AIE APXIE026/04544710") + ".",
        P("Data da Fatura") + " — das Datum rechts neben der Nummer. In diesem Beispiel " + P("2026-08-22") + ".",
        P("NIF da Entidade Emissora") + " — " + P("500278725") + ". Sie müssen ihn nirgends suchen: Er steht im Kopf der Rechnung, in der Zeile „Matriculada na CRC de Lisboa e NIPC“.",
        P("Data de Emissão do Bilhete") + " — Spalte " + P("DT.EMISSÃO") + ". Hier " + P("2026-07-31") + ": Das Ticket wurde am 31. Juli ausgestellt, die Rechnung am 22. August. Das sind zwei verschiedene Daten, und das Portal fragt nach beiden.",
        P("E-Ticket") + " — Spalte " + P("NR. DOC.") + ", dreizehn Ziffern, beginnt mit " + P("047") + ". Wird im vierten Schritt gebraucht.",
        "Die Spalte " + P("TOTAL") + " wird nicht ins Portal übertragen, dient aber der Kontrolle: " + P("Custo") + ", das das Portal selbst berechnet, muss mit dieser Zahl übereinstimmen.",
        "Die Spalte " + P("DESCONTO") + " — steht dort ein Rabatt, merken Sie ihn sich. Im vierten Schritt müssen Sie ihn vom Tarif abziehen, sonst stimmt die Summe nicht."
      ],
      imgs3: [{ src: "img/c4.jpg", cap: "Teil zwei: die Reiseroute. Darunter derselbe Block für Volta." }],
      fields3: [
        P("Origem Inicial da Viagem") + " und " + P("Destino Final da Viagem") + " — hier stehen Regionen, keine Flughäfen: " + P("Madeira") + ", " + P("Lisboa") + ".",
        P("Data de Partida") + " und " + P("Hora de Partida") + " sind Pflichtfelder. " + P("Data de Chegada") + " und " + P("Hora de Chegada") + " — ohne Sternchen, aber ausfüllen: Der Sachbearbeiter gleicht sie mit der Bordkarte ab. Daten und Uhrzeiten stammen aus den Segmenten auf Seite zwei der Rechnung (gezeigt in Schritt 4).",
        P("Companhia Aérea") + " und " + P("Número de Reserva") + " — der sechsstellige Buchungscode, das Portal zeigt als Hinweis " + P("EX: WAAXYI") + ". Das ist nicht die Ticketnummer.",
        P("Acrescentar Escala?") + " — " + P("Sim") + " nur, wenn es innerhalb eines Tickets einen Zwischenstopp gab."
      ],
      imgs4: [{ src: "img/c5.jpg", cap: "Teil drei: zwei Dateien. Die dürfen nicht verwechselt werden." }],
      fields4: [
        P("Fatura(s) de Viagem emitidas por Companhia Aérea ou intermediário") + " — hierhin kommt die <b>Rechnung</b>: Bei TAP ist das die Datei " + P("AIE APXIE026_….pdf") + ".",
        P("Título(s) de Viagem: Bilhete ou Confirmação de Reserva") + " — hierhin kommt der <b>Reisenachweis</b>: " + P("BoardingProofTAP_….pdf") + ".",
        P("Adquiriu a sua viagem através de agência ou outro intermediário de viagens?") + " — " + P("Não") + ", wenn das Ticket direkt bei der Fluggesellschaft gekauft wurde."
      ],
      warn: {
        h: "Hier passiert die häufigste Verwechslung",
        p: "Die beiden Dokumente sind nicht austauschbar. Und ein überflüssiges Dokument ist ebenfalls ein Fehler: In einem echten Korrekturbescheid steht " + P("O documento submetido não é necessário") + " — „das eingereichte Dokument wird nicht benötigt“.",
        p2: "Wie Sie bei TAP beide Dokumente bestellen, zeigt die Ausgabe <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a> — öffnet sich in einem neuen Tab."
      }
    },
    {
      h: "Dados dos passageiros",
      p: "Hier taucht das Geld auf. Sieben Felder mit Zahlen, und alle sieben werden aus der Rechnung übertragen — der Datei " + P("AIE APXIE026_….pdf") + ", die TAP auf Anfrage zusendet (wie Sie sie bestellen — <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>). Welche Gebühren erstattet werden und welche nicht — <a class=\"lnk\" href=\"./dinheiro/\">Wie viel Geld und wofür</a>.",
      imgs: [{ src: "img/c6.jpg", cap: "Ticketnummern. Auf dem Bild sieht man, wie ein gespeicherter Entwurf endet." }],
      fields: [
        P("Vai participar na viagem?") + " — muss auf " + P("Sim") + " stehen. Solange " + P("Não") + " steht, gibt es auf dem Bildschirm überhaupt keine Betragsfelder, und die Erstattung wird als 0 € angezeigt.",
        P("E-Ticket (Ida)") + " und " + P("E-Ticket (Volta)") + " — Ticketnummern, dreizehn Ziffern, bei TAP beginnen sie mit " + P("047") + ".",
        "Auf diesem Bild ist " + P("E-Ticket (Volta)") + " leer und " + P("Valor da Tarifa (Volta)") + " gleich null. So sieht ein Entwurf aus, nachdem er gespeichert und neu geöffnet wurde."
      ],
      imgs2: [{ src: "img/c7.jpg", cap: "Sieben Zahlen. Die Gebührencodes sind dieselben wie in der TAP-Rechnung." }],
      fields2: [
        P("Valor da Tarifa (Ida)") + " und " + P("(Volta)") + " — der reine Tarif, ohne Gebühren.",
        P("Taxa de Emissão de Bilhete - XP") + " — in der Rechnung kann sie als " + P("YR") + ", " + P("OB") + " oder " + P("DV") + " stehen. Angerechnet werden höchstens 35 € pro Richtung und 70 € für Hin- und Rückflug.",
        P("Taxa de Serviço a Passageiros - YP") + ", " + P("Sobretaxa de Combustível - YQ") + ", " + P("Taxa de Carbono - J9") + " und " + P("Sobretaxa de Segurança - PT") + " — werden zeilenweise nach Codes aus der Rechnung übertragen. Die Gebührenfelder haben kein Sternchen: leer gehen sie ohne Fehlermeldung durch, und bei einem normalen Ticket sind das rund 157 € — über ein Drittel der Erstattung.",
        "Schreiben Sie ein Komma, keinen Punkt. Wo kein Wert vorhanden ist — tragen Sie 0 ein."
      ],
      imgs3: [{ src: "img/f2.jpg", cap: "Die zweite Seite der Rechnung — Declaração para efeitos de Subsídio de Mobilidade. Alle sieben Zahlen stehen hier." }],
      fields3: [
        "<b>Die Tarifberechnungszeile</b> — die einzige Stelle in allen Dokumenten, an der der Tarif in „hin“ und „zurück“ aufgeteilt ist. " + P("FNC TP LIS202.00TP FNC90.00EUR292.00END") + " liest sich von links nach rechts: von FNC mit Flug TP nach LIS — <b>202,00</b>; weiter mit Flug TP nach FNC — <b>90,00</b>; insgesamt 292,00. Die erste Zahl kommt in " + P("Valor da Tarifa (Ida)") + ", die zweite in " + P("Valor da Tarifa (Volta)") + ".",
        "<b>Gebühren nach Codes.</b> " + P("YQ") + " 115,00 → " + P("Sobretaxa de Combustível - YQ") + "; " + P("PT") + " 7,12 → " + P("Sobretaxa de Segurança - PT") + "; " + P("YP") + " 35,03 → " + P("Taxa de Serviço a Passageiros - YP") + ". Die Zeile " + P("FARE") + " ist die Summe der Tarife, sie wird nicht ins Portal übertragen. Fehlt ein Code in der Liste — bleibt im Portal null.",
        "Die Spalte " + P("Tarifa") + " auf der ersten Seite der Rechnung enthält YQ bereits — diese Zahl wird nicht ins Tariffeld übertragen, sonst verdoppelt sich der Treibstoffzuschlag und der Antrag geht zur Korrektur zurück.",
        P("XVYV7W/1A") + " — der Buchungscode. Die ersten sechs Zeichen kommen in " + P("Número de Reserva") + " im dritten Schritt.",
        "Segmente: Flugnummer, Datum, Flughäfen. Von hier stammen Abflug- und Ankunftsdaten für den dritten Schritt, und hier sieht man auch, welcher „hin“ und welcher „zurück“ ist."
      ],
      imgs4: [{ src: "img/c9.jpg", cap: "Das Portal rechnet selbst. Prüfen müssen Sie trotzdem selbst." }],
      fields4: [
        "Unten addiert das Portal " + P("Custo") + ", zieht " + P("Copagamento") + " ab und zeigt " + P("Reembolso Total") + ". Wirkt die Summe seltsam — fast immer wurde ein Feld vergessen, nicht das Portal hat sich geirrt."
      ],
      warn: {
        h: "Falle: Guardar Rascunho bei einer Hin- und Rückreise",
        p: "Wir haben einen Entwurf über 208 € gespeichert, uns abgemeldet und sind zurückgekehrt — das Rücksegment war verschwunden: " + P("E-Ticket (Volta)") + " leer, " + P("Valor da Tarifa (Volta)") + " null, die Summe fiel auf 118 €.",
        p2: "Und das ist kein Anzeigefehler: Nach dem Verlassen stand auch in der Antragsliste 118 €. Füllen Sie alles in einem Durchgang aus und senden Sie es ab."
      },
      warn2: {
        h: "Der Rabatt wird vom Tarif „hin“ abgezogen",
        p: "In unserer Rechnung ergibt die Berechnungszeile für den Tarif hin <b>202,00</b>, und auf der ersten Seite steht " + P("DESCONTO") + " <b>5,00</b>. Ins Portal wurde <b>197,00</b> eingetragen — also 202,00 minus Rabatt. " + P("Custo") + " ergab 444,15, genau wie das " + P("TOTAL") + " der Rechnung, und der Antrag wurde genehmigt.",
        p2: "Die Kontrolle ist einfach: Addieren Sie beide Tarife und alle Gebühren. Es muss genau das " + P("TOTAL") + " von der ersten Seite ergeben. Kommt mehr heraus — dann wurde der Rabatt nicht abgezogen."
      }
    },
    {
      h: "Próximos Passos",
      p: "Der fünfte Bildschirm erscheint erst nach dem Klick auf " + P("Submeter") + ". Ein Bild davon haben wir noch nicht — wir haben keinen echten Antrag nur für ein Foto abgeschickt. Beim nächsten echten Flug gehen wir die Einreichung durch und ergänzen es hier. Ehrlich gesagt: Dieser Schritt wird hier nicht gezeigt. Was nach dem Absenden passiert — <a class=\"lnk\" href=\"#depois\">Nach dem Einreichen</a>.",
      imgs: []
    }
  ],

  mapH: "Übersicht: was wo in der Rechnung steht",
  mapP: "Kurz, um es beim Ausfüllen vor Augen zu haben. Die Rechnung ist die Datei " + P("AIE APXIE026_….pdf") + " von TAP, zwei Seiten; die zweite heißt " + P("Declaração para efeitos de Subsídio de Mobilidade") + ". Wie Sie sie bestellen — <a class=\"lnk\" href=\"../tap/\" target=\"_blank\" rel=\"noopener\">Documentos TAP</a>.",
  mapHead: ["Feld im Portal", "Wo in der Rechnung", "Was zu beachten ist"],
  map: [
    [P("Valor da Tarifa (Ida)") + "<br>" + P("Valor da Tarifa (Volta)"), "S. 2, Tarifberechnungszeile", "Zwei Zahlen hintereinander: …LIS<b>202.00</b>TP FNC<b>90.00</b>"],
    [P("Taxa de Emissão de Bilhete - XP"), "S. 2, Gebührenblock", "Kann als YR, OB oder DV stehen. Maximal 35 € / 70 €"],
    [P("Taxa de Serviço a Passageiros - YP"), "S. 2, Zeile YP", "Flughafengebühr pro Passagier"],
    [P("Sobretaxa de Combustível - YQ"), "S. 2, Zeile YQ", "Meist die größte Gebühr"],
    [P("Taxa de Carbono - J9"), "S. 2, Zeile J9", "Fehlt oft in der Liste — dann null"],
    [P("Sobretaxa de Segurança - PT"), "S. 2, Zeile PT", "In der Rechnung einfach PT"],
    [P("Número de Reserva"), "S. 2, über der Tarifzeile", "Sechs Zeichen vor dem Schrägstrich"],
    [P("Número da Fatura"), "S. 1, Kopf rechts", "Mitsamt den Buchstaben: AIE APXIE026/…"],
    [P("Data da Fatura"), "S. 1, neben der Nummer", "Datum der Rechnung, nicht das Abflugdatum"],
    [P("Data de Emissão do Bilhete"), "S. 1, Spalte DT.EMISSÃO", "Ein anderes Datum — wann das Ticket ausgestellt wurde"],
    [P("E-Ticket"), "S. 1, Spalte NR. DOC.", "13 Ziffern, beginnt mit 047"],
    [P("NIF da Entidade Emissora"), "S. 1, Kopf links", "500278725 — in der Zeile zu NIPC"],
    ["<b>Kontrolle</b>", "S. 1, Spalten TOTAL und DESCONTO", "Summe aller Portalfelder = TOTAL. Rabatt vom Tarif „hin“ abziehen"]
  ],
  outK: "Ausgabe 1",
  outT: "Documentos TAP",
  outD: "Wie Sie bei der Fluggesellschaft beide Dokumente bestellen — Rechnung und Reisenachweis. Acht Bildschirme, drei Fallen.",

  timeH: "Nach dem Einreichen: wie lange warten",
  timeP: "Der Antrag durchläuft einen menschlichen Sachbearbeiter: Er öffnet jede angehängte Datei und genehmigt sie einzeln. Genau das kostet Zeit.",
  timeHead: ["Ereignis", "Wann", "Was passiert"],
  times: [
    [P("Submeter Pedido"), "0", "Der Antrag wird abgeschickt"],
    [P("Em Análise"), "sofort", "Der Status ändert sich automatisch"],
    [P("Aprovar") + " der Dokumente", "ab einer Stunde", "Der Sachbearbeiter öffnet jede Datei einzeln"],
    [P("Aprovado"), "2–11 Tage", "Das Sechs-Monats-Wohnsitzkriterium ist geprüft"],
    [P("Pagamento Efetuado"), "+2–4 Tage", "Das Geld geht auf die IBAN"]
  ],
  timeNote: "Bei drei echten Anträgen vergingen von der Einreichung bis zum Geld 15, 12 und 2 Tage. Die Spanne ist groß und hängt davon ab, wie schnell der Sachbearbeiter zur letzten angehängten Datei kommt. Den Antrag verfolgen — unter " + P("Histórico de Pedidos") + " auf der Startseite des Portals.",
  statH: "Status",
  stats: [
    [P("Rascunho"), "Entwurf. Nicht abgeschickt und von niemandem eingesehen."],
    [P("Em Análise"), "Wird geprüft."],
    [P("Correção Solicitada"), "Es wird um Korrektur gebeten. Das ist keine Ablehnung — der Antrag wird neu geprüft."],
    [P("Aprovado"), "Genehmigt, das Geld steht zur Auszahlung an."],
    [P("Pago"), "Ausgezahlt."],
    [P("Compareceu / Não Compareceu"), "Eine gesonderte Prüfung, ob Sie tatsächlich geflogen sind. Bei einem ausgezahlten Antrag kann " + P("Não Verificado") + " stehen — das ist normal."]
  ],

  corrH: "Wenn Correção Solicitada kommt",
  corrP: "Das ist keine Ablehnung. Der Antrag geht zur Nachbesserung zurück und wird nach der Korrektur neu geprüft. Hier ist ein echter Bescheid — und beide Gründe darin betreffen genau das, wovon diese Seite handelt.",
  corrCap: "Análise de Pedido de Subsídio — der Bescheid kommt in den persönlichen Bereich.",
  corrQuote: [
    "„Ihr Antrag konnte aus den unten genannten Gründen nicht bestätigt werden. Der Antrag wird nach Korrektur des Folgenden neu geprüft:",
    "— " + P("Fatura de voo ou escala marítima - 01") + ": das beigefügte Dokument wird nicht benötigt.",
    "— Die Werte in den Feldern „valor da tarifa“ und den Gebühren stimmen nicht mit den eingereichten Dokumenten überein. Wir bitten, die Daten auf der Plattform zu aktualisieren (richtig wäre: Valor da Tarifa 45,50 €, Valor da Tarifa de Retorno 3,50 €, XP 0,00 €, YP 35,60 €, YQ 39,00 €, J9 0,00 €, PT 7,12 €).“"
  ],
  corrDo: "Was zu tun ist: " + P("Histórico de Pedidos") + " öffnen, den Antrag aufrufen und genau das korrigieren, was aufgeführt ist. Der Sachbearbeiter schreibt meist selbst die richtigen Werte — aber der Bescheid kommt erst zwei Wochen nach der Einreichung. Einfacher ist es, die Zahlen einmal sauber aus der Rechnung zu übertragen.",

  refH: "Zum Nachlesen",
  refP: "Was auf dieser Seite nur in einer Zeile erwähnt wird, ist an anderer Stelle ausführlich behandelt.",
  refs: [
    ["./dinheiro/", "Merkblatt 1", "Wie viel Geld und wofür", "Empfängerkategorien, die Liste dessen, was erstattet wird und was nicht, die Obergrenze für die Ausstellungsgebühr, der Rabatt und die Grenze, die es nicht mehr gibt."],
    ["./rejeitado/", "Merkblatt 2", "Erster Zugang: „Rejeitado“ ist keine Ablehnung", "Warum das Portal schon bei der Registrierung ablehnt, was zu tun ist, und was der persönliche Bereich überhaupt enthält."],
    ["./familia/", "Merkblatt 3", "Familie und für andere beantragen", "Wie Sie Ehepartner und Kinder hinzufügen, damit ihre Flüge in denselben Antrag gehören — und Regel Nummer eins, wenn Sie nicht für sich selbst beantragen."],
    ["../tap/", "Ausgabe 1", "Documentos TAP", "Wie Sie bei der Fluggesellschaft Rechnung und Reisenachweis bestellen. Acht Bildschirme, drei Fallen."]
  ],

  endH: "Wenn Sie nicht weiterkommen",
  endP: "Der einzige Kontakt im gesamten Portal ist " + P("infossm@ctt.pt") + ". Kein Telefon, kein Chat, kein Kontaktformular. Schreiben Sie auf Portugiesisch und geben Sie unbedingt die " + P("Número de Pedido") + " an.",
  lawP: "Seit dem 6. Juni 2026 gilt das Lei n.º 23/2026: Die Subsidie wurde in Mecanismo de Continuidade Territorial umbenannt, die Erstattungsobergrenze wurde aufgehoben, und das Portal ist noch nicht an die neuen Regeln angepasst. Was das für Sie ändert — <a class=\"lnk\" href=\"/?p=news\">Was sich im Gesetz geändert hat</a>.",
  shareBtn: "Diese Anleitung senden",
  shareTitle: "Der Antrag in fünf Schritten — nDm",
  shareText: "Subsidie für Flüge: wie Sie beantragen, ohne Geld zu verlieren —",
  copied: "Link kopiert"
};
