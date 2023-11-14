from flask import Blueprint, current_app, jsonify, request
from flask_wtf.csrf import generate_csrf

from app.models import Users, UsersSchema, bcrypt, db

api_bp = Blueprint("api", __name__)

# Initialize user schemas
user_schema = UsersSchema()
users_schema = UsersSchema(many=True)


@api_bp.route("/getcsrf", methods=["GET"])
def get_csrf():
    token = generate_csrf()
    response = jsonify({"detail": "CSRF cookie set"})
    response.headers.set("X-CSRFToken", token)
    response.set_cookie(f"csrftoken={token}")
    return response


# Create a new user
@api_bp.route("/user", methods=["POST"])
def add_user():
    username = request.json["username"]
    password = request.json["password"]

    user_exists = Users.query.filter_by(username=username).first()
    if user_exists:
        return jsonify({"message": "User already exists"}), 409

    new_user = Users(username, password)
    try:
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user), 201
    except Exception:
        return jsonify({"message": "Error creating user"}), 500


# Get all users
@api_bp.route("/users", methods=["GET"])
def get_users():
    all_users = Users.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


# Get user by id
@api_bp.route("/user/<id>")
def user_detail(user_id):
    user_info = Users.get(int(user_id))
    return user_schema.jsonify(user_info)


@api_bp.route("/login", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]

    user = Users.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User does not exist"})

    if bcrypt.check_password_hash(
        user.password, password + current_app.config["SECRET_PEPPER"] + user.salt
    ):
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid credentials"})
