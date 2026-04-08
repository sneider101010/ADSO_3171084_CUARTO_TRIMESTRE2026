from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str) -> None:
        self._nombre = None
        self.nombre = nombre #llama al setter

    #Getter
    @property
    def nombre(self) -> str:
        #acceso seguro al nombre del empleado
        return self._nombre
    
    @nombre.setter #decoradores "profesional"
    def nombre(self, valor: str) -> None:
        if isinstance(valor, str) and valor.strip():
            self._nombre = valor.strip()
        else:
            raise ValueError("El nombre debe tener un texto valido")
        
def trabajar(self) -> None:
    pass

class Gerente(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} está administrando la empresa")

class Desarrollador(Empleado):
    def trabajar(self) -> None:
        print(f"{self.nombre} está programando los diagramas de clase en Java")

def ejecutar_tarea(empleado: Empleado) -> None:
    empleado.trabajar()

def main():
    print("\n************ INICIO DEL PROGRAMA EMPLEADOS ************")
    gerente1 = Gerente("Laaura Perez")
    desarrollador1 = Desarrollador("Johan Jimenez")

    ejecutar_tarea(gerente1)
    ejecutar_tarea(desarrollador1)
    print("\n------------------------------------")
    print("Actualizar el nombre del desarrollador")
    desarrollador1.nombre = "Pinpunpan"
    print(f"El nuevo desarrollador es: {desarrollador1.nombre}")
    print("\n************ FIN DEL PROGRAMA EMPLEADOS ************")
if __name__ == "__main__":
    main()
     
        