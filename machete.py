import re
import json

## MACHETE ##
# - TENGO QUE PROBAR TODAS LAS FUNCIOENES PARA VER SI FUNCIONAN 
# - hACER LAS FUNCIONES MAS INDEPENDIENTES 
# - HACER VALIDACIONES 

# --- NORMALIZAR DATOS -- #

# -- NORMALIZA TODOS LOS DATOS QUE DE LA LIST:[DICT] QUE RECORREMOS -- #

def normalizar_flotantes(lista:list[dict], llave:str)->float:
    
#Esta funcion itera sobre la lista de diccionarios pasada como parametro y castea la llave a flotante

    for i in lista:
        i[llave] = float(i[llave]) 

def normalizar_entero(lista:list[dict], llave:str)->int:
    
    #Esta funcion itera sobre la lista de diccionarios pasada como parametro y castea la llave a entero
    
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
        return -3

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
        
    return retorno

## -- DECORADORES -- ##

def generara_separador(patron:str, largo:int, imprimir = True):
    
    """
    toma como parametros:
    - patron: un carácter que se utilizará como patrón para generar el separador
    - largo: un número que representa la cantidad de caracteres que va ocupar el separador.
    - imprimir: un parámetro opcional del tipo booleano (por default definir en True) que determina si la funcion va a devolver un valor o a printearlo
    Devuelve o imprime el patron pasado como parametro (patron) la cantidad de veces que lo determinemos en el argumento largo
    """
    
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

    """
    Esta funcion crea una "pared" con el separador pasado por parametro 
    Recibe como parametros:
    - linea: todos los caracteres a printear en la linea donde llamos a la funcion 
    - ubicacion: ubicacion de la linea en la cual queremos printear el separador
    - separador: string que queremos printear al final de la linea
    - Devuelve un string con la cantidad de espacios en blanco pasada en el parametro ubicacion y al final el separador 
    - Se recomienda llamar la funcion dentro de un print() aunque si guardamos el valor de retorno en una variable se puede llamar fuera de un print()
    """
    string = ""
    for i in range(ubicacion - len(linea)):
        string = string + " " 
    string = string + "|"
    return string

## -- ARCHIVOS -- ##

def parse_json(nombre_archivo:str)->list[dict]:
    
    """
    Esta funcion se encarga de leer un archivo json y devolverlo como diccionario 
    """
    
    dict_json = {}
    
    archivo = open(nombre_archivo,"r")
    
    dict_json = json.load(archivo)
    
    archivo.close()
        
    return dict_json["valor"] 

def guardar_en_csv(lista:list[dict]):
    with open("juegos.csv","w+") as archivo:
            for i in lista:
                linea = str(i["nombre"]) + "," + str(i["ventas"]) + "," + str(i["plataforma"]) + "," + (i["fecha_lanzamiento"]) + "," + i["desarrolladora"] + "," + i["genero"] + "," + str(i["precio"]) + "," + str(i["critica"]) + "," + i["clasificacion"] + "," + "\n"  
                archivo.write(linea)

def guardar_en_json(lista:list[dict]):
    
    """
    Esta funcion realiza el guaradado de la lista de diccionarios pasada como parametro en un archivo con el formato json. 
    Itera sobre cada uno de los diccionarios anexando los key y values al valor de la unica llave en el nuevo diccionario
    No devuelve nada 
    """

    data = {"personajes": []}
    
    for i in lista:
            data["personajes"].append({"nombre": i["nombre"], "rol": i["rol"], "atributos": i["atributos"]})

    with open("data,json", "w") as file:
        json.dump(data, file, indent=2)


## -- OPERACIONES -- ##

def calcular_promedio(lista:list[dict], llave)-> float:
    
    """
    esta funcion itera sobre una lista de diccionarios, acumula los valores asignados a la key pasada como parametro,
    calcula el promedio y lo retorna
    """
    
    acum = 0
    cont = 0
    for i in lista:
        acum = acum + i[llave]
        cont = cont + 1
        
    promedio = acum / cont
    
    promedio = round(promedio,2) # funcion round(numero, cantidad de decimales) 

    return promedio

def ordenar(lista:list[dict], clave:str, tipo:str)->list:

    """
    Esta funcion utiliza el algoritmo de ordenamiento burbujeo
    La variable aux se utiliza como pivote para hacer el swap de valores
    Devuelve una lista ordenada segun la clave que le hayamos pasado como parametro y el tipo ya sea ascendente o descendente
    """

    bandera_swap = True
    while bandera_swap == True: 
        bandera_swap = False 
        for i in range(len(lista)-1): # Si en ninguna de las iteraicones se cumple la condicion, bandera == False y sale del codigo
            if tipo == "ASC":
                if lista[i][clave] > lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
            elif tipo == "DESC":
                if lista[i][clave] < lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True    
    return lista

