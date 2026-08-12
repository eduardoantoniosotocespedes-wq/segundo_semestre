Algoritmo cajero_automatico
	escribir "CAJERO AUTOMATICO"
	escribir "Porfavor ingrese su contraseña: "
	intentos = 1
	mientras intentos <= 3 hacer 
		leer clave
		intentos = intentos + 1
		si clave = "1234" Entonces
			escribir"Acceso concedido"
			escribir"ingrese el monto a retirar"
			leer monto 
			monto_i = 2000
			si monto > monto_i Entonces
				escribir "saldo insuficiente"
				intentos = 4
			sino
				monto_r = monto_i - monto
				escribir "transaccion exitosa saldo restante ", monto_r
				intentos = 4
			FinSi
		sino
			si intentos = 3 Entonces
				escribir "clave incorrecta, intente denuevo."
			SiNo
				escribir "clave incorrecta, acceso bloqueado."
			FinSi
		FinSi
	FinMientras
FinAlgoritmo
