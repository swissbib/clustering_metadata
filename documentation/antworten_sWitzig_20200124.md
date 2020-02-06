* century : Stimmt die Aussage, dass es das Herstellungsjahr (year of origin) der bibliografischen Einheit ist? Soll ich es das Erscheinungsjahr (year of publication) nennen?
Das stimmt nur bedingt. Falls es sich um eine Ressource handelt die in einem Jahr erschienen ist (z.B. ein normales Buch) dann handelt es sich um das Erscheinungsjahr der Ressource. Falls es sich jedoch um eine Ressource handelt, die über einen Zeitraum erscheint (z.B. Zeitschrift, mehrbändiges Werk, etc.) dann handelt es sich um das erste Erscheinungsjahr der Ressource.
In CBS wird unter century nicht ein vollständiges Jahr sondern das Jahrhundert indexiert. Ich nehme aber nicht an, dass sowas für dich relevant ist.

* decade : Ermittelst du hier die Zehnerstelle des Jahrs, also die Dekade aus dem century? Kann ich es für meine Modellbildung weglassen?
Ja, hier wird in CBS die Dekade indexiert.

* exactDate : Ich werde das exactDate als vollständiges Herstellungsdatum der bibliographischen Einheint in meine Modellbildung einfliessen lassen. Alternativ könnte ich auf century verzichten. Wie fändest du das?
In exactDate und pubyear sind in deinen Daten die gleichen Werte enthalten. Im Vergleich zu century/decade sind hier die vollständigen Erscheinungsjahre der Ressource erfasst. D.h. bei Ressourcen, die über einen Zeitraum erscheinen, entsprechen die zweiten vier Zahlen dem letzten Erscheinungsjahr. Hingegen kann als zweites Jahr bei Ressourcen, die in einem Jahr erscheinen, zusätzlich ein Copyrightdatum oder das originale Erscheinungsjahr eines Nachdrucks erfasst sein. Ebenfalls möglich ist, dass es sich bie den zweiten vier Zahlen und Monat/Tag handelt und nicht um ein Jahr.
In den MARC-Daten wird durch einen weiteren Wert klar, um was für einen Fall es sich handelt. Ich kann nicht einschätzen, ob das für dich relevant ist oder nicht.
Für unser Clustering sind diese Unterschiede relevant und Jahre werden je nach Fall unterschiedlich indexiert. In exactDate zum Beispiel wird nur indexiert, wenn es sich bei den zweiten vier Zahlen um Monat/Tag handelt.

* pubyear : Kann ich auf dieses Feld verzichten, da ich dessen Inhalt schon mit exactDate abgedeckt habe?
Siehe unter exactDate

* corporate : Siehe meine Analyse in Jupyter Notebook 1_DataAnalysis. Stimmt diese für dich? Gebe ich dich im OneNote richtig wieder? Stimmt meine Beschreibung und der Entscheid im FeatureWiki?
Ja, ich denke du kannst auf 810 verzichten. Das ist wohl mehr standardmässig enthalten und macht auch bei uns kaum etwa aus.
Welche Stelle in OneNote meinst du?
Wichtig ist sicher, was ich letzte Woche gesagt habe: 110 und 710 auf jeden Fall zusammennehmen und nicht separat behandeln.

* doi : Kann ich den doi verwenden, wie Günter ihn mir schickt oder muss ich doi und urn unterscheiden? S. OneNote. Stimmt meine Beschreibung im FeatureWiki und in 1_DataAnalysis?
Wie unter http://www.loc.gov/marc/bibliographic/bd024.html beschrieben, werden im Feld, das wir für dich als doi exportiert haben, diverse Standardnummern erfasst. 
In CBS wird hier nur indexiert und verglichen, was tatsächlich eine DOI ist (zu erkennen an einem Unterfeld, das in deinen Daten nicht vorhanden ist oder natürlich auch an der Struktur der ID).

* edition : Kann ich das Attribut übernehmen ohne Transformation?
Ich denke nicht, aber dafür verstehe ich deine Methoden zu wenig.
In CBS wird edition sehr stark normalisiert damit verschiedene Varianten wie 2. Aufl., 2. Auflage, Zweite Auflage, etc. als gleich behandelt werden können.

* format : erscheint mir klar. Kannst du dennoch mal drüber schauen?
Hast du die Übersetzung der Codes, die wir auf swissbib.ch nutzen, mal gesehen? https://github.com/swissbib/vufind/blob/master/local/languages/formats/de.ini
In CBS verwende ich auch nur Teile des Codes, jedoch anders als du es vorgesehen hast: Bei VM01*, VM02*, MU03*, MU04* und CF01* verwende ich den ganzen Code. Bei allen anderen die ersten vier und die letzten zwei Stellen.

* isbn : Siehe meine Fragen in OneNote.
    Unter welchen Umständen wird ISBN und wann ISSN genommen?
    > ISBN ist der Identifier für Monographien, ISSN für Zeitschriften
    Wie unterscheide ich isbn von issn?
    > ISBN ist entweder 10- oder 13-stellig, ISSN ist 8-stellig
    Ist die Unterscheidung relevant?
    > Die ISBN und ISSN sind wegen der unterschiedlichen Länge nie identisch, daher nicht.
    Es gibt records mit bis zu 41 isbn Einträgen. Wie sind diese zu interpretieren? Wie sind diese zu verwenden für das Modell? Nehme ich einfach den ersten Eintrag?
    > Aufnahmen für mehrbändige Werke können mehrere ISBNs haben. In CBS werden diese alle indexiert. Ein Clustering wird nur verhindert wenn in den beiden Aufnahmen keine ISBNs übereinstimmen.

