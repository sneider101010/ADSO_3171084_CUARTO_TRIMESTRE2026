class Aprendiz:
    def __init__(self, id, nombre, apellido, edad, programa, trimestre, ambiente):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._programa = programa
        self._trimestre = trimestre
        self._ambiente = ambiente

    #Metodos

    def get_id(self):
        return self._id
    
    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    def get_edad(self):
        return self._edad
    
    def get_programa(self):
        return self._programa
    
    def get_trimestre(self):
        return self._trimestre
    
    def get_ambiente(self):
        return self._ambiente
    
    def set_edad(self, nueva_edad):
        if isinstance (nueva_edad, (int)) and nueva_edad >= 14 :
            self._edad = nueva_edad
        else:
            print("La edad debe ser mayor o igual a 14")

    def set_trimestre(self, nuevo_trimestre):
        if isinstance (nuevo_trimestre, (int)) and nuevo_trimestre > 1 :
            self._trimestre = nuevo_trimestre
        else:
            print("El trimestre debe ser mayor a 1")

    def set_ambiente(self, nuevo_ambiente):
        if isinstance (nuevo_ambiente, (str)) and nuevo_ambiente.strip() :
            self._ambiente = nuevo_ambiente
        else:
            print("El ambiente no debe de quedar con espcaios en blanco")

    #Mostrar información

    def mostrar_info(self):
        print(f"Id: {self._id}, Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}, Programa: {self._programa}, Trimestre: {self._trimestre}, Ambiente {self._ambiente}")
        print("----------------------------")

def main():
    aprendiz1 = Aprendiz(1,"Alejandra", "Carvajal", 17, "Ingenieria civil", 4, "Palos")
    aprendiz2 = Aprendiz(2,"Camila", "Cortez", 18, "Administración financiera", 5, "Sur")
    aprendiz3 = Aprendiz(3, "Sofia", "Ortega", 18, "Moda textil", 7, "Costuras")

    print("Información inicial de los aprendices")
    aprendiz1.mostrar_info()
    aprendiz2.mostrar_info()
    aprendiz3.mostrar_info()

    #Actualización edad

    print ("Edad actual:", aprendiz1.get_edad(), aprendiz2.get_edad(), aprendiz3.get_edad())

    aprendiz1.set_edad(18)
    aprendiz2.set_edad(19)
    aprendiz3.set_edad(19)

    print("Actualización de la edad aprendiz 1:", aprendiz1.get_edad())
    print("Actualización de la edad aprendiz 2:", aprendiz2.get_edad())
    print("Actualización de la edad aprendiz 3:", aprendiz3.get_edad())

    print("----------------------------")

    #Actualición trimestre

    print ("Trimestre actual:", aprendiz1.get_trimestre(), aprendiz2.get_trimestre(), aprendiz3.get_trimestre())

    aprendiz1.set_trimestre(5)
    aprendiz2.set_trimestre(6)
    aprendiz3.set_trimestre(8)

    print("Actualización del trimestre aprendiz 1:", aprendiz1.get_trimestre())
    print("Actualización del trimestre aprendiz 2:", aprendiz2.get_trimestre())
    print("Actualización del trimestre aprendiz 3:", aprendiz3.get_trimestre())

    print("----------------------------")

    #Actualización ambiente

    print ("Ambiente actual:", aprendiz1.get_ambiente(), aprendiz2.get_ambiente(), aprendiz3.get_ambiente())

    aprendiz1.set_ambiente("Cemento")
    aprendiz2.set_ambiente("Contabilidad")
    aprendiz3.set_ambiente("Crochet")

    print("Actualización del ambiente aprendiz 1:", aprendiz1.get_ambiente())
    print("Actualización del ambiente aprendiz 2:", aprendiz2.get_ambiente())
    print("Actualización del ambiente aprendiz 3:", aprendiz3.get_ambiente())

if __name__ == "__main__":
    main()