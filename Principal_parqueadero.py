from usuario_parqueadero import Usuario
from carro_parqueadero import Carro
from parqueadero import Parqueadero



obj_usuario = Usuario("1020345678 ", "Juan García", "Administrador")
obj_carro = Carro("ABC123", "Sedan", "Negro")
obj_parqueadero = Parqueadero()

obj_parqueadero.set_puesto("A-01")
obj_parqueadero.set_fecha_entrada("2026-02-16")
obj_parqueadero.set_hora_entrada("08:30")
obj_parqueadero.set_hora_salida(" ")
obj_parqueadero.set_estado("Entrada")

obj_parqueadero.guardar_info(obj_usuario, obj_carro)




obj_usuario1 = Usuario("1020345679 ", "María López", "Cliente")
obj_carro1 = Carro("XYZ789", "SUV", "Blanco")

obj_parqueadero.set_puesto("B-05")
obj_parqueadero.set_fecha_entrada("2026-02-16")
obj_parqueadero.set_hora_entrada("09:15")
obj_parqueadero.set_hora_salida(" ")
obj_parqueadero.set_estado("Entrada")

obj_parqueadero.guardar_info(obj_usuario1, obj_carro1)




obj_usuario2 = Usuario("1020345680 ", "Carlos Rodríguez ", "Cliente")
obj_carro2 = Carro("KLM456", "Pickup", "Azul")

obj_parqueadero.set_puesto("C-12")
obj_parqueadero.set_fecha_entrada("2026-02-16")
obj_parqueadero.set_hora_entrada("10:00")
obj_parqueadero.set_hora_salida("11:45")
obj_parqueadero.set_estado("Salida")


obj_parqueadero.guardar_info(obj_usuario2, obj_carro2)





obj_usuario3 = Usuario("1020345681 ", "Ana Martínez", "Cliente")
obj_carro3 = Carro("DEF321", "Hatchback", "Rojo")

obj_parqueadero.set_puesto("A-03")
obj_parqueadero.set_fecha_entrada("2026-02-16")
obj_parqueadero.set_hora_entrada("11:20")
obj_parqueadero.set_hora_salida(" ")
obj_parqueadero.set_estado("Entrada")

obj_parqueadero.guardar_info(obj_usuario3, obj_carro3)






obj_parqueadero.mostrar_tabla()



#Pruebas-----------------------
