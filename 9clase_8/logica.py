def mayor(a,b,c):
    a = float(input("ingrese su primer numero: "))
    b = float(input("ingrese su segundo numero: "))
    c = float(input("ingrese su tercer numero: "))
    if a > b and a > c:
        print(f"El numero mayor es: {a}")
    elif b > a and b > c:
        print(f"El numero mayor es: {b}")
    else:
        print(f"El numero mayor es: {c}")         