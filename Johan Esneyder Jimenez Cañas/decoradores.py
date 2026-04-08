class Libro:
    def __init__(self, id, titulo, precio):
        self.__id = id
        self.__titulo = titulo
        self.__precio = precio

    @property
    def titulo(self):
        return self.__titulo

    @property
    def precio(self):
        return self.__precio

    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            print("Debe ingresar un texto")

    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no debe ser menor a 0")

    def mostrar_info(self):
        print(f"El título del libro es: {self.__titulo}, El precio es ${self.__precio:.2f}")


def main():
    libro1 = Libro(1, "El principito", 250000)
    libro1.mostrar_info()

    # Modificación
    libro1.titulo = "Boulevard"  
    print(libro1.titulo)  

    libro1.precio = 160000
    print(libro1.precio)

    libro1.mostrar_info()

if __name__ == "__main__":
    main()
