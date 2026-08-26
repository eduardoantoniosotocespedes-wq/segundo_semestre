#tabla de multiplicar
print("""TABLA DE MULTIPLICAR
1.-Coloque hasta que tabla de multiplicar quiere ver""")
n = int(input("Porfavor ingrese un numero: "))
if n > 0:  
    for i in range(1,n +1):
        print(f"==TABLA DEL:{i}== ")
        for j in range(1,11):
            print(f"{j}x{i}= {j*i}")
else:
    print("Error")            