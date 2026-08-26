Algoritmo ejercicio_2
	Escribir 'PORFAVOR INGRESE SU TIPO DE CLIENTE EN MAYUSCULA: A, B, C Y SU MONTO DE COMPRA: '
	Escribir 'ingrse el tipo de cliente: '
	Leer cliente
	Escribir 'ingrese el monto:'
	Leer monto
	Si cliente<>'A' o cliente<>'B' o cliente<>'C" o monto>=0 Entonces
		Escribir 'error no existe este tipo de cliente, o monto erroneo'
	SiNo
		Si cliente=='A' Entonces
			Si monto>1000 Entonces
				descuento <- monto*0.20
				monto <- monto-descuento
				Escribir 'Su monto apagar es:', monto, 'bs'
			SiNo
				descuento <- monto*0.15
				monto <- monto-descuento
				Escribir 'Su monto apagar es: ', monto, 'bs'
			FinSi
		SiNo
			Si cliente=='B' Entonces
				Si monto>1000 Entonces
					descuento <- monto*0.10
					monto <- monto-descuento
					Escribir 'Su monto apagar es:', monto, 'bs'
				SiNo
					Si monto<=1000 Entonces
						descuento <- monto*0.05
						monto <- monto-descuento
						Escribir 'Su monto apagar es: ', monto, 'bs'
					FinSi
				FinSi
			SiNo
				Escribir 'usted no cuenta con descuento, su monto a pagar es: ', monto
			FinSi
		FinSi
	FinSi
FinAlgoritmo
