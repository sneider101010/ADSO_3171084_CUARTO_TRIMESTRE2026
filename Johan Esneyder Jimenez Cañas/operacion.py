class Operacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Inicializando Operacion...")
    def calcular(self):
        print("Operacion Generica")

class Suma(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("preparando operacion suma")
    def calcular(self):
        super().calcular()
        resultado = self.a + self.b
        print(f"La suma es {resultado}")

class Resta(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("preparando operacion resta")
    def calcular(self):
        resultado = self.a - self.b
        print(f"La Resta es: {resultado}")


class Multiplicacion(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("preparando operacion multiplicacion")
    def calcular(self):
        resultado = self.a * self.b
        print(f"La Multiplicacion es: {resultado}")


class Division(Operacion):
    def __init__(self, a, b):
        super().__init__(a,b)
        print("preparando operacion division")
    def calcular(self):
        if self.b !=0:
           resultado = self.a / self.b
           print(f"la division es: {resultado}")
        else:
           print("No se puede dividir entre cero")


def main():
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    operacion1 = Suma(num1,num2)
    operacion1.calcular()
    print("---------------------------")

    operacion1 = Resta(num1,num2)
    operacion1.calcular()
    print("---------------------------")

    operacion1 = Multiplicacion(num1,num2)
    operacion1.calcular()
    print("---------------------------")

    operacion1 = Division(num1,num2)
    operacion1.calcular()
    print("---------------------------")
    
if __name__ == "__main__":
    main()