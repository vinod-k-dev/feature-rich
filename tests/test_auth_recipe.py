import unittest
from app import create_app, db
from app.models import User, Recipe
from flask import url_for
from flask_login import login_user

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.create_test_user()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

    def create_test_user(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        self.created_by = user.id

    def login(self):
        with self.client:
            return self.client.post(url_for('auth.login'), data=dict(
                email='test@example.com',
                password='password'
            ), follow_redirects=True)

    def test_register_login_logout(self):
        response = self.client.post(url_for('auth.register'), data=dict(
            username='testuser2',
            email='test2@example.com',
            password='password',
            confirm_password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(url_for('auth.login'), data=dict(
            email='test2@example.com',
            password='password'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        response = self.client.get(url_for('auth.logout'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class RecipesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.TestConfig')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()
            self.create_test_user()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

    def create_test_user(self):
        user = User(username='testuser', email='test@example.com')
        user.set_password('password')
        db.session.add(user)
        db.session.commit()
        self.created_by = user.id

    def login(self):
        with self.client:
            return self.client.post(url_for('auth.login'), data=dict(
                email='test@example.com',
                password='password'
            ), follow_redirects=True)

    def test_create_recipe(self):
        self.login()
        response = self.client.post(url_for('recipes.create_recipe'), data=dict(
            title='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_edit_recipe(self):
        self.login()
        with self.app.app_context():
            recipe = Recipe(title='Test Recipe', description='Test Description',
                            ingredients='Test Ingredients', instructions='Test Instructions',
                            created_by=self.created_by)
            db.session.add(recipe)
            db.session.commit()
            db.session.refresh(recipe)


        response = self.client.post(url_for('recipes.edit_recipe', recipe_id=recipe.id), data=dict(
            title='Updated Recipe',
            description='Updated Description',
            ingredients='Updated Ingredients',
            instructions='Updated Instructions'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_recipe(self):
        self.login()
        with self.app.app_context():
            recipe = Recipe(title='Test Recipe', description='Test Description',
                            ingredients='Test Ingredients', instructions='Test Instructions',
                            created_by=self.created_by)
            db.session.add(recipe)
            db.session.commit()
            db.session.refresh(recipe)

        response = self.client.post(url_for('recipes.delete_recipe', recipe_id=recipe.id), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
