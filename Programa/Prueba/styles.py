from tkinter import ttk

def configure_styles():
    """Configure application-wide styles."""
    style = ttk.Style()
    style.theme_use("clam")

    # Button styles
    style.configure("Custom.TButton",
                    background="#ecb93b",
                    foreground="black",
                    font=("Garamond", 14))
    style.map("Custom.TButton",
              background=[("active", "#ecb93b")])

    # Progress bar styles
    style.configure(
        "Green.Horizontal.TProgressbar",
        troughcolor="white",
        background="green",
        thickness=20
    )

    # Treeview styles
    style.configure("Custom.Treeview", 
                    rowheight=150,
                    background='white',
                    foreground='black',
                    fieldbackground='white')
    style.map("Custom.Treeview", 
              background=[('selected', '#4A6984')],
              foreground=[('selected', 'white')])