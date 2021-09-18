class Juego:
    def __init__(self): 
        empezar = ("Comenzar el juego? (si o no): " ) 
        if comenzar = ["si" , "Si" , "SI" , "sI"]:
            self.jugarPVP()
        else: 
            print("Cancelado")
        
    def jugarPVP(self):
        nombrejugador1 = input("¡Ingrese su nombre jugador!")
        j1 = Jugador(nombrejugador1)
        j1.colocar_flota()
        j1.ver_mapa()
        self.limpiar_pantalla()

        nombrejugador2 = input("¡Ingrese su nombre jugador!")
        j2 = Jugador(nombrejugador2)
        j2.colocar_flota()
        j2.ver_mapa()
        self.limpiar_pantalla()

    bandera = True
    while bandera is True:
        j1.hunde(j2)
        if self.flota_hundida(j2) is True:
            self.victoria(j1, j2)
            bandera = False
        else: 
            self.limpiar_pantalla()

        j2.hunde(j2)
        if self.flota_hundida(j2) is True:
            self.victoria(j1, j2)
            bandera = False
        else: 
            self.limpiar_pantalla()
    print("Gracias por jugar")

    def hundir_flota(self, jugador):
        contador_barcos = 0
        for fila in range (len(jugador.tablero.rablero)):
            for columna in range (len(jugador.tablero.tablero)):
                if jugador.tablero.tablero [fila][columna] == "S":
                    contador_barcos += 1
        if contador_barcos == 0:
            return True
        else:
            return False

    def limpiar_pantalla(self):
        input("¿Desea terminar el turno? ")
        os.system( " limpiar " )

    def victoria (self, ganador, perdedor):
        print ("\n\n\n*****************************************")
        print ("la flota de %s fue destruida, %s wins!" % (perdedor.nombre, ganador.nombre))"
        print ("*****************************************")



        