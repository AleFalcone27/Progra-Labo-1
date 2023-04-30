from data_stark import lista_personajes as lista_heroes
from nueve_uno import *
import re
import json

if __name__ == "__main__":
    # 3.1
    def calcular_min_genero(lista:list,llave:str,genero:str)->str:
        # esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande que existe asignado a la clave pasada como parametro 
        nombre_mini = None
        mini = None
        for i in lista:
            if genero == i["genero"]:
                if mini == None or (i[llave]) < mini: #recordar castear en caso de ser necesario
                    mini = (i[llave]) #recordar castear en caso de ser necesario
                    nombre_mini = i["nombre"]
                    
        return nombre_mini # solo retorno el nombre o el dato tambien?

    # 3.2
    def calcular_max_genero(lista:list,llave:str,genero:str)->str:
    # esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande que existe asignado a la clave pasada como parametro 
        nombre_max = None
        max = None
        for i in lista:
            if genero == i["genero"]:
                if max == None or float(i[llave]) > max: #recordar castear en caso de ser necesario
                    max = float(i[llave]) 
                    nombre_max = i["nombre"]
                
        return nombre_max # solo retorno el nombre o el dato tambien?

    # 3.3
    def calcular_max_min_dato(lista:list[dict],llave:str,genero:str,max_o_min:str)->str:
        match max_o_min:
            case "min":
                return calcular_min_genero(lista,"altura",genero)
            case "max":
                return calcular_max_genero(lista,"altura",genero)

    # 3.4
    def stark_calcular_imprimir_guardar_heroe_genero(genero:str,llave): # Este no lo puede hacer funcionar 
        
        llave_capitalizada = capitalizar_palabras(llave)
        string = "" + obtener_nombre_capitalizado(h) + " | " +  llave_capitalizada + ": " + heroe[llave]

        return string
        

        
        
        guardar_archivo()
