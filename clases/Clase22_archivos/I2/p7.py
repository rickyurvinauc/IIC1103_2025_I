def primera_cancion(canciones):
    siguientes = []
    for cancion in canciones:
        siguientes.append(cancion[2])
    for i_cancion in range(len(canciones)):
        if i_cancion not in siguientes:
            return canciones[i_cancion][0]