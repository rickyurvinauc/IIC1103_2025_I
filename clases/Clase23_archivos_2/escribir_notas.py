import csv

def write_csv(nombre_archivo, data):
    archivo = open(nombre_archivo, mode='a') 
    # mode='a' es para abrir y escribir en la ultima 
    # linea, se puede usar 'w' para sobreescribir
    writer = csv.writer(archivo)
    writer.writerows(data)
    archivo.close()
    
def escribir_notas_actualizadas(nombre_archivo, notas):
    # Aqui primero abro el archivo en modo lectura para leer la cabecera
    archivo_lectura = open(nombre_archivo, 'r')
    reader = csv.reader(archivo_lectura)
    cabecera = next(reader)
    # Una vez que guarde la cabecera procedo a abrir el archivo en modo escritura
    archivo_escritura = open(nombre_archivo, 'w')
    writer = csv.writer(archivo_escritura)
    writer.writerow(cabecera)
    writer.writerows(notas)
    archivo_escritura.close()
    archivo_lectura.close()
  
