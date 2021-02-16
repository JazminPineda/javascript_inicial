def saludo(nombre):
    if nombre == "juan":
        print("hola como estas? ")
def pregunta(respuesta):
    if respuesta == "bien":
        print("vas a comer? ")
    else:
        print("¿por qué estas mal?")

nombre = input("quien eres? ")
saludo(nombre)
rep = input("estas bien o mal? ")
pregunta(rep)
    

