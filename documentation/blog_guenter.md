Im swissbib Projekt ist die Essenz all unserer Aktivitäten der Umgang mit und die Aufbereitung von (Meta-) Daten. Normalisieren, Anreichern, Clustern (Zusammenführen) sowie Verknüpfen von Informationen und dies alles auf maschineller Basis ist die Grundlage dafür, dass wir Services wie verschiedene Discoveries, unterschiedliche Schnittstellen oder Dienstleistungen für Dritte anbieten können.


Vor allem für das maschinelle Clustern (Deduplizieren) von Daten nutzen wir die (kommerzielle) Software eines Partners, die es uns flexibel ermöglicht, Daten so aufzubereiten, dass man sie für die unterschiedlichen Services einsetzen kann. Dies war kein statischer Vorgang in dem Sinne, dass die Software einmal geschrieben war und dann ihren Dienst erfüllen konnte sondern ein iterativer Prozess über Jahre, in denen sowohl wir vom swissbib Team als auch unser Partner gegenseitig Wissen in den Prozess zur Verbesserung der Datenaufbereitung einbrachten.


Seit gefühlt zwei, drei Jahren lassen sich kaum mehr Artikel zum Thema Daten und Informationen finden, in denen nicht mindestens einmal Begriffe wie "Maschinelles Lernen", "Artificial Intelligence" (AI) oder "Neuronale Netze" erwähnt und als das Erfolgsrezept für die Zukunft beschrieben werden. Sollte damit das, was wir in den letzten 12 Jahren gemacht haben zum alten Eisen zählen und nicht mehr relevant sein? Da wir ja nun nicht dafür bekannt sind, eine Scheu vor neuen Softwaretechnologien zu haben, schauen wir schon immer regelmässig "über den Gartenzaun" um mitzubekommen, ob sich die neuen Methoden nicht mit unseren "klassischen" Methoden verbinden liessen. Das Problem dabei: Bevor man aus der Menge des Möglichen etwas vielleicht gut Versprechendes wählen, ausprobieren und dann vielleicht produktiv einsetzen  kann, muss man sich erstmal durch die Grundlagen und Begrifflichkeiten des neuen Themengebiets kämpfen. Nicht so einfach für ein swissbib Team, dass mit Personen nicht üppig ausgestattet ist und den Laden (sprich die "grünen, orangenen oder wie auch immer farblichen Services") am Laufen halten muss.



In solchen Situationen der eigenen Begrenztheit kann Offenheit und die Möglichkeit der unkomplizierten Zusammenarbeit helfen. Andreas Jud (link Twitter, linkedin?), einem Freund eines swissbib Teammitglieds, der sich bei einer Weiterbildung an der EPFL Lausanne (link?) mit Methoden des maschinellen Lernens beschäftigt hatte, konnten wir dafür begeistern, im Rahmen seiner Abschlussarbeit die Daten von swissbib zu verwenden.


Das Thema des Abschlussprojekts:


"Deduplizierung von bibliographischen Metadaten mit Methoden des maschinellen Lernens"


Ziel war es, die Ergebnisse unterschiedlicher Methoden einander gegenüberzustellen und miteinander zu vergleichen.


Im Rahmen dieser kleinen Blogserie möchten wir ihnen die Ergebnisse der Arbeit soweit wie möglich aufbereiten und vermitteln. Am meisten würde es uns freuen, wenn wir Ihre Neugier und Interesse für das Themengebiet wecken könnten. Verfahren des Clusterns, das heisst das Zusammenführen von ähnlichen/identischen Informationen, lassen sich nicht nur auf Titeldaten bibliographischer Beschreibungen (so wie wir das in swissbib in den letzten Jahren gemacht haben) einsetzen. Das Einsatzgebiet liesse sich leicht auf z.B. Personen und Organisationen ausweiten. Wir überlassen es Ihnen, sich weitere Einsatzformen zu überlegen. Im Rahmen des swissbib Projekts (oder dessen Nachfolgeaktivitäten) sehen wir weitere Einsatzfelder aktuell z.B. in folgenden Bereichen:

     Verlinkung von Personen und Organisationen im Rahmen unseres ID Hubs nicht nur über Identifier aus Normdaten sondern auch weniger eindeutigen Datenfeatures.
    Identifizierung vor allem von Personen innerhalb unseres aktuellen memobase Projekts.  



