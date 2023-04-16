from data_stark import lista_personajes as lista_heroes


# 2.1
def generar_codigo_heroe(cont_heroes:str, genero_heroe:str):
    
    id_heroe = cont_heroes
    
    genero_heroe = genero_heroe.upper()
    
    if type(id_heroe) == int and (genero_heroe == "M" or genero_heroe == "NB" or genero_heroe == "F"):
        
        genero_heroe = genero_heroe.upper()
        
        id_heroe = str(id_heroe) # lo casteo a str para pder concatenarlo

        cero = "-" + id_heroe # agregamos un guion
        
        resta = 10 - len(genero_heroe) # restamos la longitd de genero_heroe a la longitud maxima qe debe tener el retur 
        
        cero = cero.zfill(resta) # rellenamos con ceros 
        
        resultado = genero_heroe + cero 

        return resultado
    else:
        return "N/A" 
    

# 2.2
def agregar_codigo_heroe(heroe:dict,id_heroe:int):
    
    if len(heroe) > 0 or len(id_heroe) == 10: # validamos que no nos pasen ni un diccionario vacio y que el id sea de 10 caracteres exactamente
        
        heroe["codigo_heroe"] = id_heroe # agregamos la clave "codigo_heroe" y el id_heroe ene ele diccionario
        
        return True
    else:
        return False

# 2.3
def stark_henerar_codigos_heroes(lista_heroes):
    cont_heroes = 0 
    flag = True
    
    if len(lista_heroes) > 0:
    
        for heroe in (lista_heroes):
            
            cont_heroes = cont_heroes + 1 # sumamos 1 al cotador por cad iteracion
            
            id_heroe = generar_codigo_heroe(cont_heroes, "F") # pasamos como argumento el contador 
            
            agregar_codigo_heroe(heroe, id_heroe)

            if flag == True: # guardamos el primer ingreso utilizando una bandera
                primer_ingreso = id_heroe
                flag = False

        ultimo_ingreso = id_heroe # guardamos el ultimo ingreso cuando salimos del programa
            
    print("* Se asignaron" , cont_heroes , "codigos \n",
        "* El codigo del primer heroe es", primer_ingreso ,"\n",
        "* El codigo del segundo heroe es",  ultimo_ingreso ,"\n"
        )

# 2.4        

stark_henerar_codigos_heroes(lista_heroes)      
# agregar_codigo_heroe(heroe, id_heroe)

