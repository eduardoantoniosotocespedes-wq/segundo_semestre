def verificar_login(usuario, clave):
    usuario = input("Ingresa el usuario: ")
    clave = input("Ingresa la clave: ")

    if verificar_login(usuario, clave):
        print("Acceso concedido")
    else:
        print("Acceso denegado")
    if usuario == "admin" and clave == "1234":
        return True
    else:
        return False