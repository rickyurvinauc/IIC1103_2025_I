class Persona:
    
    def __init__(self, nombre, apellido, edad, rut=2899999):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.rut = rut
        self.peso = 65
    
    def __str__(self):
        return "Nombre de la persona es:"+self.nombre
        
    def es_mayor_de_edad(self, semestre):
        
        if self.edad>18 and semestre>4:
            return "Es mayor de edad y su semestre es:"+str(semestre)
        else:
            return "No es mayor de edad"
  
objeto1= Persona("Ricardo","Urvina", 28, 279999)
print(objeto1)

# print(objeto1.es_mayor_de_edad(5))


    