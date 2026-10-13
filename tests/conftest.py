"""Fixtures pytest partagées par tous les fichiers de tests."""

import pytest

from app import app as flask_app


@pytest.fixture
def client():
    """Fournit un client de test Flask pour envoyer des requêtes sans lancer de serveur.

    Returns:
        flask.testing.FlaskClient: Client lié à l'application en mode TESTING
        (les exceptions remontent au test au lieu d'être converties en HTTP 500).
    """
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client
