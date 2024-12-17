import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.file_handler import load_file, save_file
from ui.styles import configure_styles

class ISATExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("iSAT Extractor")
        self.root.geometry("1280x720")

        self.global_dataframe = None
        self.canvas = None
        self.ax = None

        self._setup_styles()
        self._create_notebook()

    def _setup_styles(self):
        """Configure application styles."""
        configure_styles()

    def _create_notebook(self):
        """Create notebook with tabs."""
        self.notebook = ttk.Notebook(self.root)
        self._create_file_load_tab()
        self._create_data_processing_tab()
        self._create_visualization_tab()

        self.notebook.pack(expand=True, fill="both")

    # ... [rest of the methods from the original Window_Creator.py] ...

def create_main_window():
    """Function to create the main application window"""
    root = tk.Tk()
    app = ISATExtractor(root)
    root.mainloop()