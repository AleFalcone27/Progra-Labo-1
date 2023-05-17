# IMPORTAMOS MODULOS
import json 
import re

# CASTEAMOS VALORES

def parse_json(nombre_archivo:str)->list[dict]:

    """
    Esta funcion se encarga de leer un archivo json y devolverlo como diccionario 
    """

    dict_json = {}

    archivo = open(nombre_archivo,"r")

    dict_json = json.load(archivo)

    archivo.close()

    return dict_json["personajes"] 

lista = parse_json("personajes_de_lol.json")


def guardar_en_json(lista:list[dict]):
    
    data = {"personajes": []}
    for i in lista:
            data["personajes"].append({"nombre": i["nombre"], "rol": i["rol"], "atributos": i["atributos"]})

    with open("data,json", "w") as file:
        json.dump(data, file, indent=2)
        
guardar_en_json(lista)

# # IMPORTAMOS JSON