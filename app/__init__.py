from flask import Flask

#initialize an instance of flask app
app = Flask(__name__, instance_relative_config=True)

# Load the config file
app.config.from_object('config')







# Load the views
from app import views

