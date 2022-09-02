#primero le voy a pedir al usuario que digite el primer y ultimo día del intervalo de tiempo
#que quiere para hacer la reunión.
"""
Primero tengo que saber que tan grande va a ser el intervalo de tiempo para su reunion, cuales son los dias posibles para realizarla,
para esto pregunto directamente el dia inicial y el dia final.
"""

def Intervalo():
    
    print("Entre que días quiere realizar la reunión.")
    diai=int(input("Digite el primer día de este intervalo: "))
    diaf=int(input("Digite el último día de este intervalo: "))
    #verifico si los números que dio esta dentro de los días del mes
    if (diai>31 or diai==0 or diaf>31 or diaf==0):
        print("No esta dando un día real")
    else:
        _=0
        val=0
#si el primer dia es mayor corresponde al mes siguente, por lo que se hace el siguente calculo.
        if(diai>diaf):
            _=31-diai
            val=_+diaf
            print(f"Este es el intervalo de días de su reunion {val}")
#si esta dentro del mismo mes, simplemente se le resta primer dia al ultimo.
        elif(diai<diaf):
            val=diaf-diai
            print(f"Este es el intervalo de días de su reunion {val}")
    return val

tiempo = Intervalo()


print("Perfecto, ahora los usuarios tendran que poner las fechas disponibles que tiene cada uno")


usuarios=int(input("Cuantos usuarios van a utilizar el programa?"))

#preguntandole a los usuarios que días tienen disponibles para poder asisitir a la reunion.
def fusuarios ():
    asistencia=bool(input("puede asistir a la reunion? si=1 no=0: "))
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
    
def horas()
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
