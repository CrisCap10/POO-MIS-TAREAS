# ===============================
# Clase Producto
# ===============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# ===============================
# Clase Inventario con archivos
# ===============================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # Cargar inventario desde archivo
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                    except ValueError:
                        print(f" Línea inválida en el archivo y fue ignorada: {linea.strip()}")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
            self.guardar_en_archivo()
        except PermissionError:
            print("Error: No tienes permiso para acceder al archivo.")

    # Guardar inventario en archivo
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            print("Error: No se pudo guardar el archivo. Verifica permisos.")

    # Añadir producto (validando ID único)
    def agregar_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos.append(producto)
            self.guardar_en_archivo()
            print("Producto añadido con éxito y guardado en archivo.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("Producto eliminado con éxito del archivo.")
                return
        print("Error: No se encontró el producto con ese ID.")

    # Actualizar cantidad o precio por ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                self.guardar_en_archivo()
                print("Producto actualizado con éxito en el archivo.")
                return
        print("Error: No se encontró el producto con ese ID.")

    # Buscar productos por nombre (pueden haber varios)
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print("Resultados de la búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n Inventario actual:")
            for p in self.productos:
                print(p)


# ===============================
# Menú interactivo
# ===============================
def menu():
    inventario = Inventario()

    while True:
        print("\n=== MENÚ DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID único: "))
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: ID inválido.")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))
                nueva_cantidad = input("Nueva cantidad (deje vacío si no cambia): ")
                nuevo_precio = input("Nuevo precio (deje vacío si no cambia): ")

                cantidad = int(nueva_cantidad) if nueva_cantidad else None
                precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# ===============================
# Ejecutar el programa
# ===============================
if __name__ == "__main__":
    menu()




