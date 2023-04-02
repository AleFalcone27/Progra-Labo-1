ESTADIA = 15.000

estacion = input("Ingrese la estacion en la que desea viajar: ")
while estacion != "Invierno" and estacion != "Verano" and estacion != "Otoño" and estacion != "Primavera":
    estacion = input("Ingrese la estacion en la que desea viajar: ")
    
localidad = input("Ingrese la localidad a la cual desea viajar: ")
while localidad != "Bariloche" and localidad != "Mar del plata" and localidad != "Cordoba" and localidad != "Cataratas":
    localidad = input("Ingrese la localidad a la cual desea viajar: ")

if estacion == "Invierno":
    if localidad == "Bariloche" or localidad == "Mar del plata":
        descuento = 20
    elif localidad == "Cataratas" or localidad == "Cordoba":
        descuento = 10
        
elif estacion == "Verano":
    if localidad == "Bariloche" or localidad == "Mar del plata":
        descuento = 10
    elif localidad == "Cataratas" or localidad == "Cordoba":
        descuento = 20
        
elif estacion == "Otoño" or estacion == "Primavera":
    if localidad == "Cordoba":
        descuento = 0
    else:
        descuento = 10

print(descuento)