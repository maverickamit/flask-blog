from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import data_required, length, email, equal_to


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[
                               data_required(), length(min=2, max=20)])
    email = StringField('Email', validators=[data_required(), email()])
    password = PasswordField('Password', validators=[data_required()])
    confirm_password = PasswordField(
        'Password', validators=[data_required(), equal_to('password')])
    submit = SubmitField('Sign Up')

