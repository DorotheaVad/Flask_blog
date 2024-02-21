from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SECRET_KEY"]= "05f9d68146e9379ac7ce72f92b0ecc2c"
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
db=SQLAlchemy(app)

from flask_blog import routes