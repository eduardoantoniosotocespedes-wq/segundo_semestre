for curso in range(1,5):
    suma = 0
    suma_1= 0
    print(f"Curso {curso}")
    for stu in range(1,7):
        print(f"ingrese si el estudiante {stu} del curso {curso} asisitio con 1 o 0")
        asis = int(input("Responda aqui: "))
        if asis == 1:
            suma =  suma + 1
        elif asis == 0:
            suma_1 = suma_1 + 1
        else:
            print("error opcion invalida")
        print("")
    print(f"En el curso {curso} asistieron {suma} estudienates y faltaron {suma_1} estudiantes ")
    print("")