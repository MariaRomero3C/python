num = int(input("Dime una edad: "))

def rango (num):
    if (num < 18):
        print("Menor de edad")
    elif (num > 60):
        print("Adulto mayor")
    else:
        print("Adulto")

print(rango(num))
