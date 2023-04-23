import re 
from data_stark import lista_personajes as lista_heroes 

h = { "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""}

# 1.1
def extraer_iniciales(nombre_heroe:str):

    # recibe como parametro un str omite si existe un 'the' y un '-' y nos devuelve las iniciales separadas con un '.'
    
    if nombre_heroe == "":
        return "N/A"
    else:
        iniciales = ""
        
        nombre_heroe = nombre_heroe.upper() 
        
        nombre_heroe = re.sub("THE"," ", nombre_heroe)
        nombre_heroe = re.sub("[-]"," ",nombre_heroe)
        
        lista_nombre_heroe = nombre_heroe.split()

        for i in range(len(lista_nombre_heroe)):
            iniciales = iniciales + lista_nombre_heroe[i][0] + "."
            
        return iniciales
    
#1.2
def definir_iniciales_nombre(heroe:dict):

# recibe como parametro un diciconario, valida quetrnga el formato correcto, si la clave iniciales no existe la agrega y devuelve true


    if type(heroe) != dict or "nombre" not in heroe:
        return False
    
    else:
        inciales = extraer_iniciales(heroe['nombre'])
        if "iniciales" not in heroe:
            heroe["iniciales"] = inciales

            return True
        
#1.3
def agregar_iniciales_nombre(lista:list):

# itera y le agrega a cada heroe las iniciales  

    if type(lista) == list and len(lista) > 0:
            
        for heroe in lista:  

            validacion = definir_iniciales_nombre(heroe) 
            if validacion == False:

                print('El origen de los dato con contiene el formato correcto')

        return True
    
    else:

        return False

#1.4
def stark_imprimir_nombres_con_iniciales(lista:list): 

# imprime los nombres de todos los heroes con sus respectivas iniciales 

    if type(lista) == list and len(lista) > 1:
        agregar_iniciales_nombre(lista_heroes)
        for i in lista:
            print( "*" + i['nombre'], "(" + i["iniciales"] + ")")



                
