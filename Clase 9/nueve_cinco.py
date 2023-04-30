from data_stark import lista_personajes as lista_heroes
import re
from nueve_uno import * 
from funciones import * 


# 5.1
def calcular_cantidad_tipo(lista:list,llave:str):
    if len(lista) > 0: 
        dictionary = cantidad_atributo_x(lista, llave)
        
        dictionary = str(dictionary)    
        
        dictionary = dictionary.replace(",", "\n")
        
        # dictionary = dict(dictionary)
        
        dictionary = dict(dictionary)
        
    else:
        return {"Error": "La lista se encuentra vacia"} 
    
calcular_cantidad_tipo(lista_heroes,"color_pelo")

# 5.2
# def guardar_cantidad_heroes_tipo(diccionario:dict,dato:str):
    
#     for clave in diccionario:
#         print( dato + clave)
        
        
        
        
        
# guardar_cantidad_heroes_tipo(calcular_cantidad_tipo(lista_heroes,"color_ojos"),"color_ojos")



