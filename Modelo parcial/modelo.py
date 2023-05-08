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

    if cantidad <= len(lista):
        lista = lista[0:cantidad]
        
        for i in lista:
            print(i["nombre"])
    else:
        print("No existen tantos heroes")
    
    return lista

# 2 # 3
def ordenar(lista:list[dict], clave:str, tipo = "ASC")->list:
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

# 4 
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

# 5
def sort_llave(lista:list[dict],llave:str,valor:str):
    lista_sort = []
    for i in lista:
        if re.match(valor,i[llave]):
            lista_sort.append(i)
    return lista_sort
    

# 6
def export_a_csv(lista:list,nombre_archivo:str):
        

    with open(nombre_archivo,"w+") as archivo:
        for heroe in lista:
            linea = str(heroe["nombre"]) + "," + str(heroe["identidad"]) + "," + str(heroe["empresa"]) + "," + str(heroe["altura"]) + "," + str(heroe["peso"]) + "," + str(heroe["genero"]) + "," + str(heroe["color_ojos"]) + "," + str(heroe["color_pelo"]) + "," + str(heroe["fuerza"]) + "," + str(heroe["inteligencia"]) + "\n"  
            archivo.write(linea)

# Menu
opciones = ["1) Listar Heroes","2) Listar altura", "3) Listar por fuerza","4) Calcular promedio","5) Filtrar por tipos de inteligencia", "6) Guardar en CSV", "7) Salir"]

def menu_principal(opciones):
    for i in opciones:
        print(i)
        
    opcion_elegida = input("Elija una opcion: ")
    
    return opcion_elegida

def app():
    flag1 = False
    flag2 = False
    while True:
        
        opcion_elegida = menu_principal(opciones)
        opcion_elegida = int(opcion_elegida)
        
        if opcion_elegida == 1:
                cantidad = input("Cuantos héroes queres ver?: ")
                if re.match("[0-9]+",cantidad):
                    cantidad = int(cantidad)
                    if cantidad > 0 and cantidad < 24: 
                        print("-------")
                        if flag1 == False:
                            lista_mod = listar_n_heroes(lista_aux,cantidad)
                            flag1 = True
                        else:
                            lista_mod = listar_n_heroes(lista_mod,cantidad)
                        print("-------")
                else:
                    print("---Error: Ingresa un número valido Por favor [0-24] ---")
                print(lista_mod)
                
        elif opcion_elegida == 2:
                modo = input("Queres ordenarlos de manera Ascendente o Descendente [ASC-DESC]: ")
                if re.match("[ASC|DESC]", modo.upper()):
                    if flag1 == False:
                        lista_mod = ordenar(lista_aux,"altura", modo)
                        flag1 = True
                    else:
                        lista_mod = ordenar(lista_mod,"altura", modo)
                        print("-------")
                    for i in lista_mod:
                        print(i["nombre"],"Altura: ",i["altura"]) 
                        print("-------")
                else:
                    print("--Error: la opcion ingresada no es valida--")
                    
        elif opcion_elegida == 3:
                modo = input("Queres ordenarlos de manera Ascendente o Descendente [ASC-DESC]: ")
                if re.match("[ASC|DESC]",modo.upper()):
                    if flag1 == False:
                        lista_mod = ordenar(lista_aux,"fuerza", modo)
                        flag1 = True
                    else:
                        lista_mod = ordenar(lista_mod,"fuerza", modo)
                    print("-------")
                    for i in lista_mod:
                        print(i["nombre"], "Fuerza:",i["fuerza"]) 
                    print("-------")
                else:
                    print("--Error: la opcion ingresada no es valida--")
                    
        elif opcion_elegida == 4:
                llave = input("Ingresa el dato del cual quieras ver un promedio [ALTURA - PESO - FUERZA]: ")
                llave = llave.lower()
                if re.match("[altura|peso|fuerza]",llave):
                    if flag1 == False:
                        promedio = calcular_promedio(lista_aux,llave)
                        flag1 = True
                    else:
                        promedio = calcular_promedio(lista_mod,llave)
                    print("-------")
                    print(promedio)
                    print("-------")
                else:
                    print("Error: la opcion ingresada no es valida")
                tipo = input("Queres quedarte con aquellos heroes que son mayores o menores al promedio:  ")
                tipo = tipo.lower()
                if re.match("[menores|mayores]", tipo):
                    if flag2 == False:
                        lista_mod = calcular_menor_o_mayor(lista_aux,llave,tipo,promedio)
                        flag2 = True
                    else:
                        lista_mod = calcular_menor_o_mayor(lista_mod,llave,tipo,promedio)
                print("-------")
                for i in lista_mod:
                    print(i["nombre"],i[llave])
                print("-------")
            
        elif opcion_elegida == 5:
                tipo = input("Elije un tipo de inteligencia [Average - Good - High]: ")
                tipo = tipo.lower()
                if re.match("[average|good|high]",tipo):
                    if flag1 == False:
                        lista_mod = sort_llave(lista_aux,"inteligencia",tipo)
                        flag1 = True
                    else:
                        lista_mod = sort_llave(lista_mod,"inteligencia",tipo)
                    for i in lista_mod:
                        print(i["nombre"])
                else: print("Error: la opcion ingresada no es valida")

        elif opcion_elegida == 6:
                export_a_csv(lista_mod,"hola.csv")
                break
            
        elif opcion_elegida == 7:
                break
            
        else:
                print("---Error: Ingresa un número de opción valido Por favor ---")


app()       



