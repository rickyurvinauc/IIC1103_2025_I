# pos inicial de Pacman
def encontrar_pacman(matriz):
    indice_f = 0
    for fila in matriz:
        indice_c = 0
        for col in fila:
            if col == "P":
                return [indice_f, indice_c]
            indice_c += 1
        indice_f += 1

# imprimir la matriz
def imprimir_matriz(m):
    for fila in m:
        print(fila)
    print()

# moviendo a Pacman
def mover(matriz, direccion):

    fila_actual = encontrar_pacman(matriz)[0]
    columna_actual = encontrar_pacman(matriz)[1]
    
    # eliminar a Pacman de la posicion actual
    matriz[fila_actual][columna_actual] = ""

    # calcular nueva posicion
    if direccion == "arriba":
        fila_actual -= 1
    elif direccion == "abajo":
        fila_actual += 1
    elif direccion == "izquierda":
        columna_actual -= 1
    elif direccion == "derecha":
        columna_actual += 1

    # encontrar los limites de la fila
    if fila_actual < 0:
        fila_actual = 0
    elif fila_actual >= len(matriz):
        fila_actual = len(matriz) - 1

    # encontrar los limites de la columna
    if columna_actual < 0:
        columna_actual = 0
    elif columna_actual >= len(matriz[0]):
        columna_actual = len(matriz[0]) - 1

    # si la nueva posicion tiene un fantasma, remplazamos por una "X"
    if matriz[fila_actual][columna_actual] == "F":
        matriz[fila_actual][columna_actual] = "P"
    else:
        matriz[fila_actual][columna_actual] = "P"

    return [fila_actual, columna_actual, matriz]

# matriz inicia
matriz = [
    ["", "", "F"],
    ["", "P", ""],
    ["F", "", ""],
    ["", "F", ""],
]

# simulando los movimientos
imprimir_matriz(matriz)
movimientos = mover(matriz, "derecha")  # se mueve a (1,2)
fila = movimientos[0]
columna = movimientos[1]
matriz = movimientos[2]

imprimir_matriz(matriz)
movimientos = mover(matriz, "arriba")   # se mueve a (0,2) - hay un fantasma
fila = movimientos[0]
columna = movimientos[1]
matriz = movimientos[2]

imprimir_matriz(matriz)
movimientos = mover(matriz, "izquierda")  # se mueve a (0,1)
fila = movimientos[0]
columna = movimientos[1]
matriz = movimientos[2]

imprimir_matriz(matriz)
movimientos = mover(matriz, "abajo")      # se mueve a (1,1)
fila = movimientos[0]
columna = movimientos[1]
matriz = movimientos[2]

imprimir_matriz(matriz)
movimientos = mover(matriz, "abajo")      # se mueve a (2,1)
fila = movimientos[0]
columna = movimientos[1]
matriz = movimientos[2]

imprimir_matriz(matriz)
movimientos = mover(matriz, "izquierda")  # se mueve a (2,0) - hay un fantasma
imprimir_matriz(matriz)