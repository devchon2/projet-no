from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms.widgets import TextAreaField

# Ajouter une classe AddForm pour représenter le formulaire d'ajout d'une entrée.
class AddForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    category = StringField("Category", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired(), NumberRange(min=0)])
    quantity = IntegerField("Quantity", validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField("Add")

# Ajouter une classe DeleteForm pour représenter le formulaire de suppression d'une entrée.
class AddForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    body = TextAreaField('Contenu', validators=[DataRequired()])
    submit = SubmitField('Ajouter')
