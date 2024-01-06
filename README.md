# API de Gestion de Tâches avec Flask, FastAPI, et PostgreSQL (Supabase)

## Introduction

Ce projet consiste en le développement d'une API robuste pour la gestion d'une liste de tâches, utilisant Flask API et FastAPI comme frameworks côté serveur, et Supabase comme base de données PostgreSQL. L'API permet la création, la mise à jour, la suppression, et la récupération des tâches, ainsi que la catégorisation et l'association à des utilisateurs.

## Modélisation de la Base de Données

### Table "Users"

- `user_id` (Clé primaire)
- `username`
- `email`
- `password` (hashé)

Stocke les informations des utilisateurs, chaque utilisateur a un identifiant unique (`user_id`).

### Table "Tasks"

- `task_id` (Clé primaire)
- `title`
- `description`
- `completed` (Booléen)
- `due_date`
- `user_id` (Clé étrangère liée à la table "Users")

Contient les détails des tâches, chaque tâche a un identifiant unique (`task_id`) et est associée à un utilisateur via la clé étrangère `user_id`.

### Table "Categories"

- `category_id` (Clé primaire)
- `name`

Permet de catégoriser les tâches. Chaque catégorie a un identifiant unique (`category_id`) et peut être associée à plusieurs tâches.

## Utilisation

1. Cloner le dépôt.

2. Installer les dépendances en utilisant `pip install -r requirements.txt`.

3. Exécuter l'API avec Flask : `python mainFlask.py` ou avec FastAPI : `python mainFast.py`.

4. Accéder à l'API à l'adresse : [http://localhost:5000](http://localhost:3000) pour Flask ou [http://127.0.0.1:3000/docs](http://127.0.0.1:5000/docs) pour FastAPI.

## Fonctionnalités Principales pour FlaskAPI

- Obtenir la liste des tâches : GET /api/tasksmanager/tasks/
- Créer une nouvelle tâche : POST /api/tasksmanager/tasks/
- Mettre à jour une tâche existante : PUT /api/tasksmanager/tasks/<task_id>
- Supprimer une tâche : DELETE /api/tasksmanager/tasks/<task_id>

## Fonctionnalités Principales pour FastAPI

FastAPI génère automatiquement une documentation accessible à l'adresse : [http://127.0.0.1:3000/docs](http://127.0.0.1:3000/docs).

## Configuration

L'API utilise Flask et/ou Fast pour la gestion des routes. Les logs des requêtes sont enregistrés dans un fichier `logs.json` pour Flask. La politique de confidentialité est affichée à la racine de l'API.

## Auteur

[GBE Keagnon Grâce Helena](keagnon.gbe@gmail.com)

## Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

## Documentation Sphinx ReadTheDocs

La documentation complète est disponible dans le chemin suivant : `/docs/_build/index.html`.
