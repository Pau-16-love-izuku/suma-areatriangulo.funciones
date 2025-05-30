import tkinter as tk
from tkinter import messagebox
class SumaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Suma de dos números")
        self.label1 = tk.Label(master, text="Número 1:")
        self.label1.pack()
        self.entry1 = tk.Entry(master)
        self.entry1.pack()
        self.label2 = tk.Label(master, text="Número 2:")
        self.label2.pack()
        self.entry2 = tk.Entry(master)
        self.entry2.pack()
        self.boton = tk.Button(master, text="Calcular Suma", command=self.calcular_suma, width=40, height=2)
        self.boton.pack()
        self.resultado = tk.Label(master, text="")
        self.resultado.pack()
    def calcular_suma(self):
        try:
            num1 = int(self.entry1.get())
            num2 = int(self.entry2.get())
            resultado= num1 + num2
            self.resultado.config(text=f"Suma: {resultado}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números enteros válidos.")
def main():
    root = tk.Tk()
    app = SumaGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()

