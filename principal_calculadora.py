from usuario_calculadora import Usuario
from numero_calculadora import Numero
from calculadora import Calculadora

obj_usuario = Usuario("Juan García López", "1020345678  ")
obj_numero1 = Numero(50)
obj_numero2 = Numero(30)
obj_calculadora = Calculadora()

obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Suma")
obj_calculadora.hacer_operacion(obj_numero1, obj_numero2, "Suma")

obj_calculadora.guardar_info(obj_numero1, obj_numero2, obj_usuario)


obj_usuario1 = Usuario("Juan García López", "1020345678  ")
obj_numero3 = Numero(50)
obj_numero4 = Numero(30)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Resta")
obj_calculadora.hacer_operacion(obj_numero3, obj_numero4, "Resta")

obj_calculadora.guardar_info(obj_numero3, obj_numero4, obj_usuario1)



obj_usuario2 = Usuario("Juan García López", "1020345678  ")
obj_numero5 = Numero(50)
obj_numero6 = Numero(30)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Multiplicacion")
obj_calculadora.hacer_operacion(obj_numero5, obj_numero6, "Multiplicacion")

obj_calculadora.guardar_info(obj_numero5, obj_numero6, obj_usuario2)



obj_usuario3 = Usuario("Juan García López", "1020345678   ")
obj_numero7 = Numero(150)
obj_numero8 = Numero(3)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Divicion")
obj_calculadora.hacer_operacion(obj_numero7, obj_numero8, "Divicion")

obj_calculadora.guardar_info(obj_numero7, obj_numero8, obj_usuario3)



obj_usuario4 = Usuario("María López Pérez", "1020345679  ")
obj_numero9 = Numero(100)
obj_numero10 = Numero(5)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Suma")
obj_calculadora.hacer_operacion(obj_numero9, obj_numero10, "Suma")

obj_calculadora.guardar_info(obj_numero9, obj_numero10, obj_usuario4)



obj_usuario5 = Usuario("María López Pérez", "1020345679  ")
obj_numero11 = Numero(100)
obj_numero12 = Numero(5)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Resta")
obj_calculadora.hacer_operacion(obj_numero11, obj_numero12, "Resta")

obj_calculadora.guardar_info(obj_numero11, obj_numero12, obj_usuario5)




obj_usuario6 = Usuario("María López Pérez", "1020345679  ")
obj_numero13 = Numero(100)
obj_numero14 = Numero(5)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Multiplicacion")
obj_calculadora.hacer_operacion(obj_numero13, obj_numero14, "Multiplicacion")

obj_calculadora.guardar_info(obj_numero13, obj_numero14, obj_usuario6)



obj_usuario7 = Usuario("María López Pérez", "1020345679  ")
obj_numero15 = Numero(100)
obj_numero16 = Numero(5)


obj_calculadora.set_fecha("2026-02-16")
obj_calculadora.set_tipo_operacion("Divicion")
obj_calculadora.hacer_operacion(obj_numero15, obj_numero16, "Divicion")

obj_calculadora.guardar_info(obj_numero15, obj_numero16, obj_usuario7)




obj_usuario8 = Usuario("Carlos Rodríguez Sánchez", "1020345680  ")
obj_numero17 = Numero(200)
obj_numero18 = Numero(8)


obj_calculadora.set_fecha("2026-02-17")
obj_calculadora.set_tipo_operacion("Suma")
obj_calculadora.hacer_operacion(obj_numero17, obj_numero18, "Suma")

obj_calculadora.guardar_info(obj_numero17, obj_numero18, obj_usuario8)




obj_usuario9 = Usuario("Carlos Rodríguez Sánchez", "1020345680  ")
obj_numero19 = Numero(200)
obj_numero20 = Numero(8)


obj_calculadora.set_fecha("2026-02-17")
obj_calculadora.set_tipo_operacion("Resta")
obj_calculadora.hacer_operacion(obj_numero19, obj_numero20, "Resta")

obj_calculadora.guardar_info(obj_numero19, obj_numero20, obj_usuario9)




obj_usuario10 = Usuario("Carlos Rodríguez Sánchez", "1020345680  ")
obj_numero21 = Numero(75)
obj_numero22 = Numero(3)


obj_calculadora.set_fecha("2026-02-17")
obj_calculadora.set_tipo_operacion("Divicion")
obj_calculadora.hacer_operacion(obj_numero21, obj_numero22, "Divicion")

obj_calculadora.guardar_info(obj_numero21, obj_numero22, obj_usuario10)





obj_calculadora.mostrar_tabla()

