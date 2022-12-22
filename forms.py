from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, PasswordField, SelectField, ValidationError
from wtforms.validators import DataRequired

# Testing
class RegistroVeterinaria(FlaskForm):
    propietario = StringField('Nombre de usuario', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    mascota = StringField('Nombre de la mascota', validators=[DataRequired()])
    #mascota_nac = DateField('Fecha de nacimiento', validators=[DataRequired()])
    tipo = StringField('Tipo', validators=[DataRequired()])
    raza = StringField('Raza', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class SignupForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    password_confirm = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_password(form, field):
        if form.password.data != form.password_confirm.data:
            flash('Las contraseñas no coinciden')
            raise ValidationError('Las contraseñas no coinciden')

class SearchForm(FlaskForm):
    term_busqueda = StringField('Ingrese valor', validators=[DataRequired()])
    busqueda_select = SelectField('Opción', choices=[
        (None, '* Seleccione una opción *'),
        ('nombre', 'Dueño'), 
        ('dni', 'DNI'), 
        ('mascota', 'Mascota'), 
        ('fecha_nacimiento', 'Nacimiento'), 
        ('tipo', 'Tipo'), 
        ('raza', 'Raza')])