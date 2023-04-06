from data_stark import lista_personajes



# lista_nombres = []
# lista_alturas = []

# def obtener_nombres():
#     for i in lista_personajes:
#         lista_nombres.append(i["nombre"])
        
# obtener_nombres()
# print(lista_nombres)
    

# def obtener_alturas():
#     for i in lista_personajes:
#         lista_alturas.append(i["altura"])
    
# obtener_alturas()
# print(lista_alturas)



# B Recorrer la lista_personajes imprimiendo por consola el nombre de cada superhéroe
for i in lista_personajes:
    print(i["nombre"])

# C Recorrer la lista_personajes imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
for i in lista_personajes:
        print(i["nombre"], i["altura"])
            

# D. Recorrer la lista y determinar cuál es el superhéroe más mas_alto (MÁXIMO)
mas_alto = None
nombre_mas_alto = None
for i in lista_personajes:
    if mas_alto == None or float(i["altura"]) > mas_alto:
        mas_alto = float(i["altura"])
        nombre_mas_alto = i["nombre"]
        print( nombre_mas_alto , mas_alto)
    

    

