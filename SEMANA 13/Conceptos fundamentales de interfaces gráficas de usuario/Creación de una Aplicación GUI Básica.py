import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos - GUI con Tkinter")
ventana.geometry("400x400")

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Ingrese un dato y agréguelo a la lista:", font=("Arial", 11))
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Funcionalidad para agregar
def agregar_dato():
    dato = entrada.get().strip()
    if dato != "":
        lista_datos.insert(tk.END, dato)  # Insertar al final de la lista
        entrada.delete(0, tk.END)  # Limpiar campo de texto
    else:
        messagebox.showwarning("Advertencia", "No puede agregar un dato vacío.")

# Funcionalidad para limpiar
def limpiar_dato():
    seleccion = lista_datos.curselection()
    if seleccion:
        lista_datos.delete(seleccion)  # Borra solo el dato seleccionado
    else:
        lista_datos.delete(0, tk.END)  # Si no hay selección, borra todo

# Botón agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="#4CAF50", fg="white")
btn_agregar.pack(pady=5)

# Botón limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_dato, bg="#f44336", fg="white")
btn_limpiar.pack(pady=5)

# Ejecutar aplicación
ventana.mainloop()







