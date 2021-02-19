
# variable de instancia: esta variable ùnicamente se relaciona con la instancia de una clase
# se define asi

class Persona():
    edad = 18 #variables de clase, como se utiliza forma general global

    def __init__(self, nombre, nacionalidad):#al inicio se coloca parametros, self es por defecto
        self.nombre = nombre #estan predecidas con self y tenemos dos variables de instancia
        self.nacionalidad = nacionalidad
    
    #METODO DE INSTANCIA son  otras clases y se debe colocar siempre el self
    # tambien hay que crear el objeto previamente OJO 
    def nadar(self):
        print("estoy nadando")

personal = Persona("Maria", "Mexicana") #se crea la instancia del objeto 
print(personal.nombre) #imprimir variables de instancia se tienen q instanciar
print(Persona.edad)#imprimir variable clase
personal.nadar()

