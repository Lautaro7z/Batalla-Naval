class Barco:
    def __init__(self, tipo_barco, tamanio):
        self.tipo_barco = tipo_barco
        self.tamanio = tamanio
        self.coordenadas = []

    def impacto_vertical(self, fila, columna):
        for i in range(self.tamanio):
            self.coordenadas.append((fila, columna))
            fila = fila + 1
    
    def impacto_horizontal(self, fila, columna):
        for i in range(self.tamanio):
            self.coordenadas.append((fila, columna)) 
            fila = fila + 1 

    def confirmar_status(self):
        if self.coordenadas == []:
            return True
        else:
            return False
    
