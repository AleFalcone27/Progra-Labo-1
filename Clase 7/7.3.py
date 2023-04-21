from data_stark import lista_personajes
import re

num_str = ""

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

       

    

    


# print(sanitizar_flotante(num_str))
# print(sanitizar_entero(num_str))
print(sanitizar_string(num_str))