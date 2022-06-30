from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
  nombre = StringField('Nombre', validators=[DataRequired()])
  correo = EmailField('Correo', validators=[DataRequired()])
  telefono = StringField('Telefono', validators=[DataRequired()])
  mensaje = StringField('Mensaje', validators=[DataRequired()])
  submit= SubmitField('Enviar')