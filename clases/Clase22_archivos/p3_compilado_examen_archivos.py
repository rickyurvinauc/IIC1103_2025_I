# Escribe tu código aquí

def buscar_restaurantes(p):
    archivo = open('restaurantes.txt', 'r')
    contenido = archivo.readlines()
    archivo.close()
    restaurantes = []
    for linea in contenido:
        datos = linea.strip().split(';')
        if p in datos[0]:
            restaurantes.append(datos[0])

    return restaurantes
