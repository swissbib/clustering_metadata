Im swissbib Projekt ist die Essenz all unserer Aktivitäten der Umgang mit und die Aufbereitung von (Meta) - Daten. Normalisieren, Anreichern, Clustern (Zusammenführen) sowie Verknüpfen von Informationen und dies alles auf maschineller Basis ist die Grundlage dafür, dass wir Services wie verschiedene Discoveries, unterschiedliche Schnittstellen oder Dienstleistungen für Dritte anbieten können.


Vor allem für das maschinelle Clustern von Daten nutzen wir die (kommerzielle) Software eines Partners, die es uns flexibel ermöglicht, Daten so aufzubereiten, dass man sie für die unterschiedlichen Services einsetzen kann. Dies war kein statischer Vorgang in dem Sinne, dass die Software einmal geschrieben war und dann ihren Dienst erfüllen konnte sondern ein iterativer Prozess über Jahre, in denen sowohl wir (in den letzten Jahren vor allem unsere Kollegin Silvia Witzig) von der Nutzerinnenseite als auch unser Partner gegenseitig Wissen in den Prozess zur Verbesserung der Datenaufbereitung einbrachten.


Seit gefühlt zwei, drei Jahren lassen sich kaum mehr Artikel zum Thema Daten und Informationen finden, in denen nicht mindestens einmal Begriffe wie "Maschinelles Lernen", "Artificial Intelligence" (AI) oder "Neuronale Netze" erwähnt und als das Erfolgsrezept für die Zukunft beschrieben werden. Sollte damit das, was wir in den letzten 12 Jahren gemacht haben zum alten Eisen zählen und nicht mehr relevant sein? Da wir ja nun nicht dafür bekannt sind, eine Scheu vor neuen Softwaretechnologien zu haben, schauen wir schon immer regelmässig "über den Gartenzaun" um mitzubekommen, ob sich die neuen Methoden nicht mit unseren "klassischen" Methoden verbinden liessen. Das Problem dabei: Bevor man aus der Menge des Möglichen etwas vielleicht gut Versprechendes wählen, ausprobieren und dann vielleicht produktiv einsetzen  kann, muss man sich erstmal durch die Grundlagen und Begrifflichkeiten des neuen Themengebiets kämpfen. Nicht so einfach für ein swissbib Team, dass mit Personen nicht üppig ausgestattet ist und den Laden (sprich die "grünen, orangenen oder wie auch immer farblichen Services") am Laufen halten muss.


Helfen kann in so einer Situation, manchmal, Begeisterung für die Sache, Offenheit (auch von Software) und ein Netz von Personen, die man, auch wenn sie von ausserhalb und nicht aus dem "Bibliothekskuchen" kommen, neugierig machen und letztendlich davon überzeugen kann, dass "unsere Daten" die Basis für coole Projekte sein können. So geschehen mit Andreas Jud, ein Freund, der sich in einer Weiterbildung an der EPF Lausanne mit Methoden des maschinellen Lernes beschäftigt hat. Im Rahmen seines Abschlussprojekts hat er untersucht, welche der zahlreichen Methodiken sich für das Clustern von bibliographischen Metadaten einsetzen liessen. Auf diesem Blog wird er in die ausgewählten Methoden und Ergebnisse  einführen,  die komplette Dokumentation ist als eine Serie von Jupyternotebooks frei verfügbar.


Wie weiter? Die Abschlussarbeit an der EPFL ist eine tolle Basis, auf der sich weiter aufbauen lässt. Die Ergebniscluster sind von guter Qualität.

