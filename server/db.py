from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# many-to-many relationship table.

subs = db.Table('subs',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'))
)