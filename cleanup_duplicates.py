import sys
import os

# Add the app directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app import create_app, db
from app.models import SeasonalFlavor

def remove_duplicates():
    # Create an instance of the Flask application
    app = create_app()
    
    # Establish an application context
    with app.app_context():
        # Query to get all flavors
        flavors = SeasonalFlavor.query.all()
        unique_flavors = {}
        
        for flavor in flavors:
            if flavor.name in unique_flavors:
                # If a duplicate is found, delete it
                db.session.delete(flavor)
            else:
                unique_flavors[flavor.name] = flavor
        
        # Commit the changes to the database
        db.session.commit()
        print("Duplicates removed.")

if __name__ == '__main__':
    remove_duplicates()
