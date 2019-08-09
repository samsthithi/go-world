from db import db
from datetime import datetime
# from models.user import UserModel

class PostModel(db.Model):
    __tablename__ = 'posts'

    users = db.relationship('UserModel')
    group = db.relationship('GroupModel')

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)

    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self, title, text, user_id, group_id):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.group_id = group_id

    def json(self):
        return {
            'date': self.date.strftime('%m/%d/%Y'),
            'title': self.title, 
            'text': self.text, 
            # 'user_name': UserModel.find_by_id(self.user_id), 
            'user_name': self.author.username,
            'group_id': self.group_id
            }

    @classmethod
    def find_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} --- {self.title}"
