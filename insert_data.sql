-- Création de la table Users
CREATE TABLE Users (
    user_id serial PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Création de la table Categories
CREATE TABLE Categories (
    category_id serial PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Création de la table Tasks
CREATE TABLE Tasks (
    task_id serial PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    completed BOOLEAN NOT NULL,
    due_date DATE,
    user_id INTEGER REFERENCES Users(user_id),
    category_id INTEGER REFERENCES Categories(category_id)
);

-- Insertion d'un utilisateur
-- Insertion d'un utilisateur avec mot de passe hashé en SHA-256
INSERT INTO Users (user_id, username, email, password)
VALUES (1, 'john_doe', 'john@example.com', MD5('hashed_password'));

-- Insertion de catégories
INSERT INTO Categories (category_id, name)
VALUES (1, 'Work'), (2, 'Personal'), (3, 'Shopping');

-- Insertion de tâches
-- Assumez que l'utilisateur avec user_id = 1 existe déjà et que la catégorie avec category_id = 1 existe déjà.
INSERT INTO Tasks (task_id, title, description, completed, due_date, user_id, category_id)
VALUES (1, 'Complete project report', 'Finish the project report before the deadline.', false, '2023-01-31', 1, 1),
       (2, 'Buy groceries', 'Pick up groceries for the week.', false, '2023-02-05', 1, 3);
