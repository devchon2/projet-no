from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, InputRequired, Length


class AddForm(FlaskForm):
    id = StringField('ID', validators=[InputRequired(), Length(max=255)])
    name = StringField('Name', validators=[InputRequired(), Length(max=255)])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = StringField('Image URL', validators=[InputRequired()])
    submit = SubmitField("Add")


class DeleteForm(FlaskForm):
    entries = None