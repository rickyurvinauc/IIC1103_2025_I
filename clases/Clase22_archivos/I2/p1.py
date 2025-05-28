def encontrar_colores(circuito):
    colores = []
    for color in circuito:
        if color not in colores:
            colores.append(color)
    
    return colores