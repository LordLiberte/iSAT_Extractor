"""Módulo para la configurción y personalización de la pestaña 1"""
""
from librerias import *
import funciones_generales

# Variables globales

dataframe_global = pd.DataFrame()
ruta_archivo_global = ""

def obtener_dataframe():
    return dataframe_global

def obtener_ruta_archivo():
    return ruta_archivo_global

# Entorno global pestaña =================================================================
def pestana1(notebook):
    
    # Funciones de la pestaña ============================================================
    # Carga el archivo al programa -------------------------------------------------------
    def cargar_archivo():
        global dataframe_global
        global ruta_archivo_global
        ruta_archivo = filedialog.askopenfilename()  # Obtiene la ruta al archivo
        ruta_archivo_global = ruta_archivo  # Vuelve global la variable
        
        if ruta_archivo.__contains__(".csv"):
            try:
                dataframe = pd.read_csv(ruta_archivo, delimiter = ";")
            except:
                dataframe = pd.read_csv(ruta_archivo, delimiter= ",")
        elif ruta_archivo.__contains__(".xlsx") or ruta_archivo.__contains__(".xls"):
            try:
                dataframe = pd.read_excel(ruta_archivo)
            except Exception as e:
                print(f"Error: {e}")
        
        else:
            print("Archivo no soportado")
        
        
        # Asignar a la variable global sólo si se cargó correctamente
        if not dataframe.empty:
            dataframe_global = dataframe
            mostrar_datos()
            messagebox.showinfo("Info", "Archivo cargado y procesado correctamente")
        else:
            messagebox.showerror("Error", "El archivo está vacío o no se pudo procesar")
    
    # Crear tabla y mostrar información --------------------------------------------------
    def mostrar_datos():
        # Validar que el DataFrame esté cargado
        if dataframe_global.empty:
            messagebox.showerror("Error", "No hay datos para mostrar")
            return

        # Limpiar la tabla previa
        for i in tree.get_children():
            tree.delete(i)

        # Configurar las columnas con los nombres del DataFrame
        tree["columns"] = list(dataframe_global.columns)  # Asignar columnas dinámicamente
        for col in tree["columns"]:
            tree.heading(col, text=col)  # Configurar la cabecera de cada columna
            tree.column(col, width=100, anchor=tk.W)  # Opcional: ajustar el tamaño de columna

        # Llenar la tabla con los datos del DataFrame
        for index, row in dataframe_global.iterrows():
            tree.insert("", tk.END, values=list(row))
            
        etiqueta = ttk.Label(pestana1, text="", anchor="w")
        etiqueta.place(x=20, y=650, width=1240, height=30)
        nombre_archivo_cargado = ruta_archivo_global.split("/")[-1]  # Extraer el nombre
        etiqueta.config(text=f"Archivo cargado: {nombre_archivo_cargado}")
            
     
    # Creación de pestaña y botones ======================================================
    # Pestaña ----------------------------------------------------------------------------
    pestana1 = ttk.Frame(notebook, width=1280, height=720)
    pestana1.pack_propagate(False) # Evita que la pestaña cambie de tamaño
    
    # Actualizar fecha --------------------------------------------------------------------
    funciones_generales.actualizar_fecha(pestana1)
    
    # Botones ----------------------------------------------------------------------------
    # Boton cargar archivo @@@@@@@@
    boton_cargar = ttk.Button(pestana1, text="Cargar Archivo",
                              command=cargar_archivo)
    boton_cargar.place(x=50, y=30, width=100, height=50)
    
    # Cuadricula para mostrar información
    tree = ttk.Treeview(pestana1, show="headings")
    tree.place(x=20, y=100, width=1240, height=540)
    
    # FIN --------------------------------------------------------------------------------  
    return pestana1 # Devolver la pestaña configurada""