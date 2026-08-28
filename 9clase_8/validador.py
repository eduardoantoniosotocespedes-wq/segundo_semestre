def pares(a):
    print("===VALIDAR DE NUMERO PARES ")
    a = float(input("Ingrese un numero")) 
    if a % 2 == 0:
        return True
    else:
        return False

def valores(a):
    print("===VALIDAR DE NUMERO POSITIVOS ")
    a=float(input("Ingrese un numero")) 
    if a > 0:
        return True
    else:
        return False