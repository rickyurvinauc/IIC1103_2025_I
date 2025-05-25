archivo = open('examen.txt','r')
contenido = archivo.readlines()
archivo.close()


for linea in contenido:
    datos = linea.strip().split(';')
    valor = float(datos[1])
    lim_i = float(datos[2])
    lim_s = float(datos[3])
    if valor < lim_i:
        print(datos[0]+" -")
    elif valor > lim_s:
        print(datos[0]+" +")