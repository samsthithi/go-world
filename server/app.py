from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, UserGroups, Profile
from resources.post import Post, PostList
from resources.group import Group, GroupList, GroupPosts, GroupUser, GroupId

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'mohit'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(UserRegister, '/register')
api.add_resource(Post, '/post/<string:title>')
api.add_resource(PostList, '/posts')
api.add_resource(Group, '/group/<string:name>')
api.add_resource(GroupList, '/groups')
api.add_resource(GroupId, '/groupid/<string:name>')

api.add_resource(GroupPosts, '/group_posts/<string:name>')
api.add_resource(GroupUser, '/group_user')
api.add_resource(UserGroups, '/user_groups')
api.add_resource(Profile, '/profile')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
