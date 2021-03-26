equipo = [["Guadalajara",
          "Primera dicisión",
          "Vicor Manuel Vucetich",
          "25",
          "5",
          "100 MDD",
          [["José Antonio Rodríguez","Portero"],
           ["Cristian Calderón","Defensa"],
           ["Isaác Brizuela","Medio"],
           ["José Juan Macías","Delantero"]]]]
plantilla = []
categoria = []

seguir = True

while seguir:
    
    print("Selecciona una de las siguientes opciones:",
          "A. Agregar equipos de futbol",
          "B. Agregar plantilla",
          "C. Agregar catergoría",
          "D. Búsqueda de equipo",
          "E. Busqueda de jugador",
          "F. Reporte de equipos en una división seleccionada",
          sep="\n")
    menu = (input("Opcion: "))

    if menu == "A":
        agregar = True
        i = len(equipo)
        equipo.append([])
        equipo[i].append(input("Nombre: "))
        equipo[i].append(input("Disivion: "))
        equipo[i].append(input("Director Técnico: "))
        equipo[i].append(input("Puntos: "))
        equipo[i].append(input("Campeonatos: "))
        equipo[i].append(input("Valor del equipo: "))
        j = len(equipo[i])
        equipo[i].append([])
        print("Jugadores")
        x=0
        while agregar:
            equipo[i][j].append([])
            equipo[i][j][x].append(input("Jugador: "))
            equipo[i][j][x].append(input("Rol: "))
            x = x+1
            print(equipo[i])
            continuar = input("Desea agregar otro jugador(Y o N): ")
            if continuar == "N": agregar = False

    if menu == "B":
        i = len(plantilla)
        plantilla.append([])
        plantilla[i].append(input("Nombre: "))
        plantilla[i].append(input("Posición: "))
        plantilla[i].append(input("Edad: "))
        plantilla[i].append(input("Equipo: "))
        plantilla[i].append(input("División: "))
        plantilla[i].append(input("Valor: "))
        plantilla[i].append(input("Nacionalidad: "))
        plantilla[i].append(input("Peso: "))
        plantilla[i].append(input("Estatura: "))

    if menu == "C":
        i = len(categoria)
        categoria.append([])
        categoria[i].append(input("Numero: "))
        categoria[i].append(input("Nombre de Categoría: "))

    if menu == "D":
        buscar = input("Equipo: ")
        for equi in equipo:
            if equi[0] == buscar:
                print("Nombre: ",equi[0])
                print("Division: ",equi[1])
                print("Director Técnico: ",equi[2])
                print("Puntos: ",equi[3])
                print("Campeonatos: ",equi[4])
                print("Valor del equipo: ",equi[5])
                print("Jugadores: ")
                for jug in equi[6]:
                    print(jug[0], " ", jug[1])
               
    
    if menu == "E":
        buscar = input("Jugador: ")
        for plan in plantilla:
            if plan[0] == buscar:
                print("Nombre: ",plan[0])
                print("Posicion: ",plan[1])
                print("Equipo: ",plan[3])
                print("Valor: ",plan[5])
                print("Edad: ",plan[2])
                print("Nacionalidad: ",plan[6])
                print("Peso: ",plan[7])
                print("Estatura: ",plan[8])
    
    if menu == "F":
        buscar = input("Division: ")
        for cat in categoria:
            if cat[1] == buscar:
                for equi in equipo:
                    if equi[1]==buscar:
                         print(cat[0], " ",cat[1], " ", equi[0], " ", equi[5])
    
    terminar = input("Desea terminar el programa(Y o N): ")
    if terminar == "Y":
        seguir = False
    print(equipo)
print("Fin del programa")