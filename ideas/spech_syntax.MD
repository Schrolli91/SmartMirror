Beschreibung für eine mögliche Syntax zur besseren Phrasen-Erkennung der speech.py

- Normaler Text wird 1:1 verarbeitet
`zeige Uhrzeit`

- Text in (...)-Klammern darf vorkommen, muss aber nicht
`zeige (mir) (die) Uhrzeit (an)`
Erkannt wird `zeige Uhrzeit`, `zeige mir Uhrzeit`, `zeige die Uhrzeit`, `zeige mir die Uhrzeit an`, usw...

- Text in (...)-Klammern kann mehrere Möglichkeiten enthalten, welche durch | getrennt werden
`(wer|was) ist teuer`
Erkannt wird `wer ist teuer` oder `was ist teuer`

- ein * markiert einen variablen Berech `suche nach \*`
Erkannt wird `suche nach Einstein` oder `suche nach Bildern` usw...
