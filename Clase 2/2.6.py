lista  = [3, 82, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 29, 58]

flag = True

for i in lista:
    if flag == True:
        max = i
        flag = False
    if i > max:
        max = i
print(max)
            
#Buscador de maximos y tambien sirve para minimos Por cada iteracion verifica si i+1 es mas grande que i   

    
    