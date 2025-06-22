import tkinter as tk
from tkinter import messagebox

def mostrar_mensajes():
    """muestra un mensaje de alerta"""
    messagebox.showinfo("mensaje", "¡Hola,este es un mensaje de alerta!")
    
root = tk.Tk()
root.title ("Ejercicio 1")

boton = tk.Button(root, text="Mostrar mensaje " , command=mostrar_mensajes)
boton.pack(pady=20)

boton = tk.Button(root, text="segundo boton " , command=mostrar_mensajes)
boton.pack(pady=40)

#configurar el tamaño de la ventana
root.geometry("300x200")

#establecer un color de fondo
root.configure(bg="black")

# Ejecutar el bucle principal de la aplicacion
root.mainloop()
    