Algoritmo eje_1
	//Una empresa requiere un sistema que calcule el sueldo bruto de un empleado. El programa debe recibir el nombre del trabajador, las horas laboradas durante la semana y el pago por hora. Debe mostrar el nombre y el total a pagar.
	Definir nombre Como Caracter
	
	hrs_semana<-0
	pago_hrs<-35
	total_pago<-0
	
	Escribir "Ingrese el nombre del trabajor"
	Leer nombre
	
	Escribir "Ingrese horas trabajadas a la semana"
	Leer hrs_semana
	
	total_pago<-hrs_semana*pago_hrs
	
	Mostrar  "Por " hrs_semana " trabajadas del señor/a " nombre " su total pago es: " total_pago 
	
FinAlgoritmo
