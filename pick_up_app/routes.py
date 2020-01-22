from flask import render_template, redirect, request
from pick_up_app import app, config
from pick_up_app.forms import AdminRegistrationForm, LogInForm


@app.route('/')
def home():
    
    return render_template('index.html', title='Home Page')

@app.route('/register')
def register():
    form = AdminRegistrationForm
    return render_template('register.html', title='register', form=form)

@app.route('/login')
def login():
    form = LogInForm
    return render_template('login.html', title='login', form=form)