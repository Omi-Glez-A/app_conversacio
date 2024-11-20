import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def create_app():
    """Contructor del núcleo de la aplicación"""
    app = Flask( __name__ )
    db.init_app(app)
    app.config['SECRET_KEY'] = '1234'        
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')

    with app.app_context():
        # imports
        from . import routes

        # crea las tablas del modelo
        db.create_all()

        return app