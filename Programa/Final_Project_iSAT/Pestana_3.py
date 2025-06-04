"""Módulo para la configuración y diseño de la pestaña 3"""

from librerias import *
import Programa.Final_Project_iSAT.transform_page as transform_page
import funciones_generales

# Variables globales
dataframe_global = pd.DataFrame()
últimas_columnas = []

# Entorno global pestaña 3 ================================================================
def pestana3(notebook):
    
    # Funciones de la pestaña =============================================================
    # Función para actualizar dinámicamente el Combobox
    def actualizar_combobox():
        dataframe_global = transform_page.obtener_dataframe()
        
        global últimas_columnas
        # Verificar si las columnas han cambiado
        nuevas_columnas = list(dataframe_global.columns)
        
        if nuevas_columnas != últimas_columnas:  # Solo actualizar si hay cambios
            combo_opciones["values"] = nuevas_columnas
            combo_opciones.set(nuevas_columnas[0] if nuevas_columnas else "")
            combo_opciones2["values"] = nuevas_columnas
            combo_opciones2.set(nuevas_columnas[0] if nuevas_columnas else "")
            diferenciar["values"] = nuevas_columnas
            diferenciar.set(nuevas_columnas[0] if nuevas_columnas else "")
            últimas_columnas = nuevas_columnas
        
        # Ejecutar nuevamente después de 1 segundo
        pestana3.after(1000, actualizar_combobox)
        
        # Función para mostrar el estado de los Checkbuttons @@@
    def mostrar_estado():
        # Comprueba que solo se seleccione uno
        if (
           (histograma_value.get() and dispersion_value.get()) 
        or (histograma_value.get() and barras_value.get()) 
        or (dispersion_value.get() and barras_value.get()) 
        or (dispersion_value.get() and barras_value.get() and histograma_value.get())
        ):
            
            messagebox.showwarning("Warning", "Solo puede seleccionar un tipo de gráfico")
            
        elif not(histograma_value.get() or dispersion_value.get() or barras_value.get()):
            
            messagebox.showwarning("Warning", "Debe seleccionar algún tipo de gráfico")
            
        # Comprueba que tipo se ha seleccionado
        # HISTOGRAMA
        elif histograma_value.get():
            if combo_opciones.get() == "":
                messagebox.showwarning("Warning", f"No has seleccionado ningún dato")
            else:
                messagebox.showinfo("Info", f"Has seleccionado realizar un histograma de {combo_opciones.get()}")
        
        # DISPERSION
        elif dispersion_value.get():
            
            if combo_opciones.get() == "" and combo_opciones2.get() == "":
                messagebox.showwarning("Warning", "No has sleccionado ningún eje")
            elif combo_opciones.get() == "":
                messagebox.showwarning("Warning", f"No has seleccionado ningún dato en el eje X")
            elif combo_opciones2.get() == "":
                messagebox.showwarning("Warning", f"No has seleccionado ningún dato en el eje Y")
            else:
                messagebox.showinfo("Info", f"Has seleccionado realizar un gráfico de dispersión de {combo_opciones.get()} -- {combo_opciones2.get()}")
        
        # BARRAS
        elif barras_value.get():
            if combo_opciones.get() == "" and combo_opciones2.get() == "":
                messagebox.showwarning("Warning", f"No has seleccionado ningún dato")
            elif combo_opciones.get() == "":
                messagebox.showwarning("Warning", f"No has seleccionado ningún dato en el eje X")
            elif combo_opciones2.get() == "":
                messagebox.showwarning("Warning", f"No has seleccionado ningún dato en el eje Y")
            else:
                messagebox.showinfo("Info", f"Has seleccionado realizar un gráfico de barras de {combo_opciones.get()} -- {combo_opciones2.get()}")

    def realizar_grafico():
        
        global dataframe_global
        if dataframe_global.empty:
            dataframe_global = transform_page.obtener_dataframe()  # Obtenemos Dataframe de Pestaña 2
        
        # Histograma @@@@
        if histograma_value.get():
            sns.histplot(data = dataframe_global.sort_values(by=combo_opciones.get()),
                         x=combo_opciones.get(),
                         hue="Screwing Status")
            plt.show()
        
        # Dispersión @@@@
        elif dispersion_value.get():
            sns.relplot(data=dataframe_global,
                            x=combo_opciones.get(),
                            y=combo_opciones2.get())
            plt.ylim(bottom=0)  # Ajusta la parte inferior del eje Y
            plt.show()
            
        
        # Barras @@@@
        elif barras_value.get():
            sns.barplot(data=dataframe_global.sort_values(by=[combo_opciones.get(), combo_opciones2.get()]),
                        x=combo_opciones.get(),
                        y=combo_opciones2.get())
            plt.show()
            
            


    # Creación de pestaña y botones =======================================================
    # Pestaña -----------------------------------------------------------------------------
    pestana3 = ttk.Frame(notebook, width=1280, height=720)
    pestana3.pack_propagate(False)  # Evita que la pestaña cambie de tamaño

    # Actualizar fecha --------------------------------------------------------------------
    funciones_generales.actualizar_fecha(pestana3)

    # Desplegable con opciones 1 -----------------------------------------------------------
    combo_opciones = ttk.Combobox(pestana3, values=list(dataframe_global.columns), width=50)
    combo_opciones.place(x=50, y=50)
    eje_x_label = ttk.Label(pestana3, text="Eje X")
    eje_x_label.place(x=50, y=20, width=40, height=30)
    
    # Desplegable con opciones 1 -----------------------------------------------------------
    combo_opciones2 = ttk.Combobox(pestana3, values=list(dataframe_global.columns), width=50)
    combo_opciones2.place(x=50, y=110)
    eje_y_label = ttk.Label(pestana3, text="Eje Y")
    eje_y_label.place(x=50, y=80, width=40, height=30)
    
    # Iniciar la actualización dinámica del Combobox -------------------------------------
    actualizar_combobox()
    
    # Checkbuttons -----------------------------------------------------------------------
    # Checkbutton Histograma  @@@@
    histograma_value = tk.BooleanVar()  # Valor que tomará TRUE o FALSE
    histograma_check = tk.Checkbutton(pestana3, text="Histograma", variable=histograma_value)  # Checkbutton que modofica el valor 
    histograma_check.place(x=100, y=140, width=80, height=30) # Posición del checkbutton
    
    # Checkbutton Dispersión  @@@@
    dispersion_value = tk.BooleanVar() # Valor que tomará TRUE o FALSE
    dispersion_check = tk.Checkbutton(pestana3, text="Dispersión", variable=dispersion_value) # Checkbutton que modofica el valor
    dispersion_check.place(x=96, y=180, width=80, height=30) # Posición del checkbutton
    
    # Checkbutton Barras  @@@@
    barras_value = tk.BooleanVar() # Valor que tomará TRUE o FALSE
    barras_check = tk.Checkbutton(pestana3, text="Barras", variable=barras_value) # Checkbutton que modofica el valor
    barras_check.place(x=85, y=220, width=80, height=30) # Posición del checkbutton
    
    # Botón para ejecutar la función mostrar_estado --------------------------------------
    boton_seleccion = tk.Button(pestana3, text="Mostrar Estado", command=mostrar_estado)
    boton_seleccion.place(x=200, y=180)
    
    # Botón para realizar gráfico en función de lo seleccionado ---------------------------
    boton_graficar = tk.Button(pestana3, text="Realizar Gráfico", command=realizar_grafico)
    boton_graficar.place(x=400, y=78)
    
    # PENDIENTE DE REVISAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # Introducir diferenciación -----------------------------------------------------------
    diferenciar = ttk.Combobox(pestana3, values=list(dataframe_global.columns), width=50)
    diferenciar.place(x=700, y=600)
    hue_label = tk.Label(pestana3, text="Diferenciación")
    hue_label.place(x=600, y=500)
    
    
    # FIN -------------------------------------------------------------------------------------------
    return pestana3