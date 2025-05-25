def dcc_en_salto(lista):
    indice_f = 0
    for fila in lista:
        indice_c = 0
        for col in fila:
            if col == 'd':
                if indice_c+2 < len(lista[0]) and indice_c+4 < len(lista[0]):
                    letra2 = lista[indice_f][indice_c+2]
                    letra3 = lista[indice_f][indice_c+4]
                    if letra2 == 'c' and letra3 == 'c':
                        return indice_f
            indice_c += 1
        indice_f += 1