# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese la temperatura de cada día de la semana:")
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias:
        while True:
            try:
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Valor no válido. Ingrese un número.")

    return temperaturas


# Función para calcular el promedio de la semana
def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        return 0
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Función principal que organiza el flujo
def main():
    print("=== Sistema de Registro de Temperaturas Semanales ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print("\nTemperaturas registradas:", temperaturas)
    print(f"Promedio semanal de temperatura: {promedio:.2f} °C")


# Llamada a la función principal
main()

# Explicación del flujo:
#1Ingresar_temperaturas(): pide al usuario la temperatura de cada día de la semana.
#2Calcular_promedio(lista): calcula el promedio de una lista de temperaturas.
#3main(): organiza el flujo lógico del programa, llamando a las otras funciones.



