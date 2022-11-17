from flask_mysqldb import MySQL

class AdministradorDB:

    def __init__(self, app):
        #MySQL connection
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = '010420'
        app.config['MYSQL_DB'] = 'cuponurbano'
        self.mysql = MySQL(app)
    
    def insertar_contacto(self, contacto):
        cur = self.mysql.connection.cursor()
        cur.execute('INSERT INTO registro_usuarios (id_dni, nombre_usuario, apellido_usuario, mail_usuario, alias, contrasenia) VALUES(%s, %s, %s, %s, %s, %s)', (contacto.id_dni, contacto.nombre_usuario, contacto.apellido_usuario, contacto.mail_usuario, contacto.alias, contacto.contrasenia))
        self.mysql.connection.commit()
    
    def obtener_contactos(self):
        cur = self.mysql.connection.cursor()
        cur.execute('SELECT * FROM registro_usuarios')
        data = cur.fetchall()
        return data

    def obtener_contactos_por_ID(self,id):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM registro_usuarios WHERE id_dni = %s", [id])
        data = cur.fetchall()
        return data

    def editar_contacto(self,contacto):
        cur = self.mysql.connection.cursor()
        cur.execute("""
            UPDATE registro_usuarios
            SET nombre_usuario = %s,
                apellido_usuario = %s,
                mail_usuario = %s,
                alias = %s,
                contrasenia = %s
            WHERE id_dni = %s
        """, (contacto.nombre_usuario, contacto.apellido_usuario, contacto.mail_usuario, contacto.alias, contacto.contrasenia, contacto.id_dni))
        self.mysql.connection.commit()

    def borrar_contacto(self,id):
        cur = self.mysql.connection.cursor()
        cur.execute('DELETE FROM registro_usuarios WHERE id_dni = {0}'.format(id))
        self.mysql.connection.commit()
