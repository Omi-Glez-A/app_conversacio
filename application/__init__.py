from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Contructor del núcleo de la aplicación"""
    app = Flask( __name__ , instance_relative_config=False)
    db.init_app(app)
    app.config.from_object('config.Config')

    with app.app_context():
        # imports
        from . import routes

        # crea las tablas del modelo
        db.create_all()

        return app