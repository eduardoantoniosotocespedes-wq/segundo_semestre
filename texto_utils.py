def nombre_completo(nombre, apellido):
    nombre = str(input("ingrese su nombre: "))
    apellido= str(input("ingrese su apellido: "))
    completo = nombre + apellido
    return completo.upper()

def primera_letra_mayus(palabra):
    palabra = input("Ingresa una palabra: ")
    letra = primera_letra_mayus(palabra)
    print("La primera letra en mayúscula es:", letra)
    return palabra[0].upper()

def empieza_con_a(palabra):
    palabra = input("Ingresa una palabra: ")
    resultado = empieza_con_a(palabra)

    if resultado:
        print("True - La palabra empieza con A")
    else:
        print("False - La palabra no empieza con A")    
    return palabra[0].lower() == "a"