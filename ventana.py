
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera Ventana")
ventana.geometry("300x200")  # Tamaño de la ventana

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="¡Hola, bienvenido!", font=("Arial", 12))
etiqueta.pack(pady=10)  # Agrega espacio alrededor

# Crear una caja de texto
entrada = tk.Entry(ventana, width=25)
entrada.pack(pady=5)

# Función cuando se presiona el botón
def mostrar_mensaje():
    texto = entrada.get()
    etiqueta.config(text=f"Hola, {texto}!")  

# Función para cerrar la aplicación
def salir_aplicacion():
    ventana.quit()  # Cierra la ventana y termina el bucle

# Cambiar el color de fondo de la ventana
    ventana.config(bg="lightblue")  

# Crear un botón
boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
boton.pack(pady=10)

# Crear un botón de salir
boton_salir = tk.Button(ventana, text="Salir", command=salir_aplicacion)
boton_salir.pack(pady=10)

# Iniciar el bucle de la aplicación
ventana.mainloop()
