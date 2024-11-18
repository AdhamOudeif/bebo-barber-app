# Bebo Barber App

A Django-based backend application for barbers and clients to manage appointments, services, and reviews. This project uses Django REST Framework (DRF) to provide JSON APIs for interaction.

---

## Features
- User management: Clients and barbers with roles.
- Appointment booking and management.
- Service offerings by barbers.
- Reviews and ratings for barbers.
- API-based interaction.

---

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)
- Virtual environment (recommended)

### Steps
1. Clone the repository:
   git clone https://github.com/your-username/bebo_barber_app.git
   cd bebo_barber_app

2. Install Dependenceis
    cd bebo_backend
    pip install -r requirements.txt

3. Set up the database and db connection
    Run the DDL and DML in your local sql server
    go to settings.py and modify the db connection string as needed

4. Run the Server
    python manage.py runserver

## PROJECT STRUCTURE OVERVIEW
Files in bebo_backend/barber_app are the ones that will be modified the most to implement busienss logic

- Models.py: Defines structure of DB Tables
- Serializers.py: Converts model instances (data) into JSON format and validates incoming API data.
- Views.py: Contains the logic for handling API requests (e.g., GET, POST, PUT, DELETE).
- Urls.py: Maps API endpoints to views.

### How Everything Fits Together
Client sends a request to an endpoint (e.g., /api/users/).

*urls.py*:
Matches the URL /api/users/ to the UserListView view.

*views.py*:
Fetches data from the database using the User model.
Uses the UserSerializer to convert the data to JSON.
Returns the JSON response to the client.

*serializers.py*:
Ensures the data is formatted correctly and validates incoming requests.

*models.py*:
Defines the structure of the data stored in the database.
