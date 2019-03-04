# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database
SQLALCHEMY_DATABASE_URI = 'postgres://pasqmclztntnrd:1982d35438bf2dabd90d47cac54b8b56affc9c93053268419ae2b8aed9577f13@ec2-107-21-99-237.compute-1.amazonaws.com:5432/dd9lj51mfuj24m'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for signing cookies
SECRET_KEY = "secret"

# Flask settings

FLASK_APP = "my_app"
