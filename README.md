# Tennis Kata - BDD Project

Ce projet implémente un kata de scoring de tennis avec une approche BDD (Behavior Driven Development) utilisant `pytest` et `pytest-bdd`

---

## Installation et configuration

### Prérequis

- Python 3.8 ou supérieur

### Étapes

1. **Créer un environnement virtuel**

```bash
python3 -m venv venv
```

2. **Activer l’environnement virtuel**

- Linux/macOS :

```bash
source venv/bin/activate
```

- Windows (PowerShell) :

```powershell
.env\Scriptsactivate
```

3. **Installer les dépendances**

```bash
pip install -e .
```

Cette commande installe le projet en mode editable ainsi que les dépendances listées dans `setup.py` (`pytest`, `pytest-bdd`, `pytest-cov`).

4. **Vérifier les paquets installés**

```bash
pip show pytest pytest-bdd pytest-cov
```

---

## Utilisation

### Lancer les tests

```bash
pytest --cov=src tests/
```

- Lance tous les tests unitaires et BDD.
- Affiche un rapport de couverture de code.

---

## Structure des tests

- Tests BDD dans `tests/bdd/` avec les fichiers `.feature` et les définitions de steps.
- Tests unitaires dans `tests/unit/` pour tester les modules individuellement.

---

## Remarques

- Utilisation d’un environnement virtuel pour isoler les dépendances du projet.
- Le mode editable (`pip install -e .`) va nous permettre de tester facilement les modifications du code source sans réinstaller tout à chaque fois.
- Le projet suit une architecture claire avec `src/` pour le code et `tests/` pour les tests.
---

## Auteur

Denisa DUDAS 4AL1 et 
Camillia HAMMOU 4AL1