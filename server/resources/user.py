from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        print("DONE")
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()
        return {"message": "User created successfully."}, 201

class Profile(Resource):
    """Profile page of the user.
    """
    @jwt_required()
    def get(self):
        """This will return the user details of the logged in user,
        which will be shown in the profile page.
        """
        # user = UserModel.find_by_username(current_identity.name)
        return current_identity.json()
        

class UserGroups(Resource):
    """Return list of all the groups of a particular user.
    """
    @jwt_required()
    def get(self):
        user = current_identity
        print(user.groups)
        return {'groups':[g.name for g in user.groups]}