# Django Passenger Details CRUD

This Django project, built using function-based views, serves as a platform to manage passenger details effectively. It provides CRUD (Create, Read, Update, Delete) functionality for storing and manipulating passenger information such as name, age, gender, mobile number, and booking details.

## Features
Add new passenger details
View the list of all passengers
Update existing passenger information
Delete passenger records

## Prerequisites
Ensure you have the following installed:

Python (3.x recommended) <br>
Django (5.0.2 used in this project) <br>
Django REST framework <br>
PostgreSQL (or any other database you prefer, with respective settings adjustments) <br>

## Setup and Installation

Clone the repository:<br> 
```bash
git clone <repository-url>
cd Passenger
```

## Install required packages:
```bash
pip install -r requirements.txt
```
## Configure the database:

Edit the settings.py file to update your database settings under the DATABASES configuration.

Example for PostgreSQL:<br>
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdatabasename',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': 'yourportnumber',
    }
}
```
## Apply migrations:

# Applying Migrations

Once you have set up the project and configured the database, you need to apply migrations to create the necessary database schema. Navigate to the project directory and run the following command:<br>

```bash
python manage.py makemigrations
python manage.py migrate
```
## Creating a Superuser

To access the Django admin panel and perform administrative tasks, you need to create a superuser account. Run the following command:<br>

```bash
python manage.py createsuperuser
```
## Running the Server

To start the development server and run the application locally, navigate to the project directory and execute the following command:

```bash
python manage.py runserver
```
After launching the server, navigate to http://localhost:8000/ in your preferred web browser. From there, you'll be able to create, read, update, and delete passenger details using the provided function-based views.<br>

* Admin Interface: Visit http://localhost:8000/admin/ to manage passengers using the Django admin site.
* API Endpoints:
In addition to the web interface, you can also interact with your CRUD project programmatically through the following API endpoints:<br>

- **List Passengers**: `/passengers/` (GET) <br>
- **Create Passenger**: `/passengers/` (POST) <br>
- **Retrieve Passenger**: `/passengers/<passenger_id>/` (GET) <br>
- **Update Passenger**: `/passengers/<passenger_id>/` (PUT, PATCH) <br>
- **Delete Passenger**: `/passengers/<passenger_id>/` (DELETE) <br>

Replace `<passenger_id>` with the ID of the passenger you want to retrieve, update, or delete.