Der Aufbau unserer Blogserie orientiert sich am Buch

Christen, P. (2012). Data matching. Springer.


 Christen unterteilt den Data Matchingprozes in mehrere Schritte:


    Data Pre-Processing
    Indexing
    Record Pair Comparison
    Record Pair Classification
    Evaluation of Matching Quality and Complexity


In seinen Blogbeiträgen wird sich Andreas auf die Schritte 3 bis 5 konzentrieren und versuchen uns zu vermitteln, welchen Zielerreichungsgrad Methoden des maschinellen Lernens haben können. Die Neugierigen unter Ihnen können natürlich auch versuchen, die Details der Ergebnisse in den Jupyter Notebooks 0 - 8 auf der Projektseite nachzuvollziehen.

 

Das Verständnis und der Einsatz von Algorithmen ist wichtig, nicht minder wichtig ist aber auch der Schritt 1: das "Data Pre-Processing". Entsprechend aufbereitete (normalisierte) Daten sind absolut notwendig, um qualitative Features für die Modellerstellung als Input für die Methoden des maschinellen Lernens zu generieren. Hier kommt die Expertise der Metdatenspezialistin des swissbib Teams, Silvia Witzig, sowie die langjährige praktische Erfahrung im Rahmen des swissbib Projekts, auch für Drittprojekte wie SLSP, zur Geltung. Am Ende der Blogserie werden wir versuchen, die Kombination dieser praktischen Erfahrungen mit den Anforderungen neuer Verfahren des maschinellen Lernens zu verknüpfen und entsprechend aufzubereiten und zu dokumentieren.

 

Was versteckt sich nun hinter dem Begriff des Indexing im Schritt 2 ?
Etwas was wir auf Basis unserer kommerziellen Software bei swissbib ebenfalls schon lange einsetzen: Das sogenannte "Pre-clustern" von Daten, dass heisst die Bildung von vielen Datensets, die aufgrund der Kriterien, nach denen Informationen miteinander in Verbindung gestellt werden sollen, im Vorfeld des eigentlichen Clustern von Informationen gebildet werden. Dadurch verringert sich die Komplexität vor allem der Schritte 3 und 4 erheblich. Im Rahmen des produktiven swissbib Betrieb setzen wir für dieses Pre-clustern von Daten auf Indexbildung mit Informationen, die wir aus der relationalen Datenbank unserer Software erhalten. Alternativen zu dieser eher klassischen Technik sind heute Methoden der Skalierung unter Einsatz von Big Data Frameworks wie Apache Flink teilweise im Zusammenspiel mit Apache Beam oder Apache Spark. Im swissbib Projekt beschäftigen wir uns seit zwei Jahren vor allem mit den beiden Erstgenannten. In anderen Kontexten haben wir die Integration derartiger Komponenten in eine Datenplattform bereits vorgestellt.   


 
Es lässt sich zusammenfassen:
Der Umgang mit Daten ist heute nicht mehr eine "One-Person" oder "One Company" Veranstaltung hinter einem verschlossenen Vorhang. Es ist ein Zusammenspiel unterschiedlicher Rollen wie Informationsspezialistinnen, Softwareentwicklerinnen und Personen auch ausserhalb des Bibliothekskuchens wie einem promovierten Physiker. Wichtig ist die Offenheit und freie Verfügbarkeit von Software und der ungehinderte Austausch von Informationen. Auch die Hoffnung, dass die Bibliotheken erkennen, dass sie einen Datenschatz besitzen, mit dem sich etwas anfangen lässt. So wie es die Prüfer der EPFL bei der Verteidigung des Abschlussprojekts gegenüber Andreas ausdrückten: Dass er mit einem "tollen Datensatz" arbeiten konnte.   
 

