from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired

# Testing
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

class SearchForm(FlaskForm):
    term_busqueda = StringField('Ingrese valor', validators=[DataRequired()])
    busqueda_select = SelectField('Opción', choices=[
        ('nombre', 'Dueño'), 
        ('dni', 'DNI'), 
        ('mascota', 'Mascota'), 
        ('fecha_nacimiento', 'Nacimiento'), 
        ('tipo', 'Tipo'), 
        ('raza', 'Raza')])