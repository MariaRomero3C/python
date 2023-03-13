
 
temp = int(input("temperatura del agua:"))
 
if(temp < 0):
    print("Hielo")
elif(temp > 100):
    print("Vapor")
else:
    print("Líquido")