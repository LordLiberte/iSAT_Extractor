"""Módulo para las funciones que se realizará cuando se aprieten botones"""

# Librerias
from libraries import *

# Función cargar archivos
def cargar_archivo():
    # Abre el explorador de archivos
    archivo = filedialog.askopenfilename(title="Selecciona un archivo")
    
    # Si se seleccionó un archivo
    if archivo:
        try:
            # Comprueba la extensión del archivo
            if ".csv" in archivo:
                dataframe = pd.read_csv(archivo)
            
            elif ".xlsx" in archivo or ".xls" in archivo:
                dataframe = pd.read_excel(archivo)
            
            else:
                print("Formato de archivo no soportado")
                return None
            
            print("DataFrame cargado:")
            print(dataframe)
            print("\nTipo de columnas:", dataframe.dtypes)
            
            return dataframe
        
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return None
    
    return None

def configurar_tabla(tabla, dataframe):
    # Limpiar tabla existente
    for i in tabla.get_children():
        tabla.delete(i)
    
    # Limpiar columnas existentes
    tabla['columns'] = []
    
    # Configurar columnas
    columnas = list(dataframe.columns)
    tabla['columns'] = columnas
    
    # Configurar encabezados y columnas
    for columna in columnas:
        tabla.heading(columna, text=columna)
    
    # Ajustar dinámicamente el ancho de las columnas
    ajustar_ancho_columnas(tabla, dataframe)
    
    # Convertir todos los valores a cadenas para evitar errores
    datos = dataframe.astype(str)
    
    # Insertar datos
    for indice, fila in datos.iterrows():
        valores = list(fila)
        tabla.insert('', 'end', values=valores)
    
    print(f"Insertados {len(datos)} registros en la tabla")

def ajustar_ancho_columnas(tabla, dataframe):
    """
    Ajusta el ancho de las columnas basándose en el contenido
    """
    # Obtener el ancho de la ventana
    ancho_ventana = tabla.winfo_width()
    num_columnas = len(dataframe.columns)
    
    # Calcular ancho base
    ancho_base = ancho_ventana // num_columnas if num_columnas > 0 else 100
    
    # Configurar columnas
    for columna in dataframe.columns:
        # Encontrar el máximo ancho de texto en la columna
        max_ancho = max(
            dataframe[columna].astype(str).str.len().max(),
            len(columna)  # Longitud del nombre de la columna
        )
        
        # Ajustar ancho, con un mínimo y máximo
        ancho_columna = max(max_ancho * 10, ancho_base)
        ancho_columna = min(ancho_columna, 300)  # Límite máximo
        
        tabla.column(columna, width=ancho_columna, anchor='center')