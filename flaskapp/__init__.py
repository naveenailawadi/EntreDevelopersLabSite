from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c0115a8363cdd98b3c822c1adba5a7c9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///edl.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskapp import routes


'''
Further learning:
https://www.youtube.com/watch?v=u0oDDZrDz9U
'''
