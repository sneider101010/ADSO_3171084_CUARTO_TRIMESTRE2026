class Cliente:
    def __init__(self, id, nombres, apellidos, estatura, edad, saldo):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__estatura = estatura
        self.__edad = edad
        self.__saldo = saldo

    def get_id(self):
        return self.__id

    def get_nombres(self):
        return self.__nombres
    
    def get_apellidos(self):
        return self.__apellidos
    
    def get_estatura(self):
        return self.__estatura
    
    def get_edad(self):
        return self.__edad
    
    def get_saldo(self):
        return self.__saldo
    
    def set_estatura(self, nueva_estatura):
        if isinstance(nueva_estatura, (int, float)) and nueva_estatura > 1 :
            self.__estatura = nueva_estatura
        else:
            print("La estatura debe ser mayor a 1")
    
    def set_edad(self, nueva_edad):
        if isinstance(nueva_edad, (int,float)) and nueva_edad > 0 :
            self.__edad = nueva_edad
        else:
            print("La edad debe ser mayor a cero")

    def set_saldo(self, nuevo_saldo):
        if isinstance(nuevo_saldo, (int,float)) and nuevo_saldo > 0 :
            self.__saldo = nuevo_saldo
        else: 
            print("")

    def mostrar_info(self):
        print(f"\nId: {self.__id}, Nombres: {self.__nombres}, Apellidos: {self.__apellidos}, Estatura: {self.__estatura}, Edad: {self.__edad}, Saldo: {self.__saldo}\n")
        print("------------")

def main():
    cliente1 = Cliente(1,"Alejandra", "Carvajal", 1.65, 17, 5000)
    cliente2 = Cliente(2,"Camila", "Cortez", 1.63, 18, 10000)

    print("Información inicial del cliente")
    cliente1.mostrar_info()

    #Actualización edad

    print("Edad Actual:", cliente1.get_edad())

    cliente1.set_edad(18)

    print("Actualizaciòn de la edad:", cliente1.get_edad())

    #Actualización estatura

    print("Estatura actual")

    cliente1.set_estatura(1.68)

    print("Actualizaciòn de la estatura:", cliente1.get_estatura())

    #Actualización saldo

    print("Saldo actual", cliente1.get_saldo())

    cliente1.set_saldo(8000)

    print("Actualizaciòn del saldo:", cliente1.get_saldo())

    print("\nPrograma finalizado")

if __name__=="__main__":
    main()