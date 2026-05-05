Algoritmo eje13
	//Promedio de Calificaciones: Un estudiante desea saber cuál será su promedio final en una materia. El algoritmo debe solicitar las notas de cuatro exámenes y calcular la media aritmética de las mismas.
	
	contador<-1
	
	Mientras contador <=4 Hacer
		Escribir "Ingrese nota " contador
		Leer notas
		suma<-suma+notas
		promedio<-suma/4
		
		contador<-contador+1
	FinMientras

	Mostrar "El promedio de las 4 notas es " promedio
	
FinAlgoritmo
