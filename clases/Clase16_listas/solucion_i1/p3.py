# Escribe tu código aquí
from metro import primera, proxima, imprimir_linea

def esta_en(linea, estacion):
    prim = primera(linea) #primera estacion
    if prim == estacion:
        return True
    while True:
        prox = proxima(linea, prim)
        if prox == estacion:
            return True
        if prox == "":
            return False
        prim = prox
