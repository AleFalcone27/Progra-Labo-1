from data_stark import lista_personajes
import re
from funciones import *
import json



h = {  "nombre": "Howard the Duck",
"identidad": "Howard (Last name unrevealed)",
"empresa": "Marvel Comics",
"altura": "79.349999999999994",
"peso": "18.449999999999999",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Yellow",
"fuerza": "2",
"inteligencia": ""
}

# 1.1
def imprimir_menu_desafio_5():
# Esta función:
# No recibe parametros
# reutilizamos la funcion imprimir_dato e imprimimos por pantalla las opciones del menu
# No devuelve nada
    opciones = ("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n"
    "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n" 
    "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"                                                                         
    "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
    "E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n"
    "F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n"
    "G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n"
    "H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F\n"
    "I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)\n"
    "J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
    "K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
    "L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con 'No Tiene')\n"
    "M. Listar todos los superhéroes agrupados por color de ojos.\n"
    "N. Listar todos los superhéroes agrupados por color de pelo.\n"
    "O. Listar todos los superhéroes agrupados por tipo de inteligencia\n")
    imprimir_dato(opciones)
    
# 1.2
def stark_menu_desafio_5():
# Esta función:
# No recibe parametros
# Imprime el menu principal, toma un input del usuario y valida que este se encuentre dentro de las opciones permitidas 
# En el caso de que corresponda con una de las opciones devuelve el input y en el caso de que no devuelve -1
    imprimir_menu_desafio_5()
    opcion_elegida = input("Ingrese una opcion: ")
    opcion_elegida = opcion_elegida.upper()
    if re.search("[A-O]", opcion_elegida) or opcion_elegida == "Z":
        return opcion_elegida
    else:
        return -1
        
# 1.3
# def stark_marvel_app_5():
    # opcion_elegida = stark_menu_desafio_5()
    # match opcion_elegida:
    #     case "A":
    #         sorteador_generos_nombre("M")
    #     case "B":
    #         sorteador_generos_nombre("F")
    #     case "C":
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"M")
    #         print("El superhéroe ma alto mide", mas_alto)
    #     case "D":
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"F")
    #         print("La superhéroe mas alta mide", mas_alto)
    #     case "E":
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista_personajes,"M")
    #         print("El superhéroe menos alto mide", menos_alto)
    #     case "F":
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista_personajes,"F")
    #         print("La superhéroe menos alta mide", menos_alto)
    #     case "G":
    #         print(promedio_altura("M"))
    #     case "H":
    #         print(promedio_altura("F"))
    #     case "I":
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"M")
    #         print("El superheroe mas alto es", nombre_mas_alto)
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"F")
    #         print("La superheroe mas alta es", nombre_mas_alto )
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista_personajes,"M")
    #         print("El superheroe menos alto es", nombre_menos_alto)
    #         mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista_personajes,"F")
    #         print("La superheroe menos alta es", nombre_menos_alto)
    #     case "J":
    #         cantidad_atributo_x(lista, "color_ojos") ## ASIGNAR EL NO TIENE
    #     case "K":
    #         cantidad_atributo_x(lista, "color_pelo") ## ASIGNAR EL NO TIENE
    #     case "L":
    #         cantidad_tipo_inteligencia() ## ASIGNAR EL NO TIENE

# 1.4
def leer_archivo(nombre_archivo:str)->list[dict]:

# eta función toma los datos que se encuentran en el archivo json pasado como parametro y lo transforma a a una lista de diccionarios
    dict_json = {}
    
    archivo = open(nombre_archivo,"r")
    
    dict_json = json.load(archivo)
    
    archivo.close()
    
    return dict_json["heroes"]

# 1.5
def guardar_archivo(nombre_archivo:str, contenido:str)->bool:
    
# Recibe como parametros nombre_archivo un str con el nombre del archivo y contenido: otro str que tiene el contenido a guardar en el archivo
# Devuelve True en caso ed que el archivo se haya creado con exito, cso contrario devuelve False
    archivo = open("archivo.csv", "w")
    
    if contenido in archivo:
        mensaje = "Se creó el archivo" ,nombre_archivo
        retorno =  True
    else:
        mensaje = "Error al creal el archivo", nombre_archivo
        retorno =  False 
        
    return retorno

# 1.6
def capitalizar_palabras(string:str)->str:
    
# esta funcion recibe como parametro un str y devulve el mismo con todas las letras en minuscula menos las primeras de cada palabra
    
        palabras_capitalizadas = []
        string = string.split(" ")
    
        for palabra in string:
            palabra = palabra.capitalize()
            
            palabras_capitalizadas.append(palabra)
            
        palabras_capitalizadas = " ".join(palabras_capitalizadas)
        
        return palabras_capitalizadas
    
# 1.7
def obtener_nombre_capitalizado(heroe:dict)->str:
    
    #esta funcion recibe un diccionario como parametro, y reutiliza la funcion capitalizar_palabras 
    nombre = heroe["nombre"] 
    
    nombre_capitalizado = capitalizar_palabras(nombre)
    
    nombre_capitalizado = "Nombre: " + nombre_capitalizado
    
    return nombre_capitalizado

# 1.8
def obtener_nombre_y_dato(heroe:dict,llave:str)->str:
    
# recibe como parametros un diccionario y un str con una key (solo entre comillas, sin apuntar al valor de la llave)        

    llave_capitalizada = capitalizar_palabras(llave)
    string = obtener_nombre_capitalizado(h) + " | " +  llave_capitalizada + ": " + heroe[llave]

    return string
