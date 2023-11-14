import secrets

from flask import current_app
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
ma = Marshmallow()


# Define User model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    salt = db.Column(db.String(32), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password, self.salt = self._generate_hash(password)

    def _generate_hash(self, password):
        # Generate a new salt for each user
        salt = secrets.token_hex(16)

        return [
            bcrypt.generate_password_hash(
                password + current_app.config["SECRET_PEPPER"] + salt
            ).decode("utf-8"),
            salt,
        ]


# Define User Schema for serialization
class UsersSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password")
