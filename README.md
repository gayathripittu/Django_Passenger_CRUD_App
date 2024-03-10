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
***
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
