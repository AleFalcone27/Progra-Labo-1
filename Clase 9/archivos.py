
def leer_json_stark(nombre_archivo:str):
        
        dict_json = {}
        
        archivo = open(nombre_archivo,"r")
        
        dict_json = json.load(archivo)
        
        return dict_json["heroes"]
    lista_heroes = leer_json_stark("data_starkj.json")
    
    
    # Como generar un csv con una lista:
def guardar_csv_stark(nombre_archivo, lista):
        
        archivo = open(nombre_archivo, "w")
        
        for heroe in lista:
            linea = heroe["nombre"] + "," + heroe["identidad"] + "," + heroe["empresa"] + "," + str(heroe["altura"]) + "," + str(heroe["peso"]) + "," + heroe["genero"] + "," + heroe["color_ojos"] + "," + heroe["color_pelo"] + "," + heroe["fuerza"] + "," + heroe["inteligencia"] + "\n"
            archivo.write(linea)
        archivo.close()
            

guardar_csv_stark("data_stark.cvs",)

    # Como leer un csv
def parse_csv_stark(nombre_archivo:str)->list:
            
        archivo = open(nombre_archivo,"r")
        
        lista_heroes = []    
        
        for linea in archivo:
            
            heroe  = {}
            
            lista = linea.split(",")
            
            # estamos asignando los datos de la lista al diccionario que estamos armando y agregandole la clave pq en el cvs solo vienen los valores
            heroe["nombre"] = lista[0]
            heroe["identidad"] = lista[1]
            heroe["empresa"] = lista[2]
            heroe["altura"] = float(lista[3])
            heroe["peso"] = float(lista[4])            
            heroe["genero"] = lista[5] 
            heroe["color_ojos"] = lista[6]
            heroe["color_pelo"] = lista[7]
            heroe["fuerza"] = re.sub("\n","",lista[8])
            heroe["inteligencia"] = lista[9]
            
            
            lista_heroes.append(heroe)
            
        archivo.close()
        return lista_heroes
    
    lista_heroes_star("")
    pirnt(lista_heroes)