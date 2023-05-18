from copy import deepcopy 

# Hacer una copia deep copy y trabajar con la copia, de acuerdo a lo siguiente:
# De debra mapear al precio con iva, sumando el 21% sobre el precio sin iva.
# Mostrar los datos por pantalla.
# Modificar el nombre de Destornillador por Destornillador Philips.
# Mostrar los datos por pantalla.
# Agregar una herramienta con sus respectivos datos.
# Mostrar los datos.
# Eliminar dos herramientas que no sean ni la primera ni la ultima y agregarlas a una lista de herramientas eliminadas.
# Mostrar los datos.
# Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas.

lista_diccionario = [
{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
]

lista_copia = deepcopy(lista_diccionario) 



for i in lista_copia:
    precio = i.get("precio", "SIN PRECIO")
    precio_sin_iva = precio["sin_iva"]
    precio_con_iva = precio["con_iva"]
    # print(precio)   
    
# def calcular_precio_con_iva(precio):
#     precio = precio * 0.21

for i in lista_copia:
    precio_con_iva = list(map(lambda x : i["precio"]["sin_iva"] * 0.21 + i["precio"]["sin_iva"] , lista_copia["precio"]))
    i["precio"]["con_iva"] = precio_con_iva
print(lista_copia)
    



# indice = lista_copia[2]
# lista_copia[2] = indice.update({"nombre": "Destornillador Philips"})
# print(lista_copia)




