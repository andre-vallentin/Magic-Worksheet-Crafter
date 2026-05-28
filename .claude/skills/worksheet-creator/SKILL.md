---
name: worksheet-creator
description: Generiert Schularbeitsmaterialien aus ausgewählten Quellen mit Aufgaben, Lösungen und erstellt eine strukturierte Markdown-Datei.
---

# Instruktionen

## Model [Usage]
Benutze **haiku** zur Erstellung der Markdown-Datei.

## Reihe
Sollte ein Ordner einer Reihe noch nicht existieren erstelle einen neuen Ordner mit dem Namen der Reihe unter `Schulfächer/[gewähltes Fach]/Reihe/` und trenne den Namen mit Leerzeichen.

## [Schritt –1: Prompt-Angaben erfassen] [PFLICHT]

**Bevor** du Referenzen liest oder Inhalte generierst: Scanne den Eingabe-Prompt nach
Gestaltungsangaben und übernimm sie **ohne Rückfrage** direkt als Vorgaben.

Erkenne und wende folgende Angaben automatisch an:
- **Aufgabenanzahl / Aufgabentypen** (z. B. „3 Textaufgaben, 1 Tabelle", „nur SingleChoice")
- **Schwierigkeitsgrad / Klassenstufe** (z. B. „für Klasse 3", „einfacher Wortschatz")
- **Antwortzeilen-Anzahl** (z. B. „je 2 Antwortzeilen")
- **Besondere Inhalts- oder Strukturwünsche** (z. B. „kein Informationstext", „mit Bild-Platzhalter")
- **Sonstige explizite Formatierungsvorgaben** (z. B. „kurze Aufgabenstellungen")

**Regel:** Jede Angabe aus dem Prompt gilt als bestätigt. Frage **nicht** nach, ob sie
angewendet werden soll. Fehlende Angaben werden wie bisher nach den Referenzdateien und
dem Standardformat ergänzt.

## [Schritt 0: References lesen] [PFLICHT]

**VOR der Markdown-Erstellung:** Lies ZUERST alle Dateien im Ordner `references/`:
- `references/info-text-example.md`
- `references/text-task-example.md`
- `references/single-choice-example.md`
- `references/table-task-example.md`
- `references/sources-example.md`

Kopiere die exakte Struktur, Formatierung und HTML-Kommentare aus diesen Dateien.

## [Markdown-Erstellung]

Beziehe dich nur auf die ausgewählten Quellen und generiere eine strukturierte Markdown-Datei mit folgenden Anforderungen, beziehe keine anderen Dateien oder Informationen mit ein.

## [Mehrere Quellen] [PFLICHT]

Falls mehrere Quellen ausgewählt sind:
- **Informationstext**: Kombiniere Inhalte aller Quellen zu einem kohärenten Text. Keine separaten Absätze pro Quelle.
- **Aufgaben**: Verwende Inhalte aus allen Quellen gemischt. Nicht jede Aufgabe an eine einzelne Quelle binden.
- **Quellen-Dokumentation**: Dokumentiere alle verwendeten Quellen mit ihren Seiten und Aufgabenbezügen (z.B. `[Quelle] S. # → Aufgabe(n): #`).

## Reihenfolge [PFLICHT]

1. Referenz-Dateien lesen (siehe Schritt 0 oben)
2. YAML-Frontmatter schreiben
3. Informationstext schreiben (nach InfoText-Referenz)
4. Aufgaben schreiben (nach Task-Referenzen) mit HTML-Ankern
5. Lösungen schreiben
6. Quellen schreiben (nach Sources-Referenz)

Erstelle die Markdown-Datei mit folgenden Abschnitten:

### HTML-Kommentare [PFLICHT]

Jeder Abschnitt MUSS mit dem HTML-Kommentar aus den References beginnen:
- `<!-- InfoText -->` vor dem Informationstext
- `<!-- TextTask -->` vor jeder Textaufgabe
- `<!-- SingleChoice -->` vor Wahr/Falsch-Aufgaben
- `<!-- TableTask -->` vor Tabellenaufgaben
- `<!-- Sources -->` vor dem Quellen-Abschnitt

### Abschnitte

- YAML-Frontmatter mit den Metadaten aus dem `worksheet-frontmatter`-Skill 
- Einleitungstext mit den wichtigsten Informationen zum Thema (Informationstext) — **KOPIERE die exakte Formatierung aus `references/info-text-example.md`** (Fettdruck für Fachbegriffe, Kursiv für Synonyme)
- Aufgaben wie im Ordner `references` zu finden (Textaufgaben, SingleChoice, Tabellenaufgaben) mit klaren Operatoren (Nenne, Erkläre, Beschreibe, Ordne zu) und kurzen Antwortsätzen (1-3 Wörter oder kurze Sätze)
- **Aufgaben MÜSSEN aus dem Informationstext herleitbar sein.** Kein Wissen abfragen, das nicht im Informationstext steht. Schüler müssen Aufgaben nur mit Informationstext und Quellen lösen können.

- erstelle dann einen separaten Abschnitt `## Lösungen` am Ende der Datei, in dem du die Lösungen zu den Aufgaben dokumentierst, siehe wieder die Beispiele im Ordner `references`. Vermeide es, Lösungen oder Hinweise in den Aufgabenabschnitten zu platzieren.

### Sections `<!-- Section -->` [PFLICHT]

Setze `<!-- Section -->` **NUR** an genau drei Stellen in der gesamten Datei:
1. Direkt nach dem Frontmatter
2. Direkt vor `## Lösungen`
3. Direkt vor `<!-- Sources --> ## Quellen`

**NIEMALS** `<!-- Section -->` setzen:
- zwischen Aufgaben
- nach dem Informationstext
- zwischen Lösungsabschnitten

❌ Falsch:
```
## Aufgabe 1: ...
...
<!-- Section -->

## Aufgabe 2: ...
```

✅ Richtig:
```
## Aufgabe 1: ...
...
<!-- SingleChoice -->
## Aufgabe 2: ...
...
<!-- Section -->
## Lösungen
...
<!-- Section -->
## Quellen
```

- Erstelle Quellen nach dem Format in `references/sources-example.md` — **KOPIERE die exakte Formatierung** (z.B. `[PDF-Name] S. # → Aufgabe(n): #`). Dokumentiere alle Quellen, die du für die Erstellung der Aufgaben und Informationen verwendet hast.

### Format-Konformität [PFLICHT]

**KOPIERE das exakte Format aus den Referenz-Dateien. Keine eigenen Strukturvarianten erfinden.**

Beispiele:
- Antwortzeilen: `_Antwortzeilen:_ 4` (nicht `_Antwortzeilen: 4_`)
- Sources-Format: `[Quelle] Beschreibung → Aufgabe(n): #`
- InfoText: Fettdruck für Fachbegriffe, Absätze wie in Referenz

## [Ausgabe und nächste Schritte]

- Informiere den Benutzer dass die Markdown mit vollständigen Metadaten erstellt wurde
- Zeige die Metadaten-Zusammenfassung (title, class, unit)
- öffne die Markdown-Datei in einem neuen Tab
- Frage ihn ob er möchte das eine Docx erstellt wird mit "Möchtest du jetzt ein Arbeitsblatt im DOCX-Format erstellen?" (Ja/Nein)
- Wenn Ja: führe den Befehl: `python3 magic-worksheet-crafter/main.py [Pfad zur Markdown-Datei] [Pfad zur Ausgabe-DOCX-Datei]` aus und informiere ihn, dass die DOCX-Datei erstellt wird und wo er sie findet



