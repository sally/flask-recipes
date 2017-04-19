'''
Define all our models in here for our Flask app.
Need to import the 'db' object that we created in ../project/__init__.py
'''

from project import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method

class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recipe_description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.recipe_title = title
        self.recipe_description = description

    def __repr__(self):
        return '<title {}'.format(self.name)

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column(db.Binary(60), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, email, password_plaintext):
        self.email = email
        self.password = password_plaintext
        self.authenticated = False

    '''
    Hybrid properties allow you to treat calculations (e.g. first_name + last_name like any other database column.

    See
    https://github.com/flask-admin/flask-admin/tree/master/examples/sqla-hybrid_property
    http://docs.sqlalchemy.org/en/latest/orm/extensions/hybrid.html#working-with-relationships
    '''
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def set_password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, self.plaintext_password)

    def __repr__(self):
        return "<User {0}".format(self.name)
