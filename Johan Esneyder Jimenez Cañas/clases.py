class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self._precio = nuevo_precio
        else:
            print("El precio debe ser un número positivo.")

    def mostrar_info(self):
        print(f"\nTitulo: {self.__titulo}, Precio {self.__precio:,.2f}\n")
        print("------------------")

def main():
    libro1 = Libro("Boulevard", 120000)
    libro2 = Libro("casa de muñecas", 130000)

    print("Informacion inicial del libro")
    libro1.mostrar_info()
    libro2.mostrar_info()

    print("Precio actual:", libro1.get_precio())

    libro1.set_precio(120000)

    print("Nuevo precio:", libro1.get_precio())

    print("\nPrograma finalizado")

if __name__=="__main__":
    main()
        
    




