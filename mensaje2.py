import tkinter as tk
from tkinter import messagebox
    
    
root = tk.Tk()
root.title ("iniciar secion")

#Agregar una etiqueta de titulo con el nombre "nombre de usuario"
etiqueta_usuario = tk.Label(root,tex ="nombre de usuario;")
etiqueta_usuario.pack(pady=10)

#agrega un campo de entrada para el nombre de usuario
entrada-usuario = tk.Entry(root)
entrada_usuario.pack(pady=5)

boton = tk.Button(root, text="accion " , command=mostrar_mensajes)
boton.pack(pady=20)


#configurar el tamaño de la ventana
root.geometry("300x200")

#establecer un color de fondo
root.configure(bg="black")

# Ejecutar el bucle principal de la aplicacion
root.mainloop()