def horas_a_minutos(horas):
    horas = float(input("Ingresa la cantidad de horas: "))
    minutos = horas_a_minutos(horas)

    print("El equivalente en minutos es:", minutos, "min")
    return horas * 60