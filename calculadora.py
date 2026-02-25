

class Calculadora:
    def __init__(self):
        self.fecha = ""
        self.tipo_operacion = ""
        self.resultado = ""
        self.tabla = []


    def set_fecha(self,nueva_fecha):
        self.fecha = nueva_fecha
    def get_fecha(self):
        return self.fecha
    
    def set_tipo_operacion(self,nuevo_tipo_operacion):
        self.tipo_operacion = nuevo_tipo_operacion
    def get_tipo_operacion(self):
        return self.tipo_operacion
    
    def set_resultado(self,nuevo_resultado):
        self.resultado = nuevo_resultado
    def get_resultado(self):
        return self.resultado
    
    def set_tabla(self,nuevo_tabla):
        self.tabla = nuevo_tabla
    def get_tabla(self):
        return self.tabla
    



    def _hacer_suma(self, obj_numero1, obj_numero2):
        resultado = obj_numero1 + obj_numero2
        return resultado
    
    def _hacer_resta(self, obj_numero1, obj_numero2):
        resultado = obj_numero1 - obj_numero2
        return resultado
    
    def _hacer_multiplicacion(self, obj_numero1, obj_numero2):
        resultado = obj_numero1 * obj_numero2
        return resultado
    
    def _hacer_divicion(self, obj_numero1, obj_numero2):
        resultado = obj_numero1 / obj_numero2
        return resultado
    



    def hacer_operacion(self, obj_numero1, obj_numero2, tipo_operacion):

        self.tipo_operacion = tipo_operacion

        if tipo_operacion == "Suma":
            self.resultado = self._hacer_suma(obj_numero1.get_numero(), obj_numero2.get_numero())
        elif tipo_operacion == "Resta":
            self.resultado = self._hacer_resta(obj_numero1.get_numero(), obj_numero2.get_numero())
        elif tipo_operacion == "Multiplicacion":
            self.resultado = self._hacer_multiplicacion(obj_numero1.get_numero(), obj_numero2.get_numero())
        elif tipo_operacion == "Divicion":
            self.resultado = self._hacer_divicion (obj_numero1.get_numero(), obj_numero2.get_numero())

    def guardar_info(self, obj_numero1, obj_numero2, obj_usuario):

        fila = [
            obj_usuario.get_id(),
            obj_usuario.get_nombre(),
            obj_numero1.get_numero(),
            obj_numero2.get_numero(),
            self.tipo_operacion,
            self.resultado,
            self.fecha,
        ]
        self.tabla.append(fila)

    def mostrar_tabla(self):
        print(f"{'ID':<10}{'Nombre':<30}{'Numero 1':<15}{'Numero 2':<15}{'Tipo Operacion':<15}{'Resultado':<10}{'Fecha Uso':<15}")
        print("-"*125)

        for fila in self.tabla:
            print(f"{fila[0]:<10}{fila[1]:<30}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<10}{fila[6]:<15}")
        

    




    

    



""""
       Realizar -> suma, resta, dividir, multiplicar
       encapsulamiento (get y set)

           "tabla exel"

       Hacer operacion 
       mostrar info -> usar acululador de texto

       
       """


    
