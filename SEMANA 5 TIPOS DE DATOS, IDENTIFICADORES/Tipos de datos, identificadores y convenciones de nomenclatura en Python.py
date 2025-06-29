
# Programa para convertir temperaturas entre Celsius y Fahrenheit
# El usuario puede elegir el tipo de conversión y proporcionar la temperatura.
# Se hace uso de distintos tipos de datos: integer, float, string y boolean.

def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_a_celsius(fahrenheit: float) -> float:
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9

def es_opcion_valida(opcion: str) -> bool:
    """Verifica si la opción ingresada es válida."""
    return opcion.lower() in ["c", "f"]

def main():
    print("Conversor de temperaturas")
    print("Seleccione el tipo de conversión:")
    print("C - Celsius a Fahrenheit")
    print("F - Fahrenheit a Celsius")

    # Solicita al usuario una opción y la válida
    opcion_conversion: str = input("Ingrese su opción (C/F): ").strip()

    if not es_opcion_valida(opcion_conversion):
        print("Opción no válida. Intente nuevamente.")
        return

    # Solicita al usuario la temperatura a convertir
    try:
        temperatura: float = float(input("Ingrese la temperatura a convertir: "))
    except ValueError:
        print("Valor no válido. Debe ingresar un número.")
        return

    # Realiza la conversión según la opción elegida
    if opcion_conversion.lower() == "c":
        resultado: float = celsius_a_fahrenheit(temperatura)
        print(f"{temperatura} °C son {resultado:.2f} °F")
    else:
        resultado: float = fahrenheit_a_celsius(temperatura)
        print(f"{temperatura} °F son {resultado:.2f} °C")

# Llamamos a la función principal
if __name__ == "__main__":
    main()
