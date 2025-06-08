# Ejemplo de herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Habla")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def ladrar(self):
        print("Ladra")

perro = Perro("Fido", "Golden")
print(perro.nombre)  # Fido
print(perro.raza)  # Golden
perro.hablar()  # Habla
perro.ladrar()  # Ladra

# En este ejemplo, la clase `Perro` hereda la implementación de la clase `Animal` y
# agrega una nueva característica (`raza`) y un nuevo metodo (`ladrar`).

