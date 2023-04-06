# 3) Copa pistón!!!
# Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
# Se pedirá el ingreso de:

#  nombre
#  edad (mayor a 18)
#  nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
#  cantidad de carreras ganadas (no pueden ser números negativos)
#  número del vehículo (no puede ser un número negativo)

# se necesita saber:




# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.
# *Promedio de edad de los pilotos que tiene un vehículo con número par.

lista_nombres = []    
lista_edades = []
lista_nacionalidades = []
lista_cantidad_carreras_ganadas = []
lista_num_vehiculo = []

cont_vehiculos_par = 0

flag = True
flag_2 = True
    
for i in range(3):
    
    nombre = input("Ingrese su nombre: ")
    while len(nombre) <= 2 :
        nombre = (input("Su nombre no puede contener menos de 2 letras. Por favor vuelva a ingresarlo: "))        

    # edad = input("Ingrese su edad: ")
    # edad = int(edad)
    # while edad < 18:
    #     edad = input("ERROR Ingrese su edad: ")
    #     edad = int(edad)
        
    # nacionalidad = input("Ingrese nacionalidad: ")
    # while nacionalidad !="Argentino" and nacionalidad != "Ingles" and nacionalidad != "Frances" and nacionalidad != "Brasilero" and nacionalidad != "Estadounidense":
    #     nacionalidad = input("Ingrese nacionalidad: ")

    carreras_ganadas = input("Ingrese la cantidad de carreras ganadas: ")
    carreras_ganadas = int(carreras_ganadas)
    while carreras_ganadas < 0:
        carreras_ganadas = input("Ingrese la cantidad de carreras ganadas: ")
        carreras_ganadas = int(carreras_ganadas)

    numero_vehiculo = input("Ingrese el numero del vehiculo: ")
    numero_vehiculo = int(numero_vehiculo)
    while numero_vehiculo < 0:
        numero_vehiculo = input("Ingrese el numero del vehiculo: ")
        numero_vehiculo = int(numero_vehiculo)
        
        
    lista_nombres.append(nombre)   
    # lista_edades.append(edad)
    # lista_nacionalidades.append(nacionalidad)
    lista_cantidad_carreras_ganadas.append(carreras_ganadas)
    lista_num_vehiculo.append(numero_vehiculo)
    
    
    
    # *Cantidad de vehículos con número par.
    if numero_vehiculo % 2 == 0:
        cont_vehiculos_par = cont_vehiculos_par + 1
    # *Nombre del piloto con menos victorias y el número de auto impar.
    elif numero_vehiculo % 2 == 1:
        for i in lista_cantidad_carreras_ganadas: # Siempre va a funcionar mal pq estoy metiendo todas las acntidades de carreras ganasdas en la misma lista
            if flag_2 == True:
                menos_victorias = i
                flag_2 = False
                print("Entro")
            if i > menos_victorias:
                print(i)
                continue
            else:
                menos_victorias = i
                print(i)
    
menos_victorias_vehiculo_impar = lista_cantidad_carreras_ganadas.index(menos_victorias) # nos permite obtener el índice o posición de la primera aparición de un elemento dentro de una lista
nombre_menos_octorias_vehiculo_impar = lista_nombres[menos_victorias_vehiculo_impar]
    
    
    
    
    
    
   
# Nacionalidad del piloto más joven.
# for i in lista_edades:
#     if flag == True:
#         piloto_mas_joven = i
#         flag = False
#     if i > piloto_mas_joven:
#         continue
#     else:
#         piloto_mas_joven = i
    
# index_piloto_mas_joven = lista_edades.index(piloto_mas_joven) # accedo a el indice de la edad mas baja 
# nacionalidad_piloto_mas_joven = lista_nacionalidades[index_piloto_mas_joven] # busco la nacionalidad que se encuentre en el mismo lugar 




print("El nombre del piloto con menos vicotias que maneja un auto impar es de" , nombre_menos_octorias_vehiculo_impar)
print("La cantidad de vehiculos con numero par es de", cont_vehiculos_par)


# print("El piloto mas joven cuenta con" , piloto_mas_joven,  " años y es de nacionalidad", nacionalidad_piloto_mas_joven )


print(lista_cantidad_carreras_ganadas)
print(lista_nombres)
print(lista_num_vehiculo)
# print(lista_nacionalidades)
# print(nacionalidad_piloto_mas_joven)

