contador = 0
cant_pares = 0
cant_impares = 0
flag = True
flag_par = True
flag_negativos = True
acum_positivos = 0

numero = input("Ingrese un numero: ")
numero = int(numero)
while contador < 4 and numero > 0:
    numero = input("Ingrese un numero: ")
    numero = int(numero)

    print(contador)
    
    # A
    if numero % 2 == 0:
        # D
        acum_positivos = numero + acum_positivos
    
        cant_pares = cant_pares + 1
        # C
        if flag_par == True:
            mayor_numero_par = numero
            flag_par = False
        if numero > mayor_numero_par:
            mayor_numero_par = numero  
    else:
        cant_impares = cant_impares + 1
        
        # E PRODUCTO DE LOS NEGATIVOS
        if flag_negativos == True:
            acum_negativos = numero
            flag_negativos = False
        else:
            acum_negativos = acum_negativos * numero           
    
    # B
    if flag == True:
        menor_numero = numero
        flag = False
    if numero < menor_numero:
        menor_numero = numero
          

    contador = contador + 1
    
print("La cantidad de numeros pares ingresados es de: ", cant_pares)
print("La cantidad de numeros impares ingresados es de: ", cant_impares)
print("El numero mas chico ingresado es: ", menor_numero)
print("El producto de los negatios es : ", acum_negativos)
print("El numero par mas grande es: ", mayor_numero_par)
print("El total de la suma de los numeros pares ingresados es de : ", acum_positivos)