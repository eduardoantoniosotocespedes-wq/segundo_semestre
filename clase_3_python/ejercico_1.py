monto = float(input("CUAL FUE SU MONTO DE COMPRA: "))
if monto <=0:
    print("Error su monto no puede ser 0 o negativo")
elif monto > 500:
    descuento = monto * 0.10
    monto = monto - descuento
    print("Su monto total a pagar es: ",monto,"bs")
else:
    print("Monto muy bajo,no obtiene descuento")    