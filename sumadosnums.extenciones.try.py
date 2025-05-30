class Suma:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    def pedir_datos(self):
        try:
            self.num1 = int(input("Ingresa el primer número: "))
            self.num2 = int(input("Ingresa el segundo número: "))
        except ValueError:
            print("¡Error! Debes ingresar números enteros.")
            self.pedir_datos()
    def calcular_suma(self):
        resultado= self.num1 + self.num2
        print("La suma es:", resultado)
suma_obj = Suma()
suma_obj.pedir_datos()
suma_obj.calcular_suma()
