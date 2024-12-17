"""Módulo para la configuración y diseño de la pestaña 3"""

from librerias import *
import Pestana_2
import funciones_generales

# Variables globales
dataframe_global = pd.DataFrame()
últimas_columnas = []

# Entorno global pestaña 3 ================================================================
def pestana3(notebook):
    
    # Funciones de la pestaña =============================================================
    # Función para actualizar dinámicamente el Combobox
    def actualizar_combobox():
        dataframe_global = Pestana_2.obtener_dataframe()
        
        global últimas_columnas
        # Verificar si las columnas han cambiado
        nuevas_columnas = list(dataframe_global.columns)
        
        if nuevas_columnas != últimas_columnas:  # Solo actualizar si hay cambios
            combo_opciones["values"] = nuevas_columnas
            combo_opciones.set(nuevas_columnas[0] if nuevas_columnas else "")
            últimas_columnas = nuevas_columnas
        
        # Ejecutar nuevamente después de 1 segundo
        pestana3.after(1000, actualizar_combobox)


    # Creación de pestaña y botones =======================================================
    # Pestaña -----------------------------------------------------------------------------
    pestana3 = ttk.Frame(notebook, width=1280, height=720)
    pestana3.pack_propagate(False)  # Evita que la pestaña cambie de tamaño

    # Actualizar fecha --------------------------------------------------------------------
    funciones_generales.actualizar_fecha(pestana3)

    # Desplegable con opciones -----------------------------------------------------------
    combo_opciones = ttk.Combobox(pestana3, values=list(dataframe_global.columns))
    combo_opciones.place(x=50, y=50)
    # Iniciar la actualización dinámica del Combobox -------------------------------------
    actualizar_combobox()
    
    
    histograma_type = tk.BooleanVar()
    histograma_check = tk.Checkbutton(pestana3, text="Histograma", variable=histograma_type)
    histograma_check.place(x=100, y=100, width=70, height=50)
    
    # Función para mostrar el estado de los Checkbuttons
    def mostrar_estado():
        print(f"Histograma: {histograma_type.get()}")

    # Botón para ejecutar la función mostrar_estado
    boton = tk.Button(pestana3, text="Mostrar Estado", command=mostrar_estado)
    boton.pack(pady=10)
    

    return pestana3