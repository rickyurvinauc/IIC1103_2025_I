# Escribe tu código aquí
from hotel import num_habitaciones, nombre_ocupante


def revisar_asignacion():
    n_hab = num_habitaciones()
    contador = 0
    for i in range(n_hab):
        nombre = nombre_ocupante(i)
        for j in range(i + 1, n_hab):
            nombre2 = nombre_ocupante(j)
            if nombre == nombre2:
                contador += 1
                break

    return contador


