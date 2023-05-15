palabra1 = input("Dime una palabra: ")
palabra2 = input("Dime otra palabra: ")

def comparacion (palabra1, palabra2):
    if (palabra1 == palabra2):
        print("Ambas palabras son iguales")
    else:
        print ("Las palabras son diferentes")
        
print(comparacion(palabra1, palabra2))
