# Flussdiagramm: aktueller Spielablauf

```mermaid
%%{init: {"flowchart": {"curve": "step"}}}%%
flowchart TD
    Start(["Start: python tic_tac_toe.py"]) --> Menu["Terminal leeren, Logo und Spielmodi anzeigen"]
    Menu --> Mode{"Spielmodus wählen"}
    Mode -- "2: gegen Computer" --> Placeholder["Hinweis: Modus noch nicht fertig"]
    Placeholder --> Enter["Auf Eingabe warten"]
    Enter --> Menu

    Mode -- "1: gegen Spieler 2" --> Init["Spielfeld als Dictionary erstellen: Felder 1 bis 9 haben Wert 0"]
    Init --> Symbol["Spieler 1 nach X oder O fragen"]
    Symbol --> ValidSymbol{"X oder O gewählt?"}
    ValidSymbol -- Nein --> Symbol
    ValidSymbol -- Ja --> Setup["Spieler 2 erhält das andere Symbol; Spieler 1 beginnt"]
    Setup --> Board["Spielfeld mit freien Feldnummern und farbigen Symbolen anzeigen"]

    Board --> Field["Aktuellen Spieler nach einem Feld fragen"]
    Field --> ValidField{"Zahl von 1 bis 9?"}
    ValidField -- Nein --> Field
    ValidField -- Ja --> FreeField{"Feld noch frei?"}
    FreeField -- Nein --> Field
    FreeField -- Ja --> SetField["Spielernummer 1 oder 2 im Dictionary speichern"]

    SetField --> Won{"Hat der aktuelle Spieler gewonnen?"}
    Won -- Ja --> WinScreen["Terminal leeren und Gewinnergrafik für Spieler 1 oder 2 anzeigen"]
    WinScreen --> End([Spielende])
    Won -- Nein --> Full{"Alle Felder belegt?"}
    Full -- Ja --> Draw["Aktuelles Spielfeld und Unentschieden anzeigen"]
    Draw --> End
    Full -- Nein --> Next["Zum anderen Spieler wechseln"]
    Next --> Board
```

Hinweis zum aktuellen Code: Bei einer ungültigen **Spielmoduswahl** wird das Menü zwar erneut aufgerufen, das Ergebnis dieses Aufrufs aber nicht zurückgegeben. Dadurch kann anschließend ein Fehler entstehen. Die Eingabeprüfung für die **Spielfelder** wiederholt die Frage dagegen korrekt.
