# Escribe tu código aquí

a = int(input())
b = int(input())

cantidad_intro = 0
for i in range(a,b+1):

    numero = str(i)
    cant_unos = numero.count("1")
    cant_ceros = numero.count("0")
    cant_tres = numero.count("3")
    if cant_unos >= 2 and cant_ceros > 0 and cant_tres > 0:
        print(i)
        cantidad_intro += 1

print(cantidad_intro)

