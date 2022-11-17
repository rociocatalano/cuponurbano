class Contacto:

    def __init__(self,formulario_html, dni = 0):
        if(formulario_html.get('id_dni') != None) :
            self.id_dni = formulario_html['id_dni']
        else :
            self.id_dni = dni
        
        self.nombre_usuario = formulario_html['nombre_usuario']
        self.apellido_usuario = formulario_html['apellido_usuario']
        self.mail_usuario = formulario_html['mail_usuario']
        self.alias = formulario_html['alias']
        self.contrasenia = formulario_html['contrasenia']
        
    

