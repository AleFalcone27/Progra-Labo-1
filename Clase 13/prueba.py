from functools import reduce

def custom_max(num1:int,num2:int)->int:
        if num1 > num2:
            return num1
        elif num2 > num1:
            return num2
        elif num1 == num2:
            raise Exception("Los valores son iguales")
        raise Exception("Algo salió mal")
# print(max(89,5))


def max_de_tres(num1,num2,num3):
    max = custom_max(num1,num2)
    if max > num3:
        return max
    elif max == num3:
        raise Exception("num2 y 3 son iguales")
    else:
        return num3
# print(max_de_tres(7,3,1))

print(max_de_tres(1,2,2))

def is_vowel(char:str):
    
    char = char.lower() 
    
    vowels = ["a","e","i","o","u"]
    
    if char in vowels:
        return True
    else:
        return False
    
# print(is_vowel("A"))

lista_nums = [1,2,3,4]

def sum(lista:list)->int:
    suma = int(reduce(lambda x, y: x + y, lista) )
    return suma


# print(sum(lista_nums))

def mult(lista:list)->int:
    mult = int(reduce(lambda x, y: x * y, lista) )
    return mult

# print(mult(lista_nums))

def inversa(cadena:str)->str:
    return cadena [::-1]
# print(inversa("GLOBANT"))

