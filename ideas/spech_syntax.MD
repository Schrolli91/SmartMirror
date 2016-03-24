### Spech Recogn. Syntax

Beschreibung für eine mögliche Syntax zur besseren Phrasen-Erkennung der speech.py



#### Normaler Text
Normaler Text wird 1:1 verarbeitet, all diese Wörter müssen in genau dieser Reihenfolge vorkommen

`zeige Uhrzeit`



#### KANN Feld
Text in (...)-Klammern darf vorkommen, muss aber nicht

`zeige (mir) (die) Uhrzeit (an)`

###### Erkannt wird:
- `zeige Uhrzeit`
- `zeige mir Uhrzeit`
- `zeige die Uhrzeit`
- `zeige mir die Uhrzeit an`
- usw ...



#### Mehrfaches KANN Feld
Text in (...)-Klammern kann mehrere Möglichkeiten enthalten, welche durch | getrennt werden

`(wer|was) ist teuer`

###### Erkannt wird:
- `wer ist teuer`
- `was ist teuer`
- `ist teuer`



#### Mehrfaches MUSS Feld
Text in (...)-Klammern kann mehrere Möglichkeiten enthalten, welche durch | getrennt werden
Die Klammer wird mit einem + abgeschlossen, was bedeutet, das eines der enthaltenen Wörter vorkommen MUSS

`(wer|was)+ ist teuer`

###### Erkannt wird:
- `wer ist teuer`
- `was ist teuer`



#### Variable Felder

ein * markiert einen variablen Bereich, welcher mehrere Wörter kang sein kann und einen Namen haben muss

`suche nach *variabel`

###### Erkannt wird:
- `suche nach Einstein`
- `suche nach Albert Einsetin`

um auf den variablen Bereich zuzugreifen nutzt man die .group() Methode mit dem angegebenen namen
`.group("variabl")`
