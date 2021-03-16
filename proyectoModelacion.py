DiccionarioIndices = {'CCS': 0,
                      'AUA': 1,
                      'CUR': 2,
                      'BON': 3,
                      'SDQ': 4,
                      'SXM': 5,
                      'SBH': 6,
                      'POS': 7,
                      'BGI': 8,
                      'PTP': 9,
                      'FDF': 10,
                      }

matrizAdyacenciaOriginal = [[0,    40,  35,  60, 180,   0,   0, 150, 180,   0,   0],
                            [40,    0,  15,  15,   0,  85,   0,   0,   0,	0,	 0],
                            [35,   15,   0,  15,   0,  80,	 0,   0,   0,	0,	 0],
                            [60,   15,  15,   0,   0,	0,	 0,   0,   0,   0,	 0],
                            [180,   0,   0,   0,   0,  50,	 0,   0,   0,   0,   0],
                            [0,    85,  80,   0,  50,	0,  45,  90,  70, 100,   0],
                            [0,     0,   0,   0,   0,  45,   0,   0,   0,  80,   0],
                            [150,   0,   0,   0,   0,  90,	 0,   0,  35,  80,	75],
                            [180,   0,   0,   0,   0,  70,	 0,  35,   0,	0,	 0],
                            [0,     0,   0,   0,   0, 100,  80,  80,   0,	0,	 0],
                            [0,	    0,   0,   0,   0,   0,   0,  75,   0,	0,	 0]]

matrizAdyacenciaMenorDistancia = [[0,   1,   1,   1,   1,   0,   0,   1,   1,   0,   0],
                                  [1,   0,   1,   1,   0,   1,   0,   0,   0,	0,	 0],
                                  [1,   1,   0,   1,   0,   1,	 0,   0,   0,	0,	 0],
                                  [1,   1,   1,   0,   0,   0,   0,   0,   0,   0,	 0],
                                  [1,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0],
                                  [0,   1,   1,   0,   1,	0,   1,   1,   1,   1,   0],
                                  [0,   0,   0,   0,   0,   1,   0,   0,   0,   1,   0],
                                  [1,   0,   0,   0,   0,   1,   0,   0,   1,   1,   1],
                                  [1,   0,   0,   0,   0,   1,	 0,   1,   0,	0,	 0],
                                  [0,   0,   0,   0,   0,   1,   1,   1,   0,	0,	 0],
                                  [0,	0,   0,   0,   0,   0,   0,   1,   0,	0,	 0]]

#     CODIGO, DIST MIN DESDE INICIO, PREDECESOR, VISITADO, REQUIERE VISA
matrizNodos = [['CCS', 999, None, False, False],
               ['AUA', 999, None, False, True],
               ['CUR', 999, None, False, True],
               ['BON', 999, None, False, True],
               ['SDQ', 999, None, False, True],
               ['SXM', 999, None, False, True],
               ['SBH', 999, None, False, False],
               ['POS', 999, None, False, False],
               ['BGI', 999, None, False, False],
               ['PTP', 999, None, False, False],
               ['FDF', 999, None, False, False]]


def quedanNodosSinVisitar():
    for nodo in matrizNodos:
        if(nodo[3] == False):
            return True
    return False

def nodoMenorDistancia():
    menorDistancia = 999
    indice = None
    for index, nodo in enumerate(matrizNodos):
        if(nodo[3] == False):
            if(nodo[1] <= menorDistancia):
                menorDistancia = nodo[1]
                indice = index
    return indice

def actualizarTabla(nodoActual):
    for index, distNodoAdyacente in enumerate(matrizAdyacencia[nodoActual]):
        if((distNodoAdyacente != 0) and (matrizNodos[index][3] == False) and (matrizNodos[nodoActual][1] + distNodoAdyacente < matrizNodos[index][1])):
            matrizNodos[index][1] = matrizNodos[nodoActual][1] + \
                distNodoAdyacente
            matrizNodos[index][2] = nodoActual
        matrizNodos[nodoActual][3] = True

def dijkstra():
    indiceNodoActual = None
    while quedanNodosSinVisitar():
        indiceNodoActual = nodoMenorDistancia()
        actualizarTabla(indiceNodoActual)

def calcularRuta():
    cadena = matrizNodos[destino][0]
    esteNodo = destino
    while(esteNodo != origen):
        esteNodo = matrizNodos[esteNodo][2]
        cadena = matrizNodos[esteNodo][0] + ' - ' + cadena
    print('\n \n ******************** RESULTADOS ********************')
    print('')
    if(option == '1'):
        print('RUTA MAS CORTA A TOMAR:')
        print(cadena)
        print('')
        destinos = cadena.split('-')
        indicesDestinos = []
        costo = 0
        for i in destinos:
            indicesDestinos.append(DiccionarioIndices[i.strip()])
        for i in range(len(indicesDestinos)-1):
            costo = costo + matrizAdyacenciaOriginal[indicesDestinos[i]][indicesDestinos[i+1]]
        print('COSTO TOTAL: $', costo)
    else:
        print('RUTA MAS ECONÓMICA A TOMAR:')
        print(cadena)
        print('')
        print('COSTO TOTAL: $', matrizNodos[destino][1])

