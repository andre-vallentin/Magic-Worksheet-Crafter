Erstelle TableTask bzw. 'Quiz'-Aufgaben immer nach dieser Vorlage:

- einem Kommentar `<!-- TableTask -->`
- einen Header2 `## Aufgabentitel`
- eine Aufgabenbeschreibung
- eine Tabelle mit Überschriften
- im Lösungsabschnitt trage in die jeweilige Spalte ein "x" ein.

# Beispiel

## Aufgabenstellung

```
<!-- TableTask -->
## Aufgabe 1: Quiz – Nährstoffe in Lebensmitteln

Ordne die folgenden Lebensmittel den Nährstoffgruppen zu. Ein Lebensmittel kann mehreren Gruppen angehören.

| Lebensmittel | Viel Zucker | Viel Protein | Viel Ballaststoffe | Viel Vitamine |
|-|-|-|-|-
| Apfel | | | | |
| Vollkornbrot | | | | |
| Käse | | | | |
| Olivenöl | | | | |
```

## Lösung
```
<!-- TableTask -->
### Aufgabe 1: Quiz – Nährstoffe in Lebensmitteln

Ordne die folgenden Lebensmittel den Nährstoffgruppen zu. Ein Lebensmittel kann mehreren Gruppen angehören.

| Lebensmittel | Viel Zucker | Viel Protein | Viel Ballaststoffe | Viel Vitamine |
|---|---|---|---|---|
| Apfel | x | | x | x |
| Vollkornbrot | | x | x | |
| Käse | | x | | |
| Olivenöl | | | | |
```