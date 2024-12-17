"""Módulo para usar funcionalidades comunes"""

from librerias import *

def actualizar_fecha(pestana):
        fecha = datetime.datetime.today()
        fecha_label = ttk.Label(pestana, text=f"{fecha}")
        fecha_label.place(x=0, y=0, width=108, height=20)
        pestana.after(1000, lambda: actualizar_fecha(pestana))