# INICIO DE LA EJECUCION DEL PROGRAMA
runProgram = True
hasVisa = False

while(runProgram):
    #Preguntamos si el pasajero tiene visa
    print('Bienvenido ¿Usted posee Visa? (S/N)')
    option = input().upper()
    while(not(option == 'S' or option == 'N')):
        print('ERROR EN OPCIÓN INGRESADA, vuelva a ingresar la opción (S/N):')
        option = input().upper()
    #Si tiene visa marcamos como visitados los nodos que requieren visa
    if(option == 'S'):
        hasVisa = True
    else:
        for nodo in matrizNodos:
            if(nodo[4] == True):
                nodo[3] = True
        
    #Preguntamos que función del programa quiere utilizar
    print('Ingrese \n (1) Si desea obtener la ruta mas corta \n (2) Si desea obtener la ruta con el menor costo')
    option = input()
    while(not(option == '1' or option == '2')):
        print('ERROR EN OPCIÓN INGRESADA, vuelva a ingresar la opción (1)/(2):')
        option = input()
    if(option == '1'):
        matrizAdyacencia = matrizAdyacenciaMenorDistancia
    elif(option == '2'):
        matrizAdyacencia = matrizAdyacenciaOriginal

    #Preguntamos el codigo del aeropuerto de origen y verificamos si es válido
    print('Aeropuertos disponibles \n CCS: Caracas \n AUA: Aruba \n CUR: Curazao \n BON: Bonaire \n SDQ: Santo Domingo \n SXM: San Martín \n SBH: San Bartolomé \n POS: Puerto España (Trinidad) \n BGI: Barbados \n PTP: Point a Pitre (Guadalupe) \n FDF: Fort de France (Martinica) \n')
    print('Ingrese el código del aeropuerto origen:')
    origen = input().upper()
    while(not(origen in DiccionarioIndices)):
        print('ERROR EN CÓDIGO INGRESADO, vuelva a ingresar el código del aeropuerto origen:')
        origen = input().upper()
    origenCode = origen
    origen = DiccionarioIndices[origen]
    matrizNodos[origen][1] = 0
    matrizNodos[origen][3] = False

    #Preguntamos el codigo del aeropuerto de destino y verificamos si es válido
    print('Ingrese el código del aeropuerto destino:')
    destino = input().upper()
    checkDestino = True
    #Se chequeara el destino introducido hasta que esté entre los disponibles, no sea igual al origen 
    # y el estatus de visa del usuario concuerde con el necesario para el destino
    while(checkDestino):
        checkDestino = False
        if(destino == origenCode):
            checkDestino = True
            print('EL DESTINO DEBE SER DIFERENTE AL ORIGEN, vuelva a ingresar el código del aeropuerto destino:')
            destino = input().upper()
        else:
            if(not(destino in DiccionarioIndices)):
                checkDestino = True
                print('ERROR EN CÓDIGO INGRESADO, vuelva a ingresar el código del aeropuerto destino:')
                destino = input().upper()
            else:
                visaDestino = matrizNodos[DiccionarioIndices[destino]][4]
                #Verificamos si el visado del usuario es apto para el aeropuerto de destino
                if(visaDestino and not hasVisa):
                    checkDestino = True
                    print('EL DESTINO INGRESADO REQUIERE VISA, vuelva a ingresar el código del aeropuerto destino:')
                    destino = input().upper()
    destino = DiccionarioIndices[destino]

    dijkstra()
    calcularRuta()

    #Preguntamos si quiere hacer otra consulta
    print('Desea revisar otra ruta? (S/N)')
    salir = input().upper()
    while(not(salir == 'S' or salir == 'N')):
        print('ERROR EN OPCIÓN INGRESADA, vuelva a ingresar la opción (S/N):')
        salir = input().upper()
    #Si no quiere revisar otra ruta acabamos el programa
    if(salir == 'N'):
        runProgram = False
        print('Hasta la próxima!')

    #Reinicializa las variables
    hasVisa = False
    matrizNodos = [['CCS', 999, None, False, False],
                ['AUA', 999, None, False, True],
                ['CUR', 999, None, False, True],
                ['BON', 999, None, False, True],
                ['SDQ', 999, None, False, True],
                ['SXM', 999, None, False, True],
                ['SBH', 999, None, False, False],
                ['POS', 999, None, False, False],
                ['BGI', 999, None, False, False],
                ['PTP', 999, None, False, False],
                ['FDF', 999, None, False, False]]

