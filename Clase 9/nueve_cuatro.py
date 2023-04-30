from data_stark import lista_personajes as lista_heroes
from nueve_uno import *


# 4.1
def sumar_dato_heroe_genero(lista:list[dict],llave:str,genero:str):
# itera sobre una lista de diccionarios y acumula todos los valores que esten asociados a la clave pasada como parametros
    acum = 0
    for i in lista:
        if type(i) == dict and len(i) > 0:
            if genero == i["genero"]:
                acum = acum + float(i[llave])
            retorno =  acum
        else:
            retorno = -1
            
        return retorno
        
# 4.2
def cantidad_heroes_genero(lista:list[dict],genero:str):
    cont = 0
    for i in lista_heroes:
        if i["genero"] == genero:
            cont = cont +1 
    return cont
# 4.3
def calcular_promedio_genero(lista:list[dict],llave:str,genero:str):
    acum = 0
    cont = 0
    for i in lista:
        if i["genero"] == genero:
            acum = acum + float(i[llave]) # normalizar los datos o castear en la funcion
            cont = cont + 1
        
    promedio = acum / cont
    
    promedio = round(promedio,2) # funcion round(numero, cantidad de decimales) 
    
    return promedio
# 4.3
def stark_calcular_imprimir_guardar(lista:list[dict],llave:str,genero:str):
    if len(lista) > 0:
        
        promedio = calcular_promedio_genero(lista,llave,genero)
        datos = capitalizar_palabras(llave) , " promedio genero ", genero + ": " , str(promedio)
        datos = "".join(datos)
        nombre_archivo = "heroes_promedio_" + llave + "_" + genero + ".cvs"
        print(nombre_archivo)
        with open(nombre_archivo, "w") as archivo:
            archivo.write(datos)
            
            return True
        
    else: 
        print("Error: Lista de héroes vacía.")    
        return False


if __name__ == "__main__":
    stark_calcular_imprimir_guardar(lista_heroes,"peso","F")