from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS', "config.DevelopmentConfig"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def hello():
    from models import Result
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
