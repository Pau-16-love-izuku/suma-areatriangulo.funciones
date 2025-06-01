def sumar(a, b):
    return a + b

def main():
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    resultado = sumar(num1, num2)
    print("La suma es:", resultado)

if __name__ == "__main__":
    main()
