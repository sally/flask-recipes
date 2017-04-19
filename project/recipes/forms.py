from flask import flash
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AddRecipeForm(Form):
    recipe_title = StringField('Recipe Title', validators=[DataRequired()])
    recipe_description = StringField('Recipe Description', validators=[DataRequired()])

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash("Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
