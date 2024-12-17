import os
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def load_file():
    """Load file from filesystem."""
    archivo = filedialog.askopenfilename(title="Selecciona un archivo")
    
    if archivo:
        try:
            if ".csv" in archivo:
                dataframe = pd.read_csv(archivo)
            elif ".xlsx" in archivo or ".xls" in archivo:
                dataframe = pd.read_excel(archivo)
            else:
                messagebox.showerror("Error", "Formato de archivo no soportado")
                return None
            
            return dataframe
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")
            return None
    
    return None

def save_file(dataframe):
    """Save processed dataframe to Excel."""
    if dataframe is None:
        messagebox.showinfo("Info", "Primero cargue y procese un archivo")
        return

    ruta = filedialog.askdirectory(title="Selecciona Carpeta")
    
    if not ruta:
        return

    dia = time.strftime("%d%m%y")
    hora = time.strftime("%H%M%S")
    
    try:
        archivo_destino = os.path.join(ruta, f"Extraido{dia}{hora}.xlsx")
        dataframe.to_excel(archivo_destino, index=False)
        messagebox.showinfo("Éxito", f"¡Guardado con éxito en: {archivo_destino}!")
    except Exception as e:
        messagebox.showerror("Error", f"No se ha guardado debido a: {e}")