from flask import Blueprint, jsonify, request
from .database import db
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion
from datetime import datetime

main_bp = Blueprint('main', __name__)

#  seasonal flavors
@main_bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Welcome to the Chocolate_Store_Management_System  Use /flavors, /ingredients, or /suggestions to access different functionalities."})

@main_bp.route('/flavors', methods=['GET', 'POST'])
def flavors():
    if request.method == 'POST':
        data = request.get_json()

        # Check if the flavor already exists by name
        existing_flavor = SeasonalFlavor.query.filter_by(name=data['name']).first()
        if existing_flavor:
            # update the existing flavor's availability dates instead of returning an error
            existing_flavor.availability_start = datetime.strptime(data['availability_start'], '%Y-%m-%d')
            existing_flavor.availability_end = datetime.strptime(data['availability_end'], '%Y-%m-%d')
            db.session.commit()
            return jsonify({"message": "Flavor updated"}), 200  # Indicate the flavor was updated

        # If it doesn't exist, create a new flavor
        flavor = SeasonalFlavor(
            name=data['name'],
            availability_start=datetime.strptime(data['availability_start'], '%Y-%m-%d'),
            availability_end=datetime.strptime(data['availability_end'], '%Y-%m-%d')
        )
        db.session.add(flavor)
        db.session.commit()
        return jsonify({"message": "Flavor added"}), 201
    
    # Return all flavors
    flavors = SeasonalFlavor.query.all()
    return jsonify([{"name": f.name, "availability_start": f.availability_start, "availability_end": f.availability_end} for f in flavors])

# Endpoint for ingredient inventory
@main_bp.route('/ingredients', methods=['GET', 'POST'])
def ingredients():
    if request.method == 'POST':
        data = request.get_json()
        ingredient = Ingredient(name=data['name'], quantity=data['quantity'])
        db.session.add(ingredient)
        db.session.commit()
        return jsonify({"message": "Ingredient added"}), 201
    ingredients = Ingredient.query.all()
    return jsonify([{"name": i.name, "quantity": i.quantity} for i in ingredients])

# Endpoint for customer suggestions
@main_bp.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        data = request.get_json()
        suggestion = CustomerSuggestion(suggestion=data['suggestion'], allergy_concern=data.get('allergy_concern'))
        db.session.add(suggestion)
        db.session.commit()
        return jsonify({"message": "Suggestion added"}), 201
    suggestions = CustomerSuggestion.query.all()
    return jsonify([{"suggestion": s.suggestion, "allergy_concern": s.allergy_concern} for s in suggestions])
