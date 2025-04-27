# Escribe tu código aquí :D

cant_reposo = 0
cant_moderada = 0
cant_maxima = 0
edad = int(input())
fcm = 220 - edad

while True:
    frecuencia = int(input())
    porcentaje = frecuencia / fcm * 100
    if frecuencia == -1:
        break

    if porcentaje <= 55:
        cant_reposo += 1
    elif porcentaje >= 95:
        cant_maxima += 1
    else:
        cant_moderada += 1

print("Reposo:", cant_reposo)
print("Moderada:", cant_moderada)
print("Maxima:", cant_maxima)