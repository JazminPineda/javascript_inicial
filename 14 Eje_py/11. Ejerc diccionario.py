#listas mutables
lista =['paola', 'jaz', 'min']
print(len(lista))
# #for elem in lista:
#     print(lista[1], lista[2], lista[0])
#     print(elem)#
lista2 = ['ama', 5 ,'Luca', 's']
vista = (lista + lista2)
print(vista)
if 5 in lista2:
    print("si")

meses='Enero Febrero Marzo Abril'
print(meses[6:13])
dias=('Lunes','Martes','Miércoles','Jueves', 'Viernes', 'Sábado', 'Domingo')
dia=0
while dia < len(dias):
    print(dias[dia])
    dia = dia + 1
