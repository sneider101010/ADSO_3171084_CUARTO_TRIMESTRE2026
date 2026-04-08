class Empleado:
    def trabajar(self):
        print("El empleado está realizando tareas generales")

class Gerente(Empleado):
    def trabajar(self):
        print("El gerente está administrando la empresa")
    pass
class Vendedor(Empleado):
    def trabajar(self):
        print("El vendedor atiende un cliente")
    pass

def main():

    gerente1 = Gerente()
    gerente1.trabajar()
    vendedor1 = Vendedor()
    vendedor1.trabajar()

if __name__ == "__main__":
    main()




    