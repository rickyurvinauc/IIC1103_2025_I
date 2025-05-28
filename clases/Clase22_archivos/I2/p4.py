def es_posible_insertar(tablero, pieza):
    for pi in pieza:
        pieza_t = tablero[pi[0]][pi[1]]
        if pieza_t != 0:
            return False
    return True