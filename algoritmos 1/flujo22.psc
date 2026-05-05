Algoritmo flujo22
	Definir num1, num2 como entero
	Definir minutosTotales, horas, minutosRestantes Como Entero
	
	Escribir "ingrase la distancia del recorrido "
	Leer num1
	
	Escribir "ingrese la velocidad del veiculo "
	Leer num2
	
	minutosTotales=(num1/num2)*60
    
    horas <- trunc(minutosTotales / 60)
    minutosRestantes <- minutosTotales % 60
    
    Escribir " tiempo de vije ", horas, " horas y ", minutosRestantes, " minutos."
	
	
FinAlgoritmo
