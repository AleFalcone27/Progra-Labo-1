## -- INTERCAMBIO --
#Estado inicial:

#Algoritmo: 

#Estado Final
# 1 , 2 , 3, 4, 5 , 6
# 1 , 2 , 3, 4, 5 , 6
# 6, 5, 4, 3, 2, 1,

#Estado inicial
#Trabajamos con variabels auxiliares pq sino las variables se pisan y perdemos el dato 
# numero_1 = 23
# numero_2 = 10

# aux = numero_1
# numero_1 = numero_2
# numero_2 = aux
# print(numero_2)

lista = [ 2 , 5 , 3 , 1, 6 , 4]
contador = 0
for i in range(len(lista)-1): # Si no le ponemos el va a compara el ultimo elemento 2 veces
    for j in range(i+1 ,len(lista)): # con range le indicamos donde tiene que arrancar
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
            contador = contador +1


## COMO ORDENAR UNA LISTA

# Por cada iteracion de i           
# i j j j j 
#   i j j j 
#     i j j 
#       i j

# lista = [ 2 , 5 , 3 , 1, 6 , 4]
# bandera_swap = True
# contador = 0 
# while bandera_swap == True: # Esta desordenado? no bueno segui
#     bandera_swap = False 
#     for i in range(len(lista)-1): # Si en ninguna de las iteraicones se cumple la condicion, bandera == False y sale del codigo
#         if lista[i] > lista[i+1]:
#             aux = lista[i]
#             lista[i] = lista[i+1]
#             lista[i+1] = aux
#             bandera_swap = True
#             contador = contador + 1 
    
# print(lista)


# COMO ORDENAR UNA LISTA DE DICCIONARIOS

lista = [{"nombre": "Tito", "edad": 32, "nota":6}, 
        {"nombre": "Job", "edad": 37, "nota":7 },
        {"nombre": "Ana", "edad": 25, "nota":9 },
        {"nombre": "Juan", "edad": 28, "nota":8 },
        {"nombre": "Jose", "edad": 23, "nota":4}
        ]   



def ordenar(lista:list, clave:str, tipo = "ASC" )->list:
    bandera_swap = True
    while bandera_swap == True: # Esta desordenado? no bueno segui
        bandera_swap = False 
        for i in range(len(lista)-1): # Si en ninguna de las iteraicones se cumple la condicion, bandera == False y sale del codigo
            if tipo == "ASC":
                if lista[i][clave] > lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True
            else:
                if lista[i][clave] < lista[i+1][clave]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    bandera_swap = True          
    return lista

print(ordenar(lista, "nombre", "ASC"))
