
# Clase que representa una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero         # Número de la habitación
        self.tipo = tipo             # Tipo (Ej: sencilla, doble, suite)
        self.precio = precio         # Precio por noche
        self.ocupada = False         # Estado de ocupación

    def reservar(self):
        if not self.ocupada:
            self.ocupada = True
            print(f"Habitación {self.numero} ha sido reservada.")
        else:
            print(f"Habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"Habitación {self.numero} ha sido liberada.")
        else:
            print(f"Habitación {self.numero} ya está libre.")

    def mostrar_info(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        print(f"Habitación {self.numero} - Tipo: {self.tipo}, Precio: ${self.precio}, Estado: {estado}")

# Clase que representa a un cliente
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre      # Nombre del cliente
        self.cedula = cedula      # Documento de identificación

# Clase que gestiona el hotel y sus reservas
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []  # Lista de objetos Habitacion
        self.reservas = {}      # Diccionario con cédula del cliente como clave

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        for hab in self.habitaciones:
            hab.mostrar_info()

    def reservar_habitacion(self, cliente, numero_habitacion):
        for hab in self.habitaciones:
            if hab.numero == numero_habitacion:
                if not hab.ocupada:
                    hab.reservar()
                    self.reservas[cliente.cedula] = hab.numero
                    print(f"Reserva realizada a nombre de {cliente.nombre}.")
                else:
                    print("No se puede reservar: habitación ocupada.")
                return
        print("Habitación no encontrada.")

    def liberar_habitacion(self, cedula_cliente):
        if cedula_cliente in self.reservas:
            numero = self.reservas[cedula_cliente]
            for hab in self.habitaciones:
                if hab.numero == numero:
                    hab.liberar()
                    del self.reservas[cedula_cliente]
                    print(f"Habitación liberada para el cliente con cédula {cedula_cliente}.")
                    return
        print("No hay reservas activas para ese cliente.")

# -------------------------------
# Ejemplo de uso del sistema
# -------------------------------

# Crear hotel
mi_hotel = Hotel("Hotel Paraíso")

# Agregar habitaciones al hotel
mi_hotel.agregar_habitacion(Habitacion(101, "Sencilla", 30))
mi_hotel.agregar_habitacion(Habitacion(102, "Doble", 50))
mi_hotel.agregar_habitacion(Habitacion(103, "Suite", 80))

# Mostrar habitaciones disponibles
print("\n--- Habitaciones disponibles ---")
mi_hotel.mostrar_habitaciones()

# Crear un cliente
cliente1 = Cliente("Cristhian Chacha", "0250142528")

# Hacer una reserva
print("\n--- Realizando reserva ---")
mi_hotel.reservar_habitacion(cliente1, 102)

# Ver estado de las habitaciones
print("\n--- Estado actual de habitaciones ---")
mi_hotel.mostrar_habitaciones()

# Liberar una habitación
print("\n--- Liberando habitación ---")
mi_hotel.liberar_habitacion("0250142528")

# Ver estado final
print("\n--- Estado final ---")
mi_hotel.mostrar_habitaciones()



