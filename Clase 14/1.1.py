from copy import deepcopy 
from functools import reduce 
from colorama import Fore, Style



# Mostrar los datos.


lista_diccionario = [
{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

lista_copia = deepcopy(lista_diccionario) 


# 1 De debra mapear al precio con iva, sumando el 21% sobre el precio sin iva.
def sumar_porcentaje_x(lista:list[dict], procentaje=0.21)->list:
    precio_sin_iva = lista["precio"]["sin_iva"]
    precio_con_iva = (precio_sin_iva * procentaje) + precio_sin_iva
    lista["precio"]["con_iva"] = precio_con_iva


# 2 Modificar el nombre de Destornillador por Destornillador Philips.
def modificar_nombre(lista:list[dict]):
    for dic in lista:
        if dic["nombre"] == "Destornillador":
            nombre_modificado = dic.update({"nombre": "Destornillador Philips"})
    return nombre_modificado


# 3 Agregar una herramienta con sus respectivos datos.
def agregar_elemento(lista:list[dict], nombre:str, precio_sin_iva:int):

    elemento = {'nombre' : nombre,'precio': {'sin_iva': precio_sin_iva,'con_iva':0.00}}
    
    lista.insert(len(lista)+1,elemento)


# 4 Eliminar dos herramientas que no sean ni la primera ni la ultima y agregarlas a una lista de herramientas eliminadas.

def eliminar_elemento(lista:list[dict],indice:int):
    elementos_eliminados = []
    elementos_eliminados.append(lista.pop(indice))
    return elementos_eliminados
    

def printear_datos(lista:list[dict]):
    for i in lista:
        linea  = " - " + i["nombre"] + " Precio: con IVA " + str(i["precio"]["sin_iva"]) + " sin IVA " + str(i["precio"]["con_iva"])
        print(linea,generar_pared(linea,63,"|"))

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
            
        if imprimir == False:
            
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


# 5 Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas.

map(modificar_nombre(lista_copia),lista_copia)

agregar_elemento(lista_copia,"Tuerca", 35 )

list(map(sumar_porcentaje_x,lista_copia)) 

lista_herramientas_eliminadas = eliminar_elemento(lista_copia,2)


## PRINTEAMOS TODOS


print(Fore.YELLOW,Style.BRIGHT, "LISTA ORGINAL ")
print(Fore.WHITE, generara_separador("-", 64,))
printear_datos(lista_diccionario)
print(Fore.WHITE, generara_separador("-", 64,))


print()


print(Fore.GREEN,Style.BRIGHT, "LISTA MODIFICADA ")
print(Fore.WHITE, generara_separador("-", 64,))
printear_datos(lista_copia)
print(Fore.WHITE, generara_separador("-", 64,))

print()


print(Fore.RED,Style.BRIGHT, "LISTA DE HERRAMIENTAS ELIMINADAS ",)
print(Fore.WHITE, generara_separador("-", 64,))
printear_datos(lista_herramientas_eliminadas)
print(Fore.WHITE, generara_separador("-", 64,))
print(Style.RESET_ALL)