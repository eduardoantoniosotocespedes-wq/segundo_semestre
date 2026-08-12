print("""TABLAS DE MULTIPLICAR
---Ingrese el hasta que tabla quiere""")
n =int(input("Responda aqui"))
n = n + 1
for i in range(1, n):
    print(f"TABLA DEL {i}")
    for j in range(1,11):
        print(f"{j}x {i} = {j * i}")