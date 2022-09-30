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
    dian=int(intput("Hay alguna excepción dentro del intervalo de tiempo que introdujo? si=1 no=0"))
    if dian==1:
        
        



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

usuariosd=0
def info():
    
    usuariosd=(input("Usted puede este día?"))
    infor=[[1,1,usuariosd],[2,1,usuariosd],[3,1,usuariosd],[4,1,usuariosd],[5,1,usuariosd],[6,1,usuariosd],[7,1,usuariosd],[8,1,usuariosd],[9,1,usuariosd],[10,1,usuariosd],
           [11,1,usuariosd],[12,1,usuariosd],[13,1,usuariosd],[14,1,usuariosd],[15,1,usuariosd],[16,1,usuariosd],[17,1,usuariosd],[18,1,usuariosd],[19,1,usuariosd],[20,1,usuariosd],
           [22,1,usuariosd],[22,1,usuariosd],[23,1,usuariosd],[24,1,usuariosd],[25,1,usuariosd],[26,1,usuariosd],[27,1,usuariosd],[28,1,usuariosd],[29,1,usuariosd],[30,1,usuariosd],
           [31,1,usuariosd]
           [1,2,usuariosd],[2,2,usuariosd],[3,2,usuariosd],[4,2,usuariosd],[5,2,usuariosd],[6,2,usuariosd],[7,2,usuariosd],[8,2,usuariosd],[9,2,usuariosd],[10,2,usuariosd],
           [11,2,usuariosd],[12,2,usuariosd],[13,2,usuariosd],[14,2,usuariosd],[15,2,usuariosd],[16,2,usuariosd],[17,2,usuariosd],[18,2,usuariosd],[19,2,usuariosd],[20,2,usuariosd],
           [22,2,usuariosd],[22,2,usuariosd],[23,2,usuariosd],[24,2,usuariosd],[25,2,usuariosd],[26,2,usuariosd],[27,2,usuariosd],[28,2,usuariosd]
           [1,3,usuariosd],[2,3,usuariosd],[3,3,usuariosd],[4,3,usuariosd],[5,3,usuariosd],[6,3,usuariosd],[7,3,usuariosd],[8,3,usuariosd],[9,3,usuariosd],[10,3,usuariosd],
           [11,3,usuariosd],[12,3,usuariosd],[13,3,usuariosd],[14,3,usuariosd],[15,3,usuariosd],[16,3,usuariosd],[17,3,usuariosd],[18,3,usuariosd],[19,3,usuariosd],[20,3,usuariosd],
           [22,3,usuariosd],[22,3,usuariosd],[23,3,usuariosd],[24,3,usuariosd],[25,3,usuariosd],[26,3,usuariosd],[27,3,usuariosd],[28,3,usuariosd],[29,3,usuariosd],[30,3,usuariosd],
           [31,3,usuariosd]
           [1,4,usuariosd],[2,4,usuariosd],[3,4,usuariosd],[4,4,usuariosd],[5,4,usuariosd],[6,4,usuariosd],[7,4,usuariosd],[8,4,usuariosd],[9,4,usuariosd],[10,4,usuariosd],
           [11,4,usuariosd],[12,4,usuariosd],[13,4,usuariosd],[14,4,usuariosd],[15,4,usuariosd],[16,4,usuariosd],[17,4,usuariosd],[18,4,usuariosd],[19,4,usuariosd],[20,4,usuariosd],
           [22,4,usuariosd],[22,4,usuariosd],[23,4,usuariosd],[24,4,usuariosd],[25,4,usuariosd],[26,4,usuariosd],[27,4,usuariosd],[28,4,usuariosd],[29,4,usuariosd],[30,4,usuariosd],
           [31,4,usuariosd]
           [1,5,usuariosd],[2,5,usuariosd],[3,5,usuariosd],[4,5,usuariosd],[5,5,usuariosd],[6,5,usuariosd],[7,5,usuariosd],[8,5,usuariosd],[9,5,usuariosd],[10,5,usuariosd],
           [11,5,usuariosd],[12,5,usuariosd],[13,5,usuariosd],[14,5,usuariosd],[15,5,usuariosd],[16,5,usuariosd],[17,5,usuariosd],[18,5,usuariosd],[19,5,usuariosd],[20,5,usuariosd],
           [22,5,usuariosd],[22,5,usuariosd],[23,5,usuariosd],[24,5,usuariosd],[25,5,usuariosd],[26,5,usuariosd],[27,5,usuariosd],[28,5,usuariosd],[29,5,usuariosd],[30,5,usuariosd],
           [31,5,usuariosd]
           [1,6,usuariosd],[2,6,usuariosd],[3,6,usuariosd],[4,6,usuariosd],[5,6,usuariosd],[6,6,usuariosd],[7,6,usuariosd],[8,6,usuariosd],[9,6,usuariosd],[10,6,usuariosd],
           [11,6,usuariosd],[12,6,usuariosd],[13,6,usuariosd],[14,6,usuariosd],[15,6,usuariosd],[16,6,usuariosd],[17,6,usuariosd],[18,6,usuariosd],[19,6,usuariosd],[20,6,usuariosd],
           [22,6,usuariosd],[22,6,usuariosd],[23,6,usuariosd],[24,6,usuariosd],[25,6,usuariosd],[26,6,usuariosd],[27,6,usuariosd],[28,6,usuariosd],[29,6,usuariosd],[30,6,usuariosd],
           [31,6,usuariosd]
           [1,7,usuariosd],[2,7,usuariosd],[3,7,usuariosd],[4,7,usuariosd],[5,7,usuariosd],[6,7,usuariosd],[7,7,usuariosd],[8,7,usuariosd],[9,7,usuariosd],[10,7,usuariosd],
           [11,7,usuariosd],[12,7,usuariosd],[13,7,usuariosd],[14,7,usuariosd],[15,7,usuariosd],[16,7,usuariosd],[17,7,usuariosd],[18,7,usuariosd],[19,7,usuariosd],[20,7,usuariosd],
           [22,7,usuariosd],[22,7,usuariosd],[23,7,usuariosd],[24,7,usuariosd],[25,7,usuariosd],[26,7,usuariosd],[27,7,usuariosd],[28,7,usuariosd],[29,7,usuariosd],[30,7,usuariosd],
           [31,7,usuariosd]
           [1,8,usuariosd],[2,8,usuariosd],[3,8,usuariosd],[4,8,usuariosd],[5,8,usuariosd],[6,8,usuariosd],[7,8,usuariosd],[8,8,usuariosd],[9,8,usuariosd],[10,8,usuariosd],
           [11,8,usuariosd],[12,8,usuariosd],[13,8,usuariosd],[14,8,usuariosd],[15,8,usuariosd],[16,8,usuariosd],[17,8,usuariosd],[18,8,usuariosd],[19,8,usuariosd],[20,8,usuariosd],
           [22,8,usuariosd],[22,8,usuariosd],[23,8,usuariosd],[24,8,usuariosd],[25,8,usuariosd],[26,8,usuariosd],[27,8,usuariosd],[28,8,usuariosd],[29,8,usuariosd],[30,8,usuariosd],
           [31,8,usuariosd]
           [1,9,usuariosd],[2,9,usuariosd],[3,9,usuariosd],[4,9,usuariosd],[5,9,usuariosd],[6,9,usuariosd],[7,9,usuariosd],[8,9,usuariosd],[9,9,usuariosd],[10,9,usuariosd],
           [11,9,usuariosd],[12,9,usuariosd],[13,9,usuariosd],[14,9,usuariosd],[15,9,usuariosd],[16,9,usuariosd],[17,9,usuariosd],[18,9,usuariosd],[19,9,usuariosd],[20,9,usuariosd],
           [22,9,usuariosd],[22,9,usuariosd],[23,9,usuariosd],[24,9,usuariosd],[25,9,usuariosd],[26,9,usuariosd],[27,9,usuariosd],[28,9,usuariosd],[29,9,usuariosd],[30,9,usuariosd],
           [31,9,usuariosd]
           [1,10,usuariosd],[2,10,usuariosd],[3,10,usuariosd],[4,10,usuariosd],[5,10,usuariosd],[6,10,usuariosd],[7,10,usuariosd],[8,10,usuariosd],[9,10,usuariosd],[10,10,usuariosd],
           [11,10,usuariosd],[12,10,usuariosd],[13,10,usuariosd],[14,10,usuariosd],[15,10,usuariosd],[16,10,usuariosd],[17,10,usuariosd],[18,10,usuariosd],[19,10,usuariosd],[20,10,usuariosd],
           [22,10,usuariosd],[22,10,usuariosd],[23,10,usuariosd],[24,10,usuariosd],[25,10,usuariosd],[26,10,usuariosd],[27,10,usuariosd],[28,10,usuariosd],[29,10,usuariosd],[30,10,usuariosd],
           [31,10,usuariosd]
           [1,11,usuariosd],[2,11,usuariosd],[3,11,usuariosd],[4,11,usuariosd],[5,11,usuariosd],[6,11,usuariosd],[7,11,usuariosd],[8,11,usuariosd],[9,11,usuariosd],[10,11,usuariosd],
           [11,11,usuariosd],[12,11,usuariosd],[13,11,usuariosd],[14,11,usuariosd],[15,11,usuariosd],[16,11,usuariosd],[17,11,usuariosd],[18,11,usuariosd],[19,11,usuariosd],[20,11,usuariosd],
           [22,11,usuariosd],[22,11,usuariosd],[23,11,usuariosd],[24,11,usuariosd],[25,11,usuariosd],[26,11,usuariosd],[27,11,usuariosd],[28,11,usuariosd],[29,11,usuariosd],[30,11,usuariosd],
           [31,11,usuariosd]
           [1,12,usuariosd],[2,12,usuariosd],[3,12,usuariosd],[4,12,usuariosd],[5,12,usuariosd],[6,12,usuariosd],[7,12,usuariosd],[8,12,usuariosd],[9,12,usuariosd],[10,12,usuariosd],
           [11,12,usuariosd],[12,12,usuariosd],[13,12,usuariosd],[14,12,usuariosd],[15,12,usuariosd],[16,12,usuariosd],[17,12,usuariosd],[18,12,usuariosd],[19,12,usuariosd],[20,12,usuariosd],
           [22,12,usuariosd],[22,12,usuariosd],[23,12,usuariosd],[24,12,usuariosd],[25,12,usuariosd],[26,12,usuariosd],[27,12,usuariosd],[28,12,usuariosd],[29,12,usuariosd],[30,12,usuariosd],
           [31,12,usuariosd]
           ]
        

cantidad_si=int(("\nIngrese la cantidad de usuarios que si pueden en n fecha"))
if (cantidad_si>(usuarios*.6))
print("la cantidad de usuarios que digeron que si fueron más del 60%")
elif (cantidad_si>(usuarios*.8))
print("la cantidad de usuarios que digeron que si fueron más del 80%")
elif (cantidad_si>(usuarios*1))
print("la cantidad de usuarios que digeron que si fue el 100%")
else
print("parece que la mayoría de los usuarios no pueden en un día similar")
