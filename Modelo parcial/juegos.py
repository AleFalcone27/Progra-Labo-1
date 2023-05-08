import json
import re

def parse_json_juegos(nombre_archivo:str)->list[dict]:
        
    dict_json = {}
    
    archivo = open(nombre_archivo,"r")
    
    dict_json = json.load(archivo)
    
    archivo.close()
        
    return dict_json["juegos"] 


lista_juegos = parse_json_juegos("Modelo parcial\juegos.json")

copia_juegos = lista_juegos.copy()

## NORMALIZO DATOS
def normalizar_flotantes(lista:list[dict], llave:str)->float:
    
## Esta funcion itera sobre los diccionarios dentro de una lista y castea la llave pasada como parametro a flotante
    
    for i in lista:
        i[llave] = float(i[llave]) 

normalizar_flotantes(copia_juegos,"precio")
normalizar_flotantes(copia_juegos,"critica")

def normalizar_entero(lista:list[dict], llave:str)->int:
    for i in lista:
        i[llave] = int(i[llave]) 
        
normalizar_entero(copia_juegos,"ventas")



## CREO LAS FUNCIONES 

# 1
def listar_n_juegos(lista:list[dict], cantidad:int)-> list:

# Esta funcion itera sobre los dicts dentro de la lista y lista por consola la cantidad pasada como parametro 
    
    if cantidad <= len(lista):
        lista = lista[0:cantidad]
        
    else:
        print("No existen tantos juegos")
    
    return lista

# 2
def ordenar(lista:list[dict], clave:str, tipo:str)->list:
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

# 3
def buscar_valor(lista:list[dict[list]],llave:str,valor:str):
    lista_sort = []
    for i in lista:
        if valor in i[llave]:
            lista_sort.append(i)
    return lista_sort


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

def opcion_1():
    cantidad = input("Cuantos juegos queres ver?: ")
    cantidad = int(cantidad)
    lista_retorno = listar_n_juegos(copia_juegos, cantidad)

    print(generara_separador("-", 40 ,False))
    for i in lista_retorno:
        print(i["nombre"], generar_pared(i["nombre"], 38,"|"))   
    print(generara_separador("-", 40 ,False))

def opcion_2(): 
    tipo = input("Queres ordenarlos de manera ascendente o descentedente [ASC - DESC]: ")
    tipo = tipo.upper()
    while re.match("[^ASC|DESC$]", tipo) == None:
        tipo = input("Error: Queres ordenarlos de manera ascendente o descentedente [ASC - DESC]: ")
        tipo = tipo.upper()
    lista_retorno = ordenar(copia_juegos,"ventas","ASC")
    print(generara_separador("-", 60 ,False))
    for i in lista_retorno:
        linea = i["nombre"] + " " + "$" + str(i["ventas"])
        print(linea, generar_pared(linea, 60 ,"|"))
        print(generara_separador("-", 60 ,False))


def opcion_3_0():
    opciones_plataformas = []
    for i in copia_juegos:
        for i in i["plataforma"]:
            if i not in opciones_plataformas:
                opciones_plataformas.append(i)        
    for i in opciones_plataformas:
        print("-" , i)
    return opciones_plataformas

def opcion_3_1():
    opciones = opcion_3_0()
    plataforma_buscada = input("Ingrese una plataforma: ")
    plataforma_buscada  = plataforma_buscada.upper()
    
    while plataforma_buscada not in opciones:
        plataforma_buscada = input("Ingrese alguna plataforma de las listadas arriba: ")
    plataforma_buscada  = plataforma_buscada.upper()
    lista_sort = buscar_valor(copia_juegos,"plataforma", plataforma_buscada)
    print(generara_separador("-", 170 ,False))
    
    for i in lista_sort:
        linea = i["nombre"] + " " + str(i["plataforma"])
        print(linea, generar_pared(linea, 170 ,"|"))
    print(generara_separador("-", 170 ,False))
    
def opcion_4():
    valor = input("Con que clasificacion queres quedarte? [E - T - M]: ")
    valor = valor.upper()
    while re.match("[E|T|M]",valor) == None:
        valor = input("Con que clasificacion queres quedarte?: [E - T - M]: ")
        valor = valor.upper() 
    lista_copia = buscar_valor(copia_juegos,"clasificacion",valor)
    print(generara_separador("-", 50 ,False))
    for i in lista_copia:
        linea = i["nombre"]
        print(linea, generara_separador("-", 50 ,False))
    print(generara_separador("-", 50 ,False))

def opcion_5():
    tipo = input("De que manera los queres ordenar descendiente o ascendente [ASC -DESC]: ")
    tipo = tipo.upper()
    while re.match("[^ASC|DESC$]", tipo) == None:
        tipo = input("Error: Desea ordenar de manera descendiente o ascendente [ASC -DESC]: ")
        tipo = tipo.upper()
    copia_juegos = ordenar(copia_juegos,"precio",tipo)
    print(generara_separador("-", 50 ,False))
    for i in copia_juegos:
        linea = i["nombre"] + " " + "%" + i["precio"]
        print(linea, generara_separador("-", 50 ,False))
    print(generara_separador("-", 50 ,False))
    
opciones = ["1) Listar juegos","2) Ordenar por cantidad de ventas", "3) Filtrar juegos por plataforma", "4) Filtrar por clasificacion", "5) Listar por precio"]

def menu_principal(opciones:list):
    for i in opciones:
        print(i)
        
    opcion_elegida = input("Elija una opcion: ")
    
    return opcion_elegida

def app():
    
##recordemos castear la opcion

    while True:
        
        opcion_elegida = menu_principal(opciones)

        if opcion_elegida == "1":
            opcion_1()
            
        elif opcion_elegida == "2":
            opcion_2()

        elif opcion_elegida == "3":
            opcion_3_1()

                    
        elif opcion_elegida == "4":
            opcion_4()
        
        elif opcion_elegida == "5":
            opcion_5()
        

        # elif opcion_elegida == 5:
            

        # elif opcion_elegida == 6:

            
        # elif opcion_elegida == 7:
            
        # else:
        #     break

app()

## arreglar las validaciones del 5
## HACER LAS BANDERAS PARA QUE LA MOFICACION DE LA LISTA SEA ALGO ACUMULATIVO 
## HACER EL GUARDADO DEL ARCHIVO 