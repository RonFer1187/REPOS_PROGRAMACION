Algoritmo eje13
	//Debe mostrar el costo total. Tiempo de Viaje: Un autobús viaja de una ciudad a otra a una velocidad constante (km/h). Dado que se conoce la distancia entre ciudades (km), determine cuánto tiempo (en horas y minutos) tardará el autobús en llegar a su destino.
	

	
	
	Escribir "Ingrese la distancia entre las dos ciudades"
	Leer distancia
	
	Escribir "Ingrese la velocidad k/h"
	Leer velocidad
	
	tiempo_total<-distancia/velocidad
	
	horas<- TRUNC (tiempo_total)
	
	minutos<- TRUNC ((tiempo_total - horas)*60)
	
	Mostrar "El tiempo estimado de viaje es: " horas, " hrs. con " minutos, " minutos"
	
	
FinAlgoritmo
