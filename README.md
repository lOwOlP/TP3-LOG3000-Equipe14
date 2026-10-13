# Calculatrice Flask — LOG3000 TP3

**Équipe 14** — Polytechnique Montréal, LOG3000

| Membre | GitHub |
|---|---|
| Chahinez Benhamla | [@chahinezb23](https://github.com/chahinezb23) |
| Saymon-Alexandr Sakr | [@Zixer1](https://github.com/Zixer1) |
| Wei Duo Xu | [@lOwOlP](https://github.com/lOwOlP) |

## 1. But et portée du projet

Application web de calculatrice construite avec **Flask** (Python). L'utilisateur compose
une expression avec les boutons de l'interface, puis appuie sur **=** : le navigateur envoie
l'expression au serveur, qui la calcule et réaffiche la page avec le résultat.

**Dans la portée :**
- Une seule opération binaire par calcul : `<nombre> <opérateur> <nombre>` (ex. `12+7`).
- Les quatre opérations : addition `+`, soustraction `-`, multiplication `*`, division `/`.
- Messages d'erreur affichés dans l'écran (`Error: ...`) pour les expressions invalides.

**Hors de la portée :**
- Expressions à plusieurs opérateurs ou avec parenthèses (`1+2*3`).
- Priorité des opérations, fonctions scientifiques, historique des calculs.

Le dépôt sert aussi à appliquer un flux de travail professionnel : documentation, tests
automatisés, suivi des bogues par issues GitHub et correctifs par branches et pull requests.

## 2. Structure du dépôt

```
.
├── app.py              # Serveur Flask : route "/" et fonction calculate()
├── operators.py        # Fonctions arithmétiques add, subtract, multiply, divide
├── requirements.txt    # Dépendances Python (Flask, pytest)
├── pytest.ini          # Configuration de pytest (dossier tests/, chemin d'import)
├── templates/          # Interface HTML (voir templates/README.md)
│   └── index.html
├── static/             # Feuille de style (voir static/README.md)
│   └── style.css
└── tests/              # Tests automatisés pytest (voir tests/README.md)
```

### Module backend (racine)

| Fichier | Responsabilité |
|---|---|
| `app.py` | Crée l'application Flask, associe chaque symbole à sa fonction (`OPS`), analyse l'expression (`calculate`) et gère la route `/` (`GET` : affichage, `POST` : calcul). |
| `operators.py` | Implémente les quatre opérations sur deux nombres. Aucune dépendance. |

**Hypothèses :** l'expression reçue ne contient qu'un seul opérateur et deux opérandes
convertibles en `float` ; elle n'est jamais passée à `eval()`. Le résultat est toujours un
`float` (ex. `3+4` affiche `7.0`).

## 3. Installation (étape par étape)

Prérequis : **Git**, **Python 3.10+** et **pip**.

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/lOwOlP/TP3-LOG3000-Equipe14.git
   cd TP3-LOG3000-Equipe14
   ```
2. Créer un environnement virtuel :
   ```bash
   python -m venv .venv
   ```
3. L'activer :
   - Windows (PowerShell) : `.venv\Scripts\Activate.ps1`
   - Windows (cmd) : `.venv\Scripts\activate.bat`
   - macOS / Linux : `source .venv/bin/activate`
4. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## 4. Utilisation

1. Lancer le serveur (environnement virtuel activé) :
   ```bash
   python app.py
   ```
2. Ouvrir <http://127.0.0.1:5000> dans un navigateur.
3. Composer un calcul avec les boutons, par exemple `1` `2` `+` `7`.
4. Appuyer sur **=** : le résultat (`19.0`) s'affiche dans l'écran.
5. Appuyer sur **C** pour effacer l'écran.

| Entrée | Résultat attendu |
|---|---|
| `8+2` | `10.0` |
| `8-2` | `6.0` |
| `8*2` | `16.0` |
| `8/2` | `4.0` |
| `8/0` | `Error: ...` (division par zéro) |
| `+8` | `Error: invalid expression format` |

Pour arrêter le serveur : `Ctrl+C` dans le terminal.

## 5. Tests

Les tests utilisent **pytest** et se trouvent dans `tests/`. Depuis la racine du dépôt,
environnement virtuel activé :

```bash
pytest -v                                   # toute la suite
pytest tests/test_operators.py -v           # un seul fichier
pytest tests/test_operators.py::test_subtract_positive   # un seul test
```

Le détail de ce qui est couvert est dans [`tests/README.md`](tests/README.md).

## 6. Flux de contribution

1. **Issue d'abord.** Tout bogue ou fonctionnalité commence par une issue GitHub décrivant
   le problème, les étapes de reproduction (ou le test qui échoue) et le résultat attendu.
   L'issue est assignée à un membre de l'équipe.
2. **Une branche par issue**, créée à partir de `main` à jour :
   ```bash
   git switch main && git pull
   git switch -c fix/issue-<numéro>-<description-courte>
   ```
   Préfixes : `fix/` (bogue), `feat/` (fonctionnalité), `docs/` (documentation), `test/` (tests).
3. **Commits au format [Conventional Commits](https://www.conventionalcommits.org/fr/)** :
   `type(portée optionnelle): description`, puis un corps expliquant *comment* le
   changement corrige le problème. Types utilisés : `fix` (bogue), `feat`
   (fonctionnalité), `docs` (documentation), `test` (tests), `chore` (configuration).
   Ex. `fix(operators): subtract retourne a - b au lieu de b - a (#1)`.
4. **Vérifier localement** que le test ciblé passe, puis pousser la branche :
   `git push -u origin <branche>`.
5. **Pull request** vers `main` avec `Closes #<numéro>` dans la description et la sortie
   pytest prouvant que le test passe.
6. **Revue** par au moins un autre membre de l'équipe avant la fusion. Mettre la branche
   à jour avec `main` en cas de conflit.
7. Après la fusion, supprimer la branche et relancer toute la suite de tests sur `main`.

Les correctifs et nouvelles fonctionnalités passent toujours par une branche et une pull
request ; seuls la mise en place, la documentation et les tests initiaux ont été poussés
directement sur `main`.
