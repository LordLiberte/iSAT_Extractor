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
    tabla_pestaña1 = Treeviews(pestaña1)

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
        pestaña1,
        text="Cargar Archivo",
        style="Custom.TButton",
        command=cargar_y_mostrar_tabla,
    )
    btn_cargar.pack(pady=10)

    # Pestaña 2 - Procesamiento con barra de progreso
    pestaña2 = ttk.Frame(notebook)
    notebook.add(pestaña2, text="Procesamiento de Datos")
    tabla_pestaña2 = Treeviews(pestaña2)
    progreso = ttk.Progressbar(pestaña2, orient="horizontal", mode="determinate", length=400)
    progreso.pack(pady=10)

    def procesar_datos():
        global global_dataframe  # Importante: usar la variable global
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
                            if "DataTime" in titulo:
                                valor = pd.to_datetime(valor, format="%Y%m%d %H%M%S")
                            fila[titulo] = valor
                    
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
            configurar_tabla(tabla_pestaña2, global_dataframe.head(20))

            # Llamar a actualizar_combobox con el dataframe global
            window.after(0, lambda: actualizar_combobox(global_dataframe))

        # Ejecutar procesamiento en hilo separado
        threading.Thread(target=tarea_procesamiento, daemon=True).start()

    btn_procesar = ttk.Button(
        pestaña2,
        text="Procesar Archivo",
        style="Custom.TButton",
        command=procesar_datos,
    )
    btn_procesar.pack(pady=10)

    def actualizar_combobox(df):
        """
        Actualiza el combobox con las columnas procesadas limpiando nombres.
        También verifica si el DataFrame tiene columnas válidas.
        """
        # Validar las columnas
        if df is None or df.empty:
            tk.messagebox.showerror("Error", "El DataFrame está vacío después de procesar los datos.")
            return

        # Mostrar en consola las columnas disponibles
        print("Columnas disponibles para el combobox:", df.columns.tolist())

        # Asegurarse de que el combobox existe antes de actualizar
        if 'combo_columna' in locals() or 'combo_columna' in globals():
            combo_columna["values"] = df.columns.tolist()
            
            # Seleccionar la primera columna como predeterminada, si existe
            if not df.columns.empty:
                columna.set(df.columns[0])
        else:
            print("Error: combo_columna no está definido")

    # Pestaña 3 - Visualización de datos
    pestaña3 = ttk.Frame(notebook)
    notebook.add(pestaña3, text="Visualización de datos")
    
    # Variables para selección
    tipo_grafico = tk.StringVar(value="Bar")
    columna = tk.StringVar()
    intervalo = tk.BooleanVar(value=False)
    color = tk.StringVar(value="#0000FF")
    cantidad = tk.IntVar(value=10)
    
    ttk.Label(pestaña3, text="Seleccione la columna:").pack(anchor="w", padx=10, pady=5)
    combo_columna = ttk.Combobox(pestaña3, textvariable=columna, state="readonly")
    combo_columna.pack(fill="x", padx=10)

    # Lógica para generar gráficos
    def generar_grafico():
        if global_dataframe is None:
            tk.messagebox.showwarning("Advertencia", "Primero debe cargar y procesar un archivo.")
            return

        col = columna.get()

        if col not in global_dataframe.columns:
            tk.messagebox.showerror("Error", f"La columna '{col}' no existe en los datos.")
            return

        try:
            df = global_dataframe[col].dropna().head(cantidad.get())
            plt.figure(figsize=(10, 6))
            df.plot(kind="bar", color=color.get())
            plt.title(f"Gráfico de barras de {col}")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al generar el gráfico: {e}")

    ttk.Button(pestaña3, text="Generar Gráfico", style="Custom.TButton", command=generar_grafico).pack(pady=10, padx=10)

    notebook.pack(expand=True, fill="both")
    window.mainloop()

