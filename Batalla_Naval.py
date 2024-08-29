class Jugador():
    def __init__(self, nombre): 
        self.nombre = nombre
        self.Victorias = 0
        self.Derrotas = 0

    def sumarDerrotas(self):
        self.Derrotas += 1
    
    def getDerrotas(self):
        return self.Derrotas

    def sumarVictorias(self):
        self.Victorias += 1
    
    def getVictorias(self):
        return self.Victorias
    
class Maquina(Jugador):
    def __init__(self,nombre):
        super.__init__(nombre)

class DatosJugadores():
    def __init__(self):
        self.Jugadores = []

    def agregarJugadores(self, nombreJugador):
        self.Jugadores.append(Jugador(nombreJugador))

    def sumaVictorias(self,jugador:Jugador):
        jugador.sumarVictorias

    def sumarDerrota(self,jugador:Jugador):
        jugador.sumarDerrotas
    
    def getVictoriasJugador(self,jugador:Jugador):
        if jugador in self.Jugadores:
            print(f"Las victorias consegidas por el jugador {jugador.nombre} fueron {jugador.getVictorias}")
        else:
            print(f"El jugador Especificado no Existe")

    def getDerrotasJugador(self,jugador:Jugador):
        if jugador in self.Jugadores:
            print(f"Las derrotas consegidas por el jugador {jugador.nombre} fueron {jugador.getDerrotas}")
        else:
            print(f"El jugador Especificado no Existe")

class Fichas():
    def __init__(self):
        self.fichas8x8 = []
        self.fichas10x10 = []

    def generarFichas8x8(self):
        self.fichas8x8 = ["AAA","PPP","SSS","F","F"]
        return self.fichas8x8 
    
    def generarFichas10x10(self):
        self.fichas8x8 = ["AAA","AAA","PPP","SSS","SSS","F","F"]
        return self.fichas10x10 

class Tablero():
    def __init__ (self):
        self.tablero = [[]]

    def generarTablero_Fichas (self, opcion,fichas:Fichas):
        if opcion == 1:
            self.tablero = [[0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0]]
            
            numeroFichas = fichas.generarFichas8x8

            return self.tablero , numeroFichas

        elif opcion == 2:
            self.tablero = [[0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0,0,0]]
            
            numeroFichas = fichas.generarFichas10x10

            return self.tablero , numeroFichas
        
        else:
            print(f"Opcion Erronea vuelva a elegir")

class Juego():

    def __init__(self, jugador1 , jugador2, fichas , tablero):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.fichas = fichas
        self.tablero = tablero


        
class Menu ():

    @staticmethod
    def mostrarDatosJugadores():
        print(f"1. Inicar Nuevo Juego contra otro jugador\n")
        print(f"2. Inicar Nuevo Juego contra Maquina\n")
        print(f"3. Datos de los Jugadores\n")
        print(f"4. Salir\n")

    @staticmethod
    def mostarMenuPrincipal():
        print(f"1. Inicar Nuevo Juego contra otro jugador\n")
        print(f"2. Inicar Nuevo Juego contra Maquina\n")
        print(f"3. Datos de los Jugadores\n")

    @staticmethod
    def mostarMenuPrincipal():
        print(f"1. Inicar Nuevo Juego contra otro jugador\n")
        print(f"2. Inicar Nuevo Juego contra Maquina\n")
        print(f"3. Datos de los Jugadores\n")

    @staticmethod
    def iniciarMenu():
        print(f"Bienvenido a Batalla Naval\n")
        Menu.mostarMenuPrincipal()
        valor = int(input(f"Ingrese una opcion a escoger:\n"))
        return valor
    
def main ():

    while True:

        valor = Menu.iniciarMenu()

        match valor:
            case 1:

                break

            case 2:

                break

            case 3:
                break

            case 4:
                print("Gracias por ingresar")
                break

        if valor == 4:
            break


main()
