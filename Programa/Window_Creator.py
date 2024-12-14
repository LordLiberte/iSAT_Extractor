import threading
from libraries import tk, ttk
from botones_decoracion import *
from function_btn import cargar_archivo, configurar_tabla


global_dataframe = None  # Variable global para el DataFrame


def Treeviews(pestaña):
    """Crea un árbol con barras de desplazamiento."""
    frame_tabla = ttk.Frame(pestaña)
    frame_tabla.pack(expand=True, fill="both", padx=10, pady=10)

    scrollbar_y = ttk.Scrollbar(frame_tabla)
    scrollbar_y.pack(side="right", fill="y")

    scrollbar_x = ttk.Scrollbar(frame_tabla, orient="horizontal")
    scrollbar_x.pack(side="bottom", fill="x")

    tabla_pestaña = ttk.Treeview(
        frame_tabla,
        yscrollcommand=scrollbar_y.set,
        xscrollcommand=scrollbar_x.set,
        show="headings",
    )
    tabla_pestaña.pack(expand=True, fill="both")
    scrollbar_y.config(command=tabla_pestaña.yview)
    scrollbar_x.config(command=tabla_pestaña.xview)

    return tabla_pestaña


def crear_ventana_pestanas():
    global global_dataframe  # Variable global para el DataFrame

    window = tk.Tk()
    window.update_idletasks()
    window.geometry("1280x720")
    window.title("iSAT_Extractor con Python")

    notebook = ttk.Notebook(window)

    # Pestaña 1 - Carga de archivos
    pestaña1 = ttk.Frame(notebook)
    notebook.add(pestaña1, text="Carga de Archivos")
    configurar_estilos()
    configurar_estilos_barra()

    # Frame principal de pestaña 1
    frame_pestaña1 = ttk.Frame(pestaña1)
    frame_pestaña1.pack(expand=True, fill="both")

    # Frame para los botones (parte superior)
    frame_botones1 = ttk.Frame(frame_pestaña1)
    frame_botones1.pack(side="top", fill="x", pady=10)

    # Frame para la tabla (parte inferior)
    frame_tabla1 = ttk.Frame(frame_pestaña1)
    frame_tabla1.pack(side="top", expand=True, fill="both")

    tabla_pestaña1 = Treeviews(frame_tabla1)

    def cargar_y_mostrar_tabla():
        global global_dataframe
        dataframe = cargar_archivo()
        if dataframe is not None:
            configurar_tabla(tabla_pestaña1, dataframe)
            global_dataframe = dataframe
        else:
            tk.messagebox.showerror(
                "Error", "No se pudo cargar el archivo. Intente nuevamente."
            )

    btn_cargar = ttk.Button(
        frame_botones1,
        text="Cargar Archivo",
        style="Custom.TButton",
        command=cargar_y_mostrar_tabla,
    )
    btn_cargar.pack(side="left", padx=10)

    # Pestaña 2 - Procesamiento de Datos
    pestaña2 = ttk.Frame(notebook)
    notebook.add(pestaña2, text="Procesamiento de Datos")

    # Frame principal de pestaña 2
    frame_pestaña2 = ttk.Frame(pestaña2)
    frame_pestaña2.pack(expand=True, fill="both")

    # Frame para los botones y barra de progreso (parte superior)
    frame_botones2 = ttk.Frame(frame_pestaña2)
    frame_botones2.pack(side="top", fill="x", pady=10)

    # Frame para la tabla (parte inferior)
    frame_tabla2 = ttk.Frame(frame_pestaña2)
    frame_tabla2.pack(side="top", expand=True, fill="both")

    tabla_pestaña2 = Treeviews(frame_tabla2)
    progreso = ttk.Progressbar(frame_botones2, orient="horizontal", mode="determinate", length=400,
                               style="Green.Horizontal.TProgressbar")
    progreso.pack(side="left", padx=10)

    def procesar_datos():
        global global_dataframe
        if global_dataframe is None:
            tk.messagebox.showerror(
                "Error", "Debe cargar un archivo antes de procesar los datos"
            )
            return

        def tarea_procesamiento():
            global global_dataframe
            df_procesado = pd.DataFrame()
            total_rows = len(global_dataframe)

            progreso["maximum"] = total_rows
            for i, row in enumerate(global_dataframe["Protocol"]):
                try:
                    if not isinstance(row, str):
                        continue
                    fila = {}
                    lineas = row.splitlines()
                    for linea in lineas:
                        if "," in linea:
                            partes = linea.split(",", 1)
                            titulo, valor = partes[0].strip(), partes[1].strip()
                            
                            # Intentar convertir a float
                            try:
                                valor_convertido = float(valor.replace(',', '.'))
                            except ValueError:
                                valor_convertido = valor
                            
                            # Manejo especial para fechas
                            if "DataTime" in titulo:
                                try:
                                    valor_convertido = pd.to_datetime(valor, format="%Y%m%d %H%M%S")
                                except:
                                    pass
                            
                            fila[titulo] = valor_convertido
                    
                    df_fila = pd.DataFrame([fila])
                    df_procesado = pd.concat([df_procesado, df_fila], ignore_index=True)
                except Exception as e:
                    print(f"Error procesando fila: {e}")

                progreso["value"] = i + 1
                window.update_idletasks()

            # Limpiar nombres de columnas
            df_procesado.columns = [col.strip() for col in df_procesado.columns]

            # Actualizar global_dataframe con los datos procesados
            global_dataframe = df_procesado

            # Mostrar datos procesados en la pestaña 2
            configurar_tabla(tabla_pestaña2, global_dataframe.head(100))

        threading.Thread(target=tarea_procesamiento, daemon=True).start()

    btn_procesar = ttk.Button(
        frame_botones2,
        text="Procesar Archivo",
        style="Custom.TButton",
        command=procesar_datos,
    )
    btn_procesar.pack(side="left", padx=10)

    btn_guardar = ttk.Button(
        frame_botones2,
        text="Guardar Archivo .xlsx",
        style="Custom.TButton",
        command=lambda: guardar_archivo(global_dataframe)
    )
    btn_guardar.pack(side="left", padx=10)
    
    
    # PESTAÑA 3
    pestaña3 = ttk.Frame(notebook)
    notebook.add(pestaña3, text="Visualizar Datos")
    
    btn_visualizar = ttk.Button(pestaña3, text="Realizar Gráfico", command=graficar,
                                style="Custom.TButton")
    btn_visualizar.pack(pady=10, padx=10)
    
    
    
    # Crear grafico
    def graficar():
        global global_dataframe
        pass
        

    # Empaquetar el notebook
    notebook.pack(expand=True, fill="both")
    window.mainloop()



