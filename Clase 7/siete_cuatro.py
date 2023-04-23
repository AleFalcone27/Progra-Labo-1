from data_stark import lista_personajes
import re

# 4.1
def generar_indices_nombres(lista:list[dict]):

# recibimos como parametro una lista de diccionarios
# iteramos la lista de personajes y por cada nombre que nos encontramos lo separamos y generamos una nueva lista   

        lista_nombres = []
        lista_nombres_separados =[]
        for heroe in lista:
            if len(lista) > 0 and type(heroe) == dict and "nombre" in heroe:
                lista_nombres.append(heroe["nombre"])
            else:               
                print("El origen de los datos no contiene un formato")
        for nombre in lista_nombres:
                lista_nombres_separados.extend(nombre.split()) 
                # con split generamos de cada cadena subcadenas separadas por coma
                # con extend agregamos cada uno de los elementos no como listas sino como elementos individuales (sin corchetes) esto no pasa si utilizamos append.
        return lista_nombres_separados

# 4.2
def stark_imprimir_indice_nombre(lista:list[dict]):
    
# unimos los nombres separados en la funcion 4.1 con "-"

    lista_nombres = generar_indices_nombres(lista_personajes)
    lista_nombres = "-".join(lista_nombres)
    print(lista_nombres)





