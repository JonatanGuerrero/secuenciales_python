
#ejercicio1
cap_inv = float(input("Digite el capital invertido"))
ganancia = cap_inv * 0.02
print(f"la ganancia del capital invertido es: {ganancia}")


#ejercicio 2
salarioBasico = float(input("Digite el valor del salario"))
venta1 = float(input("Digite el valor de la primera venta"))
venta2 = float(input("Digite el valor de la segunda venta"))
venta3 = float(input("Digite el valor de la tercera venta"))
total_venta= venta1+venta2+venta3
comision=total_venta * 0.10
valorTotal = salarioBasico + comision
print(f"el vendedor recibirá {valorTotal}\n con unas comisiones de {comision}")


#ejercicio 3
totCompra=float(input("digite el total de la compra"))
dscto=totCompra*0.15
vlrPagar=totCompra-dscto
print(f"el total a pagar con descuento es: {vlrPagar}")

#ejercicio 4
nota1=float(input("digite la primera nota"))
nota2=float(input("digite la segunda nota"))
nota3=float(input("digite la tercera nota"))
examFinal=float(input("calificacion del examen final"))
trabFinal=float(input("calificacion del trabajo final"))
prom=(nota1+nota2+nota3)/3
ppar=prom*0.55
pef=examFinal*0.30
ptf=trabFinal*0.15
notaFinal=ppar+pef+ptf
print(f"la calificación final es: {notaFinal}")

#ejercicio 5
numHombres=float(input("digite el número de hombres"))
numMujeres=float(input("digite el número de mujeres"))
totAlum=numHombres + numMujeres
porcHombres=(numHombres * 100)/totAlum
porcMujeres=(numMujeres * 100)/totAlum
print(f"el porcentaje de hombres es: {porcHombres}\n"
      f"Y el porcentaje de mujeres es: {porcMujeres}")


#ejercicio 6
yearNaci=int(input("digite el año de nacimiento"))
yearAct=int(input("digite el año actual"))
edad=yearAct-yearNaci
print(f"la edad es: {edad}")

#PROBLEMAS PROPUESTOS
#1
pesos=float(input("Digite el valor en pesos"))
vlrDolar=float(input("Digite el valor valor del dolar hoy"))
vlrDolar =pesos/vlrDolar;
print(f"la conversión de $  {pesos}  a dolares es $  {vlrDolar}")

#2
Num=int(input("Digite un número"))

if Num > 0:
    num1 = Num * (-1)
    print(f"El valor absoluto de {Num} es: {num1}")
else:
    num1 = Num * (-1)
    print(f"El valor absoluto de {Num} es: {num1}")


#3
presion=float(input("Digite la presión"))
volumen=float(input("Digite el volumen"))
temperatura=float(input("Digite la temperatura"))
masa = (presion * volumen)/(0.37 * (temperatura+460))
print(f"La masa del aire es: {masa}")

#4
edad=int(input("Digite la edad"))
numPulsaciones=(220-edad)/10
print(f"El número de pulsaciones es {numPulsaciones}")

#5
salAnt=float(input("Digite su salario anterior"))
incremento=salAnt*0.25
salActual=salAnt+incremento
print(f"El nuevo salario es: {salActual}")


#6
presupuesto=float(input("Digite el presupuesto disponible"))
gin=presupuesto*0.4
presupuesto=presupuesto-gin
trau=presupuesto*0.3
presupuesto=presupuesto-trau
ped=presupuesto*0.3
presupuesto=presupuesto-ped
print(f"El presuúesto disponible para cada una de las áreas es:\n "
      f"Ginecologia: {gin}\n"
      f"Traumatologia: {trau}\n"
      f"Pedriatria: {ped}")

#7
producto=float(input("Ingrese el precio del articulo"))
gan=producto*0.30
producto=producto+gan
print(f"El valor del producto es: {producto}")


#8
cronoDia1=float(input("Digite el tiempo obtenido del lunes"))
cronoDia2=float(input("Digite el tiempo obtenido del miercoles"))
cronoDia3=float(input("Digite el tiempo obtenido del viernes"))

promCrono=(cronoDia1+cronoDia2+cronoDia3)/3
print(f"El promedio del tiempo recorrido en una semana es: {promCrono}")

#9
cantSocio1=float(input("Digite la cantidad a invertir del primer socio"))
cantSocio2=float(input("Digite la cantidad a invertir del segundo socio"))
cantSocio3=float(input("Digite la cantidad a invertir del tercer socio"))

totInvertido=cantSocio1+cantSocio2+cantSocio3
porcSocio1=cantSocio1*100/totInvertido
porcSocio2=cantSocio2*100/totInvertido
porcSocio3=cantSocio3*100/totInvertido

print(f"el porcentaje de inversion de los socios es: \n"
      f"Socio uno : {porcSocio1} % \n"
      f"Socio dos : {porcSocio2} % \n"
      f"Socio tres : {porcSocio3} & \n")

#10


print("Calificación de Matemáticas")
exaMath=float(input("Ingrese la nota del examen"))
notaTarea1=float(input("Ingrese la nota de la primera tarea"))
notaTarea2=float(input("Ingrese la nota de la segunda tarea"))
notaTarea3=float(input("Ingrese la nota de la tercera tarea"))
promNotas=(notaTarea1+notaTarea2+notaTarea3)/3
exaMath=exaMath*0.9
promNotas=promNotas*0.1
notFinal=exaMath+promNotas/2

print("Calificación de Física")
examFis=float(input("Ingrese la nota del examen"))
notaT1=float(input("Ingrese la nota de la primera tarea"))
notaT2=float(input("Ingrese la nota de la segunda tarea"))
promNot=(notaT1+notaT2)/2
examFis=examFis*0.8
promNot=promNot*0.20
notFin=examFis+promNot/2

print("Calificación de Química")
exaQuim=float(input("Ingrese la nota del examen"))
notaTar1=float(input("Ingrese la nota de la primera tarea"))
notaTar2=float(input("Ingrese la nota de la segunda tarea"))
notaTar3=float(input("Ingrese la nota de la tercera tarea"))
promNt=(notaTar1+notaTar2+notaTar3)/3
exaQuim=exaQuim*0.85
promNt=promNt*0.15
notaf=exaQuim+promNt/2
print(f"El promedio de la calificación de Matemáticas es: {notFinal}")
print(f"El promedio de la calificación de Física es: {notFin}")
print(f"El promedio de la calificación de Química es: {notaf}")