
# ===============================
# Clase Libro
# ===============================
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Autor y título como tupla (inmutables una vez creados)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# ===============================
# Clase Usuario
# ===============================
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# ===============================
# Clase Biblioteca
# ===============================
class Biblioteca:
    def __init__(self):
        # Diccionario con ISBN como clave y Libro como valor
        self.libros_disponibles = {}
        # Conjunto para asegurar IDs únicos
        self.usuarios_registrados = set()
        # Diccionario para mapear ID de usuario -> objeto Usuario
        self.usuarios = {}

    # ---------- Gestión de Libros ----------
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print("No se encontró un libro con ese ISBN.")

    # ---------- Gestión de Usuarios ----------
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            self.usuarios_registrados.remove(id_usuario)
            usuario = self.usuarios.pop(id_usuario)
            print(f"Usuario dado de baja: {usuario}")
        else:
            print("No existe un usuario con ese ID.")

    # ---------- Préstamos ----------
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("El libro no está disponible para préstamo.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros_disponibles.pop(isbn)
        usuario.libros_prestados.append(libro)
        print(f"Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro devuelto: {libro}")
                return
        print("El usuario no tenía prestado este libro.")

    # ---------- Búsqueda ----------
    def buscar_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.info[0].lower() == titulo.lower()]
        return resultados

    def buscar_por_autor(self, autor):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.info[1].lower() == autor.lower()]
        return resultados

    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros_disponibles.values() if libro.categoria.lower() == categoria.lower()]
        return resultados

    # ---------- Listar libros prestados ----------
    def listar_prestados_usuario(self, id_usuario):
        if id_usuario not in self.usuarios_registrados:
            print("Usuario no registrado.")
            return []
        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados


# ===============================
# PRUEBAS DEL SISTEMA
# ===============================

# Crear biblioteca
biblio = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "12345")
libro2 = Libro("El Quijote", "Miguel de Cervantes", "Clásico", "67890")
libro3 = Libro("Python para Todos", "Raúl González", "Tecnología", "11223")

# Añadir libros
biblio.añadir_libro(libro1)
biblio.añadir_libro(libro2)
biblio.añadir_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Cristhian", "U001")
usuario2 = Usuario("Luis", "U002")

# Registrar usuarios
biblio.registrar_usuario(usuario1)
biblio.registrar_usuario(usuario2)

# Prestar libro
biblio.prestar_libro("U001", "12345")

# Intentar prestar un libro ya prestado
biblio.prestar_libro("U002", "12345")

# Listar libros prestados de un usuario
print("Libros prestados a Cristhian:", [str(libro) for libro in biblio.listar_prestados_usuario("U001")])

# Devolver libro
biblio.devolver_libro("U001", "12345")

# Buscar libros
print("Buscar por autor 'Miguel de Cervantes':", [str(libro) for libro in biblio.buscar_por_autor("Miguel de Cervantes")])
print("Buscar por categoría 'Tecnología':", [str(libro) for libro in biblio.buscar_por_categoria("Tecnología")])



