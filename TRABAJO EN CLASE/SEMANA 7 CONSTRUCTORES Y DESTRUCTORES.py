#Cristhian Chacha
#SEGUNO SEMESTRE "A"
#POO

class Vehiculo:
    def __init__(self, placa, tipo):
        """
        Constructor que simula el ingreso de un vehículo al parqueadero.
        """
        self.__placa = placa  # atributo encapsulado
        self.__tipo = tipo    # atributo encapsulado
        print(f"[ENTRADA] Vehículo tipo '{self.__tipo}' con placa '{self.__placa}' ha ingresado al parqueadero.")

    def mostrar_info(self):
        """
        Método para mostrar información del vehículo.
        """
        print(f"Vehículo: Tipo = {self.__tipo}, Placa = {self.__placa}")

    def __del__(self):
        """
        Destructor que simula la salida del vehículo del parqueadero.
        """
        print(f"[SALIDA] Vehículo tipo '{self.__tipo}' con placa '{self.__placa}' ha salido del parqueadero.")


# Simulación del sistema
def simular_parqueadero():
    print("Simulación del parqueadero iniciada...\n")

    # Ingreso de vehículos
    v1 = Vehiculo("ABC-123", "Carro")
    v2 = Vehiculo("XYZ-789", "Moto")
    v3 = Vehiculo("MNO-456", "Camioneta")

    print("\nMostrando información de los vehículos:")
    v1.mostrar_info()
    v2.mostrar_info()
    v3.mostrar_info()

    print("\nSimulando salida de algunos vehículos...")
    # Salida de vehículos (se elimina el objeto)
    del v1
    del v2

    print("\nVehículos restantes en el parqueadero:")
    v3.mostrar_info()

    print("\nFin de la simulación. Todos los objetos serán eliminados automáticamente al terminar el programa.")


# Ejecutar simulación
simular_parqueadero()



