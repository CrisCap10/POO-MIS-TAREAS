import tkinter as tk
from tkinter import messagebox
-
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - ToDo List")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Campo de entrada
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10, padx=10, fill="x")
        self.entry.bind("<Return>", self.add_task)  # Añadir con Enter

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, padx=10, fill="both", expand=True)
        self.task_listbox.bind("<Double-1>", self.toggle_complete)  # Doble clic marca completada

        # Botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        add_btn = tk.Button(button_frame, text="Añadir Tarea", command=self.add_task)
        add_btn.grid(row=0, column=0, padx=5)

        complete_btn = tk.Button(button_frame, text="Marcar como Completada", command=self.toggle_complete)
        complete_btn.grid(row=0, column=1, padx=5)

        delete_btn = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        delete_btn.grid(row=0, column=2, padx=5)

        # Almacenar tareas
        self.tasks = []

    def add_task(self, event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.update_task_list()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def toggle_complete(self, event=None):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_task_list()
        except IndexError:
            messagebox.showinfo("Información", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.update_task_list()
        except IndexError:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminarla.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if task["completed"]:
                self.task_listbox.insert(tk.END, f"✔ {task['text']}")
            else:
                self.task_listbox.insert(tk.END, task["text"])

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


