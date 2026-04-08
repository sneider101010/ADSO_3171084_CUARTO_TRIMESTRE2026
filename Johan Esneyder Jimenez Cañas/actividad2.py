class Mueble:
    def __init__(self, id, nombre, dimensioncm, color, propietario, material, ubicacion):
        self.__id = id
        self.__nombre = nombre
        self.__dimensioncm = dimensioncm
        self.__color = color
        self.__propietario = propietario
        self.__material = material
        self.__ubicacion = ubicacion

    # Métodos de acceso (getters)
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_dimensioncm(self):
        return self.__dimensioncm
    
    def get_color(self):
        return self.__color
    
    def get_propietario(self):
        return self.__propietario
    
    def get_material(self):
        return self.__material
    
    def get_ubicacion(self):
        return self.__ubicacion
    
    # Métodos de modificación (setters)

    def set_color(self, nuevo_color):
        if isinstance(nuevo_color, str) and nuevo_color.strip():
            self.__color = nuevo_color
        else:
            print("El color no debe quedar con espacios en blanco")

    def set_propietario(self, nuevo_propietario):
        if isinstance(nuevo_propietario, str) and nuevo_propietario.strip():
            self.__propietario = nuevo_propietario
        else:
            print("El propietario no debe quedar en blanco")

    def set_ubicacion(self, nueva_ubicacion):
        if isinstance(nueva_ubicacion, str) and nueva_ubicacion.strip():
            self.__ubicacion = nueva_ubicacion
        else:
            print("La ubicación no debe quedar con espacios en blanco")

    # Mostrar información
    def mostrar_info(self):
        print(f"Id: {self.__id}\nNombre: {self.__nombre}\nDimensión: {self.__dimensioncm}\nColor: {self.__color}\nPropietario: {self.__propietario}\nMaterial: {self.__material}\nUbicación: {self.__ubicacion}")


def main():
    mueble1 = Mueble(1, "Plana", "12cm", "Azul", "Juan", "Bronce", "Segundo piso")
    mueble2 = Mueble(2, "Cortaje", "7cm", "Blanco", "Ingrid","Plastico", "Planta baja")
    
    print("Información inicial de los muebles:")
    mueble1.mostrar_info()
    print("--------------")
    mueble2.mostrar_info()

    #Actualizacion color

    mueble1.set_color("Rojo")
    mueble2.set_color("Amarillo")

    print("\nInformacion actualizada de los muebles:")
    mueble1.mostrar_info()
    print("--------------")
    mueble2.mostrar_info()

    mueble1.set_propietario("Fernando")
    mueble2.set_propietario("Samantha")

    print("\nInformación actualizada de los muebles:")
    mueble1.mostrar_info()
    print("--------------")
    mueble2.mostrar_info() 

    mueble1.set_ubicacion("Tercer piso")
    mueble2.set_ubicacion("Ambiente costura")

    print("\nInformación actualizada de los muebles:")
    mueble1.mostrar_info()
    print("--------------")
    mueble2.mostrar_info() 


if __name__ == "__main__":   
    main()
