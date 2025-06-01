import csv

def leer_notas_forma_1(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    notas = []
    reader = csv.reader(archivo) 
    # reader es un objeto iterable
    cabecera = next(reader) 
    print(cabecera)
    # next() devuelve la siguiente linea del archivo
    print(cabecera)
    for linea in reader:
        notas.append(linea)
    archivo.close()
    return notas

nombre_archivo = 'notas.csv'
notas = leer_notas_forma_1(nombre_archivo)
print(notas)

def leer_notas_forma_2(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    contenido = archivo.readlines()
    notas = []
    for linea in contenido:
        datos = linea.strip().split(',')
        notas.append(datos)
    archivo.close()
    return notas

nombre_archivo = 'notas.csv'
notas2 = leer_notas_forma_2(nombre_archivo)
print(notas2)