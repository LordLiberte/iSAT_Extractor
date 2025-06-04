"""Módulo para la configuración y personalización de la Pestaña 2"""
from librerias import *
import load_page as load_page
import funciones_generales

# Variables globales
dataframe_global = pd.DataFrame()

# Enviar dataframe
def obtener_dataframe():
    return dataframe_global

# Entorno global pestaña 2 ================================================================
def pestana2(notebook):
    
    # Funciones de la pestaña =============================================================
 
    # Guardar archivo procesado en ruta deseada --------------------------------------------
    def guardar_archivo():
        ruta = filedialog.askdirectory(title="Selecciona Carpeta")
        
        dia = time.strftime("%d%m%y")
        hora = time.strftime("%H%M%S")
        
        if dataframe_global is None:
            print("Primero cargue y procese un archivo")
        
        else:
            dataframe_global.to_excel(f"{ruta}\Extraido{dia}{hora}.xlsx")
            try:
                os.path.isdir(f"{ruta}\Extraido.xlsx")
            
            except Exception as e:
                tk.messagebox.showinfo(message=f"No se ha guardado debido a: {e}", title="Error")
            
            else:
                tk.messagebox.showinfo(message=f"¡Guardado con éxito en: {ruta}\Extraido.xlsx!")
    
    # Limpiar y procesar información de columna Protocol ---------------------------------------
    def limpiar_info():
        # Declarar la variable global
        global dataframe_global  # Se añade para asignar a la variable global el resultado del procesado
        
        # Obtener dataframe de la pestaña 1
        try:
            dataframe = load_page.obtener_dataframe()
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo cargar el dataframe: {e}")
            return

        if "Protocol" not in dataframe.columns:
            tk.messagebox.showerror("Error", "La columna 'Protocol' no existe en el DataFrame.")
            return

        df_protocol = dataframe["Protocol"]

        # Configurar la barra de progreso
        contenedor_progreso["value"] = 0
        contenedor_progreso["maximum"] = len(df_protocol)

        filas_procesadas = []
        for idx, line in enumerate(df_protocol):
            line = line.strip()
            fila = {}
            lineas = line.splitlines()

            for i in lineas:
                try:
                    titulo, valor = i.split(",", 1)

                    if "DataTime" in titulo:
                        try:
                            valor = pd.to_datetime(valor, format="%Y%m%d %H%M%S")
                        except Exception as e:
                            pass

                    try:
                        valor = float(valor)
                    except:
                        pass
                    else:
                        valor = round(valor, 3)

                    fila[titulo.strip()] = str(valor).strip()
                except ValueError:
                    print(f"Error al procesar línea: {i}")
                    continue

            filas_procesadas.append(fila)

            # Actualizar la barra de progreso
            contenedor_progreso["value"] = idx + 1
            contenedor_progreso.update_idletasks()

        # Crear DataFrame procesado
        dataframe_procesado = pd.DataFrame(filas_procesadas)
        resultado = pd.concat([dataframe.drop(columns=["Protocol"]), dataframe_procesado], axis=1)

        # Asignar a la variable global
        dataframe_global = resultado  # Ahora se asigna globalmente

        # Limpiar la tabla previa
        for i in tree.get_children():
            tree.delete(i)

        # Configurar las columnas con los nombres del DataFrame
        tree["columns"] = list(dataframe_global.head(50).columns)  # Asignar columnas dinámicamente
        for col in tree["columns"]:
            tree.heading(col, text=col)  # Configurar la cabecera de cada columna
            tree.column(col, width=300, anchor=tk.W)  # Opcional: ajustar el tamaño de columna

        # Llenar la tabla con los datos del DataFrame
        for index, row in dataframe_global.iterrows():
            tree.insert("", tk.END, values=list(row))

        etiqueta = ttk.Label(pestana2, text="", anchor="w")
        etiqueta.place(x=20, y=650, width=1240, height=30)
        ruta_archivo_global = load_page.obtener_ruta_archivo()
        nombre_archivo_cargado = ruta_archivo_global.split("/")[-1]  # Extraer el nombre
        etiqueta.config(text=f"Archivo procesado: {nombre_archivo_cargado}")

        tk.messagebox.showinfo("Éxito", "Datos procesados con éxito.")


    # Creación de pestaña y botones =======================================================
    # Pestaña -----------------------------------------------------------------------------
    pestana2 = ttk.Frame(notebook, width=1280, height=720) # Crea la pestaña con su tamaño
    pestana2.pack_propagate(False) # Evita que la pestaña cambie de tamaño
    # Actualizar fecha --------------------------------------------------------------------
    funciones_generales.actualizar_fecha(pestana2)
    
    # Barra de progreso
    # Barra de progreso
    global contenedor_progreso
    contenedor_progreso = ttk.Progressbar(pestana2, orient="horizontal", length=400, mode="determinate")
    contenedor_progreso.place(x=190, y=43)
    
    # Botrón para guardar archivo
    boton_guardar = ttk.Button(pestana2, text="Guardar Archivo .xlsx", command=guardar_archivo)
    boton_guardar.place(x=20, y=100, width=97, height=50)
    
    # Botón procesar información
    boton_procesar = ttk.Button(pestana2, text="Limpiar y procesar datos", command=limpiar_info)
    boton_procesar.place(x=20, y=30, width=150, height=50)
    
    # Cuadricula para mostrar información
    tree = ttk.Treeview(pestana2, show="headings")
    tree.place(x=135, y=100, width=1120, height=560)
    
    
    return pestana2