from data_stark import lista_personajes as lista_personajes

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
def extraer_iniciales(nombre_heroe:str):
    
    # validamos que el string ingresado no este vacio
    if nombre_heroe == "":
        return "N/A"
    nombre_heroe = nombre_heroe.upper()
    nombre_heroe = nombre_heroe.strip()
    
    # remplazamos el "THE" por un espacio en blanco 
    nombre_heroe = nombre_heroe.replace("THE","") 
    
    # remplazamos el - por un espacio en blanco 
    nombre_heroe = nombre_heroe.replace("-","") 
    
    # creamos una lista
    lista_nombre_heroe = nombre_heroe.split() 

    # por cada uno de los elementos de la lista me quedo con el primero
    # entre cada elemento de la lista los une con un string vacio y devuelve un string
    iniciales = ""
    for i in range(len(lista_nombre_heroe)):
        iniciales = iniciales + lista_nombre_heroe[i][0] + "." 
        
    return iniciales


# 1.2
def definir_iniciales_nombre(heroe:dict):
    # validamos que el argumento pasado sea un diccionario y que este contenga la clave "nombre"
    if type(heroe) != dict or "nombre" not in heroe:
        return False
    
    # verificamos que el dict no tenga la clave "iniciales"
    if "iniciales" not in heroe:
        heroe["iniciales"] = iniciales
        return True

# 1.3
def agregar_iniciales_nombre(lista_personajes):
    # validamos que el argumento pasado sea del tipo list y que tenga al menos un elemento
    if type(lista_personajes) == list or len(lista_personajes) > 0: 
        
        for i in lista_personajes:
            # verificamos que la funcion definir_inciales_nombre() se haya ejecutado correctamente en base al valor de retorno
            validacion = definir_iniciales_nombre(i)
            if validacion == False:
                resultado = "El ordigen de los datos no coentiene el formato correcto"
            else:
                resultado = True
            return resultado
# 1.4 
def stark_imprimir_nombres_con_iniciales(lista_personajes:list):
    resultado = agregar_iniciales_nombre(lista_personajes)
    for i in lista_personajes:
        nombre = i["nombre"]
        i["iniciales"] = iniciales 
        print("*", nombre, "(" + iniciales + ")")



