from db import db,subs


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    posts = db.relationship('PostModel', backref='author', lazy=True)
    groups = db.relationship('GroupModel', secondary=subs,
                backref=db.backref('members', lazy='dynamic'))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def add_group(self, group):
        self.groups.append(group)

    def json(self):
        return {
                'username': self.username,
                'id': self.id
            }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def __repr__(self):
        return f"Username {self.username}"
