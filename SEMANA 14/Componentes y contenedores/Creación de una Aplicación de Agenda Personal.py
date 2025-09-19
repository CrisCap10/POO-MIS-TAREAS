import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Asegúrate de instalar con: pip install tkcalendar


# ==========================
# Funciones de la aplicación
# ==========================
def agregar_evento():
    """Agrega un evento a la lista de eventos"""
    fecha = date_entry.get_date()  # Devuelve objeto datetime.date
    hora = hora_entry.get().strip()
    descripcion = desc_entry.get().strip()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(str(fecha), hora, descripcion))
        # Limpiar campos después de agregar
        hora_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")


def eliminar_evento():
    """Elimina el evento seleccionado con confirmación"""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Seleccionar evento", "Por favor, seleccione un evento para eliminar.")
        return

    confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar este evento?")
    if confirm:
        tree.delete(selected_item)


def salir():
    """Cierra la aplicación"""
    root.destroy()


# ==========================
# Configuración de la ventana
# ==========================
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("700x400")
root.resizable(False, False)

# ==========================
# Frames para organización
# ==========================
frame_eventos = tk.Frame(root)
frame_eventos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10, padx=10)

frame_acciones = tk.Frame(root)
frame_acciones.pack(pady=10)

# ==========================
# TreeView para mostrar eventos
# ==========================
columns = ["Fecha", "Hora", "Descripción"]  # Debe ser lista, no tupla
tree = ttk.Treeview(frame_eventos, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200, anchor="center")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_eventos, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# ==========================
# Campos de entrada
# ==========================
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
date_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2,
                       date_pattern='yyyy-mm-dd')
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
hora_entry = tk.Entry(frame_entrada, width=10)
hora_entry.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
desc_entry = tk.Entry(frame_entrada, width=25)
desc_entry.grid(row=0, column=5, padx=5, pady=5)

# ==========================
# Botones de acción
# ==========================
btn_agregar = tk.Button(frame_acciones, text="Agregar Evento", command=agregar_evento, bg="green", fg="white")
btn_agregar.pack(side=tk.LEFT, padx=10)

btn_eliminar = tk.Button(frame_acciones, text="Eliminar Evento Seleccionado", command=eliminar_evento, bg="red",
                         fg="white")
btn_eliminar.pack(side=tk.LEFT, padx=10)

btn_salir = tk.Button(frame_acciones, text="Salir", command=salir, bg="gray", fg="white")
btn_salir.pack(side=tk.LEFT, padx=10)

# ==========================
# Ejecutar la aplicación
# ==========================
root.mainloop()




