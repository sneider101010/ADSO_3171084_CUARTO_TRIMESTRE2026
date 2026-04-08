from abc import ABC, abstractmethod
class  Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

#Ecuación circulo

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)
    
#Ecuación triangulo
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
#Ecuación rectangulo
        
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        return (self.base * self.altura)

#Ecuación cubo

class Cubo(Figura):
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return 6 * (self.lado ** 2)

#Ecuación cilindro

class Cilindro(Figura):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def calcular_area(self):
        return (2 * 3.1416 * self.radio * self.altura) + (2 * 3.1416 * self.radio ** 2)

def mostrar_area(figura: Figura):
    print(f"Area {figura.calcular_area():,.2f}")

def main():
    print("Area del circulo")
    circulo1 = Circulo(5)
    mostrar_area(circulo1)
    print("--------------------------")
    print("Area del triangulo")
    triangulo1 = Triangulo(8, 5)
    mostrar_area(triangulo1)
    print("--------------------------")
    print("Area del rectangulo")
    rectangulo1 = Rectangulo(9, 4)
    mostrar_area(rectangulo1)
    print("--------------------------")
    print("Area del cubo")
    cubo1 = Cubo(5)
    mostrar_area(cubo1)
    print("--------------------------")
    print("Area del cilindro")
    cilindro1 = Cilindro(3, 4)
    mostrar_area(cilindro1)
    print("--------------------------")
if __name__ == "__main__":
    main()
        
