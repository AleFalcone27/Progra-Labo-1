## MACHETE ##
# - TENGO QUE PROBAR TODAS LAS FUNCIOENES PARA VER SI FUNCIONAN 

# --- NORMALIZAR DATOS -- #
 
# -- NORMALIZA TODOS LOS DATOS QUE DE LA LIST:[DICT] QUE RECORREMOS -- #

def normalizar_flotantes(lista:list[dict], llave:str)->float:
    for i in lista:
        i[llave] = float(i[llave]) 
        

def normalizar_entero(lista:list[dict], llave:str)->int:
    for i in lista:
        i[llave] = int(i[llave]) 

# -- NORMALIZA DATOS ESPECIFICOS -- #

def sanitizar_entero(num_str:str):
    
# esta funcion determina si el str recibido como parametro es un numero entero positivo y lo retorna  

    num_str = str(num_str)
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
    
# esta funcion determina si el str recibido como parametro es un flotante positivo
    num_str = str(num_str)
    num_str = num_str.strip()
    
    if re.search("[a-zA-Z]+", num_str):
        return -1
    elif re.search("^-",num_str):
        return -2
    elif re.search("[0-9+]",num_str):
        num_str = float(num_str)
        return num_str
    else: 
        return -


def sanitizar_string(num_str:str, valor_por_defecto="-"):

# determina si el str recibido como parametro es solo texto

    num_str = re.sub("/"," ",num_str)
    
    if re.search("[0-9+]",num_str):
        return "N/A"
    elif num_str == "":
        valor_por_defecto = valor_por_defecto.lower()
        return valor_por_defecto
    else:
        num_str = num_str.lower()
        return num_str


def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str):

# sanitiza utilizando las funciones creadas en los puntos anteriores segun el tipo de dato que le pasemos como parametro 
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

## -- DECORADORES -- ##

def generara_separador(patron:str, largo:int, imprimir = True):

    # toma como parametros:
    # ● patron: un carácter que se utilizará como patrón para generar el
    # separador
    # ● largo: un número que representa la cantidad de caracteres que va
    # ocupar el separador.
    # ● imprimir: un parámetro opcional del tipo booleano (por default definir
    # en True)
    # esta funcion devuelve o imprime el patron pasado como parametro (patron) la cantidad de veces que lo determinemos en el argumento largo

        if len(patron) > 0 and largo > 0 and largo < 236 :
            for i in range(largo):
                
                string = patron * largo
                
            if imprimir == True:
                
                print(string, end="")
            else:
                
                return string
            
        else: 
            print("N/A")

def generar_pared(linea:str,ubicacion:int,separador:str):
    string = ""
    for i in range(ubicacion - len(linea)):
        string = string + " " 
    string = string + "|"
    return string


## -- OPERACIONES -- ##


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

## -- MENU PRINCIPAL CON OPCIONES --

opciones = ["","","","","",""]

def menu_principal(opciones):
    for i in opciones:
        print(i)
        
    opcion_elegida = input("Elija una opcion: ")
    
    return opcion_elegida

def app():
    
##recordemos castear la opcion
    
    while True:
        
        opcion_elegida = menu_principal(opciones)
        
        if opcion_elegida == 1:
            

        elif opcion_elegida == 2:

                    
        elif opcion_elegida == 3:

                    
        elif opcion_elegida == 4:
        
            
        elif opcion_elegida == 5:
            

        elif opcion_elegida == 6:

            
        elif opcion_elegida == 7:
            
        else:
            break