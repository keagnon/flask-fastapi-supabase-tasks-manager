# Task Management API with Flask, FastAPI, and PostgreSQL (Supabase)

## Introduction

This project involves the development of a robust API for managing a task list, using Flask API and FastAPI as server-side frameworks, and Supabase as the PostgreSQL database. The API facilitates the creation, updating, deletion, and retrieval of tasks, as well as categorization and association with users.

## Database Modeling

### Table "Users"

- `user_id` (Primary Key)
- `username`
- `email`
- `password` (hashed)

Stores user information, where each user has a unique identifier (`user_id`).

### Table "Tasks"

- `task_id` (Primary Key)
- `title`
- `description`
- `completed` (Boolean)
- `due_date`
- `user_id` (Foreign Key linked to the "Users" table)

Contains details of tasks, where each task has a unique identifier (`task_id`) and is associated with a user through the foreign key `user_id`.

### Table "Categories"

- `category_id` (Primary Key)
- `name`

Allows categorization of tasks. Each category has a unique identifier (`category_id`) and can be associated with multiple tasks.

## Schema Visualizer

![Schema Visualizer](images/schema_visualizer.png)

## Usage

1. Clone the repository.

2. Install dependencies using `pip install -r requirements.txt`.

3. Run the API with Flask: `python mainFlask.py` or with FastAPI: `python mainFast.py`.

4. Access the API at: [http://localhost:5000](http://localhost:5000) for Flask or [http://127.0.0.1:3000/docs](http://127.0.0.1:3000/docs) for FastAPI.

## Main Features for FlaskAPI

- Get the list of tasks: GET /api/tasksmanager/tasks/
- Create a new task: POST /api/tasksmanager/tasks/
- Update an existing task: PUT /api/tasksmanager/tasks/<task_id>
- Delete a task: DELETE /api/tasksmanager/tasks/<task_id>

## Main Features for FastAPI

FastAPI automatically generates documentation accessible at: [http://127.0.0.1:3000/docs](http://127.0.0.1:3000/docs).

## Configuration

The API uses Flask and/or Fast for route management. Request logs are saved in a `logs.json` file for Flask. The privacy policy is displayed at the root of the API.

## Author

[GBE Keagnon Grâce Helena](mailto:keagnon.gbe@gmail.com)

## Documentation Sphinx ReadTheDocs

The complete documentation is available in the following path: `/docs/_build/index.html`.
