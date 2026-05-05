Algoritmo eje6
	// Descuento de Temporada: Una tienda de ropa ofrece un descuento del 15 MOD  sobre el total de la compra. El algoritmo debe recibir el precio de tres prendas diferentes, sumarlas, aplicar el descuento y mostrar el monto final que el cliente debe pagar.
	
	Escribir "Ingrese precio producto 1"
	Leer producto1
	
	Escribir "Ingrese precio producto 2"
	Leer producto2
	
	Escribir "Ingrese precio producto 3"
	Leer producto3
	
	
	suma<-producto1+producto2+producto3
	descuento <- suma*0.15
	total_pago <- suma-descuento
	Escribir 'El costo total de los 3 productos es: ',suma,' el descuento es del 15% es : ',descuento,' el total a pagar es: ',total_pago
FinAlgoritmo
