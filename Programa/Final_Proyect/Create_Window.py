"""Módulo para la creación de la ventana principal"""

from librerias import *
import Pestana_1

def iniciar_ventana():
    
    # Ventana principal ==============================================
    window = tk.Tk()  # Arranque tkinter engine
    width = 1280  # Anchura ventana
    height = 720  # Altura ventana
    window.geometry(f"{width}x{height}")  # Tamaño ventana
    window.title("iSAT_Extractor with Python") # Nombre de la venatana
    window.resizable(False, False)
    
    
    # Notebook principal =============================================
    notebook = ttk.Notebook(window)  # Notebook para poner pestañas
    notebook.pack(pady=10, expand=True)
    
    # Cread frames (pestañas) ========================================
    pestana1 = Pestana_1.pestana1(notebook)  # Traigo la pestaña del módulo
    pestana1.pack(fill="both", expand=True)
    notebook.add(pestana1, text="Cargar Datos") # Integro la pestaña en el notebook
    
    
    window.mainloop()  # Bucle principal