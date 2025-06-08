# Ejemplo de encapsulación
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

cuenta = CuentaBancaria("Juan", 1000)
print(cuenta.get_titular())  # Juan
print(cuenta.get_saldo())  # 1000
cuenta.depositar(500)
print(cuenta.get_saldo())  # 1500
cuenta.retirar(2000)
print(cuenta.get_saldo())  # 1500

# En este ejemplo, la clase `CuentaBancaria` encapsula la información de la cuenta bancaria
# (`titular` y `saldo`) y solo expone la funcionalidad relevante a través de métodos públicos
# (`get_titular`, `get_saldo`, `depositar` y `retirar`).


