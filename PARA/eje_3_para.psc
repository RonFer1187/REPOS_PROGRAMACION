Algoritmo eje3_para
	//Una cooperativa eléctrica necesita calcular el total a pagar de un aviso de cobranza. El algoritmo debe solicitar la lectura anterior del medidor (kWh), la lectura actual (kWh) y el precio por kilovatio hora. Debe mostrar el consumo del mes y el costo total del servicio.

	Escribir "Ingrese la lectura de consumo del mes anterior"
	Leer consumo_anterior
	
	Escribir "Ingrese la lectura de consumo del mes actual"
	Leer consumo_actual
	
	kwh<-2
	
	consumo_total<-consumo_actual-consumo_anterior
	
	precio<-consumo_total*kwh
	
	Mostrar "El consumo total de este mes es : ", consumo_total " kWh ", " y el precio a pagar es ", precio
	
	
FinAlgoritmo
