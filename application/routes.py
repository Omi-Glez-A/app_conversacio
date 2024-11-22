from flask import request, render_template, make_response, redirect, url_for
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User
from forms import SignUpForm

@app.route('/', methods=['GET'])
def create_user():
    """Create a user."""
    username = request.args.get('user')
    email = request.args.get('email')
    if username and email:
        existing_user = User.query.filter(User.username == username or User.email == email).first()
        if existing_user:
            return make_response(f"{username} ({email}) already created!")
        new_user = User(
            username=username,
            email=email,
            created=dt.now(),
            admin=False
        ) # Create an instance of the User class
        db.session.add(new_user) # Adds new User record to database
        db.session.commit() # Commits all changes
    
    users = User.query.all()
    return render_template(
        'users.html',
        users=users,
        title="Show Users"
    )

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    title='Sign Up Form'
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('signup.html', form=form, title=title)