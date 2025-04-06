from flask_restx import Api
from backend.apis.auth import auth_namespace

api = Api(
    title="Dangeons and Cats game",
    version="1.0",
    description="A simple game API",
    authorizations={
        'APIKeyHeader': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': "Type in the *'Value'* input box below: **'Bearer <JWT>'**, where JWT is the token"
        }
    },
    security='APIKeyHeader'
)

api.add_namespace(auth_namespace, path="/auth")
