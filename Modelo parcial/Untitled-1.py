def generar_pared(largo_palabra:str,ubicacion):
    string = ""
    for i in range(ubicacion - len(palabra)):
        string = string + " " 
    string = string + "|"
    return string

palabra = "hola"
print("---------------------------")
print(palabra, generar_pared(len(palabra), 25))
palabra = "nico"
print(palabra, generar_pared(len(palabra), 25))
pabra = "te"
print(palabra, generar_pared(len(palabra), 25))
palabra = "amo"
print(palabra, generar_pared(len(palabra), 25))
print(palabra, generar_pared(len(palabra), 25))
print("---------------------------")