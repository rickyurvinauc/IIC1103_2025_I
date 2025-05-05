# Escribe tu código aquí

def contabilizar(lista):
    # [100,250,-340,-400,500]
    dep_total = 0
    ret_total = 0
    # for numero in lista:
    for i_lista in range(len(lista)):
        numero = lista[i_lista]
        if numero > 0:
            dep_total = dep_total + numero
        else:
            ret_total = ret_total + numero

    lista_respuesta = [dep_total, ret_total]
    return lista_respuesta
    # return [dep_total, ret_total]
