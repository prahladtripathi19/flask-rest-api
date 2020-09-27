from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Create an Instance of Flask
app = Flask(__name__)
#Include config from config.py
#app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/workindia?charset=utf8mb4'
app.secret_key = 'some_secret'
#Create an instance of SQLAclhemy
db = SQLAlchemy(app)
from app import views, models