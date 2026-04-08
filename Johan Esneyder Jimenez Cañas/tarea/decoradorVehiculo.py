class Vehiculo:
    def __init__(self, id, tipo, marca, modelo, precio):
        self.__id = id
        self.__tipo = tipo
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    # Getter

    @property
    def id(self):
        return self.__id
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def precio(self):
        return self.__precio
    
    # Setter

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if isinstance(nuevo_tipo, str) and nuevo_tipo.strip():
            self.__tipo = nuevo_tipo
        else:
            print("El tipo no debe quedar con espacios en blanco")

    @marca.setter
    def marca(self, nueva_marca):
        if isinstance(nueva_marca, str) and nueva_marca.strip():
            self.__marca = nueva_marca
        else:
            print("La marca no debe quedar con espacios en blanco")
    
    @modelo.setter
    def modelo(self, nuevo_modelo):
        if isinstance(nuevo_modelo, str) and nuevo_modelo.strip():
            self.__modelo = nuevo_modelo
        else:
            print("El modelo no debe quedar con espacios en blanco")

    @precio.setter
    def precio(self, nuevo_precio):
        if isinstance(nuevo_precio, (int, float)) and nuevo_precio > 0:
            self.__precio = nuevo_precio
        else: 
            print("El precio debe ser mayor a 0")

    # Mostrar Información
    def mostrar_info(self):
        print(f"ID: {self.__id}, Tipo: {self.__tipo}, Marca: {self.__marca}, Modelo: {self.__modelo}, Precio: {self.__precio:.2f}")
        

def main():
    vehiculo1 = Vehiculo(1, "moto", "AKT", "2027", 8500000)
    vehiculo2 = Vehiculo(2, "avión", "vuela-vuela", "2030", 55000000)

    # Información inicial
    print("La información inicial de los vehículos es: ")
    vehiculo1.mostrar_info()
    print("-------------------")
    vehiculo2.mostrar_info()
    print("-------------------")

    # Modificación tipo
    print("Tipo actual:", vehiculo1.tipo, vehiculo2.tipo)

    vehiculo1.tipo = "Dirigible"
    vehiculo2.tipo = "Submarino"

    print(vehiculo1.tipo)
    print(vehiculo2.tipo)
    print("-------------------")

    # Modificación marca
    print("Marca actual:", vehiculo1.marca, vehiculo2.marca)

    vehiculo1.marca = str(input("ingrese la marca del vehiculo 1... "))
    vehiculo2.marca = str(input("ingrese la marca del vehiculo 2... "))

    print(vehiculo1.marca)
    print(vehiculo2.marca)
    print("-------------------")

    # Modificación modelo
    print("Modelo actual:", vehiculo1.modelo, vehiculo2.modelo)

    vehiculo1.modelo = str(input("ingrese la modelo del vehiculo 1..."))
    vehiculo2.modelo = str(input("ingrese la modelo del vehiculo 2... "))

    print(vehiculo1.modelo)
    print(vehiculo2.modelo)
    print("-------------------")

    # Modificación precio
    print("Precio actual:", vehiculo1.precio, vehiculo2.precio)

    vehiculo1.precio = float(input("ingrese el precio del vehiculo 1:"))
    vehiculo2.precio = float(input("ingrese el precio del vehiculo 2:"))

    print(vehiculo1.precio)
    print(vehiculo2.precio)
    print("-------------------")

    
    vehiculo1.mostrar_info()
    vehiculo2.mostrar_info()

if __name__ == "__main__":
    main()
