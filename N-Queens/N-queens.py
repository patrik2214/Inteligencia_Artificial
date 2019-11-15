"""N reinas puzzle."""
import pygame

class NQueens:
    """Genera todas las soluciones válidas para el rompecabezas n reinas"""
    def __init__(self, tamaño):
        # Almacena el tamaño del rompecabezas (problema) y la cantidad de soluciones válidas
        self.tamaño = tamaño
        self.soluciones = 0
        self.resolver()

    def resolver(self):
        """Resuelve el rompecabezas de n reinas e imprime el número de soluciones"""
        posiciones = [-1] * self.tamaño
        self.poner_reinas(posiciones, 0)
        print("Se encontraron: ", self.soluciones, "soluciones.")

    def poner_reinas(self, posiciones, fila_destino):
        """
        Intenta colocar una reina en fila_destino marcando todos los N casos posibles.
        Si se encuentra un lugar válido, la función se llama a sí misma tratando de colocar una reina en
        la siguiente fila hasta que todas las N reinas se coloquen en el tablero NxN.
        """
        
        # Se detiene si todas las N filas están ocupadas
        if fila_destino == self.tamaño:
            print("Solucion")
            self.mostrar_tablero(posiciones)
            # self.mostrar_tablero2(positions)
            self.soluciones += 1
        else:
            # Para todas las posiciones de N columnas, intenta colocar una reina
            for columna in range(self.tamaño):
                # Rechazar todas las posiciones inválidas
                if self.comprobar_posicion(posiciones,fila_destino, columna):
                    posiciones[fila_destino] = columna
                    self.poner_reinas(posiciones, fila_destino + 1)
                    


    def comprobar_posicion(self, posiciones, filas_ocupadas, columna):
        """
        Comprueba si una posición determinada está 
        siendo atacada por alguna de las reinas ubicadas previamente (verifique la columna y las posiciones diagonales)
        """
        for i in range(filas_ocupadas):
            if posiciones[i] == columna or  posiciones[i] - i == columna - filas_ocupadas or posiciones[i] + i == columna + filas_ocupadas:
                return False
        return True

    def mostrar_tablero(self, posiciones):
        """Show the full NxN board"""
        for fila in range(self.tamaño):
            linea = ""
            for columna in range(self.tamaño):
                if posiciones[fila] == columna:
                    linea += "R "
                else:
                    linea += ". "
            print(linea)
        print("\n")

    def mostrar_tablero2(self, posiciones):
        """
        Muestre las posiciones de las reinas en el tablero en forma comprimida,
        cada número representa la posición de la columna ocupada en la fila correspondiente.
        """
        linea = ""
        for i in range(self.tamaño):
            linea += str(posiciones[i]) + " "
        print(linea)

def main():
    """Inicializa y resuelve el rompecabezas n reinas"""
    tamaño = int(input("Ingrese la cantidad de Reinas: "))
    NQueens(tamaño)

if __name__ == "__main__":
    # ejecutar solo si se ejecuta como un script
    main()

