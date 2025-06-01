class Triangulo:
    def __init__(self):
        self.base = 0
        self.altura = 0
    def pedir_datos(self):
        try:
            self.base = float(input("Ingresa la base del triángulo: "))
            self.altura = float(input("Ingresa la altura del triángulo: "))
        except ValueError:
            print("¡Error! Solo se permiten números.")
            self.pedir_datos()  # Reintenta si hubo error
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        print("El área del triángulo es:", area)
triangulo = Triangulo()
triangulo.pedir_datos()
triangulo.calcular_area()
