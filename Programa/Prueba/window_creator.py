import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import file_handler
import styles

class ISATExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("iSAT Extractor")
        self.root.geometry("1280x720")

        self.global_dataframe = None
        self.canvas = None
        self.ax = None
        self._create_file_load_tab()
        
        self._setup_styles()
        self._create_notebook()

    def _setup_styles(self):
        """Configure application styles."""
        styles.configure_styles()

    def _create_notebook(self):
        """Create notebook with tabs."""
        self.notebook = ttk.Notebook(self.root)
        self._create_file_load_tab()
        self._create_data_processing_tab()
        self._create_visualization_tab()

        self.notebook.pack(expand=True, fill="both")

    def _create_file_load_tab(self):
        """Create file loading tab."""
        pestaña1 = ttk.Frame(self.notebook)
        self.notebook.add(pestaña1, text="Carga de Archivos")

        # Frame principal de pestaña 1
        frame_pestaña1 = ttk.Frame(pestaña1)
        frame_pestaña1.pack(expand=True, fill="both")

        # Frame para los botones (parte superior)
        frame_botones1 = ttk.Frame(frame_pestaña1)
        frame_botones1.pack(side="top", fill="x", pady=10)

        # Frame para la tabla (parte inferior)
        frame_tabla1 = ttk.Frame(frame_pestaña1)
        frame_tabla1.pack(side="top", expand=True, fill="both")

        tabla_pestaña1 = self._create_treeviews(frame_tabla1)

        def cargar_y_mostrar_tabla():
            dataframe = file_handler.load_file()
            if dataframe is not None:
                self._configurar_tabla(tabla_pestaña1, dataframe)
                self.global_dataframe = dataframe
            else:
                messagebox.showerror(
                    "Error", "No se pudo cargar el archivo. Intente nuevamente."
                )

        btn_cargar = ttk.Button(
            frame_botones1,
            text="Cargar Archivo",
            style="Custom.TButton",
            command=cargar_y_mostrar_tabla,
        )
        btn_cargar.pack(side="left", padx=10)

    # ... (rest of the methods remain similar)

    def _create_treeviews(self, parent):
        """Create a treeview with scrollbars."""
        frame_tabla = ttk.Frame(parent)
        frame_tabla.pack(expand=True, fill="both", padx=10, pady=10)

        scrollbar_y = ttk.Scrollbar(frame_tabla)
        scrollbar_y.pack(side="right", fill="y")

        scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal")
        scrollbar_x.pack(side="bottom", fill="x")

        tabla = ttk.Treeview(
            frame_tabla,
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set,
            show="headings",
        )
        tabla.pack(expand=True, fill="both")
        scrollbar_y.config(command=tabla.yview)
        scrollbar_x.config(command=tabla.xview)

        return tabla

    def _configurar_tabla(self, tabla, dataframe):
        """Configure table with dataframe."""
        # Clear existing table
        for i in tabla.get_children():
            tabla.delete(i)
        
        # Set columns
        columnas = list(dataframe.columns)
        tabla['columns'] = columnas
        
        # Configure columns
        for columna in columnas:
            tabla.heading(columna, text=columna)
            tabla.column(columna, width=100, anchor='center')
        
        # Insert data
        datos = dataframe.astype(str)
        for indice, fila in datos.iterrows():
            valores = list(fila)
            tabla.insert('', 'end', values=valores)

def create_main_window():
    """Function to create the main application window"""
    root = tk.Tk()
    app = ISATExtractor(root)
    root.mainloop()