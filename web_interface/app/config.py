import os
_basedir = os.path.abspath(os.path.dirname(__file__))  # Change this if the database is located somewhere else

# General Settings
DEBUG = True
SECRET_KEY = "Replace This!"

# Database settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, '..', '..', 'database.db')