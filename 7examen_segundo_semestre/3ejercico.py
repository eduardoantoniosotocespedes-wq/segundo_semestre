print("""PLAN DES ERVICIOS DE SUSCRIBCIONES:
-1: Plan Básico (Precio: 30 Bs)
-2: Plan Estándar (Precio: 60 Bs)
-3: Plan Premium (Precio: 90 Bs)
""")
option = int(input("Responda aqui: "))
match option:
    case 1:
        print("pago exitoso de: 30bs para el plan basico" )
    case 2: 
        print("pago exitoso de: 60bs para el plan estandar" )    
    case 3:
        print("pago exitoso de: 90bs para el plan premiun" )
    case _:
        print("Opción inválida")