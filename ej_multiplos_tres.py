num = int(input("Dime un numero: "))

def multiplo3(num):
    if (num%3==0):
        print("El número es multiplo de 3")
    else:
        print("El número no es multiplo de 3")
        
print(multiplo3(num))
