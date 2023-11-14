from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from .models import bcrypt, db, ma


def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object("app.config.DevelopmentConfig")

    # Initialize plugins
    db.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)
    CSRFProtect(app)
    CORS(
        app,
        expose_headers=["Content-Type", "X-CSRFToken"],
        supports_credentials=True,
    )

    from .routes import api_bp

    app.register_blueprint(api_bp)

    return app
