for aula in range(1,5):
    suma = 0
    print(f"Aula{aula}")
    for stu in range(1,6):
        print(f"ingrese la nota del estudiante {stu} del aula {aula}")
        nota = int(input("Responda aqui: "))
        suma =  suma + nota
        print("")
    print(f"Elpromedio del aula {aula} es de: {suma / 5}")
    print("")