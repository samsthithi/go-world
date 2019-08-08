from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.group import GroupModel
from models.user import UserModel


class Group(Resource):
    def get(self, name):
        group = GroupModel.find_by_name(name)
        if group:
            return group.json()
        return {'message': 'Group not found'}, 404

    def post(self, name):
        if GroupModel.find_by_name(name):
            return {'message': "A group with name '{}' already exists.".format(name)}, 400

        group = GroupModel(name)
        try:
            group.save_to_db()
        except:
            return {"message": "An error occurred creating the group."}, 500

        return group.json(), 201

    def delete(self, name):
        group = GroupModel.find_by_name(name)
        if group:
            group.delete_from_db()

        return {'message': 'Group deleted'}

class GroupList(Resource):
    def get(self):
        return {'groups': list(map(lambda x: x.json(), GroupModel.query.all()))}

class GroupPosts(Resource):
    """
    The return the list of all the posts in a group.
    """
    def get(self, name):
        group = GroupModel.find_by_name(name)
        if group:
            # if we have found the group then return all the posts in this groups.
            return {'post': group.get_posts()}
        return {'message': 'Group not found'}, 404

class GroupUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('group_name')
    @jwt_required()
    def post(self):
        user = UserModel.find_by_username(current_identity.username)

        data = GroupUser.parser.parse_args()
        group = GroupModel.find_by_name(data.group_name)

        # check if group exit in user.
        r=1
        for u in group.members:
            if u.username == user.username:
                r=0
                # return {'group': data.group_name, 'status': '1User already a member of this group.'}
        if r==1:
            group.members.append(user)
            group.save_to_db()

        # checking if a user is already a member of this group. 
        for u in user.groups:
            if u.name == data.group_name:
                return {'group': data.group_name, 'status': 'User already a member of this group.'}
        user.groups.append(group)
        user.save_to_db()
        return {'group': data.group_name, 'status': 'added'}
    
    def get(self):
        data = GroupUser.parser.parse_args()
        group = GroupModel.find_by_name(data.group_name)
        print(group.members)
        # for u in group.members:
        #     print(u.username)
        return {'users': group.get_users()}
