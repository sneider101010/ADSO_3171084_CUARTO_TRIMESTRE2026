class Vehiculo:
    #esta clase va a ser mi clase padre
    def mover(self): #metodo que reutilizare en los hijos
        print("El vehiculo se está moviendo")

class Moto(Vehiculo):
    pass

#definición del metodo principal

def main():
    vehiculo1 = Vehiculo()
    moto1 = Moto()
    print("Metodo desde la clase vehiculo")
    moto1.mover()

if __name__ == "__main__":
    main()