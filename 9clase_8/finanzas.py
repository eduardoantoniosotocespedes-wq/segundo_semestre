def precio_con_descuento(precio, porcentaje):
    precio = float(input("Ingresa el precio del producto: "))
    porcentaje = float(input("Ingresa el porcentaje de descuento: "))

    final = precio_con_descuento(precio, porcentaje)

    print("Precio final con descuento:", final, "Bs")

    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

def calcular_iva(precio):
    precio = float(input("Ingresa el precio del producto: "))
    impuesto = calcular_iva(precio)

    print("El IVA del 13% es:", impuesto, "Bs")
    iva = precio * 0.13
    return iva