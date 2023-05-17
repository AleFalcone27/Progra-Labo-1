from copy import deepcopy
from random import shuffle

# # Armamos la lista
lista_1 = [17,15,8,7,5]

# Hacemos un copiado profundo 
lista_2 = deepcopy(lista_1) 

def mezclar_y_verificar(lista_1:list,lista_2:list):
    contador = 0
    while True:
        contador +=1
        shuffle(lista_2)
        print(lista_2)
        if lista_2 == lista_1:
            print("Tuvo que mezclar", contador, "veces para que se ordene")
            break
        

mezclar_y_verificar(lista_1,lista_2)


lista = [100.00, 200.00, 400.00, 800.00]

"""
Map: Pasa como parametros a una funcion a cada uno de los elementos de una lista, 
dando como resultado una lista 
"""    
lista_descuento = list(map(lambda x : x - (x * 0.15),lista))


print(lista_descuento)

