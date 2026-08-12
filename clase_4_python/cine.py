print("""BIENVENIDO A CINEPOLIS ELIJA SI ES:
1.- ADULTO
2.- NIÑO
3.- ADULTO MAYOR""")
option =int(input("porfavor ingrese su opcion: ")) 
match option:
    case 1:
        precio = 30
        cliente = "Adulto"
    case 2:
        precio = 15
        cliente = "Infante"
    case 3:
        precio = 20
        cliente = "Adulto mayor"
    case _:
        print("Opcion invalida ")

dia = str(input("Por favor ingrese el dia de la semana: ")).upper().strip()
if dia == "MIERCOLES":
    des = precio * 0.20
    precio = precio - des
    print(f"El cliente: {cliente} tiene un descuento del 20% su precio a pagar es{precio}bs")
else:
    print(f"El cliente: {cliente} tine que pagar el precio: {precio}bs")    