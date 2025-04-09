import cimc


altura = float(input("Ingresa tu altura: "))
peso = float(input("Ingresa tu peso: "))

imc = cimc.calcular_imc(altura, peso)

print("Tu IMC es: ", imc)