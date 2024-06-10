# Flask Recipe Manager

This project is a feature-rich web application built using Python and Flask that allows users to manage and share their favorite recipes. It includes user authentication, database interactions, and dynamic content.

## Features

1. **User Authentication and Authorization**
    - User registration and login functionality.
    - Session management using Flask-Login.
    - Users can create, edit, and delete their own recipes.

2. **Database Schema**
    - Uses a relational database (e.g., SQLite).
    - Recipe table with fields:
        - id (integer, primary key)
        - title (string, not null)
        - description (text)
        - ingredients (text)
        - instructions (text)
        - created_by (foreign key referencing user)

3. **Recipe Management**
    - CRUD (Create, Read, Update, Delete) endpoints for recipes.
    - Search functionality to find recipes by title or ingredients.
    - Pagination for listing recipes.

4. **Testing**
    - Unit tests for critical components (e.g., authentication, database interactions) using pytest.

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/flask-recipe-manager.git
    cd flask-recipe-manager
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

6. **Access the application:**
    - Open your web browser and go to `http://127.0.0.1:5000`.

## Endpoints

- **Home Page:** `/`
    - Displays a list of recipes with pagination.

- **Register:** `/register`
    - User registration page.

- **Login:** `/login`
    - User login page.

- **Logout:** `/logout`
    - Logs the user out and redirects to the home page.

- **New Recipe:** `/recipe/new`
    - Page to create a new recipe (requires login).

- **View Recipe:** `/recipe/<int:recipe_id>`
    - Displays the details of a specific recipe.

- **Edit Recipe:** `/recipe/<int:recipe_id>/update`
    - Page to edit an existing recipe (requires login and ownership).

- **Delete Recipe:** `/recipe/<int:recipe_id>/delete`
    - Deletes a recipe (requires login and ownership).

## Testing

- **Run the tests:**

    ```bash
    pytest
    ```

## Additional Notes

- Make sure to set the `SECRET_KEY` and database URI in `config.py` for production use.
- Optionally, deploy the application to a cloud platform (e.g., Heroku) and provide the live demo link.

---

This is a simple example of how you might set up and document your Flask project. Be sure to customize the details according to your specific implementation and requirements.
