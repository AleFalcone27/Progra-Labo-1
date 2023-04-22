from data_stark import lista_personajes
import re

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

# 3.1
def sanitizar_entero(num_str:str):
    
    num_str = num_str.strip()
    
    if re.search("[a-zA-Z]+",num_str):
        return -1
    elif re.search("^-", num_str):
        return -2
    elif re.search("[0-9+]",num_str):
        num_str = int(num_str)
        return num_str
    else:
        return -3

# 3.2
def sanitizar_flotante(num_str:str):
    
    num_str = num_str.strip()
    
    if re.search("[a-zA-Z]+", num_str):
        return -1
    elif re.search("^-",num_str):
        return -2
    elif re.search("[0-9+]",num_str):
        num_str = float(num_str)
        return num_str
    else: 
        return -3

# 3.3
def sanitizar_string(num_str:str, valor_por_defecto="-"):
    
    num_str = re.sub("/"," ",num_str)
    
    if re.search("[0-9+]",num_str):
        return "N/A"
    elif num_str == "":
        valor_por_defecto = valor_por_defecto.lower()
        return valor_por_defecto
    else:
        num_str = num_str.lower()
        return num_str
    
# 3.4
def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):

# heroe: diccionario con los datos de un personaje
# clave: clave del valor que queremos sanitizar en el diccionario
# tipo_dato: str que representa el tipo de dato a sanitizar

    if tipo_dato == 'str':
        dato_sanitizado = sanitizar_string(clave)
        retorno = dato_sanitizado

    elif tipo_dato == 'float':
        dato_sanitizado = sanitizar_flotante(clave)
        retorno = dato_sanitizado
        
    elif tipo_dato == 'int':
        dato_sanitizado = sanitizar_entero(clave) 
        retorno = dato_sanitizado

    elif tipo_dato != 'str' or tipo_dato != 'float' or tipo_dato != 'str':
        print('Tipo de dato no reconocido')

    elif clave not in heroe:
         print("La clave especificada no existe en el heroe")

    return retorno

def stark_normalizar_datos(lista_personajes:list[dict]):
    
    for heroe in lista_personajes:
        heroe['altura'] = sanitizar_dato(heroe,heroe["altura"],'float')
        heroe['peso'] = sanitizar_dato(heroe,heroe["peso"],'float')
        heroe['color_ojos'] = sanitizar_dato(heroe,heroe["color_ojos"],'str')
        heroe['color_pelo'] = sanitizar_dato(heroe,heroe["color_pelo"],'str')
        heroe['fuerza'] = sanitizar_dato(heroe,heroe["fuerza"],'str')
        heroe['inteligencia'] = sanitizar_dato(heroe,heroe["inteligencia"],'str')
        print(heroe)
        
stark_normalizar_datos(lista_personajes)
