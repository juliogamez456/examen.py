import tkinter as tk
from tkinter import messagebox

def mostrarDireccion():
    """muestra un mensaje de alerta"""
    messagebox.showinfo("mensaje", "¡JICARO, NUEVA SEGOVIA!") 
    
    
def mostrarEdad():
    """muestra un mensaje de alerta"""
    messagebox.showinfo("mensaje", "18 AÑOS !")
    
root = tk.Tk()
root.title("examen I parcial- Julio urbina")

# Agregar una etiqueta de titulo con el nombre "nombre de usuario"
etiqueta_usuario = tk.Label(root, text="MI NOMBRE ES JULIO URBINA;")
etiqueta_usuario.pack(pady=20)

# Crear un frame para centrar los botones
frame_botones = tk.Frame(root, bg="blue")
frame_botones.pack(pady=20)

# Botón para mostrar dirección
boton_direccion = tk.Button(frame_botones, text="VIVIENDO", command=mostrarDireccion)
boton_direccion.pack(side="left", padx=10)

# Botón para mostrar edad
boton_edad = tk.Button(frame_botones, text="EDAD", command=mostrarEdad)
boton_edad.pack(side="left", padx=10)

# Configurar el tamaño de la ventana
root.geometry("300x200")

# Establecer un color de fondo
root.configure(bg="blue")

# Ejecutar el bucle principal de la aplicacion
root.mainloop()