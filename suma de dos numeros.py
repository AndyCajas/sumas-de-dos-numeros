import tkinter as tk
from tkinter import messagebox

# Función para calcular la suma
def calcular_suma():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        suma = num1 + num2
        label_resultado.config(text=f"Resultado: {suma}", fg="red")  # Cambiar el color a rojo
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Suma")
ventana.geometry("400x400")
ventana.configure(bg="black")  # Fondo de la ventana negro

# Etiqueta de bienvenida
label_bienvenida = tk.Label(
    ventana,
    text="Bienvenido a la Calculadora de Suma",
    font=("Arial", 14, "bold"),
    bg="black",
    fg="white"  # Texto blanco para contraste
)
label_bienvenida.pack(pady=10)

# Etiquetas y campos de entrada
label_num1 = tk.Label(ventana, text="Número 1:", font=("Arial", 12), bg="black", fg="white")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana, font=("Arial", 12), width=15)
entry_num1.pack(pady=5)

label_num2 = tk.Label(ventana, text="Número 2:", font=("Arial", 12), bg="black", fg="white")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana, font=("Arial", 12), width=15)
entry_num2.pack(pady=5)

# Botón para calcular la suma
btn_calcular = tk.Button(
    ventana,
    text="Calcular Suma",
    font=("Arial", 12, "bold"),
    bg="#32cd32",  # Verde
    fg="white",
    activebackground="#228b22",
    activeforeground="white",
    command=calcular_suma
)
btn_calcular.pack(pady=15)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(
    ventana,
    text="Resultado: ",
    font=("Arial", 12, "bold"),
    bg="black",  # Fondo negro
    fg="white"   # Texto blanco
)
label_resultado.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()


