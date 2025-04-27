# Escribe tu código aquí

def agregar_puntos(texto):
    frase = ""
    indice = 0
    indice_anterior = 0
    for letra in texto:
        if letra.isupper() and indice > 0:
            frase_cortada = texto[indice_anterior:indice-1]+". "
            frase += frase_cortada
            indice_anterior = indice
        indice += 1
        if indice == len(texto):
            frase_cortada = texto[indice_anterior:]+"."
            frase+= frase_cortada
    return frase



