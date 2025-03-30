# Escribe tu código aquí
cantidad = int(input())
no_dino = 0
brach = 0
tita = 0
cant_bra = 0
cant_tita = 0
fosil_anterior = -1

for i in range(cantidad):
    fosil = int(input())
    if fosil == 0:
        no_dino += 1
        cant_bra = 0
        cant_tita = 0
    elif fosil == 1:
        cant_bra += 1
        cant_tita = 0
    elif fosil == 2:
        cant_tita += 1
        cant_bra = 0

    if cant_bra == 2 and fosil_anterior == fosil:
        brach += 1
        cant_bra = 0

    if cant_tita == 3 and fosil_anterior == fosil:
        tita += 1
        cant_tita = 0

    fosil_anterior = fosil

print("Brachiosaurus:", brach)
print("Titanosaurus:", tita)
