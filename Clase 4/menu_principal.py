opciones = ["1)Mostrar nombres","2)Mostrar Alturas","3)Mostrar mas alto","4) Salir"]

def menu_principal(opciones):
    for i in opciones:
        print(i)
        
    opcion_elegida = input("Elija una opcion: ")
    
    return opcion_elegida

while True:
    opcion_elegida = menu_principal(opciones)
    int(opcion_elegida)
    match opcion_elegida:
        case 1:
            print("Opcion 1")
        case 2:
            print("Opcion 2")
        case 3:
            print("Opcion 3")
        case 4:
            break
