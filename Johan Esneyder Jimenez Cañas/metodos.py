class Padre:
    def __init__(self, mensaje):#Constructor, creó un único atributo para ser heredado
        self.mensaje = mensaje

class Hijo(Padre):
    def __init__(self,mensaje,nombre):
        super().__init__(mensaje) # Aquí invoco al atributo que esta en el padre 
        self.nombre = nombre

def main():
    objepadre = Padre("Este es el mensaje del padre")
    print(objepadre.mensaje)
    objetohijo = Hijo("Este es el mensaje del hijo","Johan Jimenez")
    print(objetohijo.mensaje)
    print(objetohijo.nombre)

if __name__ == "__main__":
    main()