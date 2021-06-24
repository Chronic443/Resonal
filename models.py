from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)
# db.create_all()

class Polynomial(db.Model):
    id = db.Column('polynomial_id', db.Integer, primary_key=True)
    poly_string = db.Column(db.String(), unique=True)

    def __init__(self, poly_string):
        self.poly_string = poly_string
