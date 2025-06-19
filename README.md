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
   source venv/bin/activate #linux/mac
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

Nous avons écrit 22 scénarios Gherkin couvrant :
- Progression scores (15-0, 30-15, ..)
- Situations deuce et advantage
- Victoires directe et depuis advantage
- Gestion d'erreurs

Chaque scénario valide un comportement métier specifique.

### Exemple de scénario
```gherkin
Scenario: Camillia gets advantage
  Given Camillia and Denisa both have scored 3 points
  When Camillia scores a point
  Then the score should be "Advantage Camillia"
```

## Résultats

- **34 tests** (12 unitaires + 22 BDD)
- **100% couverture** de code
- **Toutes les règles tennis** sont bien validées

## Technologies

- **Python 3.12**
- **pytest** pour les tests unitaires
- **pytest-bdd** pour les scénarios Gherkin (équivalent de cucumber)
- **pytest-cov** pour la couverture

## Équipe

**Denisa DUDAS** & **Camillia HAMMOU** - 4AL1

Projet réalisé dans le cadre du cours BDD / ESGI 2024-2025
