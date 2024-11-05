from flask import Flask
from .database import db
from .models import SeasonalFlavor, Ingredient, CustomerSuggestion

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chocolatehouse.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Creating the database tables

    from .main import main_bp  # blueprint in main.py
    app.register_blueprint(main_bp)

    return app

# Add this block to run the app directly
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
