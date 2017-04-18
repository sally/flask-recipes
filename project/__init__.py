'''
Below creates an instance of flask, loads the configuration, and points to a single view file.
'''
# imports
# from flask import Flask

# config
# app = Flask(__name__)
# from . import views

'''
After using Blueprint to structure our project, we need to also add the registration of each Blueprint with the Flask object (app).
'''
# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# config
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)

# blueprints
from project.recipes.views import recipes_blueprintfrom project.users.views import users_blueprint

# register the blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(recipes_blueprint)

'''
We have registered two Blueprints and they each have their own views that they define.
'''
