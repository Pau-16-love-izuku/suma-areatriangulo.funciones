class Triangulo:
    def __init__(self):
        self.base = 0.0
        self.altura = 0.0

    def leer_datos(self):
        self.base = float(input("Ingresa la base del triángulo: "))
        self.altura = float(input("Ingresa la altura del triángulo: "))

    def calcular_area(self):
        return (self.base * self.altura) / 2

def main():
    tri = Triangulo()
    tri.leer_datos()
    area = tri.calcular_area()
    print("El área del triángulo es:", area)

if __name__ == "__main__":
    main()
