
import json

# ===============================
# Clase Producto
# ===============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Representación en texto
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

    # Serializar a diccionario (para guardar en archivo JSON)
    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    # Crear objeto desde diccionario
    @staticmethod
    def from_dict(data):
        return Producto(data["id"], data["nombre"], data["cantidad"], data["precio"])


# ===============================
# Clase Inventario (con diccionario)
# ===============================
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Usamos diccionario: {id_producto: Producto}
        self.cargar_desde_archivo()

    # Cargar inventario desde archivo JSON
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.productos = {int(d["id"]): Producto.from_dict(d) for d in data}
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
            self.guardar_en_archivo()
        except json.JSONDecodeError:
            print("Error: archivo dañado o vacío. Se reiniciará el inventario.")
            self.productos = {}
        except PermissionError:
            print("Error: No tienes permiso para acceder al archivo.")

    # Guardar inventario en archivo JSON
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
        except PermissionError:
            print("Error: No se pudo guardar el archivo. Verifica permisos.")

    # Añadir producto
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print("Producto añadido con éxito y guardado en archivo.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("🗑 Producto eliminado con éxito.")
        else:
            print("Error: No se encontró el producto con ese ID.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].cantidad = nueva_cantidad
            if nuevo_precio is not None:
                self.productos[id_producto].precio = nuevo_precio
            self.guardar_en_archivo()
            print("Producto actualizado con éxito.")
        else:
            print("Error: No se encontró el producto con ese ID.")

    # Buscar por nombre
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("\n Resultados de búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if not self.productos:
            print(" El inventario está vacío.")
        else:
            print("\n=== Inventario actual ===")
            for p in self.productos.values():
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
                print(" Error: Datos inválidos.")

        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print(" Error: ID inválido.")

        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))
                nueva_cantidad = input("Nueva cantidad (deje vacío si no cambia): ")
                nuevo_precio = input("Nuevo precio (deje vacío si no cambia): ")

                cantidad = int(nueva_cantidad) if nueva_cantidad else None
                precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)
            except ValueError:
                print(" Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print(" Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intente de nuevo.")


# ===============================
# Ejecutar el programa
# ===============================
if __name__ == "__main__":
    menu()




