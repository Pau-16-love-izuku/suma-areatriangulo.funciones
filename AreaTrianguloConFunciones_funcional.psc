Algoritmo AreaTrianguloConFunciones_funcional
	
    Definir base, altura, area Como Real
	
    Escribir "Ingresa la base del triángulo:"
    Leer base
	
    Escribir "Ingresa la altura del triángulo:"
    Leer altura
	
    CalcularArea(base, altura, area)
	
    Escribir "El área del triángulo es: ", area
	
FinAlgoritmo

SubProceso CalcularArea(base, altura Por Valor, area Por Referencia)
    area <- (base * altura) / 2
FinSubProceso
