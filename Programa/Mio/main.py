import logging
import traceback
import tkinter as tk
from tkinter import messagebox
from ui.window_creator import create_main_window

def configure_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='logs/app_log.log',
        filemode='w'
    )

def run_application():
    """
    Safely run the application with error handling.
    """
    try:
        configure_logging()
        logging.info("Application starting...")
        create_main_window()
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        logging.error(traceback.format_exc())
        
        error_message = (
            "Ha ocurrido un error al iniciar la aplicación.\n\n"
            "Detalles técnicos han sido registrados en el archivo de registro."
        )
        
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error de Inicialización", error_message)
        except Exception:
            print(error_message)
        
        raise

def main():
    """Main entry point for the application."""
    run_application()

if __name__ == "__main__":
    main()
    
    
    