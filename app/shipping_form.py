from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

choices = [(city ,city) for city in map.keys()]
# destination = [()]
# print(destination)


class ShippingForm(FlaskForm):
    sender = StringField('Sender', validators=[DataRequired()])
    recipient = StringField('Recipient', validators=[DataRequired()])
    origin = SelectField('origin', validators=[DataRequired()], choices=choices)
    destination = SelectField('destination', validators=[DataRequired()], choices=choices)
    express_shipping = BooleanField('express shipping')
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')
