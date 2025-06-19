# Tennis Kata - Approche BDD

Implémentation du kata Tennis en utilisant Behavior Driven Development avec Python.

## Pourquoi ce kata ?

Le Tennis présente des règles métier intéressantes pour démontrer l'approche BDD : scoring particulier, cas deuce/advantage, gestion des victoires. Chaque règle devient un scénario testable :)

## Règles implémentées

### Scoring tennis
- **0 point** → "0" (love)
- **1 point** → "15" 
- **2 points** → "30"
- **3 points** → "40"

### Cas spéciaux
- **Deuce** : 40-40, il faut 2 points d'écart pour gagner
- **Advantage** : un joueur mène d'1 point après deuce
- **Retour deuce** : égalisation depuis advantage

### Victoire
Premier à 4 points avec minimum 2 d'écart.

## Architecture

```
BDD-TennisProject/
├── src/tennis/        #Code métier
│   ├── game.py        #Logique du jeu
│   └── score.py       #Gestion affichage scores
├── tests/unit/        #Tests unitaire
└── tests/bdd/         #Tests comportementaux
    ├── features/      #Specifications Gherkin
    └── steps/         #Definitions steps
```

## Installation

1. **Environnement virtuel**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  #Linux/mac
   ```

2. **Installation projet**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## Tests

### Tous les tests
```bash
pytest tests/unit/ tests/bdd/steps/tennis_steps.py --cov=src/tennis -v
```

### Tests unitaires seulement
```bash
pytest tests/unit/ -v
```

### Scénarios BDD seulement  
```bash
pytest tests/bdd/steps/tennis_steps.py -v
```

## Approche BDD

Nous avons écrit 24 scénarios Gherkin couvrant :
- Progression scores (15-0, 30-15, etc.)
- Situations deuce et advantage
- Victoires directes et depuis advantage
- Gestion d'erreurs

Chaque scénario valide un comportement métier spécifique.

### Exemple de scénario
```gherkin
Scenario: Player 1 gets advantage
  Given both players have scored 3 points
  When Player 1 scores a point
  Then the score should be "Advantage Player 1"
```

## Résultats

- **36 tests** (12 unitaires + 24 BDD)
- **100% couverture** de code
- **Toutes les règles tennis** sont bien validées

## Technologies

- **Python 3.12**
- **pytest** pour les tests unitaires
- **pytest-bdd** pour les scénarios Gherkin (équivalent de cucumber)
- **pytest-cov** pour la couverture

## Équipe

**Denisa DUDAS** & **Camillia HAMMOU** - 4AL1

Projet réalisé dans le cadre du cours BDD - ESGI 2024-2025