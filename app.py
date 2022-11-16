#import email
from urllib import request
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

#MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '****'
app.config['MYSQL_DB'] = 'cuponurbano'
mysql = MySQL(app)

# settings de la sesion
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM registro_usuarios')
    data = cur.fetchall()
    print(data)
    return render_template('register.html', contacts = data)

@app.route('/admin')
def admin():
   cur = mysql.connection.cursor()
   cur.execute('SELECT * FROM registro_usuarios')
   data = cur.fetchall()
   print(data)
   return render_template('admin.html', contacts = data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id_dni = request.form['id_dni']
        nombre_usuario = request.form['nombre_usuario']
        apellido_usuario = request.form['apellido_usuario']
        mail_usuario = request.form['mail_usuario']
        alias = request.form['alias']
        contrasenia = request.form['contrasenia']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO registro_usuarios (id_dni, nombre_usuario, apellido_usuario, mail_usuario, alias, contrasenia) VALUES (%s, %s, %s, %s, %s, %s)', (id_dni, nombre_usuario, apellido_usuario, mail_usuario, alias, contrasenia))
        mysql.connection.commit()
        flash('Contact added succesfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM registro_usuarios WHERE id_dni = %s", [id])
    data = cur.fetchall()
    print(data[0])
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if (request.method == 'POST'):
        nombre_usuario = request.form['nombre_usuario']
        apellido_usuario = request.form['apellido_usuario']
        mail_usuario = request.form['mail_usuario']
        alias = request.form['alias']
        contrasenia = request.form['contrasenia']
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE registro_usuarios
            SET nombre_usuario = %s,,
                apellido_usuario = %s
                mail_usuario = %s,
                alias = %s,
                contrasenia = %s
            WHERE id_dni = %s
        """, (nombre_usuario,apellido_usuario, mail_usuario, alias, contrasenia, id))
        mysql.connection.commit()
        flash('Contact Updated Succesfully')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM registro_usuarios WHERE id_dni = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact removed succesfully')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
