import tkinter as tk
from tkinter import messagebox

# Funciones para manejar eventos
def add_task(event=None):
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

def mark_as_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task_index)
        listbox_tasks.delete(selected_task_index)
        listbox_tasks.insert(tk.END, f"[Completada] {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Entrada de nueva tarea
entry_task = tk.Entry(root, width=35)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)  # Añadir tarea con la tecla Enter

# Lista de tareas
listbox_tasks = tk.Listbox(root, height=10, width=50)
listbox_tasks.pack(pady=10)

# Botones
button_add_task = tk.Button(root, text="Añadir Tarea", command=add_task)
button_add_task.pack(pady=5)

button_complete_task = tk.Button(root, text="Marcar como Completada", command=mark_as_completed)
button_complete_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete_task.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
