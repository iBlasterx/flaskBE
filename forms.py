# APP: No guarda los datos en la db.

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class RegistroVeterinaria(FlaskForm):
    propietario = StringField('Nombre de usuario', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    mascota = StringField('Nombre de la mascota', validators=[DataRequired()])
    mascota_nac = DateField('Fecha de nacimiento', validators=[DataRequired()])
    tipo = StringField('Tipo', validators=[DataRequired()])
    raza = StringField('Raza', validators=[DataRequired()])
    submit = SubmitField('Enviar')