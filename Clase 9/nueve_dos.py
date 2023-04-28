from data_stark import lista_personajes as lista_heroes
import re
import json

h = {
        "nombre": "Howard the Duck",
        "identidad": "Howard (Last name unrevealed)",
        "empresa": "Marvel Comics",
        "altura": "79.349999999999994",
        "peso": "18.449999999999999",
        "genero": "M",
        "color_ojos": "Brown",
        "color_pelo": "Yellow",
        "fuerza": "2",
        "inteligencia": ""
        }
# 2.1
def es_genero(dict:dict,genero:str)->bool:
    
# es funcion verifica que el genero pasado como parametro de ecneuntre dentro del diccionario pasado como parametro

    genero = genero.upper()
    
    if genero in dict.values(): # por defecto la palabra reservada in nos compara con las llaves, pero como en este caso necesitamos saber si el genero es un valor dentro del diccionario pasado como parametro utilizamos el metodo .values()
        
        return True
    else: 
        return False
    
    
# 2.1
def stark_guardar_genero_heroe(lista:list[dict],genero)->bool:
    
    genero = genero.upper()
    
    for heroe in lista_heroes:
        if heroe["genero"] == genero:
            print(heroe["nombre"])
            if genero == "F":
                archivo = open("heroes_F.csv","a") 
                archivo.write(heroe["nombre"] + ",")
                archivo.close()
            elif genero == "M":
                archivo = open("heroes_M.csv","a")
                archivo.write(heroe["nombre"] + ",")
                archivo.close()
            elif genero == "NB":
                archivo = open("heroes_NB.csv","a")  
                archivo.write(heroe["nombre"] + ",")
                archivo.close()
        
        #     retorno = True
        # else:
        #     retorno = False
            

            
stark_guardar_genero_heroe(lista_heroes,"m")