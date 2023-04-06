edades = [15,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]

flag = True

for i in edades:
    if flag == True:
        min = i
        flag = False
    if i < min:
        min = i
        menor_edad = edades.index(min) # guardamos el indice del numero mas chico
            
# buscamos en la lista nombre el nombre que este en la misma posicion que la edad mas chcia 
# podemos guardar en una variable un indice y obtener el valor del mismo mediante lista[variable]
nombre_menor = nombre[menor_edad] 

print("El nombre de la persona mas joven es ", nombre_menor)

