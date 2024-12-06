"""Módulo para las funciones que se realizará cuando se aprieten botones"""

# Librerias
from libraries import *

# Función cargar archivos

def cargar_archivo():
    
    # Abre el explorador de archivos
    archivo = filedialog.askopenfilename(title="Selecciona un archivo")
    
    # Comprueba laextensión del archivo
    if ".csv" in archivo:
        dataframe = pd.read_csv(archivo)
    
    elif ".xlsx" in archivo or ".xls" in archivo:
        dataframe = pd.read_excel(archivo)