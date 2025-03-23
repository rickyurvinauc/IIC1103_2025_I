# Imagina que quieres realizar un viaje en auto desde tu
#  ciudad hasta una ciudad vecina. Necesitas calcular el 
# costo total del viaje, teniendo en cuenta varios 
# factores como la distancia a recorrer, el consumo 
# de combustible del auto, el precio del combustible, 
# y si habrá costos adicionales como peajes.

#Datos de entrad
distancia = int(input("Ingresa la distancia: "))
consumo = float(input("Ingresa el consumo: "))
precio = int(input("Ingresa el precio del combustible: "))
peajes = int(input("Ingresa el costo peajes: "))

#Solucion

consumo_vehiculo = consumo * distancia
costo_consumir_bencina = consumo_vehiculo * precio
costo_total = costo_consumir_bencina + peajes

#Salida
print("El costo total del viaje es: ", costo_total)
print("El costo total del viaje es: "+ str(costo_total))
