numer = int(input("Ingrese nùmero > 5 "))
pago = False
if numer > 5:
    print(f" el {numer} es mayor que 5")
    if pago == True: # condicional anidada
        print("Es mayor y pago")
        
    else:
        print("Es mayor pero no pago")

else:
    print(f" el {numer} es menor que 5 y no pago ")


