import re 
from data_stark import lista_personajes as lista_heroes 

#2.1
def generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    if type(id_heroe) == int and genero_heroe != "" and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB":
        
# genera un codigo_heroe de 10 digitos de longitud utilizando el genero y el id del heroe y rellenando los valores restantes con 0.  
    
        id_heroe = str(id_heroe)
        
        espacios_ocupados = len(genero_heroe + id_heroe) + 1 
        
        codigo_heroe = ""
        
        ceros = codigo_heroe.zfill(10 - espacios_ocupados)
        
        codigo_heroe = genero_heroe + "-" + ceros + id_heroe
        
        return codigo_heroe
    
    else:
        
        return "N/A"
        

#2.2
def agregar_codigo_heroe(heroe:dict, codigo_heroe:int):
    
# agrega una la nueva clave genero_heroe y el valor codigo_heroe generado en el punto 2.1
    
    if len(heroe) > 0 or len(codigo_heroe) == 10:
            
        if "codigo_heroe" not in heroe:
            
            heroe["codigo_heroe"] = codigo_heroe
            
        return True

    else:
        
        return False
    

# 2.3
def stark_generar_codigos_heroes(lista:list):
    
# itera sobre la lista heroes validando que cada heroe tenga mas de 1 elemento y que todos sean del tipo dict y que todos tengan la clave "genero"
# y printeamos la ultima, la primera y la cantidad total de asignaciones que se realizaron

    posicion = 0
    flag = True      

    if len(lista) > 0:
        
        for heroe in lista_heroes:
            if type(heroe) == dict and "genero" in heroe:
                
                posicion = posicion + 1
                
                codigo_heroe = generar_codigo_heroe(posicion, heroe["genero"])
                agregar_codigo_heroe(heroe, codigo_heroe)
                
                if flag == True:
                    primer_asignacion = codigo_heroe
                    flag = False

                ultima_asignacion = codigo_heroe
        
        print("* El codigo del primer héroe es:" , primer_asignacion)
        print("* El codigo del ultimo héroe es:" , ultima_asignacion)
    




