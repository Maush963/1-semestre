def mes(meses, mesi, mesf, diai, diaf):
    inter = []
    for cont in meses:
        for info in cont:
            if mesf == mesi and info[0] == diaf + 1:
                break
            if info[1] == mesi and info[0] >= diai:
                inter.append(info)
            if mesf >= info[1] > mesi:
                inter.append(info)
                if info[0] == diaf and info[1] == mesf:
                    break
    return inter


def max_y_min(intervalo, mesi, mesf):
    mlista = []
    for info in range(mesi, mesf + 1):
        lista = []
        for cont in intervalo:
            if info == cont[1]:
                lista.append(cont[0])
        mlista.append([min(lista), max(lista), info])
    print("Min,Max,Mes", mlista)
    return mlista


def quitar_intervalo(intervalo, mlista, mesi, mesf):
    inter = intervalo
    cond = 1
    pase = False
    while cond == 1:
        cond = int(input("Quieres quitar un día del intervalo? si(1), no(0): "))
        while 1 != cond != 0:
            cond = int(input(f"Eso no es valido, escoja para 1 si y 0 para no: "))
        if cond == 0:
            break
        mesq = int(input("En que MES esta el día que quieres quitar?: "))
        diaq = int(input("Cuál es el DÍA que quieres quitar?: "))
        for c in mlista:
            if (c[1] >= diaq >= c[0]) and (mesq == c[2]) and (mesi <= mesq <= mesf):
                pase = True
        if not pase:
            print("Esto no se puede, inténtelo de nuevo")
        for i in inter:
            if diaq == i[0] and mesq == i[1]:
                inter.remove(i)
                print(inter)
    return inter


def asistencia(intervalo, mlista, mesi, mesf):
    print("\n")
    cantusuarios = int(input("Digite la cantidad de usuarios que asistirán a la reunion: "))
    for i in intervalo:
        i[2] = cantusuarios
    print("\n")

    for i in range(cantusuarios):
        cont = i
        mest = 0
        diat = 0
        asis = 1
        pase = False
        while asis == 1:
            asis = int(input(f"¿Hay algún día que el usuario {i + 1} no pueda asistir ?\t si(1) , no(0): "))
            while 1 != asis != 0:
                asis = int(input(f"Eso no es valido, escoja para 1 si y 0 para no: "))
            if asis == 0:
                break
            quitar_asistencia_mes = int(input("¿En que MES esta el día que no puede asistir?: "))
            quitar_asistencia_dia = int(input("¿Cuál es el DÍA que no puede asistir?: "))
            if cont > i and (mest == quitar_asistencia_mes and diat == quitar_asistencia_dia):
                print("No se puede quitar el mismo día dos veces para el mismo usuario")
            else:
                for c in mlista:
                    if (c[1] >= quitar_asistencia_dia >= c[0]) and (quitar_asistencia_mes == c[2]) and \
                            (mesi <= quitar_asistencia_mes <= mesf):
                        pase = True
                        for j in intervalo:
                            if quitar_asistencia_dia == j[0] and quitar_asistencia_mes == j[1]:
                                info = ((j[2]) - 1)
                                j[2] = info
                                print("[Día, Mes ,Usuarios/día]\n", f"   {j}   ", "\n\n")
            mest = quitar_asistencia_mes
            diat = quitar_asistencia_dia
            cont += 1
            if not pase:
                print("Esto no se puede, inténtelo de nuevo")
        print("\n")


def dia_asistencia(intervalo):
    print("Estos son los mejores días para su junta:\n")
    for i in intervalo:
        if i[2] >= 2:
            print(f"Día-{i[0]},  Mes-{i[1]},  Asis-{i[2]}")
    print("\nLos días que no aparecen tienen menos de dos asistentes")


