"""Tests de ``app.py`` : analyse des expressions et route Flask ``/``.

Trois groupes :
- ``calculate()`` appelée directement (cas valides et invalides) ;
- la route ``/`` via le client de test Flask (affichage et soumission) ;
- le HTML rendu, pour vérifier que chaque bouton affiche le caractère qu'il insère.
"""

import re

import pytest

from app import calculate


# --- calculate() : expressions valides -----------------------------------------

@pytest.mark.parametrize("expr, expected", [
    ("8+2", 10),
    ("8-2", 6),
    ("8*2", 16),
    ("8/2", 4),
])
def test_calculate_each_operator(expr, expected):
    """calculate() applique l'opération correspondant au symbole de l'expression."""
    assert calculate(expr) == pytest.approx(expected)


def test_calculate_ignores_spaces():
    """Les espaces autour des opérandes et de l'opérateur sont ignorés."""
    assert calculate(" 12 + 7 ") == 19


def test_calculate_decimal_operands():
    """Les opérandes décimaux sont acceptés (ex. un résultat précédent comme 2.5)."""
    assert calculate("2.5+1") == pytest.approx(3.5)


# --- calculate() : nombres négatifs --------------------------------------------
# Le résultat d'un calcul reste affiché à l'écran et l'utilisateur peut enchaîner
# (ex. 2-5 = -3.0, puis "+1"). Un opérande négatif doit donc être accepté.

def test_calculate_negative_left_operand():
    """Un premier opérande négatif est accepté : -5+3 = -2."""
    assert calculate("-5+3") == pytest.approx(-2)


def test_calculate_negative_right_operand():
    """Un second opérande négatif est accepté : 5+-2 = 3."""
    assert calculate("5+-2") == pytest.approx(3)


# --- calculate() : expressions invalides ---------------------------------------

@pytest.mark.parametrize("expr", [
    "",        # vide
    "1+2+3",   # plusieurs opérations
    "+5",      # opérateur au début
    "5+",      # opérateur à la fin
    "42",      # aucun opérateur
    "a+b",     # opérandes non numériques
])
def test_calculate_invalid_expression_raises(expr):
    """Une expression mal formée lève ValueError plutôt qu'un résultat faux."""
    with pytest.raises(ValueError):
        calculate(expr)


# --- Route "/" -----------------------------------------------------------------

def _display_value(html):
    """Extrait la valeur affichée dans l'écran (champ #display) d'une page rendue.

    Args:
        html (str): Page HTML retournée par la route ``/``.

    Returns:
        str: Contenu de l'attribut ``value`` du champ ``display``.
    """
    return re.search(r'id="display" value="([^"]*)"', html).group(1)


def test_get_index_shows_empty_calculator(client):
    """GET / répond 200 avec un écran vide."""
    response = client.get("/")
    assert response.status_code == 200
    assert _display_value(response.get_data(as_text=True)) == ""


def test_post_valid_expression_shows_result(client):
    """POST / avec une expression valide affiche le résultat dans l'écran."""
    response = client.post("/", data={"display": "8+2"})
    assert _display_value(response.get_data(as_text=True)) == "10.0"


def test_post_invalid_expression_shows_error(client):
    """POST / avec une expression invalide affiche un message d'erreur, sans HTTP 500."""
    response = client.post("/", data={"display": "+5"})
    assert response.status_code == 200
    assert _display_value(response.get_data(as_text=True)).startswith("Error:")


def test_post_division_by_zero_shows_error(client):
    """Une division par zéro est affichée comme erreur au lieu de planter le serveur."""
    response = client.post("/", data={"display": "8/0"})
    assert response.status_code == 200
    assert _display_value(response.get_data(as_text=True)).startswith("Error:")


# --- Libellés des boutons ------------------------------------------------------

def _button_labels(client):
    """Associe chaque caractère inséré par un bouton au texte affiché sur ce bouton.

    Args:
        client: Client de test Flask.

    Returns:
        dict[str, str]: ex. ``{'1': '1', '+': '+'}`` pour les boutons
        ``appendToDisplay('<caractère>')``.
    """
    html = client.get("/").get_data(as_text=True)
    pairs = re.findall(r"appendToDisplay\('(.)'\)\">([^<]*)</button>", html)
    return {value: label.strip() for value, label in pairs}


@pytest.mark.parametrize("digit", list("0123456789"))
def test_digit_button_label_matches_value(client, digit):
    """Le bouton qui insère un chiffre affiche exactement ce chiffre."""
    assert _button_labels(client)[digit] == digit


@pytest.mark.parametrize("operator", ["+", "-", "*", "/"])
def test_operator_button_label_matches_value(client, operator):
    """Le bouton qui insère un opérateur affiche ce symbole (il n'est pas vide)."""
    assert _button_labels(client)[operator] == operator
