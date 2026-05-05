Algoritmo sin_titulo
	//Conversión de Medidas de Construcción: Un contratista necesita comprar arena, pero el proveedor la vende por metros cúbicos ($m^3$) y él solo tiene las medidas en pies cúbicos ($ft^3$). Realice un algoritmo que convierta una cantidad "X" de pies cúbicos a metros cúbicos.
	Definir pie_cubico, metro_cubico Como Real
	
	pie_cubico<-35.315
	
	Escribir "Ingrese la cantidad de pies cubicos que desea comprar"
	Leer dato
	
	metro_cubico<-dato/pie_cubico
	
	Mostrar "La cantidad de metros cubicos que necesita son : " metro_cubico
	
FinAlgoritmo