def calcular_menor_o_mayor(lista:list[dict],llave:str,tipo:str,comparador:float) -> list:
    lista_menores = []
    lista_mayores = []
    if tipo == "menores":
        for i in lista:
            if i[llave] < float(comparador): #recordar castear en caso de ser necesario
                lista_menores.append(i)
        return lista_menores
    if tipo == "mayores":
        for i in lista:
            if i[llave] > float(comparador): #recordar castear en caso de ser necesario
                lista_mayores.append(i)         
        return lista_mayores   

def buscar_llave(lista:list[dict],llave:str,valor:str):
    
    """
    Esta funcion itera la lista de diccionarios pasada por parametro y crea una nueva lista anexando a la misma aquellos diccionarios que 
    contengan en la key pasada como parametro el valor buscado
    Esta funcion recibe como parametro:
        - lista: una lista de diccionarios
        - llave: un string que representa una key
        - valor: un string que representa un valor a buscar las keys de los diccionarios 
    """
    
    lista_sort = []
    for i in lista:
        if re.match(valor,i[llave]):
            lista_sort.append(i)
    return lista_sort

def informar_nombre(lista:list[dict], llave:str):
# esta función itera sobre una lista de diccionarios y printea el valor vinculado a la key pasada como parametro
    for i in lista:
        print(llave)

def informar_nombre_y_altura(lista:list[dict],llave1, llave2):
# esta función itera sobre una lista de diccionarios y printea los valores vinculados a las keys pasada como parametros
    for i in lista:
        print(i[llave1], i[llave2])    

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

def calcular_maximo(lista:list[dict],llave:str):
    """  
    Esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande que existe asignado a la clave pasada como parametro 
    Recibe como parametros:
    - lista: una lista de diccionarios
    - llave: un string que representa una llave 
    """
    nombre_max = None
    max = None
    for i in lista:
        if max == None or float(i[llave]) > max: #recordar castear en caso de ser necesario
            max = float(i[llave]) 
            nombre_max = i[max]
            
    return max , nombre_max

def calcular_minimo(lista:list[dict],llave): 
    """  
    Esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande que existe asignado a la clave pasada como parametro 
    Recibe como parametros:
    - lista: una lista de diccionarios
    - llave: un string que representa una llave 
    """
    for i in lista:
        if mini == None or float(i[llave]) < mini: #recordar castear en caso de ser necesario
                mini = float(i[llave])
                nombre_mini = i[mini]
            
    return mini , nombre_mini  

def calcular_maximo_o_minimo(lista:list[dict],llave:str,tipo:str):
    
    """  
    Esta funcion itera sobre una lista de diccionarios y calcula el valor mas grande o mas pequeño que existe asignado a la clave pasada como parametro 
    Recibe como parametros:
    - lista: una lista de diccionarios
    - llave: un string que representa una llave 
    - tipo: un string que determina el modo de busqueda (ya sea un minimo o un maximo)
    """
    
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
    
    flag = False
    while True:
        
        opcion_elegida = menu_principal(opciones)
        match opcion_elegida:
            case "1":
                if flag == False:
                    lista_retorno = opcion_1(lista_copia)
                    flag = True
                else:
                    lista_retorno = opcion_1(lista_retorno)
                    
            case  "2":
                if flag == False:
                    lista_retorno = opcion_2(lista_copia)
                    flag = True
                else:
                    lista_retorno = opcion_2(lista_retorno)

            case "3":
                if flag == False:
                    lista_retorno = opcion_3_1(lista_copia)
                    flag = True
                else:
                    lista_retorno = opcion_3_1(lista_retorno)

            case "4":
                if flag == False:
                    lista_retorno = opcion_4(lista_copia)
                    flag = True
                else:
                    lista_retorno = opcion_4(lista_retorno)
            
            case "5":
                if flag == False:
                    lista_retorno = opcion_5(lista_copia)
                    flag = True
                else:
                    lista_retorno = opcion_5(lista_retorno)
                
            case "6":
                if flag == False:
                    lista_retorno = opcion_6(lista_copia)
                    flag = True
                else:
                    lista_retorno = opcion_6(lista_retorno)
                    
            case other:
                app()

app()