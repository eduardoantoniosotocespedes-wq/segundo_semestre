def pares(a):
    print("===VALIDADOR DE NUMERO PARES ")
    a = float(input("Ingrese un numero:")) 
    if a % 2 == 0:
        return True
    else:
        return False

def valores(a):
    print("===VALIDADOR DE NUMEROS POSITIVOS ")
    a=float(input("Ingrese un numero: ")) 
    if a > 0:
        return True
    else:
        return False