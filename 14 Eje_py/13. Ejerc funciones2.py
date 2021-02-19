#paradigma como resolver un problema en base de una herramienta q nos da hay varios
#POO Programaciòn orientada de objetos
# se crea la clase q es una plantilla caracteristicas
# los objetos se crean a traves de estas clases
# los objetos tienen propiedades / pensamos 
# metodos 
# pass no generra error

# atributos: son las formas q se describen las caracteristicas de nuestros objetos en las 
# clases se declaran los atributos ya que son las plantillas y se puede utilizar dependiendo
# del valor que le indiquemos  

# METODOS sirven para hacer un calculo o algun cambio sobre los atributos, se puede modificar
#son las acciones y modifican el estado 



 
class Persona():
    nbrazos= 0
    npiernas= 0
    cabello= True
    ccabello = "Defecto"
    hambre = 0

#CONSTRUCTO O INICILIZADOR: Inicializar a los objetos de una forma predeterminada
    def __init__(self):
        #se iniciliza atributos q se tienen y se les asigna un valor INICIAL o estado objeto
        self.nbrazos = 2
        self.npiernas = 2



    def dormir():
        pass
    #self modifica el atributo del atributo en si mismo
    def comer(self):
        # de mismo ingrese al atributo hambre y cambialo al valor q estoy indicando
        self.hambre= 20 #metodo que modific atributos 

class Hombre(Persona):#Aqui se accede por medio de la
    # Herencia "Persona" hereda clases y atributos 
    nombre ="Defecto"
    sexo = "m"
    def cambio_Nombre(self, nombre):
        self.nombre= nombre #metodo que modific atributos y recibe parametro

class Mujer(Persona):
    nombre ="Defecto"
    sexo = "f"

jose = Hombre()#se llama la clase
jose.comer() #se llama un metodo y se accede 
print(jose.hambre) #se accede a los atributos del objeto
