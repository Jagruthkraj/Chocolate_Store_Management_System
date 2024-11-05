from .database import db

class SeasonalFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    availability_start = db.Column(db.Date, nullable=False)
    availability_end = db.Column(db.Date, nullable=False)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    quantity = db.Column(db.Integer, nullable=False)

class CustomerSuggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    suggestion = db.Column(db.String(500), nullable=False)
    allergy_concern = db.Column(db.String(100), nullable=True)
