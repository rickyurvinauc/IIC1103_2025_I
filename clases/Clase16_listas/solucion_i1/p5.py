# Escribe tu código aquí

from metro import nombre, numero, primera, proxima

l1 = input()
l2 = input()
n_l1 = numero(l1)
n_l2 = numero(l2)
for indice_l1 in range(n_l1):
    nombre_l1 = nombre(l1, indice_l1)
    for indice_l2 in range(n_l2):
        nombre_l2 = nombre(l2, indice_l2)
        if nombre_l1 == nombre_l2 and nombre_l1 != "":
            print(nombre_l1)
            break