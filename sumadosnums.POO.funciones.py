class Calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def leer_datos(self):
        self.num1 = int(input("Ingresa el primer número: "))
        self.num2 = int(input("Ingresa el segundo número: "))

    def sumar(self):
        return self.num1 + self.num2

def main():
    calc = Calculadora()
    calc.leer_datos()
    resultado = calc.sumar()
    print("La suma es:", resultado)

if __name__ == "__main__":
    main()
