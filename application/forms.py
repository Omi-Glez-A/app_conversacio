from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    RadioField,
    BooleanField,
    DateTimeField,
    SubmitField,
    PasswordField,
    SelectField
)
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
    username = StringField(
        'Name',
        [DataRequired()]
    )
    email = StringField(
        'Email',
        [
            Email(message='Please, enter valid email address.'),
            DataRequired()]
    )
    password = PasswordField(
        'Password',
        [
            DataRequired(message='Please enter a password.')
        ]
    )
    confirmPassword = PasswordField(
        'Confirm Password',
        [
            EqualTo(password, message='Passwords must match.')
        ]
    )
    created = DateTimeField(
        'Created'
    )
    admin = BooleanField(
        'Admin',
        [DataRequired()]
    )
    submit = SubmitField('Signup!')