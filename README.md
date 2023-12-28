# flask-fastapi-supabase-tasks-manager
Développer une API robuste pour gérer une liste de tâches, utilisant Flask API et FastAPI comme frameworks côté serveur, et Supabase comme base de données.

Modélisation pour un système de gestion de tâches :

1. Table "Users" :

    Champs :
        user_id (Clé primaire)
        username
        email
        password (hashé)

    Description :
        Stocke les informations des utilisateurs, chaque utilisateur a un identifiant unique (user_id).

2. Table "Tasks" :

    Champs :
        task_id (Clé primaire)
        title
        description
        completed (Booléen)
        due_date
        user_id (Clé étrangère liée à la table "Users")

    Description :
        Contient les détails des tâches, chaque tâche a un identifiant unique (task_id) et est associée à un utilisateur via la clé étrangère user_id.

3. Table "Categories" :

    Champs :
        category_id (Clé primaire)
        name

    Description :
        Permet de catégoriser les tâches. Chaque catégorie a un identifiant unique (category_id) et peut être associée à plusieurs tâches.