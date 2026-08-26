Algoritmo ejercicio_1
	escribir "CUAL FUE SU MONTO DE COMPRA"
	leer monto
	si monto <=0 Entonces
		escribir"Error su monto no puede ser 0 o negativo"
	SiNo
		si monto > 500 entonces
			descuento = monto * 0.10
			monto = monto - descuento
			escribir "Su monto total a pagar es: ",monto,"bs"
		sino
			escribir "Monto muy bajo,no obtiene descuento"
		FinSi
		
	FinSi
FinAlgoritmo
