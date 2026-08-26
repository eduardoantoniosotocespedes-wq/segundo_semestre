Algoritmo sistema_evaluacion_academica
	escribir "Ingrese las notas del estudiante, p1, p2, EF"
	leer a, b, c
	p1 = a * 0.30
	p2 = b * 0.30
	ef = c * 0.40
	suma = (p1+p2+ef)
	si suma >100 o suma <0 entonces
		escribir "nota errona, fuera de sistema"
	SiNo
		si suma >=61 Entonces
			escribir "aprobado"
		sino
			si suma <= 60 y suma >= 40 Entonces
				escribir "Recuperatorio"
			SiNo
				escribir"Reprobado"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
