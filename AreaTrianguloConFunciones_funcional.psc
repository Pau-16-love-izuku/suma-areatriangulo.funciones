Algoritmo AreaTrianguloConFunciones_funcional
	
    Definir base, altura, area Como Real
	
    Escribir "Ingresa la base del tri�ngulo:"
    Leer base
	
    Escribir "Ingresa la altura del tri�ngulo:"
    Leer altura
	
    CalcularArea(base, altura, area)
	
    Escribir "El �rea del tri�ngulo es: ", area
	
FinAlgoritmo

SubProceso CalcularArea(base, altura Por Valor, area Por Referencia)
    area <- (base * altura) / 2
FinSubProceso
