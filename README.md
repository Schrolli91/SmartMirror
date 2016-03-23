# SmartMirror
MirrorOS is a simple and easy to use Framework for SmartMirrors


## Allgemein
MirrorOS ist ein Python Script zum Betrieb eines Smart Mirrors.

Jedes Modul wird in einem eigenen Thread ausgeführt. Durch die dadurch erreichte Parallelisierung der Module ist ein reibungsloser Ablauf garantiert.


## Aktuelle Module
Follgende Module sind derzeit in MirrorOS implementiert oder geplant:

:white_check_mark: fertig implementiert | :x: bisher nicht implementiert | :question: evtl. geplant

|Modul|Beschreibung|Fertig|
|-----|------------|:----:|
|Uhrzeit|Zeigt die aktuelle Uhrzeit an|:white_check_mark:|
|Datum|Zeigt das aktuelle Datum an|:white_check_mark:|
|Wetter|Zeigt das Aktuelle Wetter + 2 Tages  Vorhersage an|:white_check_mark:|
|Kalender|Zeigt die nächsten Termine aus dem Google Calendar|:white_check_mark:|
|Focus News|Liest den RSS Feed der Focus Eilmeldungen aus|:white_check_mark:|
|Begrüßung|Uhrzeitabhängige Begrüßungen|:white_check_mark:|
|Spracherkennung|Steuerung des Mirrors durch Spracheingaben|:x:|
|Text to Speech|Sprachausgabe durch den Mirror|:x:|
|Wikipedia|Suche auf Wikipedia|:x:|
|Gesichtserkennung|Benutzer durch Webcam unterscheiden|:question:|
|Maps|Zeigt eine Karte oder Route an|:question:|
|Verkehr|Zeigt die aktuelle Verkehrslage auf einer Route an|:question:|


#### Debug und Entwickler Module
|Modul|Beschreibung|Fertig|
|-----|------------|:----:|
|Log View|liest die letzten 10 Meldungen aus dem Logfile aus|:white_check_mark:|
|Modul Status|Listet alle aktuel laufenen Module auf|:white_check_mark:|


## Installation



## Konfiguration
Alle wichtigen Einstellungen können in der config.ini vorgenommen werden.
