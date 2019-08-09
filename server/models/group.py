from db import db


class GroupModel(db.Model):
    __tablename__ = 'groups'

    # user = db.relationship('UserModel')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    posts = db.relationship('PostModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'posts': [post.json() for post in self.posts.all()]}

    def get_posts(self):
        """
        return a list of al the posts in a group.
        """
        return [post.json() for post in self.posts.all()]

    def get_users(self):
        return [user.username for user in self.members.all()]

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'name: {self.name}'
