from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from backend.models import Player
from backend.core.database import db


auth_namespace = Namespace("auth", description="Authentication related operations")

login_schema = auth_namespace.model(
    "Login",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },  
)

@auth_namespace.route("/register")
class Register(Resource):
    @auth_namespace.expect(login_schema)
    def post(self):
        new_player = Player(
            username=auth_namespace.payload["username"],
            password=auth_namespace.payload["password"],
        )
        db.session.add(new_player)
        db.session.commit()
        return {"message": "Player registered successfully"}, 201
    
@auth_namespace.route("/login")
class Login(Resource):
    @auth_namespace.expect(login_schema)
    def post(self):
        username = auth_namespace.payload["username"]
        password = auth_namespace.payload["password"]
        
        player = Player.query.filter_by(username=username, password=password).first()
        
        if player:
            access_token = create_access_token(identity=player.username)
            return {"token": access_token}, 200

        return {"message": "Invalid credentials"}, 401