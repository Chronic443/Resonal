from flask import Flask
from polynomial import polynomial

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///polynomial.sqlite3'
app.register_blueprint(polynomial, url_prefix="/api")

