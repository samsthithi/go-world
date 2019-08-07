from flask_restful import Resource
from models.group import GroupModel


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