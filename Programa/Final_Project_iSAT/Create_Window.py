"""Módulo para la creación de la ventana principal"""
from librerias import *
import Programa.Final_Project_iSAT.load_page as load_page
import Programa.Final_Project_iSAT.transform_page as transform_page
import Pestana_3

def iniciar_ventana():
    
    # Ventana principal, configuración ==============================================
    window = tk.Tk()  # Arranque tkinter engine
    width = 1280  # Anchura ventana
    height = 720  # Altura ventana
    window.geometry(f"{width}x{height}")  # Tamaño ventana
    window.title("iSAT_Extractor with Python") # Nombre de la venatana
    window.resizable(False, False)
    
    
    # Notebook principal =============================================
    notebook = ttk.Notebook(window)  # Notebook para poner pestañas
    notebook.pack(pady=10, expand=True)
    
    
    # Crear frames (pestañas) ========================================
    # Pestaña 1 ------------------------------------------------------
    pestana1 = load_page.pestana1(notebook)  # Traigo la pestaña del módulo
    pestana1.pack(fill="both", expand=True)
    notebook.add(pestana1, text="Cargar Datos") # Integro la pestaña en el notebook
    
    # Pestaña 2 ------------------------------------------------------
    pestana2 = transform_page.pestana2(notebook)  # Traigo pestaña al módulo
    pestana2.pack(fill="both", expand=True)
    notebook.add(pestana2, text="Procesar Datos") # Integro la pestaña al notebook
    
    # Pestaña 3
    pestana3 = Pestana_3.pestana3(notebook) # Traigo pestaña al módulo
    pestana3.pack(fill="both", expand=True) 
    notebook.add(pestana3, text="Visualizar Datos")  # Integro pestaña al notebook
    
    
    window.mainloop()  # Bucle principal