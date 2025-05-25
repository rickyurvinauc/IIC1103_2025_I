def super_estudiantes(estudiantes, indicados):
    # Escribe tu código aquí!
    indice_e = 0
    lista = []
    encontrado = False
    for estudiante in estudiantes:
        cant = 0
        for indicado in indicados:
            if indicado  in estudiante:
                cant += 1
        if cant == len(indicados):
            lista.append(indice_e)
        indice_e += 1
    return lista