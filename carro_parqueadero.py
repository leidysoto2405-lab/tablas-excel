class Carro:
    def __init__(self, dato_placa, dato_tipo_carro, dato_color):
        self.placa =  dato_placa
        self.tipo_carro = dato_tipo_carro
        self.color = dato_color

    def set_placa(self, nuevo_placa):
        self.placa = nuevo_placa
    def get_placa(self):
        return self.placa
    
    def set_tipo_carro(self, nuevo_tipo_carro):
        self.tipo_carro = nuevo_tipo_carro
    def get_tipo_carro(self):
        return self.tipo_carro
    
    def set_color(self, nuevo_color):
        self.color = nuevo_color
    def get_color(self):
        return self.color
    

    def mostrar_info(self):
        print(f"Placa: {self.placa}  Tipo de carro: {self.tipo_carro}  color: {self.color}")