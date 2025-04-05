# Escribe tu código aquí
from hotel import num_habitaciones, nombre_ocupante

def obtener_habitacion(nombre):
    n_hab = num_habitaciones()

    for hab in range(n_hab):
        nombre_oc = nombre_ocupante(hab)
        if nombre == nombre_oc:
            return hab
    return -1