import csv
import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz de recolección de información")

# Crear las etiquetas y campos de entrada para cada dato
bin_fallo_label = tk.Label(ventana, text="BIN de fallo:", font=("Arial", 12))
bin_fallo_entry = tk.Entry(ventana, font=("Arial", 12))

id_empleado_label = tk.Label(ventana, text="ID empleado:", font=("Arial", 12))
id_empleado_entry = tk.Entry(ventana, font=("Arial", 12))

resolucion_label = tk.Label(ventana, text="Resolución del caso:", font=("Arial", 12))
resolucion_entry = tk.Entry(ventana, font=("Arial", 12))

fecha_registro_label = tk.Label(ventana, text="Fecha de registro de BIN de fallo:", font=("Arial", 12))
fecha_registro_entry = tk.Entry(ventana, font=("Arial", 12))

# Colocar las etiquetas y campos de entrada en la ventana
bin_fallo_label.grid(row=0, column=0, padx=10, pady=10)
bin_fallo_entry.grid(row=0, column=1, padx=10, pady=10)

id_empleado_label.grid(row=1, column=0, padx=10, pady=10)
id_empleado_entry.grid(row=1, column=1, padx=10, pady=10)

resolucion_label.grid(row=2, column=0, padx=10, pady=10)
resolucion_entry.grid(row=2, column=1, padx=10, pady=10)

fecha_registro_label.grid(row=3, column=0, padx=10, pady=10)
fecha_registro_entry.grid(row=3, column=1, padx=10, pady=10)

# Crear el botón para guardar los datos
guardar_boton = tk.Button(ventana, text="Guardar", font=("Arial", 12), bg="#40CFFF", fg="white", command=lambda: guardar_datos())
guardar_boton.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Función para guardar los datos ingresados por el usuario
def guardar_datos():
    # Obtener los datos ingresados por el usuario
    bin_fallo = bin_fallo_entry.get()
    id_empleado = id_empleado_entry.get()
    resolucion = resolucion_entry.get()
    fecha_registro = fecha_registro_entry.get()

    # Escribir los datos en un archivo CSV
    with open('datos3.csv', mode='a', newline='') as archivo:
        writer = csv.writer(archivo, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([bin_fallo, id_empleado, resolucion, fecha_registro])

    # Mostrar mensaje de confirmación
    messagebox.showinfo("Confirmación", "Los datos se han guardado correctamente.")

    # Eliminar los datos ingresados por el usuario
    bin_fallo_entry.delete(0, tk.END)
    id_empleado_entry.delete(0, tk.END)
    resolucion_entry.delete(0, tk.END)
    fecha_registro_entry.delete(0, tk.END)

#UL 3/26/2023

# Iniciar la aplicación
ventana.mainloop()
