from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AdminRegistrationForm(FlaskForm):
    full_name = StringField('FullName', validators=[DataRequired(), Length(min=3, max=50)])
    position = StringField('Position', validators=[DataRequired(), Length(min=3, max=15)])
    house_address = StringField('HouseAddress', validators=[DataRequired(), Length(min=3, max=50)])
    email_address = StringField('EmailAddress', validators=[DataRequired(), Email()])
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=6, max=12)])
    confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired(), Length(min=6, max=12), EqualTo('password')])
    submit = SubmitField('Add')


class SecurityRegistrationForm(FlaskForm):
    full_name = StringField('FullName', validators=[DataRequired(), Length(min=3, max=50)])
    position = StringField('Position', validators=[DataRequired(), Length(min=3, max=15)])
    house_address = StringField('HouseAddress', validators=[DataRequired(), Length(min=3, max=50)])
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=6, max=12)])
    confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired(), Length(min=6, max=12), EqualTo('password')])
    submit = SubmitField('Add')


class LogInForm(FlaskForm):
    email_address = StringField('EmailAddress', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=12)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')
    