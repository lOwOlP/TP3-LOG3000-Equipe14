# `templates/` — Interface utilisateur (HTML)

## Raison d'être

Contient les gabarits HTML rendus par Flask. C'est la couche présentation de la
calculatrice : ce que l'utilisateur voit et avec quoi il interagit.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `index.html` | Page unique de la calculatrice : écran (`#display`), grille de boutons et petit script JavaScript qui construit l'expression côté client. |

## Fonctionnement

1. Les boutons chiffres/opérateurs appellent `appendToDisplay()` qui ajoute un caractère à l'écran.
2. Le bouton **+/-** appelle `toggleSign()`, qui inverse le signe du dernier nombre
   de l'écran (expression régulière `LAST_OPERAND`, aucune requête serveur).
3. Le bouton **C**, seul sur la dernière rangée, appelle `clearDisplay()` (aucune requête serveur).
4. Le bouton **=** soumet le formulaire en `POST /` avec le champ `display`.
5. Flask (`app.py`) évalue l'expression et réaffiche ce gabarit avec la variable `{{ result }}`.

## Dépendances et hypothèses

- Rendu par **Jinja2** via `render_template('index.html', result=...)` dans `app.py` ;
  la variable `result` doit toujours être fournie (chaîne vide au premier affichage).
- La feuille de style est chargée par `url_for('static', filename='style.css')` :
  le fichier doit donc rester dans `static/`.
- Le champ `display` est `readonly` : le serveur suppose que l'expression ne contient
  que des chiffres et les opérateurs `+ - * /` produits par les boutons.
- Le `name="display"` du champ doit correspondre à `request.form.get('display')` dans `app.py`.
