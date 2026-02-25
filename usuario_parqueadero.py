class Usuario: 
    def __init__(self, dato_id, dato_nombre, dato_tipo_usuario):
        self.id = dato_id
        self.nombre = dato_nombre
        self.tipo_usuario = dato_tipo_usuario

    def set_id(self, nuevo_id):
        self.id = nuevo_id
    def get_id(self):
        return self.id
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def get_nombre(self):
        return self.nombre
    
    def set_tipo_usuario(self, nuevo_tipo_usuario):
        self.tipo_usuario = nuevo_tipo_usuario
    def get_tipo_usuario(self):
        return self.tipo_usuario
    

    def mostrar_info(self):
        print (f"Nombre: {self.id}  Id: {self.id}  Tipo de usuario: {self.tipo_usuario}")

    
    



        