Bereiche, an denen gearbeitet werden kann/muss/sollte:


    Für die genutzten Modelle im Rahmen des maschinellen Lernens mussten Featurematrizen generiert werden. Die Daten, welche in den Features berücksichtigt wurden, haben, wegen des knappen Zeitrahmens und weil es sich um ein "Freizeitprojekt" handelt noch nicht die Qualität und Ausprägung, wie wir das in Jahren auf unserer produktiven swissbib Komponente entwickeln konnten.
    Skalierbarkeit des Verfahrens.
    Die Projektarbeit von Andreas hatte ihren Schwerpunkt im Gegenüberstellen und Ergebnisvergleich unterschiedlicher Methoden. Optimierunsmöglichkeiten in der Verarbeitung wurden bisher nicht berücksichtigt. Aktuell fassen wir zwei Varianten ins Auge:

        Ähnlich wie in unserem produktiven System können sogenannte "Pre-cluster" gebildet, so dass der Datenraum, auf den die Verfahren angewendet werden, sehr viel kleiner wird.
        Seit drei Jahren beschäftigen wir uns im Projekt mit Softwarekomponenten, die für die verteilte Verarbeitung eingesetzt werden. In anderen Posts auf diesem Blog haben wir darüber bereits berichtet . Dies gibt uns einige Möglichkeiten, Lösungen für das Skalierungsproblem zu finden. Kommt hinzu, dass wir im Rahmen des Memobaseprojekts den Grossteil der Infrastruktur für das Projekt auf einem Kubernetes Cluster der Uni Basel aufsetzen. Hier lernen und sehen wir, dass in vielleicht zwei bis drei Jahren die Frage von knappen Rechnerressourcen ein viel geringere Rolle als z.T. heute noch spielen wird. Die Abstraktionsschicht Kubernetes lässt leicht zwischen der eigenen (privaten) Cloud oder einer Public Cloud wie Google und Co., auch nur temporär, wechseln.

    "Die Mischung machts"
    Auch wenn die Ergebnisse der Abschlussarbeit vielversprechend und die Möglichkeiten moderner offener Software noch so cool sind, bleibt der alte Spruch "garbage in, garbage out". Modelle des maschinellen Lernens müssen trainiert werden und die in die Modelle einfliessenden Daten möglichst von guter Qualität. Auch ist dies nicht ein einmaliger, statischer Vorgang sondern ein iterativer. Für diesen Prozess braucht es sowohl Menschen, die sich mit Daten und auch Formaten auskennen, als auch Personen auf der Softwareseite. Mit unseren swissbib Erfahrungen bringen wir Know-How auf beiden Seiten ein und werden auch versuchen, in den kommenden 6 Monaten unsere Expertise, die wir mit der "klassischen" Komponente gesammelt haben und die uns nach wie vor hervorragende Ergebnisse liefert, noch besser zu dokumentieren. 
    Ein offenes Projekt mit vielen Wegen und Möglichkeiten.
    Als "Freizeitprojekt" kann man über knappe Ressourcen klagen, gleichzeitig bietet dies aber auch vielfältige Einstiegsmöglichkeiten für Personen mit unterschiedlichem Hintergrund. Es war lustig mit anzusehen, wie Andreas als promovierter Physiker mit Interesse und Ausdauer die MARC-Regeln der LOC studiert und den Input aus unserem swissbib Team für sein Arbeit aufgenommen hat. Das nun vorliegende Ergebnis, wie Methoden des maschinellen Lernens auf den Bereich "Aggregation (Clustern) von bibliographischen Metadaten" angewendet werden können, bietet für Menschen mit eher informationswissenschaftlichem Hintergrund eine Möglichkeit, die Magie, die mit den Themen maschinelles Lernen und AI einherzugehen scheint, besser anzupacken. Wir freuen uns dazu über Rückmeldungen und versuchen, in diesem Blog weiter zu berichten.
      

Eine Anekdote zum Abschluss.

Bei der Verteidigung des Projekts an der EPFL sassen Andreas Prüfer gegenüber, die äusserten, dass er mit einem "tollen Datensatz" gearbeitet hat und natürlich auch seine Ergebnisse lobten. Das hat selbstverständlich auch uns gefreut. Vielleicht ist dies aber auch ein Satz, der zum Nachdenken darüber anregt, ob unsere Daten nicht mehr verdient haben, als nur in ein Bibliothekssystem mit relationalem Datenbankssystem gesteckt zu werden.