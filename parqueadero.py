class Parqueadero:
    def __init__(self):
        self.puesto = ""
        self.fecha_entrada = ""
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = ""
        self.tabla = []

    def set_puesto(self, nuevo_puesto):
        self.puesto = nuevo_puesto
    def get_puesto(self):
        return self.puesto
    
    def set_fecha_entrada(self, nuevo_fecha_entrada):
        self.fecha_entrada = nuevo_fecha_entrada
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def set_hora_entrada(self, nueva_hora_entrada):
        self.hora_entrada = nueva_hora_entrada
    def get_hora_entrada(self):
        return self.hora_entrada
    
    def set_hora_salida(self, nueva_hora_sallida=None):
        self.hora_salida = nueva_hora_sallida
    def get_hora_salida(self):
        return self.hora_salida
    
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    def get_estado(self):
        return self.estado       

    def set_tabla(self, nuevo_tabla): 
        self.tabla = nuevo_tabla
    def get_tabla(self):
        return self.tabla

    def guardar_info(self, obj_usuario, obj_carro):

        fila = [
            obj_usuario.get_id(),
            obj_usuario.get_nombre(),
            obj_usuario.get_tipo_usuario(),
            obj_carro.get_placa(),
            obj_carro.get_tipo_carro(),
            obj_carro.get_color(),
            self.puesto,
            self.fecha_entrada,
            self.hora_entrada,
            self.hora_salida,
            self.estado,
        ]

        self.tabla.append(fila)
     
        
    def mostrar_tabla(self):
        print(f"{'ID':<10}{'Nombre':<15}{'TipoUsuario':<15}{'Placa':<10}{'TipoCarro':<15}{'Color':<10}{'Puesto':<10}{'Fecha':<15}{'H.Entrada':<12}{'H.Salida':<12}{'Estado':<12}")
        print("-"*140)

        for fila in self.tabla:
            print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<10}{fila[4]:<15}{fila[5]:<10}{fila[6]:<10}{fila[7]:<15}{fila[8]:<12}{fila[9]:<12}{fila[10]:<12}")
        

