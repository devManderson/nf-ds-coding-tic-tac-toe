# Flussdiagramm: Tic-Tac-Toe

```mermaid
flowchart TD
    A([Start: python main.py]) --> C[Spieler 1 wählt X oder O]
    C --> D[Spieler 2 erhält das andere Symbol]
    D --> B[Leeres Spielfeld mit neun Feldern erstellen]
    B --> E[Spieler 1 beginnt]
    E --> F[Spielfeld anzeigen]
    F --> G[Aktuellen Spieler nach einer Position fragen]
    G --> H{Feld bereits belegt?}
    H -- Ja --> I[Erneut nach einer Position fragen]
    I --> G
    H -- Nein --> J[Symbol auf das Feld setzen]
    J --> K[Aktualisiertes Spielfeld anzeigen]
    K --> L{Hat der aktuelle Spieler gewonnen?}
    L -- Ja --> M[Gewinner anzeigen]
    M --> N([Spielende])
    L -- Nein --> O{Sind alle Felder belegt?}
    O -- Ja --> P[Unentschieden anzeigen]
    P --> N
    O -- Nein --> Q[Zum anderen Spieler wechseln]
    Q --> G
```

Die Prüfung auf ein bereits belegtes Feld ist eine optionale Erweiterung aus der Aufgabenstellung. Weitere Eingabefehler und zusätzliche Spielrunden sind hier nicht dargestellt.
