"""Crearemos la ventana y sus pestañas"""
from libraries import *


def crear_ventana_pestañas():
    window = Tk()  # Ventana Principal

    # PESTAÑA 1 - CARGA DE DATOS ======================================================
    pestaña1 = ttk.Frame(window, padding=10)
    pestaña1.grid()


    window.mainloop()  # Ejecuta la ventana
