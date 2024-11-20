from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User

@app.route('/', method=['GET'])
def create_user():
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        new_user = User(
            username = username,
            email = email,
            created = dt.now(),
            admin = True
        )
        db.session.add(new_user)
        db.session.commit()

    return make_response(f"{new_user} successfully created!")