from colorama import Fore,Back, init
from copy import deepcopy
from random import shuffle
from functools import reduce
import random

init()

series =[ {"nombre": "Dragon BallZ", "año": 1989,"Rating": 7.2 },
        {"nombre": "SailorMoon", "año": 1992, "Rating": 8.7},
        {"nombre": "Pokemon","año": 1997, "Rating": 9.3},
        {"nombre": "Digimon Adventure","año": 1999, "Rating":6.6},
        {"nombre": "Yu YuHakusho", "año": 1992, "Rating":9.8},
        {"nombre": "NeonGenesisEvangelion", "año": 1995, "Rating":8.4},
        {"nombre": "One Piece","año": 1999, "Rating":8.5},
        {"nombre": "RurouniKenshin", "año": 1996, "Rating":10.0}]

lista_copia = deepcopy(series)

# 1 Obtener una lista con los nombres de todas las series de anime.
def filter_names(lista:list):
    
    lista_resultado = list((map(lambda serie : serie["nombre"] , lista_copia)))

    return lista_resultado

# print(Fore.GREEN, filter_names(lista_copia))

# 2 Obtener las series de anime lanzadas después de 1995.
def after_1995(lista:list)-> list:
    
    lista_retorno = list(filter(lambda año : año["año"] > 1995, lista))
    
    return lista_retorno

# print(Fore.MAGENTA, after_1995(lista_copia)) 

# 3. Obtener la suma de los años de lanzamiento de las series.
def sumar_años(lista:list[dict]):
    
    suma_años = int(reduce(lambda y , x : y + x["año"] ,lista,0)) # se utiliza el 0 al final de reduce para inicialiazr en 0 el contador 
    
    return suma_años

print(Fore.GREEN,sumar_años(lista_copia))

# 4 Realizar una copia superficial de la lista de series.
series = series.copy

# 6 Obtener el año de lanzamiento de una serie utilizando una función de diccionario
def obtener_año(lista:list[dict]):

    año_random = lista[random.randint(0,7)].pop("año")
    
    return año_random
    
print(Fore.RED,obtener_año(lista_copia))


# 7 Obtener una lista de tuplas con los pares clave-valor de una serie utilizando una función de diccionario
def obtener_clave_valor(lista:list[dict]):
    random_clave_valor = lista[random.randint(0,7)].items()
    return random_clave_valor
print(Fore.BLUE,obtener_clave_valor(lista_copia))

# 8 Eliminar una serie de la lista por su índice utilizando una función de lista.
def eliminar_serie(lista:list[dict])->list:
    ran_num = random.randint(0,7)
    serie_eliminada = lista.pop(ran_num)
    return serie_eliminada

# print(Fore.LIGHTRED_EX, "ELIMNADO: ", eliminar_serie(lista_copia))

# 9 Obtener una lista con los nombres de las series en mayúsculas utilizando una función de transformación.
def upper_nombres(lista:list[dict])->list:
    
    nombres_upper = list(map(lambda nombre : nombre["nombre"].upper(), lista))
    
    return nombres_upper

print(Fore.GREEN, upper_nombres(lista_copia))


# 10 Obtener las series de anime con nombres que contengan la palabra "Adventure" utilizando una función de filtrado.
def buscar_nombre(lista:list[dict], palabra:str):
    nombre_filtrado = list(filter(lambda nombre : palabra in nombre["nombre"], lista))

    return nombre_filtrado

print(Fore.MAGENTA,buscar_nombre(lista_copia,"Adventure"))

# 11 Generar una función que busque los nombres de las series con el rating mayor a 8.5
# def filtrar_rating(lista:list[dict], rating_buscado):
    
#     rating_filtrado = list(filter(lambda rating : rating["Rating"] > rating_buscado, lista))
    
#     return rating_filtrado

# print(Fore.CYAN, filtrar_rating(lista_copia,.5))