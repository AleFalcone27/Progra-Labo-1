## MACHETE ##
# - TENGO QUE PROBAR TODAS LAS FUNCIOENES PARA VER SI FUNCIONAN 

lista = lista_personajes


def informar_nombre(lista:list[dict], llave:str):
# esta función itera sobre una lista de diccionarios y printea el valor vinculado a la key pasada como parametro
    for i in lista:
        print(llave)
        

def informar_nombre_y_altura(lista:list[dict],llave1, llave2):
# esta función itera sobre una lista de diccionarios y printea los valores vinculados a las keys pasada como parametros
    for i in lista:
        print(i[llave1], i[llave2])
            

def calcular_promedio(lista:list[dict], llave)-> float:
# esta funcion itera sobre una lista de diccionarios acumulando el valor asignado a la key pasada como parametro y sacando el promedio
    acum = 0
    cont = 0
    for i in lista:
        acum = acum + i[llave]
        cont = cont + 1
        
    promedio = acum / cont
    
    promedio = round(promedio,2) # funcion round(numero, cantidad de decimales) 
    
    return promedio
    
def calcular_promedio_genero(lista:list[dict],llave:str,genero:str)-> float:
    acum = 0
    cont = 0
    for i in lista:
        if i["genero"] == genero:
            acum = acum + float(i[llave]) # normalizar los datos o castear en la funcion
            cont = cont + 1
        
    promedio = acum / cont
    
    promedio = round(promedio,2) # funcion round(numero, cantidad de decimales) 
    
    return promedio


def calcular_maximo(lista,llave): #QUE DEVUELVE?
# esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande que existe asignado a la clave pasada como parametro 
    nombre_max = None
    max = None
    for i in lista:
        if max == None or float(i[llave]) > max: #recordar castear en caso de ser necesario
            max = float(i[llave]) 
            nombre_max = i[max]
            
    return max , nombre_max


def calcular_minimo(lista:list[dict],llave): #QUE DEVUELVE?
    for i in lista:
        if mini == None or float(i[llave]) < mini: #recordar castear en caso de ser necesario
                mini = float(i[llave])
                nombre_mini = i[mini]
            
    return mini , nombre_mini  
    
def calcular_maximo_o_minimo(lista:list[dict],llave:str,tipo:str):
# esta funcion itera sobre una lista de diccionarios y calcula el valor mas pequeño que existe asignado a la clave pasada como parametro 
    nombre_mini = None
    mini = None
    if tipo == "menor":
        for i in lista:
            if mini == None or float(i[llave]) < mini: #recordar castear en caso de ser necesario
                    mini = float(i[llave])
                    nombre_mini = i[mini]    
        return mini , nombre_mini             
    elif tipo == "mayor":
            nombre_max = None
            max = None
            for i in lista:
                if max == None or float(i[llave]) > max: #recordar castear en caso de ser necesario
                    max = float(i[llave]) 
                    nombre_max = i[max]
            
    return max , nombre_max
        

def calcular_min_genero(lista:list,llave:str,genero:str):
    # esta funcion itera sobre una lista de diccionarios y calcula el valor mas pequeño que existe dentro del genero especificado, asignado a la clave pasada como parametro 
    nombre_mini = None
    mini = None
    for i in lista:
        if genero == i["genero"]:
            if mini == None or (i[llave]) < mini: #recordar castear en caso de ser necesario
                mini = (i[llave]) #recordar castear en caso de ser necesario
                nombre_mini = i["nombre"]
                
    return nombre_mini  # devuelvo solo el nombre


def calcular_max_genero(lista:list,llave:str,genero:str):
# esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande que existe dentro del genero pasado como parametro, asignado a la clave tambien pasada como parametro 
    nombre_max = None
    max = None
    for i in lista:
        if genero == i["genero"]:
            if max == None or float(i[llave]) > max: #recordar castear en caso de ser necesario
                max = float(i[llave]) 
                nombre_max = i["nombre"]
            
    return nombre_max # solo retorno el nombre
calcular_max_genero(lista_heroes,"altura","F")

AGREGAR VALIDACIONES CON REGEX DE TODOS LOS TIPOS DE DATOS CON MATCH
        
--------------------------------------------------------------------------------

# H. Calcular e informar cual es el superhéroe más y menos pesado.
def informar_mas_y_menos_pesado(lista):
    mas_pesado = None
    menos_pesado = None
    for i in lista:
        if mas_pesado == None or float(i["peso"]) > mas_pesado:
            mas_pesado = float(i["peso"])
            nombre_mas_pesado = i["nombre"]
        if menos_pesado == None or  float(i["peso"]) < menos_pesado:
            menos_pesado = float(i["peso"]) 
            nombre_menos_pesado = i["nombre"]

def menu_principal(opciones):
    for opcion in opciones:
        print(opcion)
    
    opcion_elegida = input("Elija una opcion: ") 

    return opcion_elegida

while True:
    opcion_elegida = menu_principal(opciones)
    opcion_elegida = int(opcion_elegida) # Casteo la variable y la renombro
    
    match opcion_elegida:
        case 1:
            informar_nombre(lista)    
        case 2:
            informar_nombre_y_altura(lista)
        case 3:
            altura_promedio = informar_altura_promedio(lista)
            print(altura_promedio)
        case 4:
            identidad_mas_alto, identidad_mas_bajo = informar_mas_y_menos_alto(lista)
            print(identidad_mas_alto,identidad_mas_bajo)
        case 5:        
            informar_mas_y_menos_pesado(lista)
        
