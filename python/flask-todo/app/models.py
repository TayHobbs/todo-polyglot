from .db import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    completed = db.Column(db.Boolean)

    def __repr__(self):
        return '<Todo %r>' % (self.name)
