from data_stark import lista_personajes

# Creo la lista de opciones 
opciones = ["Elija la opcion:",
"Presione 1 para obtener todos los nombres de los superhéroes",
"Presione 2 para obtener los nombres y alturas de cada uno de los superhéroes",
"Presione 3 para obtener la altura promedio", 
"Presione 4 para obtener el superhéreo mas alto y mas bajo", 
"Presione 5 para obtener el superhéroe mas y menos pesado" ] 

lista = lista_personajes


# B Recorrer la lista_personajes imprimiendo por consola el nombre de cada superhéroe
def informar_nombre(lista):
    for i in lista:
        print(i["nombre"])
        

# C Recorrer la lista_personajes imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def informar_nombre_y_altura(lista):
    for i in lista:
        print(i["nombre"], float(i["altura"]))
            
# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def informar_altura_promedio(lista):
    acum_alturas = 0
    cantidad_personajes = 0
    for i in lista:
        acum_alturas = acum_alturas + float(i["altura"])
        cantidad_personajes = cantidad_personajes + 1
    promedio_altura = acum_alturas / cantidad_personajes
    promedio_altura = round(promedio_altura,2) # funcion round(numero, cantidad de decimales) 
    return promedio_altura
    
# D. Recorrer la lista y determinar cuál es el superhéroe más mas_alto (MÁXIMO)
# # E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def informar_mas_y_menos_alto(lista):
    nombre_mas_alto = None
    nombre_mas_bajo = None
    mas_bajo = None
    mas_alto = None
    for i in lista:
        # Si la primer condicion es verdadera python nisiquiera lee la segunda y ejecuta el codigo de todas maneras
        if mas_alto == None or float(i["altura"]) > mas_alto: # En la primer vuelta se cumple la primer condicion y en las siguientes solo se entra al if si i["altura"] > mas_alto y se pisa la variable con los valores de la iteracion en curso 
            mas_alto = float(i["altura"]) 
            nombre_mas_alto = i["identidad"]
        if mas_bajo == None or float(i["altura"]) < mas_bajo:
            mas_bajo = float(i["altura"])
            nombre_mas_bajo = i["identidad"]
            
    identidad_mas_bajo = "El superhéroe mas alto es ", nombre_mas_alto, "y mide", mas_alto
    identidad_mas_alto = "El superhéroe mas bajo es ", nombre_mas_bajo, "y mide", mas_bajo
        
    return identidad_mas_alto, identidad_mas_bajo

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
        
