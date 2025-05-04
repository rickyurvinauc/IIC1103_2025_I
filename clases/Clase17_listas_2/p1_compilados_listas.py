# Escribe tu código aquí

def descifrar_it(letras, instrucciones):
    lista_final = []
    indice_i = 0
    indices_anteriores = 0  # 1
    for indice_i in range(0, len(instrucciones), 2):
        accion = instrucciones[indice_i]
        if accion == "agregar":
            cant = instrucciones[indice_i + 1]  # 1
            # print("cant", cant)
            for i in range(cant):
                # print("i", i)
                # print("indices_anteriores", indices_anteriores)
                # print("letras[indices_anteriores+i]", letras[indices_anteriores+i])
                lista_final.append(letras[indices_anteriores + i])
        indices_anteriores += instrucciones[indice_i + 1]
        indice_i += 1

    return lista_final



