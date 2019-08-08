from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.post import PostModel


class Post(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('title',
    #                     # type=text,
    #                     required=True,
    #                     help="This field cannot be left blank!"
    #                     )
    parser.add_argument('text',
                        # type=string,
                        required=True,
                        help="This field cannot be left blank!"
                        )
                    
    parser.add_argument('group_id',
                        type=int,
                        required=True,
                        help="Every post needs a group_id."
                        )

    @jwt_required()
    def get(self, title):
        post = PostModel.find_by_title(title)
        if post:
            return post.json()
        return {'message': 'Post not found'}, 404

    @jwt_required()
    def post(self, title):
        if PostModel.find_by_title(title):
            return {'message': "An post with title '{}' already exists.".format(title)}, 400

        data = Post.parser.parse_args()
        data['user_id'] = current_identity.id
        
        post = PostModel(title, **data)

        try:
            post.save_to_db()
        except:
            return {"message": "An error occurred inserting the post."}, 500

        return post.json(), 201

    def delete(self, title):
        post = PostModel.find_by_title(title)
        if post:
            post.delete_from_db()
            return {'message': 'Post deleted.'}
        return {'message': 'Post not found.'}, 404

    def put(self, title):
        data = Post.parser.parse_args()

        post = PostModel.find_by_title(title)

        if post:
            post.title = data['title']
        else:
            post = PostModel(title, **data)

        post.save_to_db()

        return post.json()


class PostList(Resource):
    @jwt_required()
    def get(self):
        print(current_identity.id)
        return {'posts': list(map(lambda x: x.json(), PostModel.query.all()))}
