
# Clase que representa un archivo
class Archivo:
    def __init__(self, nombre, contenido):
        """
        Constructor de la clase Archivo.

        Inicializa el nombre y el contenido del archivo.

        :param nombre: Nombre del archivo
        :param contenido: Contenido del archivo
        """
        self.nombre = nombre
        self.contenido = contenido
        print(f"Archivo '{nombre}' creado con éxito.")

    def __del__(self):
        """
        Destructor de la clase Archivo.

        Se activa cuando el objeto es eliminado.
        Realiza una limpieza de recursos cerrando el archivo.
        """
        print(f"Archivo '{self.nombre}' eliminado con éxito.")

    def leer_contenido(self):
        """
        Método que devuelve el contenido del archivo.

        :return: Contenido del archivo
        """
        return self.contenido

    def escribir_contenido(self, nuevo_contenido):
        """
        Método que actualiza el contenido del archivo.

        :param nuevo_contenido: Nuevo contenido del archivo
        """
        self.contenido = nuevo_contenido
        print(f"Contenido de '{self.nombre}' actualizado con éxito.")


# Clase que representa un directorio
class Directorio:
    def __init__(self, nombre):
        """
        Constructor de la clase Directorio.

        Inicializa el nombre del directorio.

        :param nombre: Nombre del directorio
        """
        self.nombre = nombre
        self.archivos = []
        print(f"Directorio '{nombre}' creado con éxito.")

    def __del__(self):
        """
        Destructor de la clase Directorio.

        Se activa cuando el objeto es eliminado.
        Realiza una limpieza de recursos eliminando los archivos del directorio.
        """
        print(f"Directorio '{self.nombre}' eliminado con éxito.")
        for archivo in self.archivos:
            del archivo

    def agregar_archivo(self, archivo):
        """
        Método que agrega un archivo al directorio.

        :param archivo: Archivo a agregar
        """
        self.archivos.append(archivo)
        print(f"Archivo '{archivo.nombre}' agregado al directorio '{self.nombre}' con éxito.")

    def eliminar_archivo(self, archivo):
        """
        Método que elimina un archivo del directorio.

        :param archivo: Archivo a eliminar
        """
        self.archivos.remove(archivo)
        print(f"Archivo '{archivo.nombre}' eliminado del directorio '{self.nombre}' con éxito.")


# Crear un directorio
directorio = Directorio("Mis Archivos")

# Crear archivos y agregarlos al directorio
archivo1 = Archivo("archivo1.txt", "Contenido del archivo 1")
archivo2 = Archivo("archivo2.txt", "Contenido del archivo 2")
directorio.agregar_archivo(archivo1)
directorio.agregar_archivo(archivo2)

# Leer contenido de archivos
print(archivo1.leer_contenido())
print(archivo2.leer_contenido())

# Actualizar contenido de archivos
archivo1.escribir_contenido("Nuevo contenido del archivo 1")
archivo2.escribir_contenido("Nuevo contenido del archivo 2")

# Eliminar archivos del directorio
directorio.eliminar_archivo(archivo1)

# Eliminar directorio
del directorio
