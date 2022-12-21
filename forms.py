from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, PasswordField
from wtforms.validators import DataRequired

# APP: No guarda los datos en la db.
class RegistroVeterinaria(FlaskForm):
    propietario = StringField('Nombre de usuario', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    mascota = StringField('Nombre de la mascota', validators=[DataRequired()])
    mascota_nac = DateField('Fecha de nacimiento', validators=[DataRequired()])
    tipo = StringField('Tipo', validators=[DataRequired()])
    raza = StringField('Raza', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class SignupForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')