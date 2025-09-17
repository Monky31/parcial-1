import tkinter as tk
from tkinter import messagebox

# Mantenemos el índice del color fuera de la función para que su valor persista entre llamadas
color_index = 0
colores = ["green", "blue", "yellow", "gray"]

# Funciones de botones y menús
def cambiar_texto():
    etiqueta_dinamica.config(text="¡El texto ha cambiado! 👋")

def cambiar_color():
    global color_index
    global colores
    
    # Cambiamos el color al siguiente en la lista
    root.config(bg=colores[color_index])
    
    # Incrementamos el índice para el próximo clic
    color_index += 1
    
    # Si el índice llega al final de la lista, lo reiniciamos a 0
    if color_index >= len(colores):
        color_index = 0

def mostrar_mensaje():
    messagebox.showinfo("Mensaje del Botón", "¡Este es un mensaje simple del tercer botón!")

def mostrar_tutorial():
    messagebox.showinfo("Tutorial de la Aplicación", "¡Bienvenido a la aplicación GUI! Aquí aprenderás a usarla. \n\nUsa el menú superior para acceder a diferentes opciones y los botones de la izquierda para interactuar con la aplicación.")

def salir_aplicacion():
    # Muestra un cuadro de confirmación antes de salir
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir de la aplicación?"):
        root.destroy()

def mostrar_funcionalidad1():
    messagebox.showinfo("Funcionalidad 1", "Esta funcionalidad muestra un cuadro de diálogo con información al hacer clic en un botón o en una opción del menú.")

def mostrar_funcionalidad2():
    messagebox.showinfo("Funcionalidad 2", "Esta funcionalidad cambia el color de fondo de la ventana principal con cada clic.")

def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Aplicación de demostración de Tkinter\n\nAutor: Mateo Lastra Castillo\nPropósito: Practicar la creación de interfaces gráficas con menús, marcos, botones y etiquetas.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Mi Aplicación Tkinter")
root.geometry("600x400")
root.config(bg="gray")

# Establecer el ícono de la ventana
try:
    root.iconbitmap("app_icon.ico")
except tk.TclError:
    print("Advertencia: No se encontró el archivo 'app_icon.ico'. La aplicación se ejecutará sin un ícono personalizado.")

# Crear el menú superior
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Menú Inicio
menu_inicio = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
menu_inicio.add_command(label="Tutorial de la aplicación", command=mostrar_tutorial)
menu_inicio.add_separator()
menu_inicio.add_command(label="Salir", command=salir_aplicacion)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Funcionalidad 1", command=mostrar_funcionalidad1)
menu_ayuda.add_command(label="Funcionalidad 2", command=mostrar_funcionalidad2)

# Menú Acerca de
menu_acerca_de = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Acerca de", menu=menu_acerca_de)
menu_acerca_de.add_command(label="Acerca de la aplicación", command=mostrar_acerca_de)

# Crear los marcos para dividir la ventana
marco_izquierdo = tk.Frame(root, bg="white", width=250)
marco_derecho = tk.Frame(root, bg="#f0f0f0") 

# Usar pack() para organizar los marcos
marco_izquierdo.pack(side="left", fill="both", expand=False, padx=10, pady=10)
marco_derecho.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Contenido del Marco Izquierdo
etiqueta_izquierda = tk.Label(marco_izquierdo, text="¡Bienvenido!\n\nUsa los botones a continuación para interactuar con la aplicación. También puedes usar el menú en la parte superior.", bg="white", wraplength=200, justify="center")
etiqueta_izquierda.pack(pady=20, padx=5)

# Crear los botones en el marco izquierdo
boton_texto = tk.Button(marco_izquierdo, text="Cambiar texto", command=cambiar_texto)
boton_color = tk.Button(marco_izquierdo, text="Cambiar color de fondo", command=cambiar_color)
boton_mensaje = tk.Button(marco_izquierdo, text="Mostrar mensaje", command=mostrar_mensaje)

# Empaquetar los botones
boton_texto.pack(pady=5)
boton_color.pack(pady=5)
boton_mensaje.pack(pady=5)

# Contenido del Marco Derecho
etiqueta_dinamica = tk.Label(marco_derecho, text="Este es el área de texto dinámico.", bg="#f0f0f0", font=("Arial", 16), justify="center", wraplength=300)
etiqueta_dinamica.pack(expand=True, padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()