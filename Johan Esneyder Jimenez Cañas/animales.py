class Animal:
    def sonido(self):
        print("El animal hace sonidos")

class Perro(Animal):
    def sonido(self):
        print("El perro hace:")
        print("Guau Guau")
    pass

class Gato(Animal):
    def sonido(self):
        print("El gato hace:")
        print("Miau Miau")
    pass

class Leon(Animal):
    def sonido(self):
        print("El leon hace:")
        print("rawr rawr")
    pass

class Aguila(Animal):
    def sonido(self):
        print("El aguila hace:")
        print("fiuuu cúcuaaa cúcuaaa")
    pass

def main():
    perro1 = Perro()
    perro1.sonido()
    gato1 = Gato()
    gato1.sonido()
    leon1 = Leon()
    leon1.sonido()
    aguila1 = Aguila()
    aguila1.sonido()

if __name__ == "__main__":
    main()
    