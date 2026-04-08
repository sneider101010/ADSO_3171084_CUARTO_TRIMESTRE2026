class Operacion: #clase
    def __init__(self, dato1, dato2): #constructor
        self.dato1 = dato1 #atributos 
        self.dato2 = dato2
        #metodos
    def calcular(self):
        print("Operaciones genericas en matematicas")

class Suma(Operacion):
    def calcular(self):
        resultado = self.dato1 + self.dato2
        print(f"La suma es: {resultado}")

class Resta(Operacion):
    def calcular(self):
        resultado = self.dato1 - self.dato2
        print(f"La resta es: {resultado}")

class Multiplicacion(Operacion):
    def calcular(self):
        resultado = self.dato1 * self.dato2
        print(f"La multiplicacion es: {resultado}")

class Division(Operacion):
    def calcular(self):
        if self.dato2 !=0:
            resultado = self.dato1 / self.dato2
            print(f"La division es: {resultado}")
        else:
            print("No se puede dividir entre cero")

def main():
    dato1 = float(input("Ingrese el primer dato:"))
    dato2 = float(input("Ingrese el segundo dato:"))

    operacion1 = Suma(dato1,dato2)
    operacion1.calcular()

    operacion1 = Resta(dato1,dato2)
    operacion1.calcular()

    operacion1 = Multiplicacion(dato1,dato2)
    operacion1.calcular()

    operacion1 = Division(dato1,dato2)
    operacion1.calcular()


if __name__ == "__main__":
    main()