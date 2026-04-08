class Aprendiz:
    def __init__(self, nombre, documento, edad, programa, promedio):
        self.__nombre = nombre
        self.__documento = documento
        self.__edad = edad
        self.__programa = programa
        self.__promedio = promedio

    #Metodos

    def get_nombre(self):
        return self.__nombre
    
    def get_documento(self):
        return self.__documento
    
    def get_edad(self):
        return self.__edad
    
    def get_programa(self):
        return self.__programa
    
    def get_promedio(self):
        return self.__promedio
    
    def set_nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, (str)) and nuevo_nombre.strip():
            self.__nombre = nuevo_nombre
        else:
            print("El nombre no puede quedar con espacios en blanco")

    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, (int)) and nueva_edad >= 14:
            self.__edad = nueva_edad
        else:
            print("La edad debe de ser mayor o igual a 14")

    def set_programa(self, nuevo_programa):
        if isinstance(nuevo_programa, (str)) and nuevo_programa.strip():
            self.__programa  = nuevo_programa
        else:
            print("El programa no puede quedar con espacios en blanco")

    def set_promedio(self, nuevo_promedio):
        if isinstance(nuevo_promedio, (int)) and nuevo_promedio <= 50 :
            self.__promedio = nuevo_promedio
        else:
            print("El promedio debe ser menor o igual a 50")

    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}\nDocumento: {self.__documento}\nEdad: {self.__edad}\nPrograma: {self.__programa}\nPromedio: {self.__promedio}")


#metodo principal

def main():
    aprendiz1 = Aprendiz("Samuel Qkisuelta", 1012363479, 18, "tu chapa", 39)
    aprendiz2 = Aprendiz("Sofia mama", 1254632514, 18, "vacas a la u", 50)
    aprendiz3 = Aprendiz("Josep ra", 4512365214, 25, "brinquen", 48)

    #Informacion inicial

    print("--------------------")
    print("Informacion inicial de los aprendices:")
    aprendiz1.mostrar_info()
    print("--------------------")
    aprendiz2.mostrar_info()
    print("--------------------")
    aprendiz3.mostrar_info()
    print("--------------------")

    #Modificacion

    aprendiz1.set_edad(19)
    aprendiz2.set_edad(25)
    aprendiz3.set_edad(43)
    print("Actualizacion de la edad:", aprendiz1.get_edad(), aprendiz2.get_edad(), aprendiz3.get_edad()) 

    aprendiz1.set_programa("MySQL")
    aprendiz2.set_programa("Azul")
    aprendiz3.set_programa("Mongo")
    print("Actualizacion del programa:", aprendiz1.get_programa(), aprendiz2.get_programa(), aprendiz3.get_programa()) 

    aprendiz1.set_promedio(26)
    aprendiz2.set_promedio(41)
    aprendiz3.set_promedio(46)
    print("Actualizacion del promedio:", aprendiz1.get_promedio(), aprendiz2.get_promedio(), aprendiz3.get_promedio()) 

    #Informacion modificada

    print("Informacion actualiza")
    aprendiz1.mostrar_info()
    print("--------------------")
    print("Información actualizada")
    aprendiz2.mostrar_info()
    print("--------------------")
    print("Información actualizada")
    aprendiz3.mostrar_info()

if __name__ == "__main__":
    main()

#Creacion nuevos aprendices

def main(): 
    nombre = input("Ingrese el nombre: ") 
    documento = int(input("Ingrese el documento: ")) 
    edad = int(input("Ingrese la edad: ")) 
    programa = input("Ingrese el programa: ") 
    promedio = int(input("Ingrese el promedio: ")) 
    aprendiz_nuevo = Aprendiz(nombre, documento, edad, programa, promedio) 
    print("\nInformación del aprendiz creado:") 
    aprendiz_nuevo.mostrar_info()

if __name__ == "__main__":
    main()