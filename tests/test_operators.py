"""Tests unitaires des fonctions arithmétiques de ``operators.py``.

Chaque fonction est testée isolément, sans Flask. Les cas sont choisis pour
distinguer l'opération attendue d'erreurs plausibles : par exemple ``8 - 2``
et ``2 - 8`` donnent des résultats différents, ce qui détecte des opérandes
inversés ; ``7 / 2`` n'est pas entier, ce qui détecte une division entière.
"""

import pytest

from operators import add, subtract, multiply, divide


# --- add ---------------------------------------------------------------------

def test_add_positive():
    """La somme de deux entiers positifs est correcte."""
    assert add(8, 2) == 10


def test_add_negative_and_float():
    """L'addition gère les négatifs et les décimaux."""
    assert add(-3, 1.5) == pytest.approx(-1.5)


# --- subtract ----------------------------------------------------------------

def test_subtract_positive():
    """subtract(a, b) retourne a - b (et non b - a)."""
    assert subtract(8, 2) == 6


def test_subtract_negative_result():
    """Un résultat négatif est possible quand b > a."""
    assert subtract(2, 8) == -6


# --- multiply ----------------------------------------------------------------

def test_multiply_positive():
    """multiply(a, b) retourne le produit a * b.

    8 * 2 = 16 alors que 8 ** 2 = 64 : ce cas distingue produit et puissance.
    """
    assert multiply(8, 2) == 16


def test_multiply_by_zero():
    """Tout nombre multiplié par zéro donne zéro."""
    assert multiply(5, 0) == 0


# --- divide ------------------------------------------------------------------

def test_divide_exact():
    """Une division sans reste donne le quotient attendu."""
    assert divide(8, 2) == 4


def test_divide_non_integer_result():
    """La division est réelle : 7 / 2 = 3.5 (pas de troncature à 3)."""
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_by_zero_raises():
    """Diviser par zéro lève ZeroDivisionError (affichée comme erreur par app.py)."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
