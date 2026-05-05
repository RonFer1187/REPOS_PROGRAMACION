Algoritmo eje5
	//Cálculo de Pendiente: Desarrolle un algoritmo que permita calcular la pendiente de una recta que pasa por dos puntos en el plano cartesiano ($P1$ y $P2$). El programa debe solicitar las coordenadas $(x1, y1)$ y $(x2, y2)$ y aplicar la fórmula correspondiente.
	
	Escribir "Ingrese coordenada x1"
	Leer x1
	
	Escribir "Ingrese coordenada y1"
	Leer y1
	
	Escribir "Ingrese coordenada x2"
	Leer x2
	
	Escribir "Ingrese coordenada y2"
	Leer y2
	
	si x1 == x2 Entonces
		Escribir "La pendiente es indefinida "
	SiNo
		
	y_total<- y2-y1
	x_total<- x2-x1
	pendiente<-y_total/x_total
	
	FinSi
	
	Mostrar "La pendiente es : " pendiente

FinAlgoritmo
