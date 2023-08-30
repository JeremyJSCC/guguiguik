colones = 0 
dolares = 0
euros = 0
yenes = 0
for i in range (2):
    print("""
(1) convertir a  dolares
(2) convertir a  euros
(3) convertir a yenes
""")
    cambio_cliente = int(input("ingrese el tipo de cambio a realizar: "))
    monto_cliente = int(input("ingrese cuantos colones desea combertir: "))
    cambio = int(input("ingrese el tipo de cambio: "))
    if cambio_cliente == 1:
        multiplicacion =  monto_cliente / cambio
        print("el monto en colones es de ",monto_cliente, "en dolares seria",multiplicacion)
        colones = colones + monto_cliente
        dolares = dolares + multiplicacion
    if cambio_cliente == 2:
        multiplicacion =  monto_cliente / cambio
        print("el monto en colones es de ",monto_cliente, "en euros seria",multiplicacion)
        colones = colones + monto_cliente
        euros = euros + multiplicacion
    if cambio_cliente == 3:
        multiplicacion =  monto_cliente / cambio
        print("el monto en colones es de ",monto_cliente, "en yenes seria",multiplicacion)
        colones = colones + monto_cliente
        yenes = yenes + multiplicacion
print("la totalidad en colones es de: ",colones)
print("la totalidad en dolares es de: ",dolares)
print(" la toralidad es euros es de ", euros)
print(" la toralidad es yenes es de ", yenes)