# Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
# respectivas listas. Validar el ingreso de datos según su criterio.
# Datos:

# nombre, sexo (f/m), nota (validar).
# Una vez cargados los datos:
# Mostrar el nombre del hombre con nota más baja
# Mostrar el promedio de notas de las mujeres

# Ejemplo:
# nombres = ["Juan","Pedro","Sol","Paco","Ana"]
# sexo = ["m","m","f","m","f"]
# nota = [6,8,10,8,5]


lista_nombres = []
lista_sexo = []
lista_nota = []

flag = True
acumulador_nota = 0
contador_mujeres = 0


for i in range(3):
    
    nombre = input("Ingrese su nombre: ")
    while len(nombre) <= 2 :
        nombre = (input("Su nombre no puede contener menos de 2 letras. Por favor vuelva a ingresarlo: "))        
    
    sexo = input("Ingrese su sexo [F - M]: ")
    sexo = sexo.capitalize()
    while sexo !="F" and sexo !="M":
        sexo = input("ERROR Ingrese [F - M] según corresponda: ")
        sexo = sexo.capitalize()

    
    nota = input("Ingrese su nota: ")
    nota = int(nota)
    while nota < 0:
        nota = input("ERROR Ingrese su nota: ")
        nota = int(nota)

    lista_nombres.append(nombre)
    lista_sexo.append(sexo)
    lista_nota.append(nota)

# B

    if sexo == "F":
        acumulador_nota = acumulador_nota + i
        contador_mujeres = contador_mujeres + 1





# A
for i in lista_nota:
    if flag == True:  
        menor_nota = i # el primero valor de la lista es i
        flag = False
    if sexo == "M":
        if i > menor_nota: # si i es mayor a menor nota vuelve a iterar
            continue 
        else:
            menor_nota = i  # guardamos la edad mas chica
            
posicion_menor_nota = lista_nota.index(menor_nota) # guardamos el indice del numero mas chico en la varaible posicion_menor_nota
nombre_menor_nota = lista_nombres[posicion_menor_nota] # en la lista nobres accedo al indice que coincide con la edad mas chica

        
promedio_nota_mujeres = acumulador_nota / contador_mujeres


print("El hombre con la nota mas baja es ", nombre_menor_nota)
print("El promedio de la edad de las mujeres es de " , promedio_nota_mujeres)

