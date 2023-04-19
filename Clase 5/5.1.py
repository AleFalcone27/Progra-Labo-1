from data_stark import lista_personajes as lista

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def sorteador_generos(genero:str):
    for i in lista:
        if i["genero"] == genero:
            print(i["nombre"])

sorteador_generos("M")
sorteador_generos("F")

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
def informar_mas_y_menos_alto(lista:list,genero:str):
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
        
mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"F")
print("La superheroe mas alta es", nombre_mas_alto , "y mide:", mas_alto )

mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"M")
print("El superheroe mas alto es", nombre_mas_alto , "y mide:", mas_alto )

mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"F")
print("La superheroe menos alta es", nombre_menos_alto, "y mide:", menos_alto )

mas_alto, nombre_mas_alto, menos_alto , nombre_menos_alto = informar_mas_y_menos_alto(lista,"M")
print("El superheroe menos alto es", nombre_menos_alto, "y mide:", menos_alto )


def promedio_altura(genero:str):
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
        
        if atributo == "":
            atributo = "No tiene"
        
        if atributo not in dict: # Brown es una clave del diccionario ojos?
            dict[atributo] = 0 # Si no esta el color le ponemos 0 # Le estamos cambiando el valor a la clave "Marron"o "Azul"  # Azul
        dict[atributo] = dict[atributo] + 1 # Le sumamos 1 #chekear como funciona esto llave valor

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
        