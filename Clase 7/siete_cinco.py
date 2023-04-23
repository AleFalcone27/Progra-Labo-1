from data_stark import lista_personajes as lista_heroes
from siete_uno import *
from siete_dos import *
from siete_tres import *
from siete_cuatro import *
from siete_cinco import *
import re

if __name__ == "__main__":
    # 5.1
    def convertir_cm_a_mtrs(valor_cm):
        
    # esta funcion recibe como parametro un numero, verifica que sea un flotante positivo y lo tranforma de cm a mts 
        
        valor_cm = float(valor_cm)
        
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
        
    # Generamos la ficha del heroe

        generar_encabezado("principal")
        print( 
        "NOMBRE DEL HÉROE:","                            ", heroe["nombre"] , "(" + extraer_iniciales(heroe["nombre"]) + ")", "\n" # MAL
        "IDENTIDAD SECRETA:","                           ",sanitizar_dato(heroe,heroe["identidad"] ,"str"), "\n"
        "CONSULTORA:","                                  ",sanitizar_dato(heroe,heroe["empresa"],"str") , "\n"
        "CODIGO DE HEROE:","                             ",heroe["empresa"] , "NO LO PUEDO GENERAR" # MAL
            )
        
        generar_encabezado("fisico")
        print(
        "ALTURA:","                                      ",convertir_cm_a_mtrs(heroe["altura"]) , "Mts" "\n"
        "PESO:","                                        ",sanitizar_dato(heroe,heroe["peso"],"float") , "Kg." "\n"
        "FUERZA:","                                      ",sanitizar_dato(heroe,heroe["fuerza"],"int") , "N." "\n"
            )
        
        generar_encabezado("señas particulares")
        print(
            "COLOR DE OJOS:","                               ",sanitizar_dato(heroe,heroe["color_ojos"],"str"), "\n" 
            "COLOR DE PELO:","                               ",sanitizar_dato(heroe,heroe["color_pelo"],"str"), "\n"
            )
                    

    # 5.5
    def stark_navegar_fichas(lista_heroes:list):
        numero_heroe = 1
        
        continuar = True
        while continuar:
            
            imprimir_ficha_heroe(lista_heroes[numero_heroe])
            
            opcion = input(
                " [1] Ir a la izquierda \n [2] Ir a la derecha \n [S] Salir \n ------- \n Elija una opcion: "
                    )
            
            if opcion == "1":
                numero_heroe = numero_heroe - 1
                
            elif opcion == "2":
                numero_heroe = numero_heroe +1
            
            elif opcion > 24:
                opcion == 0
            
            elif opcion == "s" or opcion == "S":
                break
                
                

            
stark_navegar_fichas(lista_heroes)


    # print(convertir_cm_a_mtrs(79.349999999999994))
    # string = (generara_separador("***",43,True))
    # generar_encabezado("pagina principal")