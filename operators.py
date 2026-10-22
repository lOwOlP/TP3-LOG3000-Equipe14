"""Opérations arithmétiques de base utilisées par la calculatrice.

Chaque fonction reçoit deux opérandes numériques et retourne le résultat de
l'opération. Ces fonctions sont associées aux symboles de l'interface
(``+``, ``-``, ``*``, ``/``) par le dictionnaire ``OPS`` de ``app.py``.
"""


def add(a,b):
    """Additionne deux nombres.

    Args:
        a (float): Premier opérande.
        b (float): Second opérande.

    Returns:
        float: La somme ``a + b``.
    """
    return a + b

def subtract(a,b):
    """Soustrait le second nombre du premier.

    Args:
        a (float): Opérande de gauche (diminuende).
        b (float): Opérande de droite (diminuteur).

    Returns:
        float: La différence ``a - b``.
    """
    return a - b

def multiply(a,b):
    """Multiplie deux nombres.

    Args:
        a (float): Premier facteur.
        b (float): Second facteur.

    Returns:
        float: Le produit ``a * b``.
    """
    return a * b

def divide(a,b):
    """Divise le premier nombre par le second.

    Args:
        a (float): Dividende.
        b (float): Diviseur.

    Returns:
        float: Le quotient réel ``a / b``.

    Raises:
        ZeroDivisionError: Si ``b`` vaut 0.
    """
    return a // b
