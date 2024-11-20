from os import environ

class Config:
    """Establece la configuración de las variables de venv"""

    # General
    TESTING = environ["TESTING"]
    FLASK_DEBUG = environ["FLASK_DEBUG"]
    SECRET_KEY = environ.get('SECRET_KEY')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
