from random import randrange
class Tablero: 
    def __init__(self,x = 8 , y = 8):
        self.tablero = [["-" for i in range(x)] for i in range(y)]
    
    def __getitem__(self, punto):
        columna, fila = punto
        return self.tablero [columna][fila]

    def __setitem__(self, punto, valor):
        columna, fila = punto
        self.tablero [fila][columna] = valor

    def generador_de_barcos(self, generador, coordx, coordy):
        generador = None
        coordx = None
        coordy = None
        for i in range (8):
            coordx = randrange(1,tamanio)
            coordy = randrange(1,tamanio)


    def ver_tablero(self):
        for fila in self.tablero:
            print("".join(fila))

    def columna_valida(self, fila):
        try:
            self.tablero[fila]
            return True
        except IndexError:
            return False
    def fila_valida(self, columna):
        try:
            self.tablero [0][columna]
            return True
        except IndexError:
            return False

    def columna_libre(self, fila, columna, tamanio,):
        coordenada_valida = []
        for i in range(1, tamanio):
            if self.columna_valida(columna) and self.fila_valida(fila):
                if self.tablero[fila][columna] == "-":
                    coordenada_valida.append ((fila, columna))
                    columna = columna + 1
                else:
                    columna = columna + 1
            else: 
                return False

        if tamanio == len(coordenada_valida):
            return True
        else:
            return False

    def fila_libre(self, columna, fila, tamanio, coordenadas_validas):
        coordenadas_validas = []
        for i in range(tamanio): 
            if self.fila_valida(fila) and self.columna_valida(columna):
                if self.tablero[columna][fila] == "-":
                    coordenadas_validas.append ((fila, columna))
                    fila = fila + 1
                else:
                    fila = fila + 1
            else: 
                return False

        if tamanio == len(coordenadas_validas):
            return True
        else:
            return False

    def colocar_barco_encolumna(self, fila, columna, tamanio):
        for i in range(tamanio): 
            self.tablero[columna][fila] = "S"

    def colocar_barco_enfila(self, fila, columna, tamanio):
        for i in range(tamanio):
            self.tablero[columna][fila] = "S"
   