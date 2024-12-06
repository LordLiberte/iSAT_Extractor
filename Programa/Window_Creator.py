"""Crearemos la ventana y sus pestañas"""
from libraries import tk, ttk
from botones_decoracion import func_pestaña1

def crear_ventana_pestanas():
    window = tk.Tk()  # Ventana Principal
    window.geometry("1280x720")  # Tamaño de la ventana
    window.title("iSAT_Extractor with Python - Carlos")  # Título de la ventana
    
    # NOTEBOOK de PESTAÑAS -- CONTENEDOR
    notebook = ttk.Notebook(window)

    # PESTAÑA 1 - CARGA DE DATOS ======================================================
    pestaña1 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña1, text="Carga de Archivos")  # añade la pestaña al notebook
    func_pestaña1(pestaña1)
    
    # PESTAÑA 2 - PROCESAMIENTO DE DATOS ======================================================
    pestaña2 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña2, text="Procesamiento de datos")  # añade la pestaña al notebook
    
    # PESTAÑA 3 - VISUALIZACIÓN DE DATOS ======================================================
    pestaña3 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña3, text="Visualización de datos")  # añade la pestaña al notebook

    # RENDERIZADO VENTANA 
    notebook.pack(expand=True, fill="both")  # añade el notebook con sus pestañas a la ventana
    window.mainloop()  # Ejecuta la ventana