class Numero:
    def __init__(self, dato_numero ):
        self.numero = dato_numero

    def set_numero(self, nuevo_numero):
        self.numero = nuevo_numero
    def get_numero(self):
        return self.numero

    
    def mostrar_info(self):
        print(f"Numero seleccionados: {self.numero}")



"""
   Responsabilidad de esta clase segun la historia de usuario
   1.Encapsulamiento de atributos (Get y Set)
   2.Mostrar info
"""

