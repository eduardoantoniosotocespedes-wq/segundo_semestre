print("""MENU DE OPCIONES DE VEICULOS:
1.- AUTO
2.- MOTO
3.- CAMION""")
option =int(input("porfavor ingrese su opcion: ")) 
match option:
    case 1:
        variable = 5
    case 2:
        variable = 3
    case 3:
        variable = 10
hour =float(input("ingresa la hora(ejemplo: 1200 = 12:00pm): "))   
if hour>=1200 and hour <=1300:
    descuento=(variable * 0.15)
    variable = variable + descuento
    print(variable,"bs de peaje")
else:
    print(variable,"bs de peaje")

                