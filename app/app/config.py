from os import environ, path

from app.utils import get_docker_secrets

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration vars"""

    # General Config
    SECRET_KEY = get_docker_secrets("secret-key")
    SESSION_COOKIE_HTTPONLY = bool(environ.get("SESSION_COOKIE_HTTPONLY"))
    REMEMBER_COOKIE_HTTPONLY = bool(environ.get("REMEMBER_COOKIE_HTTPONLY"))
    SESSION_COOKIE_SAMESITE = bool(environ.get("SESSION_COOKIE_SAMESITE"))
    STATIC_FOLDER = environ.get("STATIC_FOLDER")
    SECRET_PEPPER = get_docker_secrets("pepper")

    # Database
    SQL_DRIVERS = environ.get("SQL_DRIVERS")
    MYSQL_USER = get_docker_secrets("mysql-user")
    MYSQL_USER_PASSWORD = get_docker_secrets("mysql-user-password")
    IP = environ.get("IP")
    PORT = environ.get("PORT")
    MYSQL_DATABASE = get_docker_secrets("mysql-database")
    SQLALCHEMY_DATABASE_URI = f"{SQL_DRIVERS}://{MYSQL_USER}:{MYSQL_USER_PASSWORD}@{IP}:{PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")


class DevelopmentConfig(Config):
    DEBUG = True
    ENVIRONMENT = "development"


class ProductionConfig(Config):
    DEBUG = False
    ENVIRONMENT = "production"
