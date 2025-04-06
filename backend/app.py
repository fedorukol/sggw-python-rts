from flask import Flask
from flask_migrate import Migrate
from backend.core.database import db
from backend.core.api import api
from backend.core.auth import jwt
from backend.models import Player # noqa

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['JWT_SECRET_KEY'] = 'super puper key'
db.init_app(app)
jwt.init_app(app)
api.init_app(app)
migrate = Migrate(app, db)