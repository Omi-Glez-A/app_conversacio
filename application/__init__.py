from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    """Contructor del núcleo de la aplicación"""
    app = Flask( __name__ , instance_relative_config=False)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        # imports
        from . import routes

        # crea las tablas del modelo
        db.create_all()

        return app