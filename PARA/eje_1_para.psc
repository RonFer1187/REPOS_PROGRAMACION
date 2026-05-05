Algoritmo eje_1
	//Un exportador de quinua produce sacos de 50 kilogramos, pero el mercado internacional compra el producto por libras. Realice un algoritmo que reciba la cantidad de sacos producidos y, sabiendo que 1 kilogramo equivale a 2.20462 libras, determine el total de libras producidas y el valor total de la venta si cada libra se paga a un precio "X" proporcionado por el usuario.
	

	Escribir "¿Cuántas kilos usted desea vender?"
	Leer kilos
	
	Escribir "Ingrese el precio por cada kilo"
	Leer precio_kl
	
	libras<-kilos*2.20462
	precio<-libras*kilos
	
	Mostrar "Usted debe vender " libras " libras " "el precio es ", precio " bs."
	
FinAlgoritmo
