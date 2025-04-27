# Escribe tu código aquí
from metro import primera, proxima


def cuan_lejos(linea, estacion_1, estacion_2):
    if estacion_1 == estacion_2:
        return 0
    prim = estacion_1
    cant_estaciones = 0
    while True:
        prox = proxima(linea, prim)
        if prox == "":
            return -1
        cant_estaciones += 1
        if prox == estacion_2:
            return cant_estaciones
        prim = prox
    return -1

