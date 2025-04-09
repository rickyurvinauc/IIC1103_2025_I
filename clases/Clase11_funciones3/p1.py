from hotel import nombre_ocupante, num_habitaciones

def obtener_habitacion(nombre):
    cantidad_hab = num_habitaciones()
    for hab in range(cantidad_hab): #(0,1,2)
        nombre_oc = nombre_ocupante(hab)
        if nombre_oc == nombre:
            return hab
    return -1