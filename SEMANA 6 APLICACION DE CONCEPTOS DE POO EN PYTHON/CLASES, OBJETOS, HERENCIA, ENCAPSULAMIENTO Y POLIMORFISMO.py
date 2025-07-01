# Clase base que representa a una persona
class Persona:
    def __init__(self, nombre, edad):
        # Encapsulamos los atributos con doble guion bajo
        self.__nombre = nombre
        self.__edad = edad

    # Método para mostrar información (acceso a atributos encapsulados)
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre}, Edad: {self.__edad}")

    # Métodos getter y setter para acceder y modificar el nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre


# Clase derivada que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.carrera = carrera

    # Sobrescribimos el método para demostrar polimorfismo
    def mostrar_info(self):
        print(f"Estudiante de {self.carrera} - Nombre: {self.get_nombre()}")


# Otra clase para mostrar polimorfismo con métodos diferentes
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def mostrar_info(self):
        print(f"Profesor de {self.materia} - Nombre: {self.get_nombre()}")


# Función que demuestra polimorfismo al recibir cualquier tipo de persona
def presentar_persona(persona):
    persona.mostrar_info()


# Crear instancias y demostrar funcionamiento
persona1 = Persona("Cristhian", 20)
estudiante1 = Estudiante("Ana", 18, "Ingeniería")
profesor1 = Profesor("Carlos", 30, "Matemáticas")

# Encapsulación: accedemos a atributos privados mediante getters/setters
print("Encapsulación:")
print(persona1.get_nombre())  # Acceso al nombre con getter
persona1.set_nombre("Cristhian Rimael")  # Modificamos con setter
persona1.mostrar_info()

print("\nHerencia y Polimorfismo:")
# Cada objeto usa su propio método mostrar_info (polimorfismo)
presentar_persona(persona1)
presentar_persona(estudiante1)
presentar_persona(profesor1)
