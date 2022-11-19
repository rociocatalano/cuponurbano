from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField)
from wtforms.validators import InputRequired
from wtforms.validators import Length

class FormValidator(FlaskForm):
    nombre_usuario = StringField('Nombre:', validators=[InputRequired()])
    apellido_usuario = StringField('Apellido:', validators=[InputRequired()])
    id_dni = IntegerField('DNI:', validators=[InputRequired(), Length(min=1, max=8)])
    alias = StringField('Alias:', validators=[InputRequired()])
    mail_usuario = StringField('Email:', validators=[InputRequired()])
    contrasenia = StringField('Contraseña:', validators=[InputRequired(), Length(min=8)] )