# `tests/` — Tests automatisés

## Raison d'être

Vérifie que la calculatrice se comporte comme documenté dans les docstrings de
`operators.py` et `app.py`. Les tests décrivent le comportement **attendu** : un test qui
échoue signale un bogue dans le code, pas dans le test.

## Exécuter les tests

Depuis la **racine** du dépôt, environnement virtuel activé (voir le README principal) :

```bash
pytest -v                                        # toute la suite
pytest tests/test_operators.py -v                # un seul fichier
pytest tests/test_operators.py::test_subtract_positive    # un seul test
pytest -k subtract -v                            # tous les tests dont le nom contient "subtract"
```

`pytest.ini` (à la racine) indique à pytest de chercher les tests dans `tests/` et
d'ajouter la racine au chemin d'import, ce qui permet `from app import ...`.

## Fichiers

| Fichier | Ce qui est couvert |
|---|---|
| `conftest.py` | Fixture `client` : client de test Flask, pour tester les routes sans lancer de serveur. |
| `test_operators.py` | Tests unitaires de `add`, `subtract`, `multiply`, `divide` : cas simples, négatifs, décimaux, multiplication par zéro, division non entière et division par zéro. |
| `test_app.py` | `calculate()` : les 4 opérateurs, espaces, décimaux, opérandes négatifs, expressions invalides (vide, plusieurs opérateurs, opérateur au début/à la fin, absent, non numérique). Route `/` : `GET` affiche un écran vide, `POST` affiche le résultat ou `Error: ...` (y compris division par zéro). HTML : chaque bouton affiche le caractère qu'il insère. |

## Choix de conception

- **Valeurs discriminantes** : `8, 2` plutôt que `2, 2`, car `2 + 2 = 2 * 2 = 2 ** 2`
  masquerait un mauvais opérateur. De même, `7 / 2` détecte une division entière.
- **`pytest.approx`** pour les résultats décimaux, afin d'éviter les faux échecs dus aux
  arrondis des `float`.
- **Tests paramétrés** (`@pytest.mark.parametrize`) : chaque cas apparaît séparément dans
  le rapport (ex. `test_digit_button_label_matches_value[8]`), ce qui identifie précisément
  le cas fautif.
- Le style CSS n'est pas testé automatiquement : il est vérifié visuellement dans le navigateur.

## Dépendances et hypothèses

- `pytest` (voir `requirements.txt`) et Flask.
- Les tests de libellés supposent que les boutons appellent `appendToDisplay('<caractère>')`
  et que le libellé est le texte du `<button>` (voir `templates/README.md`).
