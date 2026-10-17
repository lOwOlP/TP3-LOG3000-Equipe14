"""Point d'entrée de la calculatrice web Flask.

Ce module crée l'application Flask, expose la route ``/`` qui affiche
l'interface de la calculatrice et évalue les expressions soumises par le
formulaire. L'évaluation est volontairement limitée à une seule opération
binaire de la forme ``<nombre><opérateur><nombre>`` (ex. ``12+7``).

Lancement : ``python app.py`` puis ouvrir http://127.0.0.1:5000.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Table de correspondance symbole -> fonction. Ajouter un opérateur ici suffit
# pour qu'il soit reconnu par calculate() (le bouton doit aussi exister dans le HTML).
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def is_sign_number(s: str, i:int): 
    """Indique si s[i] est le signe du nombre qui suit (et non une soustraction).

    Un '-' est un signe s'il ouvre l'expression ou suit directement un autre
    opérateur.

    Args:
        s (str): Expression sans espaces, ex. ``"5*-2"``.
        i (int): Position du caractère à examiner dans ``s``.

    Returns:
        bool: ``True`` si ``s[i]`` est un moins unaire, ``False`` sinon.
    """
    return s[i] == '-' and (i == 0 or s[i - 1] in OPS)

def calculate(expr: str):
    """Évalue une expression contenant exactement un opérateur binaire.

    Les espaces sont ignorés. L'expression est découpée autour de l'opérateur,
    puis chaque côté est converti en ``float`` avant d'appliquer l'opération
    correspondante de ``OPS``. Les opérandes peuvent être négatifs : un ``-``
    au début ou juste après l'opérateur est un signe (voir :func:`is_sign_number`).

    Args:
        expr (str): Expression à évaluer, par exemple ``"12 + 7"``, ``"-5+3"``
            ou ``"5*-2"``.

    Returns:
        float: Le résultat de l'opération.

    Raises:
        ValueError: Si l'expression est vide, contient plus d'un opérateur,
            a un opérateur au début/à la fin ou absent, ou si un opérande
            n'est pas un nombre.
        ZeroDivisionError: Si l'expression est une division par zéro.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcours manuel plutôt que eval() : on n'exécute jamais de code fourni
    # par l'utilisateur et on garantit qu'il n'y a qu'une seule opération.
    for i, ch in enumerate(s):
        if ch not in OPS or is_sign_number(s,i):
            continue
        if op_pos != -1:
            raise ValueError("only one operator is allowed")
        op_pos = i
        op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la calculatrice et traite la soumission du formulaire.

    - ``GET`` : affiche l'interface avec un écran vide.
    - ``POST`` : lit le champ ``display`` du formulaire, l'évalue avec
      :func:`calculate` et réaffiche la page avec le résultat (ou un message
      ``Error: ...`` si l'expression est invalide).

    Returns:
        str: La page HTML rendue à partir de ``templates/index.html``.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # On affiche l'erreur dans l'écran de la calculatrice plutôt que de
            # renvoyer une erreur HTTP 500 : l'utilisateur peut corriger et réessayer.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # debug=True active le rechargement automatique : réservé au développement local.
    app.run(debug=True)
