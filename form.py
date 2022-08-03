from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length

class Form(#Aca falta algo):

#completar lo de abajo
    name=StringField("", validators=[])
    password=PasswordField("",validators=[])
    email=StringField("",validators=[])
    submit=SubmitField("")