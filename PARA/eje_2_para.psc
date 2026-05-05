Algoritmo eje_2_para
	//Una empresa distribuye sus ganancias anuales de la siguiente manera: Socio A (45%), Socio B (30%) y Reserva Operativa (25%). Dado un monto total de utilidades, determine cuánto dinero le corresponde a cada parte.

	Escribir "Ingrese monto total utilidades"
	Leer utilidades
	
	socio_a<-utilidades*0.45
	socio_b<-utilidades*0.30
	reserva<-utilidades*0.25
	
	Mostrar "El socio A tiene una ganancia de : " socio_a
	Mostrar "El socio B tiene una ganancia de : " socio_b
	Mostrar "La reserva es de : " reserva
	
FinAlgoritmo
