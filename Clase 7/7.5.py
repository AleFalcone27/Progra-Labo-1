from data_stark import lista_personajes
import re

h = { "nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""}


# 5.1
def convertir_cm_a_mtrs(valor_cm):
    
# esta funcion recibe como parametro un numero, verifica que sea un flotante positivo y lo tranforma de cm a mts 
    
    
    
    if type(valor_cm) == float and valor_cm > 0:
        valor_cm = valor_cm / 100
        return valor_cm
    else:
        return -1
        
# 5.2
def generara_separador(patron:str, largo:int, imprimir=True):

# toma como parametros:
# ● patron: un carácter que se utilizará como patrón para generar el
# separador
# ● largo: un número que representa la cantidad de caracteres que va
# ocupar el separador.
# ● imprimir: un parámetro opcional del tipo booleano (por default definir
# en True)
# esta funcion devuelve o imprime el patron pasado como parametro (patron) la cantidad de veces que lo determinemos en el argumento largo

    if len(patron) > 0 and len(patron) and largo > 0 and largo < 236 :
        for i in range(largo):
            
            string = patron * largo
            
        if imprimir == True:
            
            print(string, end="")
        else:
            
            return string
        
    else: 
        print("N/A")
    

# 5.3
def generar_encabezado(titulo:str):
    
    titulo = titulo.upper()
    
    string = (generara_separador("***",43,False))
    
    print(string)
    print(titulo)
    print(string)
    
# 5.4
def imprimir_ficha_heroe(heroe:dict):
    
    generar_encabezado("principal")
    print( 
    "ALTURA:","                                       ",convertir_cm_a_mtrs(heroe["altura"])


        )
    
    
    
imprimir_ficha_heroe(h)




# print(convertir_cm_a_mtrs(79.349999999999994))
# string = (generara_separador("***",43,True))
# generar_encabezado("pagina principal")