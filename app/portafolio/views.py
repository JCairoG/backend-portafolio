from flask import Flask,render_template,session,flash,redirect,url_for

from . import portafolio

from .forms import ContactForm

from app import fb

@portafolio.route('/')
def index():
    dicBiografia = fb.getCollection('biografia')[0]
    session['biografia'] = dicBiografia
    return render_template('portafolio/index.html')

@portafolio.route('/portafolio')
def portafolios():
  dicPortaf = fb.getCollection("proyectos")
  context = {"proyectos": dicPortaf}
  return render_template('portafolio/portafolio.html',**context)

@portafolio.route('/acercade')
def acercade():
  return render_template('portafolio/acercade.html')

@portafolio.route('/contacto',methods=["GET","POST"])
def contacto():
  contacto_form = ContactForm()
  context = {'contacto_form': contacto_form}

  if contacto_form.validate_on_submit():
    dataContact = {
      "nombre" : contacto_form.nombre.data,
      "correo" : contacto_form.correo.data,
      "telefono" : contacto_form.telefono.data,
      "mensaje" : contacto_form.mensaje.data
      }
    result = fb.insertDocument('contacto', dataContact)
    flash("Sus datos han sido registrados!")
    return redirect(url_for('portafolio.index'))

  return render_template('portafolio/contacto.html',**context)