# Escribe tu código aquí

def todos_los_nums(lista):
    lista.sort()
    for indice in range(len(lista)):
        if indice != lista[indice]:
            return False
    return True
