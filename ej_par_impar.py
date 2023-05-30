def par_impar(num):
    if(num % 2 == 0):
        return "par"
    else:
        return "impar"
    
print (par_impar(5))
print (par_impar(8))

num = int(input("Dime un número"))
print(par_impar(num))
