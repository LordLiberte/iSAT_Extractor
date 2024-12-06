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

# PESTAÑA 1 =====================================================
def func_pestaña1(pestaña1):
    configurar_estilos()  # Asegúrate de configurar el estilo
    btn_cargar = ttk.Button(pestaña1, text="Cargar Archivo", style="Custom.TButton",
                            command=cargar_archivo)  # no agregar () a la función, si no se ejecuta directamente
    btn_cargar.pack(padx=10, pady=10)  # Ajusta aquí el espacio