print("""PARQUE TEMATICO COMPRE SU ENTRADA: 
Precio(cualquiera que no sea menor a 1bs)""")
precio = int(input("Responda aqui: "))
if precio <=0 :
    print("Error")
else:
    des = str(input("Cuenta con algun descuento? S(si), N(no)")).upper()
    eda = int(input("Ingrese su edad: "))
    if eda <12 :
        descuento = precio * 0.50
        total = precio - descuento
        print(f"Usted tiene un descuento de 50% su pago debe ser: {total}bs ")
    elif eda >=12 and des == "S":
        descuento = precio * 0.20
        total = precio - descuento
        print(f"Usted tiene un descuento de 20% elprecio a pagar es: {total}bs ")
    else:
        total = precio
        print(f"Ustednocuenta ningun descuento su totalapagar es: {total}bs ")