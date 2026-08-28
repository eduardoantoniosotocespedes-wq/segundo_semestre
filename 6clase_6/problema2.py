for aula in range(1,4):
    suma = 0
    print(f"La categoria numero {aula} ")
    for stu in range(1,5):
        print(f"ingrese el precio delproducto {stu}")
        nota = int(input("Responda aqui: "))
        suma =  suma + nota
        print("")
    print(f"La suma de losp`recios de la categoria {aula} es de: {suma }bs")
    print("")