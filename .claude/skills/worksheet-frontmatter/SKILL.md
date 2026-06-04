---
name: worksheet-frontmatter
description: Interaktiver Guide für die Erfassung aller Metadaten (Fach, Reihe, Klasse, Titel, Quellen) vor der Materialgenerierung. Bereitet alle nötigen Informationen vor und übergeben dann automatisch an markdown-creator.
metadata:
  trigger: Nutzer möchte ein Arbeitsblatt/Aufgabenblatt/Schulaufgabe erstellen ("erstelle...", "mach...", "entwickle...") mit Angaben zu Klassenstufe, Schulfach und Thema
---

# Instruktionen

## Pflichtfelder in Metadaten
Jede Markdown-Datei MUSS am Anfang folgende YAML-Metadaten enthalten:
```yaml
---
title: [Titel des Arbeitsblatts]
gradeOfSchool: [Klassenstufe]
teacher: Herr Mustermann
unit: [Thema/Lerneinheit]
study: [Schulfach]
---
```

**VOR jeder Erstellung: Folgende Fragen NACHEINANDER stellen** (nicht alle auf einmal):

### Schritt 0: [Validierung der Pflichtfelder] [Usage: haiku]
Prüfe VOR dem Fragenablauf, dass folgende Informationen vorhanden oder ermittelbar sind:
- **title**: Titel/Thema des Arbeitsblatts (erforderlich)
- **gradeOfSchool**: Klassenstufe 1-6 (erforderlich)
- **teacher**: Wird aus der CLAUDE.md bezogen (optional, aber wenn vorhanden, sollte er in die Metadaten übernommen werden)
- **unit**: Thema/Lerneinheit/Reihe (erforderlich)
- **study**: Schulfach (erforderlich)

Falls eine dieser Informationen fehlt oder unklar ist, breche ab und fordere sie an, bevor du fortfährst.

### Schritt 1: [Frage nach dem Schulfach] [Usage: haiku]
- **Frage:** "Für welches Schulfach soll dieses Arbeitsblatt sein?"
- Auswählbare Optionen: Nutze den `projectRoot` aus CLAUDE.md und liste alle existierenden Ordner unter `{projectRoot}/Schulfächer/` auf
- Zeige sie als nummerierte Liste und erweitere es mit "Anderes Fach"
- Akzeptiere Nummer oder Freitext

### Schritt 2: [Reihe] [Usage: haiku]
- **Frage:** "Aus welcher Reihe soll das Arbeitsblatt sein?"
- Auswählbare Optionen: Nutze den `projectRoot` aus CLAUDE.md und liste alle existierenden Ordner unter `{projectRoot}/Schulfächer/[gewähltes Fach]/Reihe/` auf
- Zusätzlich erlauben: Neue Reihe eingeben
- Zeige sie als nummerierte Liste und erweitere es mit "Neue Reihe"
- Akzeptiere Nummer oder Freitext

### Schritt 3: [Klassenstufe] [Usage: haiku]
- **Frage:** "Für welche Klassenstufe ist das Arbeitsblatt?"
- Auswählbare Optionen: 1, 2, 3, 4, 5, 6 (alle sind Grundschule in Berlin)
- **Validierung:** Stelle sicher, dass eine gültige Klassenstufe (1-6) eingegeben wurde
- **Hinweis:** In Berlin sind die Klassen 1-6 Teil der Grundschule

### Schritt 4: [Thema/Titel] [Usage: haiku]
- **Frage:** "Wie soll das Thema/der Titel lauten?"
- Freie Texteingabe
- **Validierung:** Der Titel darf nicht leer sein und sollte aussagekräftig sein

### Schritt 5: [Frage nach Quellen] [Usage: haiku]
- **WICHTIG:** Nutze den `projectRoot` aus CLAUDE.md und liste die vorhandenen Quelldateien unter `{projectRoot}/Schulfächer/[ausgewähltes Fach]/Quellen/` auf
- **Frage:** "Möchtest du dich auf bestimmte Quellen beziehen?"
- Zeige die gefundenen Quellen als nummerierte Liste an und biete noch "Andere/freie Quellenangabe" als Option an

### Schritt 6: [Quelleneingrenzung] [Usage: sonnet] 
"Bitte gib für jede ausgewählte Quelle die Seitenzahlen im Format S. XX–YY an."

Beispiel:

Cornelsen Natur_und_Technik: S. XX–YY
Klett Naturwissenschaften: S. XX–YY

Verboten:

Kapitelangaben akzeptieren
Themenangaben akzeptieren
Schlüsselbegriffe akzeptieren
"alle relevanten Inhalte" akzeptieren
Alternativen anbieten
Zusatzfragen stellen
Auswahlmöglichkeiten auflisten

Wenn der Benutzer keine Seitenzahlen angibt:

Antworte ausschließlich mit:

"Ich brauche Seitenzahlen im Format S. XX–YY."

Wenn der Benutzer Kapitel, Themen, Begriffe oder "alle relevanten Inhalte" angibt:

Antworte ausschließlich mit:

"Ich brauche Seitenzahlen im Format S. XX–YY."

Erst fortfahren, wenn für jede ausgewählte Quelle Seitenzahlen vorliegen.


- Verwende dann zur Erstellung nur die vom Benutzer ausgewählten Quellen.
- Sollte eine Quelle keinen passenden Inhalt bereitstellen, informiere den Benutzer und frage, ob er eine andere Quelle auswählen möchte.

### Schritt 7: [Markdownerstellung]
Sobald alle Metadaten (Schulfach, Reihe, Klassenstufe, Titel, Quellen) vollständig gesammelt wurden:
- beginne direkt mit dem Schritt (Markdown-Erstellung) mit allen gesammelten Metadaten im Kontext
- Informiere den Benutzer: "Die Markdown-Datei wird jetzt mit den gesammelten Informationen erstellt."  
## Fehlerbehandlung und Edge Cases [Usage: haiku]

### Falls Pflichtfelder fehlen 
- Breche ab und liste auf, welche Felder fehlen
- Frage präzise nach jedem fehlenden Feld
- Fortsetzen erst nach vollständiger Erfassung aller Pflichtfelder

### Falls Klassenstufe ungültig ist
- Akzeptiere nur: 1, 2, 3, 4, 5, 6
- Bei ungültiger Eingabe: "Bitte wähle eine Klassenstufe zwischen 1 und 6"
- Wiederhole die Frage bis gültige Eingabe erfolgt

### Falls Titel/Unit leer ist
- Akzeptiere nicht: Leere Strings, nur Whitespace, oder unbedeutende Eingaben
- Fordere aussagekräftigen Text ein

### Falls keine passenden Quellen gefunden werden
- Füge diese nicht in die Markdown-Datei ein

### Falls Quellen vorhanden sind, aber keine relevanten Informationen enthalten
- Informiere den Benutzer und frage, ob er eine andere Quelle auswählen möchte.

### Falls die Quelle nicht verarbeitet werden kann
- Informiere den Benutzer über das Problem und warte weitere Anweisungen ab, bevor du fortfährst.
