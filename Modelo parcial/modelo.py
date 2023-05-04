import json
import re


def parse_json_stark(nombre_archivo:str)->list[dict]:
        
    dict_json = {}
    
    archivo = open(nombre_archivo,"r")
    
    dict_json = json.load(archivo)
    
    archivo.close()
        
    return dict_json["heroes"] 

lista_heroes = parse_json_stark("Modelo parcial\data_stark.json")

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
            heroe = i["nombre"] 
            lista_n_heroes.append(heroe) 
            print(heroe)
        
        return lista_n_heroes   
    else:
        print("No existen tantos heroes")

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


# 5
def sort_llave(lista:list[dict],llave:str,valor:str):
    lista_sort = []
    for i in lista_aux:
        if re.match(valor,i[llave]):
            lista_sort.append(i["nombre"])
    return lista_sort
    

# 6
def export_a_csv(contenido:list,nombre_archivo:str):

    with open(nombre_archivo,"w+") as archivo:
        
        for i in contenido:
            valor = str(i) + ","
            archivo.write(valor)   
export_a_csv(sort_llave(lista_aux,"inteligencia","average"),"modelo.cvs")


# Menu
opciones = ["1) Listar Heroes","2) Listar altura", "3) Listar por fuerza","4) Calcular promedio","5) Salir"]


def menu_principal(opciones):
    for i in opciones:
        print(i)
        
    opcion_elegida = input("Elija una opcion: ")
    
    return opcion_elegida


def app():
    while True:
        opcion_elegida = menu_principal(opciones)
        opcion_elegida = int(opcion_elegida)

        match opcion_elegida:
            case 1:
            # listar_n_heroes(lista_aux,5)
                print("ME mato")
            case 2:
                modo = input("Queres ordenarlos de manera Ascendente o Descendente [ASC-DESC]: ")
                if re.match("[ASC|DESC]",modo):
                    print(ordenar(lista_aux,"altura", modo))
                else:
                    print("Error: la opcion ingresada no es valida")
            case 3:
                modo = input("Queres ordenarlos de manera Ascendente o Descendente [ASC-DESC]: ")
                if re.match("[ASC|DESC]",modo):
                    print(ordenar(lista_aux,"altura", modo))
                else:
                    print("Error: la opcion ingresada no es valida")
            case 4:
                llave = input("El promedio de que dato qures ver [ALTURA - PESO - FUERZA]: ")
                llave = llave.upper()
                if re.match("[ALTURA|PESO|FUERZA]",llave):
                    promedio = print(calcular_promedio(lista_aux,llave))
                    tipo = input("Queres quedarte con aquellos heroes que son mayores o menores al promedio:  ")
                    if re.match("[MENORES|MAYORES]", tipo):

                        menores_o_mayores = calcular_menor_o_mayor(lista_aux,llave,tipo,promedio)
                        print(menores_o_mayores)

app()   


