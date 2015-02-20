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

    def test_todos_show_up_on_index(self):
        todo = models.Todo(name='first todo')
        db.session.add(todo)
        db.session.commit()
        response = self.app.get('/')
        self.assertIn('first todo', response.data)

    def test_can_add_todo_through_post_to_add_todo(self):
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

if __name__ == '__main__':
    unittest.main()
