letra1 = input("Dime la primera letra de la palabra: ")
letra2 = input("Dime la segunda letra de la palabra: ")
letra3 = input("Dime la tercera letra de la palabra: ")
letra4 = input("Dime la cuarta letra de la palabra: ")
palabra = letra1 + letra2 + letra3 + letra4


def palindromo (palabra):
    if (letra1 == letra4 and letra2==letra3):
        return "Es un palindromo"
    else:
        return "No es palindromo"
    
print(palindromo(palabra))
