# Escribe tu código aquí
# ['14/02', '19:30', 120, 'Cena romantica', 1930]
def criterio(item):
    return item[4]

def encontrar_mas_temprano(actividades):
    for actividad in actividades:
        hora = int(actividad[1][:2] + actividad[1][len(actividad[1])-2:])
        actividad.append(hora)
    actividades.sort(key=criterio)
    return actividades[0][3]

