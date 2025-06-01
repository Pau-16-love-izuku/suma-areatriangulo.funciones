import tkinter as tk
from tkinter import messagebox
class TrianguloGUI:
    def __init__(self, master):
        self.master = master
        master.title("Área de un Triángulo")
        self.label_base = tk.Label(master, text="Base:")
        self.label_base.pack()
        self.entry_base = tk.Entry(master)
        self.entry_base.pack()
        self.label_altura = tk.Label(master, text="Altura:")
        self.label_altura.pack()
        self.entry_altura = tk.Entry(master)
        self.entry_altura.pack()
        self.boton_calcular = tk.Button(master, text="Calcular Área", command=self.calcular_area, width= 40, height=2)
        self.boton_calcular.pack()
        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()
    def calcular_area(self):
        try:
            base = float(self.entry_base.get())
            altura = float(self.entry_altura.get())
            area = (base * altura) / 2
            self.resultado_label.config(text=f"Área: {area}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa solo números válidos.")
def main():
    ventana = tk.Tk()
    app = TrianguloGUI(ventana)
    ventana.mainloop()
if __name__ == "__main__":
    main()
