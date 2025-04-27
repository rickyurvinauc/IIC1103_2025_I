# Escribe tu código aquí

def parentesis(texto, indice):
    indice_mayor = 0
    for indice_texto in range(indice):
        letra = texto[indice_texto]
        if letra == "(":
            indice_mayor = indice_texto
    return indice_mayor
