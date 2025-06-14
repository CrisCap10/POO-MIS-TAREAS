# Clase base que representa el clima diario
class ClimaDia:
    def __init__(self, dia, temperatura):
        self._dia = dia                # Encapsulamiento: atributos privados
        self._temperatura = temperatura

    def get_temperatura(self):
        return self._temperatura

    def get_dia(self):
        return self._dia

    def __str__(self):
        return f"{self._dia}: {self._temperatura} °C"


# Clase hija que representa una semana de clima, usando herencia
class ClimaSemana:
    def __init__(self):
        self._registro_semanal = []  # Lista de objetos ClimaDia

    def ingresar_datos(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    clima_dia = ClimaDia(dia, temp)
                    self._registro_semanal.append(clima_dia)
                    break
                except ValueError:
                    print("Error: Debe ingresar un número válido.")

    def calcular_promedio(self):
        if not self._registro_semanal:
            return 0
        total = sum([dia.get_temperatura() for dia in self._registro_semanal])
        return total / len(self._registro_semanal)

    def mostrar_datos(self):
        print("\n Registro de temperaturas semanales:")
        for dia in self._registro_semanal:
            print(dia)

        print(f"\n Promedio semanal: {self.calcular_promedio():.2f} °C")


# Clase alternativa que redefine comportamiento para mostrar datos en Fahrenheit (polimorfismo)
class ClimaSemanaFahrenheit(ClimaSemana):
    def mostrar_datos(self):
        print("\n Registro en Fahrenheit:")
        for dia in self._registro_semanal:
            fahrenheit = dia.get_temperatura() * 9/5 + 32
            print(f"{dia.get_dia()}: {fahrenheit:.2f} °F")

        promedio = self.calcular_promedio() * 9/5 + 32
        print(f"\n Promedio semanal: {promedio:.2f} °F")


# Función principal que ejecuta todo
def main():
    print("=== Registro de Temperaturas (POO) ===")

    semana = ClimaSemana()  # o ClimaSemanaFahrenheit() para mostrar en °F
    semana.ingresar_datos()
    semana.mostrar_datos()


# Ejecutar
main()

# En este programa se aplican tres conceptos fundamentales de la Programación Orientada a Objetos.

# Primero, el encapsulamiento se utiliza al declarar los atributos _dia y _temperatura como privados
# dentro de la clase ClimaDia, protegiendo así la integridad de los datos y accediendo a ellos mediante métodos.

# Luego, se aplica la herencia al crear la clase ClimaSemanaFahrenheit, que hereda de ClimaSemana para reutilizar
# sus métodos y atributos sin tener que reescribir todo el código.

# Finalmente, se implementa el polimorfismo al redefinir el método mostrar_datos() en la subclase ClimaSemanaFahrenheit,
# modificando su comportamiento para presentar las temperaturas en grados Fahrenheit en lugar de Celsius.

