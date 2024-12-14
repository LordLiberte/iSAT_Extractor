"""Módulo destinado a asignar botones y colores a las pestañas"""
from tkinter import ttk
from function_btn import *

# Configurar estilo del botón
def configurar_estilos():
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Custom.TButton",
                        background="#ecb93b",
                        foreground="black",
                        font=("Garamond", 14))
    estilo.map("Custom.TButton",
                  background=[("active", "#ecb93b")])

# Configurar estilo de barra de progreso
def configurar_estilos_barra():
    estilo_barra = ttk.Style()
    estilo_barra.theme_use("clam")  # Usamos un tema que soporte personalización
    estilo_barra.configure(
        "Green.Horizontal.TProgressbar",
        troughcolor="white",  # Color del fondo de la barra
        background="green",  # Color de relleno de la barra
        thickness=20,        # Grosor de la barra (opcional)
    )