#fibonacci
print("""SUCECION FIBONACCI,INGRESE HASTA QUE TERMINO 
QUIERE QUE LLEGUE LA SUCECION QUE NO SEA MENOR O IGUAL A 0""")
a = 0
b = 1 
n = int(input("Responda aqui: "))
if n <=0:
    print("Numero invalido")
else:
    for i in range(1, n+1):
        print(a)
        c= a + b
        a=b
        b=c