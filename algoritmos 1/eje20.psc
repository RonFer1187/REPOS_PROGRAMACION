Algoritmo eje20
	//Validar que el usuario ingrese un número mayor a 0 (repetir hasta que lo haga correctamente).
	
	Definir dato, contador Como Entero
	
	contador<-0
	
	Escribir "ingrese un numero negativo"
	Leer dato
	
	Mientras dato<0 Hacer
		Escribir "ingrese un numero mayor a 0 si quiere terminar el juego"
		Leer dato
		contador<-contador-1
	FinMientras
	Escribir "Gracias por ingresar un numero positivo"
FinAlgoritmo
