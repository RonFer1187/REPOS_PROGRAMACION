Algoritmo eje14
	//Cambio de Divisas: Una casa de cambio requiere un software que reciba una cantidad en Bolivianos (BOB) y la convierta a Euros (EUR) y a Dólares (USD), basándose en un tipo de cambio proporcionado por el usuario al inicio.
	Definir BOB, EUR, USD Como Real
	
	Escribir "Ingrese cantidad de Bs. que desea cambiar"
	Leer BOB
	
	Escribir "Ingres Cambio oficial en EUR"
	Leer EUR
	
	Escribir "Ingrese Cambio oficial en USD"
	Leer USD
	
	Cambio_EUR<- BOB/EUR
	Cambio_USD<- BOB/USD
	Cambio_EURok<- REDON(Cambio_EUR*100)/100
	Cambio_USDok<-REDON(Cambio_USD*100)/100
	
	
	Mostrar "El cambio de BOB a USD son :", Cambio_USDok, " USD"
	Mostrar "El cambio de BOB a EUR son :", Cambio_EURok, " EUR"
	

FinAlgoritmo
