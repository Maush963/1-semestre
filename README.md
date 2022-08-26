# 1-semestre
Pensamiento computacional para ingeniería
Calendario Equipo
Como alumno del Tec, he notado que hay dos elementos esenciales, que debes de tomar en cuenta a la hora de estudiar, la primera es primordial, la organización, 
afecta directamente tu día a día y la segunda es el trabajo en equipo. Por eso es que opte por crear un calendario, un calendario puede ser una herramienta muy 
útil para poder realizar tus tareas en tiempo y forma.
Para relacionar el trabajo en equipo con este concepto, voy a hacer que el calendario tenga la opción de poder juntar la información de múltiples usuarios, 
de esta forma los usuarios podrán ingresar los horarios que tengan disponibles para poder trabajar en equipo, después de digitar varias opciones, la computadora 
va a buscar cuales son las mejores opciones para poder realizar un trabajo en equipo, puede que no coincidan todos los participantes en una hora, pero de todas 
formas el algoritmo indicará cual es la hora en la que más personas están disponibles.

Preguntar al organizador entre que días quiere hacer una reunión
Preguntar al organizador entre qué hora quiere que sea la reunión
Preguntar el número de usuarios (dependiendo del número de usuarios va a ser la cantidad de veces que se repitan las mismas preguntas)
Preguntar a los usuarios entre los días previamente escogidos por usuario1, que horas tienen disponibles para la junta.
Si cantidad de usuarios que dijeron que si>50 y <60%
Devolver las horas en las que un 50% de los participantes puedan asistir
Y decir la cantidad de participantes
Si cantidad de usuarios que dijeron que si>75 y <80%
Devolver las horas en las que un 75% de los participantes puedan asistir
Y decir la cantidad de participantes
Si cantidad de usuarios que dijeron que si>90%
Devolver las horas en las que un 90% de los participantes puedan asistir
Y decir la cantidad de participantes




Segundo Avance (operadores)
#primero le voy a pedir al usuario que digite el primer y ultimo día del intervalo de tiempo
#que quiere para hacer la reunión.

print("Entre que días quiere realizar la reunión.")
diai=int(input("Digite el primer día de este intervalo: "))
diaf=int(input("Digite el último día de este intervalo: "))
intervalo=diaf-diai
print(f"Cantidad de días de intervalo: {intervalo}")
print("\nDigite las posibles horas para la reunión")
hora1=int(input("Primera hora"))
usuarios=int(("\nDigite el número de usuarios"))

print("Perfecto, ahora los usuarios tendran que poner las fechas disponibles que tiene cada uno")


cantidad_si=int(("\nIngrese la cantidad de usuarios que si pueden en n fecha"))
if (cantidad_si>(usuarios*.6))
print("la cantidad de usuarios que digeron que si fueron más del 60%")
else
if (cantidad_si>(usuarios*.8))
print("la cantidad de usuarios que digeron que si fueron más del 80%")
else
if (cantidad_si>(usuarios*1))
print("la cantidad de usuarios que digeron que si fue el 100%")
else
print("parece que la mayoría de los usuarios no pueden en un día similar")
