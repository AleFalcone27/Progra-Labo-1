from data_stark import lista_personajes as lista

def imprimir_dato(dato:str):
    print(dato)
    

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def sorteador_generos_nombre(genero:str):
# Esta funcion:
# Recibe como parametro un str que indica un genero
# Itera la lista de diccionarios y printea el nombre de cada uno de los diccionarios en los que se encuentre el valor pasado como parametro
# No retorna nada
    
    for i in lista:
        if i["genero"] == genero:
            print(i["nombre"])

sorteador_generos_nombre("M")
sorteador_generos_nombre("F")

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def informar_mas_y_menos_alto(lista:list[dict],genero:str):
# Esta funciones:
# Esta funcion recibe como parametros una lista de diccionarios y un string que contenga un genero
# Itera en la lista y busca un minimo y maximo segun el genero que pasemos como argumento, guardando el nombre y la altura 
# Devuelve 4 valores como strs

    mas_alto = None
    menos_alto = None
    for i in lista:
        if i["genero"] == genero:
            if mas_alto == None or float(i["altura"]) > mas_alto:
                mas_alto = float(i["altura"])
                nombre_mas_alto = i["nombre"] 
            if menos_alto == None or float(i["altura"]) < menos_alto:
                menos_alto = float(i["altura"])
                nombre_menos_alto = i["nombre"]
                
    return mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto
        
# mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"F")
# print("La superheroe mas alta es", nombre_mas_alto , "y mide:", mas_alto )

# mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"M")
# print("El superheroe mas alto es", nombre_mas_alto , "y mide:", mas_alto )

# mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"F")
# print("La superheroe menos alta es", nombre_menos_alto, "y mide:", menos_alto )

# mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"M")
# print("El superheroe menos alto es", nombre_menos_alto, "y mide:", menos_alto )


def promedio_altura(genero:str):
# Esta funcion:
# Recibe como parametro un str que representa un genero
# Iteramos la lista de personajes segun que genero pasemos como argumento acumulamos las edades, contamos la cantidad de heroes y acumulamos las alturas de los heroes que pertecen a ese genero 
# Devuelve el un float con el promedio de la altura de ese grupo 

    acum = 0
    cont = 0 
    for i in lista:
        if i["genero"] == genero:
            acum = acum + float(i["altura"])
            cont = cont + 1
            promedio_altura = acum / cont
            
    return promedio_altura

promedio_alturas = promedio_altura("F") 
print("El promedio de alturas del genero F es", promedio_alturas)

promedio_alturas = promedio_altura("M") 
print("El promedio de alturas del genero M es", promedio_alturas)


def cantidad_atributo_x(list:list, atributo_buscado:str):
    
    dict = {}
    for i in lista:
        atributo = i[atributo_buscado] # Azul
        if atributo not in dict: # Azul es una clave del diccionario ojos?
            dict[atributo] = 0 # Si no esta el color le ponemos 0 # Le estamos cambiando el valor a la clave "Marron"o "Azul"  # Azul
        dict[atributo] = dict[atributo] + 1 # Le sumamos 1 #chekear como funciona esto llave valor

    for atributo, cantidad in dict.items(): # al poner una coma accedemos a la clave , valor # dict.items{} Returns a list containing a tuple for each key value pair
        print(atributo , cantidad)
        
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# print(cantidad_atributo_x(lista, "color_pelo"))

# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
cantidad_atributo_x(lista, "color_ojos")

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
def cantidad_tipo_inteligencia():
    dict = {}
    for i in lista:
        atributo = i["inteligencia"] # Azul
        
        if len(atributo) == 1:
            dict[atributo] = "No tiene"
        
        if atributo not in dict: # Brown es una clave del diccionario ojos?
            dict[atributo] = 0 # Si no esta el color le ponemos 0 # Le estamos cambiando el valor a la clave "Marron"o "Azul"  # Azul
        dict[atributo] = + 1 # Le sumamos 1 #chekear como funciona esto llave valor

    for atributo, cantidad in dict.items(): # al poner una coma accedemos a la clave , valor # dict.items{} Returns a list containing a tuple for each key value pair
        print(atributo , cantidad)
        
        
# cantidad_tipo_inteligencia()

# # M. Listar todos los superhéroes agrupados por color de ojos.
def listar_color_de_ojos():
    brown = []
    green = []
    for i in lista:
        if i["color_ojos"] == "Brown":
            brown.append(i["nombre"])
        if i["color_ojos"] == "Green":
            green.append(i["nombre"])
            ## Seguir hasta terminar todos los colores
    print(brown)
    print(green)

listar_color_de_ojos()
        