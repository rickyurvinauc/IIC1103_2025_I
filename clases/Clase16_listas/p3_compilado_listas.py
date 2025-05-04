# Escribe tu código aquí

def contabilizar(lista):
    lista_depostios = []
    lista_retiros = []

    for valor in lista:
        if valor>0:
            lista_depostios.append(valor)
        else:
            lista_retiros.append(valor)
    
    suma_depositos = sum(lista_depostios)
    suma_retiros = sum(lista_retiros)

    return [suma_depositos, suma_retiros]