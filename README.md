# Calculatrice Flask — LOG3000 TP3

**Équipe :** 14 — Chahinez Benhamla ([@chahinezb23](https://github.com/chahinezb23)),
Saymon-Alexandr Sakr ([@Zixer1](https://github.com/Zixer1)), Wei Duo Xu ([@lOwOlP](https://github.com/lOwOlP))

## Objectif

Application web de calculatrice simple construite avec Flask (Python). L'utilisateur
compose une expression à l'aide des boutons de l'interface (ex. `12+7`) et le serveur
calcule le résultat. Ce dépôt sert à mettre en place de bonnes pratiques de gestion de
versions : documentation, tests, suivi des bogues par issues et correctifs par branches.

## Prérequis

- Git
- Python 3.10 ou plus récent
- pip

## Installation

```bash
git clone https://github.com/lOwOlP/TP3-LOG3000-Equipe14.git
cd TP3-LOG3000-Equipe14
python -m venv .venv
# Windows : .venv\Scripts\activate    |    macOS/Linux : source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

L'application est ensuite accessible à l'adresse <http://127.0.0.1:5000>.