def es_num(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False


def main():
    usuariosd = 0
    print("\n___________!Bienvenido a Maulendario!____________\n"
          "|                                               |\n"
          "|                 (╯°□°）╯︵ ┻━┻                 |\n"
          "_________________________________________________\n"
          "    Con este programa podrá agendar una junta    \n"
          "    Solo son validos números para las fechas     \n"
          "             Para realizar su junta              \n")

    mesi = (input('Digite el mes inicial: '))
    while not es_num(mesi):
        mesi = (input('Ese no es un valor valido, inténtelo de nuevo: '))
    mesi = int(mesi)
    while mesi < 1 or mesi > 12:
        print("Esta no es una expresión valida")
        mesi = int(input('Digite el mes final una vez más: '))

    diai = (input('Digite el día inicial: '))
    while not es_num(diai):
        diai = (input('Ese no es un valor valido, inténtelo de nuevo: '))
    diai = int(diai)
    while diai < 1 or diai > 31:
        print("Esta no es una expresión valida")
        diai = int(input('Digite el día inicial una vez más: '))

    print("\n")
    mesf = (input('Digite el mes final: '))
    while not es_num(mesf):
        mesf = (input('Ese no es un valor valido, inténtelo de nuevo: '))
    mesf = int(mesf)
    while mesf < mesi:
        mesf = int(input("El mes final no puede ser menor al inicial, inténtelo de nuevo: "))
    while mesf < 1 or mesf > 12:
        print("Esta no es una expresión valida")
        mesf = int(input('Digite el mes final una vez más: '))

    diaf = (input('Digite el día final: '))

    while not es_num(diaf):
        diaf = (input('Ese no es un valor valido, inténtelo de nuevo: '))
    diaf = int(diaf)
    while diaf < 1 or diaf > 31:
        print("Esta no es una expresión valida")
        diaf = int(input('Digite el día final una vez más: '))
    while (diaf < diai) and (mesi == mesf):
        print("Esta no es una expresión valida")
        diaf = int(input('Digite el día final una vez más: '))

    while (diaf > 30) and (mesf == 4) or (diaf > 30) and (mesf == 6) or (diaf > 30) and (mesf == 9) or \
            (diaf > 30) and (mesf == 11):
        print("El mes final es de 30 días, no puede ser mayor a esto")
        diaf = int(input('Digite el día final una vez más: '))

    while (diaf > 28) and (mesf == 2):
        print("El mes final es de 28 días, no puede ser mayor a esto")
        diaf = int(input('Digite el día final una vez más: '))
    print("\n")
    meses = [[[1, 1, usuariosd], [2, 1, usuariosd], [3, 1, usuariosd], [4, 1, usuariosd], [5, 1, usuariosd],
              [6, 1, usuariosd], [7, 1, usuariosd], [8, 1, usuariosd], [9, 1, usuariosd], [10, 1, usuariosd],
              [11, 1, usuariosd], [12, 1, usuariosd], [13, 1, usuariosd], [14, 1, usuariosd], [15, 1, usuariosd],
              [16, 1, usuariosd], [17, 1, usuariosd], [18, 1, usuariosd], [19, 1, usuariosd], [20, 1, usuariosd],
              [21, 1, usuariosd], [22, 1, usuariosd], [23, 1, usuariosd], [24, 1, usuariosd], [25, 1, usuariosd],
              [26, 1, usuariosd], [27, 1, usuariosd], [28, 1, usuariosd], [29, 1, usuariosd], [30, 1, usuariosd],
              [31, 1, usuariosd]],
             [[1, 2, usuariosd], [2, 2, usuariosd], [3, 2, usuariosd], [4, 2, usuariosd], [5, 2, usuariosd],
              [6, 2, usuariosd], [7, 2, usuariosd], [8, 2, usuariosd], [9, 2, usuariosd], [10, 2, usuariosd],
              [11, 2, usuariosd], [12, 2, usuariosd], [13, 2, usuariosd], [14, 2, usuariosd], [15, 2, usuariosd],
              [16, 2, usuariosd], [17, 2, usuariosd], [18, 2, usuariosd], [19, 2, usuariosd], [20, 2, usuariosd],
              [21, 2, usuariosd], [22, 2, usuariosd], [23, 2, usuariosd], [24, 2, usuariosd], [25, 2, usuariosd],
              [26, 2, usuariosd], [27, 2, usuariosd], [28, 2, usuariosd]],
             [[1, 3, usuariosd], [2, 3, usuariosd], [3, 3, usuariosd], [4, 3, usuariosd], [5, 3, usuariosd],
              [6, 3, usuariosd], [7, 3, usuariosd], [8, 3, usuariosd], [9, 3, usuariosd], [10, 3, usuariosd],
              [11, 3, usuariosd], [12, 3, usuariosd], [13, 3, usuariosd], [14, 3, usuariosd], [15, 3, usuariosd],
              [16, 3, usuariosd], [17, 3, usuariosd], [18, 3, usuariosd], [19, 3, usuariosd], [20, 3, usuariosd],
              [21, 3, usuariosd], [22, 3, usuariosd], [23, 3, usuariosd], [24, 3, usuariosd], [25, 3, usuariosd],
              [26, 3, usuariosd], [27, 3, usuariosd], [28, 3, usuariosd], [29, 3, usuariosd], [30, 3, usuariosd],
              [31, 3, usuariosd]],
             [[1, 4, usuariosd], [2, 4, usuariosd], [3, 4, usuariosd], [4, 4, usuariosd], [5, 4, usuariosd],
              [6, 4, usuariosd], [7, 4, usuariosd], [8, 4, usuariosd], [9, 4, usuariosd], [10, 4, usuariosd],
              [11, 4, usuariosd], [12, 4, usuariosd], [13, 4, usuariosd], [14, 4, usuariosd], [15, 4, usuariosd],
              [16, 4, usuariosd], [17, 4, usuariosd], [18, 4, usuariosd], [19, 4, usuariosd], [20, 4, usuariosd],
              [21, 4, usuariosd], [22, 4, usuariosd], [23, 4, usuariosd], [24, 4, usuariosd], [25, 4, usuariosd],
              [26, 4, usuariosd], [27, 4, usuariosd], [28, 4, usuariosd], [29, 4, usuariosd], [30, 4, usuariosd],
              ],
             [[1, 5, usuariosd], [2, 5, usuariosd], [3, 5, usuariosd], [4, 5, usuariosd], [5, 5, usuariosd],
              [6, 5, usuariosd], [7, 5, usuariosd], [8, 5, usuariosd], [9, 5, usuariosd], [10, 5, usuariosd],
              [11, 5, usuariosd], [12, 5, usuariosd], [13, 5, usuariosd], [14, 5, usuariosd], [15, 5, usuariosd],
              [16, 5, usuariosd], [17, 5, usuariosd], [18, 5, usuariosd], [19, 5, usuariosd], [20, 5, usuariosd],
              [21, 5, usuariosd], [22, 5, usuariosd], [23, 5, usuariosd], [24, 5, usuariosd], [25, 5, usuariosd],
              [26, 5, usuariosd], [27, 5, usuariosd], [28, 5, usuariosd], [29, 5, usuariosd], [30, 5, usuariosd],
              [31, 5, usuariosd]],
             [[1, 6, usuariosd], [2, 6, usuariosd], [3, 6, usuariosd], [4, 6, usuariosd], [5, 6, usuariosd],
              [6, 6, usuariosd], [7, 6, usuariosd], [8, 6, usuariosd], [9, 6, usuariosd], [10, 6, usuariosd],
              [11, 6, usuariosd], [12, 6, usuariosd], [13, 6, usuariosd], [14, 6, usuariosd], [15, 6, usuariosd],
              [16, 6, usuariosd], [17, 6, usuariosd], [18, 6, usuariosd], [19, 6, usuariosd], [20, 6, usuariosd],
              [21, 6, usuariosd], [22, 6, usuariosd], [23, 6, usuariosd], [24, 6, usuariosd], [25, 6, usuariosd],
              [26, 6, usuariosd], [27, 6, usuariosd], [28, 6, usuariosd], [29, 6, usuariosd], [30, 6, usuariosd],
              ],
             [[1, 7, usuariosd], [2, 7, usuariosd], [3, 7, usuariosd], [4, 7, usuariosd], [5, 7, usuariosd],
              [6, 7, usuariosd], [7, 7, usuariosd], [8, 7, usuariosd], [9, 7, usuariosd], [10, 7, usuariosd],
              [11, 7, usuariosd], [12, 7, usuariosd], [13, 7, usuariosd], [14, 7, usuariosd], [15, 7, usuariosd],
              [16, 7, usuariosd], [17, 7, usuariosd], [18, 7, usuariosd], [19, 7, usuariosd], [20, 7, usuariosd],
              [21, 7, usuariosd], [22, 7, usuariosd], [23, 7, usuariosd], [24, 7, usuariosd], [25, 7, usuariosd],
              [26, 7, usuariosd], [27, 7, usuariosd], [28, 7, usuariosd], [29, 7, usuariosd], [30, 7, usuariosd],
              [31, 7, usuariosd]],
             [[1, 8, usuariosd], [2, 8, usuariosd], [3, 8, usuariosd], [4, 8, usuariosd], [5, 8, usuariosd],
              [6, 8, usuariosd], [7, 8, usuariosd], [8, 8, usuariosd], [9, 8, usuariosd], [10, 8, usuariosd],
              [11, 8, usuariosd], [12, 8, usuariosd], [13, 8, usuariosd], [14, 8, usuariosd], [15, 8, usuariosd],
              [16, 8, usuariosd], [17, 8, usuariosd], [18, 8, usuariosd], [19, 8, usuariosd], [20, 8, usuariosd],
              [21, 8, usuariosd], [22, 8, usuariosd], [23, 8, usuariosd], [24, 8, usuariosd], [25, 8, usuariosd],
              [26, 8, usuariosd], [27, 8, usuariosd], [28, 8, usuariosd], [29, 8, usuariosd], [30, 8, usuariosd],
              [31, 8, usuariosd]],
             [[1, 9, usuariosd], [2, 9, usuariosd], [3, 9, usuariosd], [4, 9, usuariosd], [5, 9, usuariosd],
              [6, 9, usuariosd], [7, 9, usuariosd], [8, 9, usuariosd], [9, 9, usuariosd], [10, 9, usuariosd],
              [11, 9, usuariosd], [12, 9, usuariosd], [13, 9, usuariosd], [14, 9, usuariosd], [15, 9, usuariosd],
              [16, 9, usuariosd], [17, 9, usuariosd], [18, 9, usuariosd], [19, 9, usuariosd], [20, 9, usuariosd],
              [21, 9, usuariosd], [22, 9, usuariosd], [23, 9, usuariosd], [24, 9, usuariosd], [25, 9, usuariosd],
              [26, 9, usuariosd], [27, 9, usuariosd], [28, 9, usuariosd], [29, 9, usuariosd], [30, 9, usuariosd],
              ],
             [[1, 10, usuariosd], [2, 10, usuariosd], [3, 10, usuariosd], [4, 10, usuariosd], [5, 10, usuariosd],
              [6, 10, usuariosd], [7, 10, usuariosd], [8, 10, usuariosd], [9, 10, usuariosd], [10, 10, usuariosd],
              [11, 10, usuariosd], [12, 10, usuariosd], [13, 10, usuariosd], [14, 10, usuariosd], [15, 10, usuariosd],
              [16, 10, usuariosd], [17, 10, usuariosd], [18, 10, usuariosd], [19, 10, usuariosd], [20, 10, usuariosd],
              [21, 10, usuariosd], [22, 10, usuariosd], [23, 10, usuariosd], [24, 10, usuariosd], [25, 10, usuariosd],
              [26, 10, usuariosd], [27, 10, usuariosd], [28, 10, usuariosd], [29, 10, usuariosd], [30, 10, usuariosd],
              [31, 10, usuariosd]],
             [[1, 11, usuariosd], [2, 11, usuariosd], [3, 11, usuariosd], [4, 11, usuariosd], [5, 11, usuariosd],
              [6, 11, usuariosd], [7, 11, usuariosd], [8, 11, usuariosd], [9, 11, usuariosd], [10, 11, usuariosd],
              [11, 11, usuariosd], [12, 11, usuariosd], [13, 11, usuariosd], [14, 11, usuariosd], [15, 11, usuariosd],
              [16, 11, usuariosd], [17, 11, usuariosd], [18, 11, usuariosd], [19, 11, usuariosd], [20, 11, usuariosd],
              [21, 11, usuariosd], [22, 11, usuariosd], [23, 11, usuariosd], [24, 11, usuariosd], [25, 11, usuariosd],
              [26, 11, usuariosd], [27, 11, usuariosd], [28, 11, usuariosd], [29, 11, usuariosd], [30, 11, usuariosd],
              ],
             [[1, 12, usuariosd], [2, 12, usuariosd], [3, 12, usuariosd], [4, 12, usuariosd], [5, 12, usuariosd],
              [6, 12, usuariosd], [7, 12, usuariosd], [8, 12, usuariosd], [9, 12, usuariosd], [10, 12, usuariosd],
              [11, 12, usuariosd], [12, 12, usuariosd], [13, 12, usuariosd], [14, 12, usuariosd], [15, 12, usuariosd],
              [16, 12, usuariosd], [17, 12, usuariosd], [18, 12, usuariosd], [19, 12, usuariosd], [20, 12, usuariosd],
              [21, 12, usuariosd], [22, 12, usuariosd], [23, 12, usuariosd], [24, 12, usuariosd], [25, 12, usuariosd],
              [26, 12, usuariosd], [27, 12, usuariosd], [28, 12, usuariosd], [29, 12, usuariosd], [30, 12, usuariosd],
              [31, 12, usuariosd]]
             ]

    intervalo = mes(meses, mesi, mesf, diai, diaf)
    print(f"\nEste es el intervalo que escogió:\n{intervalo}\n")
    mlista = max_y_min(intervalo, mesi, mesf)
    quitar_intervalo(intervalo, mlista, mesi, mesf)
    asistencia(intervalo, mlista, mesi, mesf)
    dia_asistencia(intervalo)


main()
