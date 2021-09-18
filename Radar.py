class Radar:
    def __init__(self, x=8, y=8):
        self.radar = [["." for i in range (x)]for i in range (y)]
    
    def __getitem__(self, item):
        fila, columna = punto
        return self.radar [columna][fila]

    def __setitem__(self, item):
        fila, columna = punto
        return self.radar [columna][fila] = valor
    
    def ver_radar(self):
        for columna in self.radar:
            print (" ".join(fila))
