# `static/` — Ressources statiques (CSS)

## Raison d'être

Contient les fichiers servis tels quels par Flask, sans traitement côté serveur.
Actuellement, uniquement la mise en forme de la calculatrice.

## Fichiers

| Fichier | Responsabilité |
|---|---|
| `style.css` | Style de la page : centrage de la calculatrice, thème sombre, écran, grille 4 colonnes des boutons et couleurs (gris pour les chiffres, orange pour les opérateurs via `.operator`). |

## Dépendances et hypothèses

- Flask sert ce dossier automatiquement à l'URL `/static/...` (comportement par défaut
  de `Flask(__name__)`).
- Les sélecteurs dépendent de la structure de `templates/index.html` :
  `.calculator`, `#display`, `.buttons`, `.btn`, `.operator`. Renommer une classe
  ou un id dans le HTML exige de la renommer ici aussi.
- `.buttons` suppose des rangées de **4** boutons (`grid-template-columns: repeat(4, 1fr)`).
- Aucun préprocesseur ni dépendance externe (pas de framework CSS).
