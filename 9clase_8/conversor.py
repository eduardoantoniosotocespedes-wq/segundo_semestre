def dolares_a_bolivianos(dolares):
    cantidad = float(input("Ingresa la cantidad en dolares: "))
    resultado = dolares_a_bolivianos(cantidad)

    print("Equivalente en bolivianos:", resultado, "Bs")
    cambio = 6.96
    return dolares * cambio

def celsius_a_fahrenheit(celsius):
    grados_c = float(input("Ingresa la temperatura en grados Celsius: "))
    grados_f = celsius_a_fahrenheit(grados_c)

    print("Equivalente en Fahrenheit:", grados_f, "°F")
    return celsius * 1.8 + 32