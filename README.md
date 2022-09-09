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


#primero le voy a pedir al usuario que digite el primer y ultimo día del intervalo de tiempo
#que quiere para hacer la reunión.
"""
Primero tengo que saber que tan grande va a ser el intervalo de tiempo para su reunion, cuales son los dias posibles para realizarla,
para esto pregunto directamente el dia inicial y el dia final.
"""

#funcion para sacar el tiempo de intervalo entre la fecha inicial y la final, es del mismo año.
def intervalo():
    mesi=int(input("Digite el mes de la fecha inicial: "))
    diai=int(input("Digite el día de la fecha inicial: "))
    mesf=int(input("Digite el mes de la fecha final:  "))
    diaf=int(input("Digite el día de la fecha final:  "))
    mesc=mesi
    guard=31
    intervalo=0
#En estos ifs me aseguro de que sea real la fecha 
    if (diai>31 or diai<0 or diaf>31 or diaf<0):
        print("No esta dando una fecha real")
        
    if (mesi>12 or mesi<0 or mesf>12 or mesf<0):
        print("No esta dando una fecha real")
        
#aqui me aseguro de que no este en el mismo mes el día digitado.
    if (mesi==mesf):
        intervalo=diaf-diai
        if (diai>diaf):
           print("Esto no es posible: ")
#si no esta en el mismo mes, se le suman los dias que se requieren.        
    else:
        while (mesc<mesf):
            mesc=mesc+1
            intervalo=intervalo+guard
        
        diai=diai-31
        intervalo=intervalo+diaf+diai

    return intervalo

print(f"Este es el intervalo: {intervalo()} días")

tiempo = Intervalo()


print("Perfecto, ahora los usuarios tendran que poner las fechas disponibles que tiene cada uno")


usuarios=int(input("Cuantos usuarios van a utilizar el programa?"))

#preguntandole a los usuarios que días tienen disponibles para poder asisitir a la reunion.
def fusuarios ():
    asistencia=int(input("puede asistir a la reunion? si=1 no=0: "))
    if (asistencia==False):
        print("No puede asistir a la reunion")
    elif (asistencia==True):
        while (asistencia==True):
            num=int(input(f"¿Que día puede asistir a la reunion? considere que la reunion es en {tiempo} dias"))
            asistencia=bool(input("Puede asistir otro día a la reunion? si=1 no=0"))
            print(num)

    
    
while (usuarios!=0):
    usuarios=usuarios-1
    print ("a")
    fusuarios()
    
def horas():
    canth=int(input("Cuantas horas quiere poner para la reunion?"))
    while(canth>0):
        print("\nDigite las posibles horas para la reunión")
        hora1=int(input("hora:"))
        canth=canth-1
        print(hora1)
        
horas()

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
