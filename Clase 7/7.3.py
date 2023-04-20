from data_stark import lista_personajes
import re

numero_str = "23"


def sanitizar_entero(num_str:str):
    
    num_str = num_str.strip()
    
    if num_str.isnumeric() == False:
            return -1
    else:
        return True

    
    # print(re.search("[0-9]",numero_str))
    #contiene caracteres no numericos return -1
    
    # elif #el numero es negativo return -2
    
    # elif:
    
    # else:
    #     return -3
    
print(sanitizar_entero(numero_str))