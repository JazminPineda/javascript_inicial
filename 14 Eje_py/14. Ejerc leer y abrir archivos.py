def crear_Archivo():
    archiv = open("datos.txt" , "w") #modo escritura o lectura si existe solo lo tomamos 
    archiv.close()#se tiene que cerrar 
crear_Archivo()

def escrib_archiv():
    archivo=open("datos.txt" , "a")#no se modifica solo se agrega, no se sobreescribe
    archivo.write("mario pirto \n")
    archivo.write("959852")
    archivo.close()
escrib_archiv()

def leer_Archivo():
    archivo=("datos.txt" , "r") #solo lee el contenido del archivo
    linea= archivo.readline()
    while linea != " ":
        print(linea)
        linea = archivo.readline()
    archivo.close()

leer_Archivo()