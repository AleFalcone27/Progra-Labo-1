from copy import deepcopy

# lista_1 = [[1,2],3,4,5]

# lista_2 = lista_1.copy()

# lista_2 [0][0] = "hola"

# print("Lista 2: ", lista_1)
# print("Lista 2: ", lista_2)


# lista_1 = [1,2,3,4]

# lista_2 = deepcopy(lista_1)

# lista_2 [0] = "hola"

# print("Lista 2: ", lista_1)
# print("Lista 2: ", lista_2)

"""
lista_2 = lista_1 -> Lo que hace es copiar la referencia (dirección de memoria) de la lista, 
por lo que ambas variables van a modificar la misma lista ya que apuntan al mismo espacio de memoria

lista_2 = lista_1.copy() -> El shallow copy (copia de superficie) copia los valores que contiene
las variables en caso que sean variables simples (tipo int, float o str). 
En caso de que los datos de la lista sean datos compuestos (un diccionario, otra lista) lo que copia en ese índice es la referencia de la variable

lista_2 = deepcopy(lista_1) -> Hace una copia de TODOS los valores de lista_1, sean simples o compuestos. 
Este ultimo te garantiza que si tu lista tiene datos compuestos y no queres tocar la lista original puedas manejar una copia y modificarla 
sin afectar a la primera
"""