* ismn : Warum ist die ismn gleich dem doi, s. FeatureWiki? Kann ich sie dann weglassen?
Das Feld enthält in deinen Daten den gleichen Inhalt wie doi. 
In CBS wird hier nur indexiert, was eine ISMN ist (ebenfalls an einem weiteren Wert oder der Struktur erkennbar).

* coordinate : Das Attribut macht mich noch etwas unglücklich. Ich spiele mit dem Gedanken, aus der List nur das jeweils erste E- oder W-element und das jeweils erste N- oder S-element zu beziehen. Dann muss ich es noch umformen und die '.'e entfernen, sowie die Länge trimmen. Ist das schlau?
Ja, das sollte so Sinn machen. Ich habe den Eindruck, dass Günter dir hier mehr geliefert hat als er wollte. 
In CBS wird auch das jeweils erste E/W, resp. N/S-Element benutzt

* musicid : Vgl. 1_DataAnalysis, warum haben so viele Formate ungleich MU eine musicid?
Wie unter http://www.loc.gov/marc/bibliographic/bd028.html beschrieben, werden hier diverse Verlagsnummern erfasst. Diese werden hauptsächlich bei Musiknoten, Tonträger und Filmen erfasst. Ich denke es macht Sinn, wenn du diese insgesamt berücksichtigst.

* pages : Ist identisch mit volumes. Ich nehme an, hier wurden die Anzahl Seiten von volumes extrahiert und separat gespeichert. Nach welchem Algorithmus machst du das? Kann ich das Attribut weglassen?
Ja, das stimmt. Der Algorithmus dazu ist ziemlich ausgefeilt. Es wird einerseits versucht Angaben in denen nur Seitenzahlen enthalten sind zu erkennen (Bsp.: 768 p., 575 Seiten, 575 S.) und andererseits die Seitenzahlen aus Angaben, wo noch etwas anderes vorhanden ist auszulesen (Bsp.: 1 online resource (245 pages), xvii, 332 Seiten). Zudem wird hier eine Abweichung der Seitenzahl zugelassen in dem, dass +/- 1 Seiten indexiert wird (ich halte den Wert für zu vorsichtig und werde ihn wohl auf +/- 5 ändern).
Auch hier wird stark normalisiert und Text möglichst ignoriert damit z.B. 362 pages, 362 Seiten, 362 S., etc. als gleich behandelt werden können.
Ob weglassen oder nicht, kann ich nicht beurteilen (siehe auch Volume).

* part : Scheint eine Sammlung diverser Quell-Felder von MARC zu sein. Ich transformiere die Liste in einen einzigen String-Wert, mit dem ich in die Feature-Matrix gehe. Muss ich etwas beachten?
Ja, das Feld enthält Angaben zur Bandnummer aus diversen Feldern. 
Wir normalisieren das Feld auch relativ stark damit Vol. 5, Volume 5, Bd. 5, etc. als gleich behandelt werden können.

* person : Vgl. 1_DataAnalysis, ich identifiziere das Feld 245c als das am besten geeignete MARC 21 Feld. Kann ich die anderen Felder einfach weglassen?
Dem würde ich nicht unbedingt zustimmen. Wir nutzen 245 $c nur als Fallback, wenn 100/700 nicht vorhanden sind. In 245c wird die Verfasserangabe, wie sie auf der Publikation erscheint angegegeben. In 100/700 sind hingegegen normierte Namen erfasst.
Vielleicht sieht das mit deinen Methoden aber anders aus.

* pubinit : Wie beurteilst du meine Analyse in 1_DataAnalysis?
In CBS werden in pubinit die Initialen aller Worte, die nicht ein "Verlags-Wort" sind, indexiert. Mit Verlags-Wort meine ich zum Beispiel Verl., Verlag, Verlagsgesellschaft, Publ., Publisher, Ed., Editor, Edition, ...

* pubword : Ist identisch zu pubinit. Welche Transformation machst du in dieses Feld hinein? Kann ich das Feld weglassen?
In CBS wird hier nur bei Zeitschriften und Reihen die Verlagsangabe (ebenfalls ohne Verlags-Worte) indexiert.
Mit den publisher Angaben kann man aber sicher auch anders umgehen, als CBS das im Moment macht.

* scale : Scheint klar zu sein. Vielleich magst du in 1_DataAnalysis nachschauen und mir noch einen Hinweis geben.
Alles klar, wir passen hier auch kaum etwas an.

* ttlfull : Ich splitte ttlfull in seine zwei Teile und lasse dafür ttlpart weg. Was denkst du dazu? Wäre es besser, beide zu vereinen und ttlpart separat zu belassen?
Verstehe ich das richtig? Wenn du 245 und 246 wie geplant in zwei Attribute aufteilst, werden die Angaben nicht mehr miteinander verglichen?
Zum Hintergrund der beiden Felder: in 245 wird im Prinzip der Titel, wie er auf der Publikation erscheint erfasst. In 246 werden Titelvarianten erfasst (Titel auf dem Buchrücken, auf dem Umschlag, andere Schreibweise und diverses weitere was Katalogisierenden so einfällt). Jetzt kann es natürlich vorkommen, das der Titel in 245 mit dem in 246 übereinstimmt. Das kann entweder der richtige Hinweis für einen merge sein, ist aber gleichzeitig auch eine Gefahr für falsche merges.

* ttlpart : s. ttlfull.

* volumes : vgl. 1_DataAnalysis und Fragen zu pages oben.
Vgl. pages oben.
Hier wird versucht die Anzahl Bände aus der Angabe herauszulesen (Bsp. 1 online Ressource -> 1, 5 Vol. -> 5, 5 Bände -> 5).
