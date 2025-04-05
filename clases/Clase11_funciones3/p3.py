# Escribe tu código aquí

from hotel import num_habitaciones, nombre_ocupante, obtener_caracter


def se_puede_excursion(cantidad):
    contador_tim = 0
    contador_extro = 0

    for i in range(num_habitaciones()):
        nombre = nombre_ocupante(i)
        caracter = obtener_caracter(nombre)

        if caracter == "timido":
            contador_tim += 1
        else:
            contador_extro += 1

    necesidad_tim = contador_tim / 5
    necesidad_ext = contador_extro / 5
    necesidad_tim_ = int(necesidad_tim)
    necesidad_ext_ = int(necesidad_ext)
    if necesidad_tim % 1 > 0:
        necesidad_tim_ += 1
    if necesidad_ext % 1 > 0:
        necesidad_ext_ += 1
    cantidad_necesidad_total = necesidad_ext_ + necesidad_tim_
    if cantidad >= cantidad_necesidad_total:
        print(f"Suficientes: se tienen {cantidad} y se necesitan {cantidad_necesidad_total}")
    else:
        print(f"Insuficientes: se tienen {cantidad} y se necesitan {cantidad_necesidad_total}")

