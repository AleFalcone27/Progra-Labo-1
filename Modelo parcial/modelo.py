import json
import re


def parse_json_stark(nombre_archivo:str)->list[dict]:
        
    dict_json = {}
    
    archivo = open(nombre_archivo,"r")
    
    dict_json = json.load(archivo)
    
    archivo.close()
        
    return dict_json["heroes"] 

lista_heroes = parse_json_stark("data_stark.json")

lista_aux = lista_heroes.copy()

def normalizar_flotantes(lista:list[dict], llave:str)->float:
    for i in lista:
        i[llave] = float(i[llave]) 
        
def normalizar_entero(lista:list[dict], llave:str)->int:
    for i in lista:
        i[llave] = int(i[llave]) 

normalizar_flotantes(lista_aux,"altura")
normalizar_flotantes(lista_aux,"peso")
normalizar_entero(lista_aux,"fuerza")

# 1
def listar_n_heroes(lista:list, cantidad:int)-> list:

    if cantidad <= len(lista_aux):
        lista_n_heroes = []
        
        # Agregar la funcion sanitizar entero positivo
    
        for i in range(cantidad):
            heroe = lista_aux[i]["nombre"]
            lista_n_heroes.append(heroe) 
            print(heroe)
        
        return lista_n_heroes   
        
    else:
        
        print("No existen tantos heroes")
        

# listar_n_heroes(lista_aux,23)

# 2
def ordenar(lista:list[dict], clave:str, tipo = "ASC")->list:
    bandera_swap = True
    while bandera_swap == True: 
        bandera_swap = False 
        for i in range(len(lista)-1): # Si en ninguna de las iteraicones se cumple la condicion, bandera == False y sale del codigo
            if tipo == "ASC":
                if lista[i][clave] < lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
            elif tipo == "DESC":
                if lista[i][clave] > lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True      
    return lista_aux
lista_aux = ordenar(lista_aux,"altura","ASC")

# 3
lista_aux = ordenar(lista_aux,"fuerza","ASC")

# 4 Anidar esta con calcular menor o mayor
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

def calcular_menor_o_mayor(lista:list[dict],llave:str,tipo:str,comparador:float) -> list:
    lista_menores = []
    lista_mayores = []
    if tipo == "menor":
        for i in lista:
            if i["altura"] < comparador: #recordar castear en caso de ser necesario
                lista_menores.append(i["nombre"])
        retorno = lista_menores
    if tipo == "mayor":
        for i in lista:
            if i["altura"] > comparador: #recordar castear en caso de ser necesario
                lista_mayores.append(i["nombre"])         
        retorno = lista_mayores   

    return retorno
# promedio = calcular_promedio(lista_aux,"altura")
# calcular_menor_o_mayor(lista_aux,"altura","menor",promedio)
# print(promedio)
# normalizar_flotantes(lista_aux, "altura")

# lista_aux = ordenar(lista_aux, "altura", "ASC")

# 5
def sort_llave(lista:list[dict],llave:str,valor:str):
    lista_sort = []
    for i in lista_aux:
        if re.match(valor,i[llave]):
            lista_sort.append(i["nombre"])
    return lista_sort
    
# print(sort_llave(lista_aux,"inteligencia","average"))


# def depurar_ultimo_separador(separador:str,contenido:str,nombre_archivo:str,largo_cotenido:int):
#     with open(nombre_archivo, "w") as archivo:
#             archivo.readlines()
#             re.sub(separador,"",contenido,largo_cotenido)
#             print(contenido)
#   depurar_ultimo_separador(",",contenido,"parcial.cvs",len(contenido)) 


# 6
def export_a_csv(contenido:list,nombre_archivo:str):

    with open(nombre_archivo,"w+") as archivo:
        
        for i in contenido:
            valor = str(i) + ","
            archivo.write(valor)   
export_a_csv(sort_llave(lista_aux,"inteligencia","average"),"modelo.cvs")


        
