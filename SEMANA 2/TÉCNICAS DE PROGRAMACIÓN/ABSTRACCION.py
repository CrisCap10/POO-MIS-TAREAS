# Ejemplo de abstracción
class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrar_detalle(self):
        print(f"Color: {self.color}, Ruedas: {self.ruedas}")

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Velocidad: {self.velocidad}")

coche = Coche("Rojo", 4, 120)
coche.mostrar_detalle()

#En este ejemplo, la clase `Vehiculo` es una abstracción que define una interfaz común
# para todos los vehículos. La clase `Coche` hereda de `Vehiculo` y agrega una nueva
# característica (`velocidad`) que no está presente en la clase base.
