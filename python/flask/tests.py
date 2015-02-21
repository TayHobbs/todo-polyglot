import os
import unittest

from app.config import basedir
from app import app, models
from app.db import db


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_hit_index(self):
        response = self.app.get('/')
        self.assertIn('What needs to be done?', response.data)

    def test_can_add_todo_through_post_to_add_todo(self):
        self.app.post(
            '/add-todo',
            data={'todo': 'New Todo'},
            follow_redirects=True)
        self.assertEqual(False, models.Todo.query.get(1).completed)

    def test_creating_todo_defaults_to_incomplete(self):
        response = self.app.post(
            '/add-todo',
            data={'todo': 'New Todo'},
            follow_redirects=True)
        self.assertIn('New Todo', response.data)

    def test_can_delete_todo_through_post_to_delete_todo(self):
        todo = models.Todo(name='first todo')
        db.session.add(todo)
        db.session.commit()
        self.app.post('/delete-todo', data={'id': '1'})
        self.assertEqual(0, len(models.Todo.query.all()))

    def test_can_edit_todo_through_post_to_edit_todo(self):
        todo = models.Todo(name='first todo')
        db.session.add(todo)
        db.session.commit()
        db.session.commit()
        response = self.app.post(
            '/edit-todo',
            data={'id': '1', 'todo': 'edited todo'},
            follow_redirects=True)
        self.assertIn('edited todo', response.data)

    def test_completed_view_only_shows_completed_todos(self):
        complete = models.Todo(name='completed todo', completed=True)
        incomplete = models.Todo(name='incomplete todo', completed=False)
        db.session.add(complete)
        db.session.add(incomplete)
        db.session.commit()
        response = self.app.get('/completed')
        self.assertIn('completed todo', response.data)
        self.assertNotIn('incomplete todo', response.data)

    def test_completed_todos_route_switches_from_true_to_false(self):
        complete = models.Todo(name='completed todo', completed=True)
        db.session.add(complete)
        db.session.commit()
        self.app.post('/completed', data={'id': complete.id})
        self.assertEqual(False, models.Todo.query.get(1).completed)

    def test_completed_todos_route_switches_from_false_to_true(self):
        complete = models.Todo(name='completed todo', completed=False)
        db.session.add(complete)
        db.session.commit()
        self.app.post('/completed', data={'id': complete.id})
        self.assertEqual(True, models.Todo.query.get(1).completed)

    def test_active_view_only_shows_active_todos(self):
        complete = models.Todo(name='completed todo', completed=True)
        incomplete = models.Todo(name='incomplete todo', completed=False)
        db.session.add(complete)
        db.session.add(incomplete)
        db.session.commit()
        response = self.app.get('/active')
        self.assertNotIn('completed todo', response.data)
        self.assertIn('incomplete todo', response.data)


if __name__ == '__main__':
    unittest.main()
