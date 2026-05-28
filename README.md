# <a name="about"></a>Magic Worksheet Crafter

This program is an assistant that transforms Markdown into a DOCX file to create worksheets for school.

# Content

- [About](#about)
- [Pre-Requisites](#pre-requisites)
- [How to use](#how-to-use)
- [Build the app for macOS](#build-the-app)

# <a name="about"></a>About

The main intended usage of this application is to use it as a worksheet creator for schools with given pre-defined styles of exercises. 

The provided excersices are:
- information texts
- single choice (true or false)
- table tasks
- text excersise

It also includes a pre-defined header and footer with a fixed style.

# <a name="prerequisites"></a>Prerequisites

To use this tool successfully you will need a markdown file with a predefined structure.

## Frontmatter

The markdown needs to start with a frontmatter in the format like this:
```
---
title: Nährstoffe und ausgewogene Ernährung
gradeOfSchool: 6
teacher: Herr Mustermann
unit: Körper und Gesundheit
study: Naturwissenschaften
---
```

## Exercise structure

Each exercise needs to be marked with a specific comment, a title and with the given content. Here one example.

```
<!--- InfoText -->
## Your title

Die **Ernährung** versorgt deinen Körper mit Energie und Nährstoffen, die er braucht. Die **sieben Säulen der Ernährung** sind Kohlenhydrate, Fette, Eiweiße, Mineralstoffe, Vitamine, Ballaststoffe und Wasser. Jede Gruppe hat wichtige Aufgaben für deinen Körper.
```

The full list of available excersise-tasks are:
```
<!--- InfoText -->
<!--- TableTask -->
<!--- SingleChoice -->
<!--- TextTask -->
```

Please see the [Example.md](Example.md) for further reference.

## Source structure

At the end of each Markdown could be your list of sources. To mark it properly use this structure:

```
<!--- Sources -->
## Quellen

[Nährstoffe.pdf] S. 336–337 → Aufgaben: 1, 2, 3

[Energie-für-dich.png] → Aufgaben: 1, 2
```

# <a name="how-to-use"></a> How to use

## App
You can install the tool locally at the `magic_worksheet_crafter/ ` folder with:
```
pip install -e .
```

### Terminal

Now you can start the tool with:
```
magic_worksheet_crafter source_markdown_path output_docx_path
```
### GUI 
Go to the parent folder and execute: `python3 build_app/app_entry.py` to start the GUI straight from the script.

# <a name="build-app"></a> Build the app for macOS

To build the application as a standalone program, execute the following commands from the 
`magic_worksheet_crafter` folder:

1. Install py2app (one-time setup):
```
python3.13 -m pip install py2app
```

2. Build the macOS app bundle:
```
python3.13 build_app/setup.py py2app
```
A temporary `build`-folder is been deleted after the creation of the application in the `dist`-folder.

# <a name="assets"></a> Project-Assets

The application logo has been designed from [Gondola](https://www.canva.com/p/gondola-1990/?utm_medium=referral&utm_source=creator_share&utm_campaign=creator_share)
and has been paid for 1€ at the 25.05.2026 by myself.

The Icons are made by ThoseIcons from www.flaticon.com
https://www.flaticon.com/authors/those-icons
