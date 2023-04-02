edad = input("Ingrese edad: ")    
edad = int(edad)

estado_civil = input("Ingrese su estado civil: ")
while estado_civil != "Soltero" and estado_civil != "Casado" and estado_civil != "Divorciado":
    estado_civil = input("Ingrese su estado civil: ")
    
if edad < 18 and edad != "Soltero":
    print("Es muy pequeño para NO ser soltero")
    
    

