def solo_dcc(lista):
    for indice_l in range(len(lista)):
        letra = lista[indice_l]
        if letra != 'd' and letra != 'c':
            lista[indice_l] = '-'
    return lista

