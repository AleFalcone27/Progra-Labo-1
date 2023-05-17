import json
import re

"""
REVISAR PARA EL RECU:
- Como funciona el tema de las listas
- Validaciones con regex
- Agilizar la progrmaacion

"""

# Parseamos al json 
def parse_json(nombre_archivo:str)->list[dict]:
    
    """
    Esta funcion se encarga de leer un archivo json y devolverlo como diccionario 
    """
    
    dict_json = {}
    
    archivo = open(nombre_archivo,"r")
    
    dict_json = json.load(archivo)
    
    archivo.close()
        
    return dict_json["juegos"] 

lista_juegos = parse_json("data_pp.json")

# Hacemos una copia de la lista 
lista_copia = lista_juegos.copy()


def filtrar_llave(lista:list[dict],llave:str,valor:str,modo:str):
    
    """
    Esta funcion itera la lista de diccionarios pasada por parametro y crea una nueva lista anexando a la misma aquellos diccionarios que 
    no contengan en la key pasada como parametro el valor buscado
    Esta funcion recibe como parametro:
        - lista: una lista de diccionarios
        - llave: un string que representa una key
        - valor: un string que representa un valor a buscar las keys de los diccionarios 
    """
    
    lista_filtrada = []
    if modo == "no_esta":
        for i in lista:
            if not re.match(valor,i[llave].split(",")):
                lista_filtrada.append(i)
    if modo == "esta":
        for i in lista:
            if re.match(valor,i[llave]):
                lista_filtrada.append(i)
            
    return lista_filtrada
        

def filtrar_decada(lista:list[dict],llave:str,año_ingresado:int):
    lista_filtrada = []
    for i in lista:
        anio = int(i[llave])    
        if anio >= año_ingresado and anio < año_ingresado + 10:
            lista_filtrada.append(i)
    return lista_filtrada

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
            
            print(string, end="") , 
        else:
            
            return string
        
    else: 
        print("N/A")


def guardar_en_csv(lista:list[dict]):
    with open("juegos_parcial.csv","w+") as archivo:
            for i in lista:
                linea = str(i["id"]) + "," + i["nombre"] + "," + i["plataforma"] + "," + i["empresa"] + "," + i["anio"] + "," + i["pais"] + "," + str(["genero"]) +"\n"  
                archivo.write(linea)

opciones = ["1) Listar los juegos cuyo genero no contengan la palabra [pelea]","3) Listar los juegos ordenamos por empresa", "5) Exportar a CSV"]

def menu_principal(opciones):
    for i in opciones:
        print(i)
        
    opcion_elegida = input("Elija una opcion: ")
    
    return opcion_elegida

def app():
    
    flag = False
    while True:
        
        opcion_elegida = menu_principal(opciones)
        match opcion_elegida:
            
            case "1":
                if flag == False:
                    lista_retorno = filtrar_llave(lista_copia,"genero","Pelea","no_esta")
                    flag = True
                else:
                    lista_retorno = filtrar_llave(lista_retorno,"genero","Pelea","no_esta")

                print(generara_separador("-", 50 ,False))
                for i in lista_retorno:
                    print(i["nombre"], "Genero: ", i["genero"])
                print(generara_separador("-", 50 ,False))

            case "2":
                cont = 0
                decada = input("Ingrese el año completo : ")  
                while decada.isnumeric() == False:
                    decada = input("Error! Ingrese el año completo ")  
                decada = int(decada)
                if flag == False:
                    lista_retorno = filtrar_decada(lista_copia,"anio",decada)
                    flag = True
                else:
                    lista_retorno = filtrar_decada(lista_retorno,"anio",decada)
                
                print(generara_separador("-", 80 ,False))
                for i in lista_retorno:
                    cont += 1
                    print(str(i["id"]) + " - " + i["nombre"] + " - " + i["plataforma"] + " - " + i["empresa"] + " - " + i["anio"] + " - " + i["pais"] + " - " + str(i["genero"]) + "\n")
                print("La cantidad de juegos en la decada ingresada es de", cont)
                print(generara_separador("-", 80 ,False))

            case "3":
                tipo = input("Queres ordenarlos de manera ascendente o descentedente [ASC - DESC]: ")
                tipo = tipo.upper()
                while re.match("[ASC|DESC]", tipo) == None:
                    tipo = input("Error: Queres ordenarlos de manera ascendente o descentedente [ASC - DESC]: ")
                    tipo = tipo.upper()
                if flag == False:
                    lista_retorno = ordenar(lista_copia,"empresa",tipo)
                    flag = True
                else:
                    lista_retorno = ordenar(lista_retorno,"empresa",tipo)
                    
                print(generara_separador("-", 90 ,False))
                for i in lista_retorno:
                    print(str(i["id"]) + " - " + i["nombre"] + " - " + i["plataforma"] + " - " + i["empresa"] + " - " + i["anio"] + " - " + i["pais"] + " - " + str(i["genero"]) + "\n")
                print(generara_separador("-", 90 ,False))
                
            case "4":
                lista_retorno = filtrar_llave(lista_copia,"modo",".+multijugador$|.+cooperativo$","esta")
                for i in lista_retorno:
                    print(str(i["id"]) + " - " + i["nombre"] + " - " + i["plataforma"] + " - " + i["empresa"] + " - " + i["anio"] + " - " + i["pais"] + " - " + str(i["genero"]) + "\n")
                
            case "5":
                if flag == False:
                    lista_retorno = guardar_en_csv(lista_copia)
                    flag = True
                else:
                    lista_retorno = guardar_en_csv(lista_retorno)


            case "6":
                break
app()
