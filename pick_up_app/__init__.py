from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

config = yaml.load(open('config.yaml'), yaml.FullLoader)

app = Flask(__name__)
app.config['SECRET_KEY'] = config['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = config['sql_database']
app.config['ENV'] = config['env']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['sqlalchemy_modification']

db = SQLAlchemy(app)

from pick_up_app import routes