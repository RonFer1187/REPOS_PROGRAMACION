Algoritmo eje7
	//Conversión de Temperatura Industrial: Un sistema de enfriamiento reporta datos en grados Fahrenheit. Desarrolle un algoritmo que convierta dicha temperatura a grados Celsius para que los técnicos puedan registrarla en el manual local.
	Definir grados_F,celcius Como Real
	
	Escribir "Ingrese grados Fahrenheit"
	Leer grados_F
	
	celcius<-(grados_F-32)/1.8
	
	Mostrar "La temperatura es: ", celcius, " grados Celcius" 
FinAlgoritmo
