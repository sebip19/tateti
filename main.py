# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Tablero:
    turno = 0
    grilla = [None, None, None, None, None, None, None, None, None]
    cantidad_veces_jugado = 0
    terminado = False

    def establecer_ganador(self, quien):
        print("GANO: " + self.quien_es(quien))
        self.imprimir_grilla()
        terminado = True

    def ya_termino(self):
        for i in range(2):
            for j in range(0,9,3):
                if self.grilla[j] == i and self.grilla[j+1] == i and self.grilla[j+2] == i:
                    self.establecer_ganador(i)
                    return True
            for j in range(3):
                if self.grilla[j] == i and self.grilla[j + 3] == i and self.grilla[j + 6] == i:
                    self.establecer_ganador(i)
                    return True
            for x in ([2,4,6], [0,4,8]):
                if self.grilla[x[0]] == i and self.grilla[x[1]] == i and self.grilla[x[2]] == i:
                    self.establecer_ganador(i)
                    return True
        if self.cantidad_veces_jugado == 9:
            return True
        return False

    def imprimir_grilla(self):
        grilla = ""
        contador = 0
        for i in range(9):
            grilla +=" " + self.quien_es(self.grilla[i]) + " "
            if contador==2:
                grilla+="\n"
                contador=0
                continue
            contador+=1
            grilla+="|"
        print(grilla)

    def imprimir_grilla_vacia(self):
        print(" 1 | 2 | 3\n 4 | 5 | 6\n 7 | 8 | 9\n")

    def quien_es(self, numero):
        if numero is None:
            return "-"
        equis = "X"
        circulo = "O"
        return circulo if numero == 0 else equis

    def a_quien_le_toca(self):
        return self.quien_es(self.turno)

    def pasar_turno(self):
        self.turno =  1 if self.turno == 0 else 0

    def comprobar_eleccion(self, seleccion):
        if not seleccion.isnumeric():
            print("no es numero excep")
            return
        seleccion = int(seleccion)
        seleccion=seleccion-1
        if 0 > int(seleccion) or int(seleccion) > 8:
            print("fuera de rango excep")
            return
        if not self.grilla[seleccion] is None:
            print("Ya esta ocupado. Elegí otro lugar.\n")
            return
        self.grilla[seleccion] = self.turno
        self.pasar_turno()
        self.cantidad_veces_jugado+=1
        return

    def jugar(self):
        while not self.ya_termino():
            self.imprimir_grilla_vacia()
            self.imprimir_grilla()
            print("Es el turno de " + self.a_quien_le_toca() + ".")
            pos_elegida = input("Elegí la posición: ")
            self.comprobar_eleccion(pos_elegida)

def main():
    juego = Tablero()
    juego.jugar()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
