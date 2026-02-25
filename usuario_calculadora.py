class Usuario:
    def __init__(self,dato_nombre, dato_id):
        self.nombre = dato_nombre 
        self.id = dato_id


    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def get_nombre(self):
        return self.nombre
    
    def set_id(self, nuevo_id):
        self.id = nuevo_id
    def get_id(self):
        return self.id
    
    def mostrar_info(self):
        print(f"Nombre del usuario: {self.nombre}  ID del usuario: {self.id}")
        


"""
   Responsabilidad de esta clase segun la historia de usuario
   1.Encapsulamiento de atributos (Get y Set)
   2.Mostrar info
"""


