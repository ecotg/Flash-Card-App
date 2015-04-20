from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class Deck(Form):
	word = StringField('word', validators = [DataRequired()])
	definition = StringField('definition', validators = [DataRequired()])