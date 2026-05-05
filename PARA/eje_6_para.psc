Algoritmo eje_6_para
	//Un vendedor recibe un sueldo base más un 10% de comisión sobre el total de sus ventas mensuales. El algoritmo debe recibir el sueldo base y el monto de sus tres ventas más importantes del mes, calculando el pago total que recibirá el vendedor.
	
	
	Escribir "Ingrese sueldo base"
	Leer sueldo
	
	Para i Desde 1 Hasta 3 Hacer
		Escribir "Ingrese venta ", i
		Leer ventas
		
		suma_ventas<-(suma_ventas+ventas)
		
		comision<-suma_ventas*0.10
		
		total<- sueldo+comision
	FinPara
	
	Escribir " El total de sus ventas fue: ", suma_ventas," Bs"
	Escribir " La comision por sus ventas fue: ", comision, " Bs"
	Escribir " El total pago es :", total, " Bs"
	
FinAlgoritmo
