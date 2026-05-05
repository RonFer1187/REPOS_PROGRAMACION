Algoritmo eje8
//Un inversionista desea colocar su capital en un banco que ofrece un interés del 1.5% mensual. El programa debe calcular cuánto dinero tendrá el inversionista en su cuenta después de un mes, considerando el capital inicial más los intereses.
	
	Definir capital, interes, ganancia Como Real
	
	Escribir "Ingrese capital a invertir"
	Leer capital
	
	interes<-0.015
	ganancia<- capital*interes
	cuenta<-ganancia+capital
	
	Mostrar " Su inversion es de ", capital, " y su ganancia mensual es de : ", ganancia
	Mostrar "Su cuenta en el banco al cabo de un mes tendra : ", cuenta
	
	
FinAlgoritmo
