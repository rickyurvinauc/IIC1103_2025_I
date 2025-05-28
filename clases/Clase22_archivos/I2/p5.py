def verificar_t(indice_f, indice_c, tablero):
    pos_b_1 = [indice_f + 1,indice_c]
    pos_b_2 = [indice_f + 2, indice_c]
    pos_f_c = [indice_f + 1, indice_c + 1]
    lista = [pos_b_1, pos_b_2, pos_f_c]
    for pos in lista:
        if pos[0] >= len(tablero) or pos[1]>= len(tablero[0]):
            return False
        letra_t = tablero[pos[0]][pos[1]]
        if letra_t != 0:
            return False
    return True

def numero_posibles(tablero):
    indice_f = 0
    cant = 0
    for fila in tablero:
        indice_c = 0
        for col in fila:
            if col == 0:
                res = verificar_t(indice_f, indice_c, tablero)
                if res == True:
                    cant += 1
            indice_c += 1
        indice_f += 1
    return cant