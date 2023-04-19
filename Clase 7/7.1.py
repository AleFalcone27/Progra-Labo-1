import re 

heroe = { "nombre": "Howard the Duck",
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
def extraer_iniciales(nombre_heroe):
    
    if nombre_heroe == "":
        return "N/A"
    else:
        iniciales = ""
        
        nombre_heroe = nombre_heroe.upper() #me tira error aca cualquiera
        
        nombre_heroe = re.sub("THE"," ", nombre_heroe)
        
        nombre_heroe = re.sub("[-]"," ",nombre_heroe)
        
        lista_nombre_heroe = nombre_heroe.split()

        for i in range(len(lista_nombre_heroe)):
            iniciales = iniciales + lista_nombre_heroe[i][0] + "."
            
        return iniciales
    
#1.2
def definir_iniciales_nombre(heroe):
    iniciales = extraer_iniciales(heroe)
    if type(heroe) != dict or "nombre" not in heroe:
        return False
    else:
        if "iniciales" not in heroe:
            heroe["iniciales"] = iniciales
            return True

definir_iniciales_nombre(heroe)