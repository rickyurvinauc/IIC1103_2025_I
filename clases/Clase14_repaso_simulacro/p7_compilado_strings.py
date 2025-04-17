# Escribe tu código aquí

def encadenado(frase):

    palabra = ''
    indice = 0
    numeros = '0123456789'
    for letra in frase:
        if letra in numeros:
            cant = int(letra)
            palabra += frase[indice+1:indice+1+cant]
        
        indice += 1
    
    return palabra



