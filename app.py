#import email
import json
from administradorDB import AdministradorDB 
from contacto import Contacto
from urllib import request
from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)

# settings de la sesion
app.secret_key = 'mysecretkey'

administradorDb = AdministradorDB(app)

@app.route('/')
def Index():
    data = administradorDb.obtener_contactos()
    print(data)
    return render_template('register.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    contacto = Contacto(request.form)
    administradorDb.insertar_contacto(contacto)
    flash('Contact added succesfully')
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
    data = administradorDb.obtener_contactos_por_ID(id)
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if (request.method == 'POST'):
        contacto = Contacto(request.form)
        administradorDb.iditar_contacto(contacto)
        flash('Contact Updated Succesfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    administradorDb.borrar_contacto(id)
    flash('Contact removed succesfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
