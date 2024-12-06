"""Crearemos la ventana y sus pestañas"""
from libraries import tk, ttk, pd
from botones_decoracion import *
from function_btn import *

def crear_ventana_pestanas():
    window = tk.Tk()  # Ventana Principal
    window.geometry("1280x720")  # Tamaño de la ventana
    window.title("iSAT_Extractor with Python - Carlos")  # Título de la ventana
    
    # NOTEBOOK de PESTAÑAS -- CONTENEDOR
    notebook = ttk.Notebook(window)

    # PESTAÑA 1 - CARGA DE DATOS ======================================================
    pestaña1 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña1, text="Carga de Archivos")  # añade la pestaña al notebook
    
    # Configurar estilo y botón
    configurar_estilos()
    
    # Crear Treeview con scrollbars
    frame_tabla = ttk.Frame(pestaña1)
    frame_tabla.pack(expand=True, fill="both", padx=10, pady=10)
    
    # Scrollbar vertical
    scrollbar_y = ttk.Scrollbar(frame_tabla)
    scrollbar_y.pack(side='right', fill='y')
    
    # Scrollbar horizontal
    scrollbar_x = ttk.Scrollbar(frame_tabla, orient='horizontal')
    scrollbar_x.pack(side='bottom', fill='x')
    
    # Treeview
    tabla_pestaña1 = ttk.Treeview(frame_tabla, 
                                  yscrollcommand=scrollbar_y.set, 
                                  xscrollcommand=scrollbar_x.set,
                                  show='headings')  # Mostrar solo encabezados
    tabla_pestaña1.pack(expand=True, fill="both")
    
    # Configurar scrollbars
    scrollbar_y.config(command=tabla_pestaña1.yview)
    scrollbar_x.config(command=tabla_pestaña1.xview)
    
    # Botón de carga
    btn_cargar = ttk.Button(pestaña1, text="Cargar Archivo", style="Custom.TButton",
                            command=lambda: cargar_y_mostrar_tabla(tabla_pestaña1))
    btn_cargar.pack(padx=10, pady=10)

    # PESTAÑA 2 - PROCESAMIENTO DE DATOS ======================================================
    pestaña2 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña2, text="Procesamiento de datos")  # añade la pestaña al notebook
    
    # PESTAÑA 3 - VISUALIZACIÓN DE DATOS ======================================================
    pestaña3 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña3, text="Visualización de datos")  # añade la pestaña al notebook

    # RENDERIZADO VENTANA 
    notebook.pack(expand=True, fill="both")  # añade el notebook con sus pestañas a la ventana
    window.mainloop()  # Ejecuta la ventana