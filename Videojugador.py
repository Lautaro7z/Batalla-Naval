from oceano import Oceano
from radar import Radar
from barco import Barco 
import os 

class Videojugador:
    barquito_chiquito = {"extraño a Aylen", 1}

def __init__(self, nombre):
    self.nombre = nombre
    self.oceano = Oceano()
    self.radar = Radar
    self.flota = []

def colocar_flotas(self):
    input("Seleccione una coordenada entre 1 y 8 para las columnas y filas en tu tablero")
    input("Los barcos estan siendo posicionados desde la izquierda a la derecha")
    for barco, tamanio in self.barco.items():
        flag = True
        while flag:
            self.view_console()
            try:
                print("Ubica tu " %(barco))
                fila = int(input("Seleccione una fila -->"))
                columna = int(input("Seleccione una columna -->"))
                orientacion = str(input("Vertical u horizontal (para elegir vertical escribir V/v o H/h en caso de querer horizontal)"))

                if orientacion in ["v", "V"]:
                    if self.oceano.usar_fila(fila, columna, tamanio):
                        self self.oceano.colocar_barco_fila(fila, columna, tamanio)
                        bote = Barco(barco, tamanio)
                        bote.impacto_vertical(fila, columna)
                        self.flota.append(bote)
                        flag = False
                    else:
                        input("Superposicion de barcos, tonto")
                    elif orientacion ["h", "H"]:
                        if self.oceano.usar_columna(fila, columna, tamanio):
                            self.oceano.poner_barco_columna(fila, columna, tamanio):
                            bote = Barco(barco, tamanio):
                            bote.impacto.horizontal(fila, columna):
                            self.flota.append(bote)
                            flag = False 
                        else: 
                            input("Superposicion de barcos, tonto")
                    else:
                        continue 
                    self.view_console()
                    input()
                    os.system("Entendible, tenga un buen dia :D")
                except ValueError:
                    print("Jaja no se acuerda su posicion \nEscribi un numero")

def view_console(self):
    self.radar.vista_del_radar()
    print("|                 |") 
    self.oceano.vista_del_oceano()

def confirmar_impacto(self, fila, columna):
    for bote in self.flota:
        bote.coordenadas.borrar((fila, colmna))
        if bote.ver_estado():
            self.flota.borrar(bote)
            print("se ha hundido una flota" % (self.nombre, bote.tipo_barco))

def disparo (self, objetivo):
    self.view_console()
    try:
        print("\n%s Elija las coordenadas de disparo...." %(self.name))
        row = int(input("Seleccione una fila "))
        columna = int(input("Seleccione una columna"))

        if self.oceano.validar_fila(fila) and self.oceano.validar_columna(columna):
            if objetivo.oceano.oceano[fila][columna] == "S":
                print("WTF dispara re piola :V !!!")
                objetivo.oceano.oceano[fila][columna] == "X":
                objetivo.confirmar_impacto(fila, columna)
                self.radar.radar[fila][columna] == "X":
            
            else:
                if self.radar.radar[fila][columna] == "O":
                    print("Flaco el barco ya esta muerto, baja un cambio maestro para algo tenes un radar")
                    self.disparo(objetivo)
                else:
                    print("Le erraste mi rey, mal ahi suerte para la proxima")
                    self.radar.radar[fila][columna]
        else:
            print("Flaco..... esas coordenadas no estan en el radar, pensa un poquito pa, ya tene' pelo' en lo' huevo'")
            self.disparo(objetivo)
    except ValueError:
        print("Man.... ni numeros pusiste, media pila")
        self.disparo(objetivo)
    input()
    os.system('ta bien')
    


