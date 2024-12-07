from libraries import tk, ttk
from botones_decoracion import *
from function_btn import cargar_archivo, configurar_tabla  # Importar específicamente

# Variable global para almacenar el DataFrame
global_dataframe = None

def Treeviews(pestaña):
    # Crear Treeview con scrollbars
    frame_tabla = ttk.Frame(pestaña)
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
    tabla_pestaña1.pack(expand=True, fill="both")  # añadirlo a la pestaña
    
    # Configurar scrollbars
    scrollbar_y.config(command=tabla_pestaña1.yview)  # vertical
    scrollbar_x.config(command=tabla_pestaña1.xview)  # horizontal
    return tabla_pestaña1

def crear_ventana_pestanas():
    global global_dataframe  # Declarar global para poder modificarlo
    
    window = tk.Tk()  # Ventana Principal
    window.update_idletasks()
    window.geometry("1280x720")  # Tamaño de la ventana
    window.title("iSAT_Extractor with Python - Carlos")  # Título de la ventana
    
    # NOTEBOOK de PESTAÑAS -- CONTENEDOR
    notebook = ttk.Notebook(window)

    # INICIO PESTAÑAS =================================================================
    # PESTAÑA 1 - CARGA DE DATOS ======================================================
    pestaña1 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña1, text="Carga de Archivos")  # añade la pestaña al notebook
    
    # Configurar estilo y botón
    configurar_estilos()
    
    tabla_pestaña1 = Treeviews(pestaña1)  # Creación de la tabla de pestaña 1
    
    # Definir función de carga y mostrar tabla
    def cargar_y_mostrar_tabla():
        global global_dataframe  # Usar la variable global
        # Cargar archivo
        dataframe = cargar_archivo()
        
        # Si se cargó correctamente el DataFrame
        if dataframe is not None:
            # Configurar la tabla con el DataFrame
            configurar_tabla(tabla_pestaña1, dataframe)
            
            # Guardar el DataFrame en la variable global
            global_dataframe = dataframe
    
    # Botón de carga
    btn_cargar = ttk.Button(pestaña1, text="Cargar Archivo", style="Custom.TButton",
                            command=cargar_y_mostrar_tabla)
    btn_cargar.pack(padx=10, pady=10)
    # FIN PESTAÑA 1 ===========================================================================
    #
    
    #
    # PESTAÑA 2 - PROCESAMIENTO DE DATOS ======================================================
    pestaña2 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña2, text="Procesamiento de datos")  # añade la pestaña al notebook
    
    tabla_pestaña2 = Treeviews(pestaña2)  # Introduce una tabla en pestaña 2
    
    def procesar_protocol():
        # Usar la variable global
        if global_dataframe is not None:
            df_procesar = global_dataframe.copy()  # copia del dataframe original
            serie_protocol = df_procesar["Protocol"]  # copia de la columna a procesar
            df_protocol = pd.DataFrame(serie_protocol)  # convierte la Serie de pandas en un Dataframe
            
            df_protocol_striped = df_protocol.applymap(lambda x: x.strip('\n') if isinstance(x, str) else x)  # elimina los \n de cada celda, para futuros problemas
            print(type(df_protocol_striped))
            
            
            
            # Mostrar el DataFrame en la tabla de la pestaña 2
            #configurar_tabla(tabla_pestaña2, global_dataframe)
        else:
            # Opcional: Mostrar un mensaje si no hay DataFrame cargado
            tk.messagebox.showwarning("Advertencia", "Primero debe cargar un archivo -> Cargar Archivos")
    
    # Botón para realizar procesamiento de los datos
    btn_procesar = ttk.Button(pestaña2, text="Procesar Archivo",
                              style="Custom.TButton", command=procesar_protocol)
    btn_procesar.pack(pady=10, padx=10)
    # FIN PESTAÑA 2 ===========================================================================
    #
    
    #
    # PESTAÑA 3 - VISUALIZACIÓN DE DATOS ======================================================
    pestaña3 = ttk.Frame(notebook)  # asigna la pestaña al notebook
    notebook.add(pestaña3, text="Visualización de datos")  # añade la pestaña al notebook

    # RENDERIZADO VENTANA 
    notebook.pack(expand=True, fill="both")  # añade el notebook con sus pestañas a la ventana
    window.mainloop()  # Ejecuta la ventana

# Ejecutar la aplicación
if __name__ == "__main__":
    crear_ventana_pestanas()