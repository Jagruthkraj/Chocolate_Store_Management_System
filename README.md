# Chocolate Store Management System

## Overview
The Chocolate Store Management System is a RESTful API designed for a fictional chocolate house. This API allows the management of:

- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

The API uses Flask as the web framework, Flask-SQLAlchemy (an Object-Relational Mapper, or ORM) for database interaction, and SQLite as the underlying database. It is fully containerized using Docker. This project provides a set of endpoints to add, update, and retrieve information about flavors, ingredients, and customer suggestions in a seamless, Pythonic way via SQLAlchemy.

## Setup Instructions

### Prerequisites
- Python3
- Docker
- Git
- Invoke-WebRequest (Powershell)

### 1. Clone the Repository

- git clone https://github.com/JagruthRaj/Chocolate_Store_Management_System.git
- cd ChocolateHouse

## Install Dependencies
Create a virtual environment and install dependencies from requirements.txt:
- python -m venv venv
- source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
- pip install -r requirements.txt



## Run the Application Locally
Start the Flask server by running:

##### python run.py
###### The server will start at http://127.0.0.1:5000 with debugging enabled.

![a](https://github.com/user-attachments/assets/cc5b91d8-b130-4901-ae6f-e4cac28e514e)

## Running with Docker
Build and run the Docker container:
- docker build -t chocolate-house-api .
- docker run -p 5000:5000 chocolate-house-api

![f](https://github.com/user-attachments/assets/1bad641d-010d-4a0b-8b35-374dc3d887dc)

## Accessing the API
Once running, you can access the API at:

- http://127.0.0.1:5000/ (Displays a welcome message)
- Other endpoints (detailed below)
![e](https://github.com/user-attachments/assets/07f88717-d794-4537-96c4-7de6c1b3aa70)

## API Endpoints
#### Home Endpoint
- URL: /
- Method: GET
- Response: Displays a welcome message.
#### Seasonal Flavors
- URL: /flavors
###### Methods:
- GET: Fetches all flavors.
- POST: Adds or updates a seasonal flavor.

##### Example:

#### PowerShell command to add a flavor
##### $uri = "http://127.0.0.1:5000/flavors"
##### $headers = @{ "Content-Type" = "application/json" }
##### $body = '{ "name": "Caramel Swirl", "availability_start": "2024-12-01", "availability_end": "2024-12-31" }'
##### Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $body
![d](https://github.com/user-attachments/assets/fa2df8dd-af26-4bb7-bfa2-181c700c067e)

#### Ingredients
- URL: /ingredients
###### Methods:
- GET: Retrieves all ingredients.
- POST: Adds a new ingredient.

##### Example:

#### PowerShell command to add an ingredient
##### $uri = "http://127.0.0.1:5000/ingredients"
##### $headers = @{ "Content-Type" = "application/json" }
##### $body = '{ "name": "Cocoa Powder", "quantity": 100 }'
##### Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $body
![Screenshot 2024-11-05 153613](https://github.com/user-attachments/assets/fb790100-ef6b-42d2-afe4-60b358a26b5e)


### Customer Suggestions
- URL: /suggestions
##### Methods:
- GET: Fetches all suggestions.
- POST: Adds a customer suggestion with optional allergy concerns.

##### Example:

#### PowerShell command to add a suggestion
##### $uri = "http://127.0.0.1:5000/suggestions"
##### $headers = @{ "Content-Type" = "application/json" }
##### $body = '{ "suggestion": "Add more seasonal flavors.", "allergy_concern": "nuts" }'
##### Invoke-WebRequest -Uri $uri -Method Post -Headers $headers -Body $body
![c](https://github.com/user-attachments/assets/9fa77e64-edcd-4e06-b22b-c6dec733a2ac)
