# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SQLALCHEMY_DATABASE_URI = 'postgres://yn277:Galgalon1.@localhost:5432/amicibo'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for signing cookies
SECRET_KEY = "secret"

# Flask settings

FLASK_APP = "my_app"
