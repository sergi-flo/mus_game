import os
import secrets

from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from utils import get_docker_secrets

# Initialize Flask app
app = Flask(__name__)

# Configure the database connection
sql_drivers = os.environ.get("SQL_DRIVERS")
user = get_docker_secrets("mysql-user")
pwd = get_docker_secrets("mysql-user-password")
ip = os.environ.get("IP")
port = os.environ.get("PORT")
db_name = get_docker_secrets("mysql-database")
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"{sql_drivers}://{user}:{pwd}@{ip}:{port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)


# Define a secret pepper
app.config["SECRET_PEPPER"] = get_docker_secrets("pepper")


# Define User model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    salt = db.Column(db.String(32), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash, self.salt = self._generate_hash(password)

    def _generate_hash(self, password):
        # Generate a new salt for each user
        salt = secrets.token_hex(16)

        return [
            bcrypt.generate_password_hash(
                password + app.config["SECRET_PEPPER"] + salt
            ).decode("utf-8"),
            salt,
        ]


# Define User Schema for serialization
class UsersSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "password")


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


# Create a new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json["username"]
    password = request.json["password"]

    new_user = Users(username, password)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = Users.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Get user by id
@app.route("/user/<id>")
def user_detail(user_id):
    user_info = Users.get(int(user_id))
    return user_schema.jsonify(user_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
