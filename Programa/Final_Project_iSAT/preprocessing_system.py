from librerias import *
import load_page as load_page
import funciones_generales
import transform_page as transform_page

def pestana3(notebook):
    ## Creación de la pestaña ===================================================
    pestana3 = ttk.Frame(notebook)  # Crear frame para la pestaña
    notebook.add(pestana3, text="Preprocesar Datos")  # Añadir pestaña al notebook
    
    # Actualizar fecha --------------------------------------------------------------------
    funciones_generales.actualizar_fecha(pestana3)
    
    return pestana3