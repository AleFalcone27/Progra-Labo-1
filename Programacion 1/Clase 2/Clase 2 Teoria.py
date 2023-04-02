# -OPERADOR DE ASIGANICON-
# = asignacion 
# a + = suma
# a - = resta
# a * = multiplicacion
# a / = division
# a % = modulo (nos da el resto)

# -OPERADORES ARITMETICOS-
# +   suma
# -   resta
# *   multiplicacion
# /   division
# %   modulo (nos da el resto)
# //  cociente
# **  potencia

# -OPERADORES LOGICOS-
# NOS DEVUELVEN UN VALOR DE VERDAD O TRUE - 
# AND (Devuelve True si ambos operandos son True)
# OR (Devuelve True si alguno de los operando es True)
# NOT (Duevuelve True si operando es False o viceversa)

# -OPERADORES RELACIONALES-
# > Devuelve True si el operador en izquierda es mayor que el operador de la derecha
# < Devuelve True si el operador en derecha es mayor que el operador de la izquierda
# == Devuelve True si ambos operandos son iguales
# >= Devuelve True si el operando de la izquierda es mayor o igual que el operador de la derecha
# <= Devuelve True si el operador de la derecha es maypr o igual que el operador de la izquierda
# != Devuelve True si ambos operandos no son iguales 

# FUNCION RANGE() GENERA UNA SECUENCIA DE NUMEROS QUE VAN DESDE CERO POR DEFECTO HASTA EL NUMERO
# QUE SE PASA COMO PARAMETRO MENOS UNO
# sintaxis range(inicio,fin,salto)
# lista = list(range(10,20,2)) 
# print(lista) 0,1,2,3,4

# lista = [1,2,3,4]
# for numeros in lista:
#     print(numeros, end="")
# salida = 1 2 3 4 
# Si no utilizamos el end="" nos printea 1 x 1 

# BREAK nos permite salir del bucle y lo podemos condicionar
# lista = [1,2,3,4]
# for numero in lista:
#     if numero == 3:
#         break
#     print(numero)

# CONTINUE termina la iteracion corriente y vuelve al inicio del codigo y sigue iterando  
# lista = [1,2,3,4]
# for numero in lista:
#     if numero == 3:
#         continue
#     print(numero)

# TIPO DE DATO: Lo que define al dato en si mismo para la utilidad que le voy a dar
# El dato que le asigne a la variable va a decirnos que tipo de variable es 
# La funcion type(variable) no permite saber que tipo de varibale es

# ENTERO: 23

# FLOAT: 23.5

# BOOLEAN: True o False

# STRINGS: "Alejo"

#LISTAS
# lista = [1, "Hola", 3.76]
# Las listas tienen datos e indices y se puede iterar con un for
# Te permite almacenar un conjunto arbitrario de datos
# Se puede acceder a cada uno mediante el index print(lista[0]) y tambien podemos modificarlos lista[0] = "Alejo"


#TUPLAS
# A diferencia de las listas los elementos son inalterables
# tuple([1, "Hola", 3.76])
    

# Diccionarios
# Tienen un valor y una llave
# diccionario = {"nombre" : "Juan" , "edad" : 21}
# print(diccionario["nombre"]) "Juan"
# print(diccionario["edad"]) 21

# Ser o conjunto
# Elementos inalterables y no se pueden modificar
# c = {1, 2, 3, 4,}