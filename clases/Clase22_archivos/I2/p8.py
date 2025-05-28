def siguiente(lista, cancion_actual):
    for item in lista:
        if cancion_actual == item[0]:
            indice_item = item[2]
            if indice_item == -1:
                return "No disponible"
            return lista[indice_item][0]
    return "No disponible"