#forma tradicional
#encapsulamiento y validaciones seguras a los atributos

class Libro:
    def __init__(self, titulo, precio):
        self.__titulo = titulo
        self.__precio = precio

#Getter = Consulta, ve, muestra: nos permite acceder al valor almacenado en el atributo de forma segura

    def get_titulo(self):
        #vamos a devolver el valor almacenado en titulo 
        return self.__titulo
    
    def get_precio(self):
        return self.__precio
    
#Setter: modificar valores. controlar y validar los valores antes de ser modificados

    def set_titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, (str)) : #controla y valida el valor de titulo antes de ser modificados
            self.__titulo = nuevo_titulo           #modifica el valor del titulo
        else:
            print("Debe ingresar un titulo valido")
        
    def set_precio(self, nuevo_precio):      #este metodo, me valida y modifica el precio del libro
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio >= 0 :
            self.__precio = nuevo_precio
        else:
            print("Debe ingresar un precio que se un numero valido \n")

#metodo adicional para mostrar la informacion completa del libro

    def mostrar_info(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Precio: {self.__precio:,.2f}")

#metodo principal

def main():
    print("\n === Sistema de libros ADSO ===")

    libro1 = Libro("Boulevar", 300000)

    print("Informacion inicial de los libros")
    libro1.mostrar_info()

    print("Precio actual:", libro1.get_precio())
    
    libro1.set_precio(500000)
    print("El nuevo precio es: ", libro1.get_precio())

    print("Informacion nueva del libro\n")
    libro1.mostrar_info()

    print("Programa finalizado")

if __name__ == "__main__":
    main()
