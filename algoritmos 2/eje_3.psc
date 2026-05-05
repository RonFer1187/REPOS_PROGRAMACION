Algoritmo eje_3
	//En un hospital, el presupuesto anual se divide en tres áreas: Ginecología (40%), Traumatología (30%) y Pediatría (30%). Dado un monto presupuestal total, determine cuánto dinero recibirá cada área
	definir presupuesto,gineco,trauma,pediatria Como Real

	
	Escribir "Ingrese presupesto total"
	Leer presupuesto
	
	gineco<-presupuesto*0.4
	trauma<-presupuesto*0.3
	pediatria<-presupuesto*0.3
	
	Mostrar "El presupuesto asignado para ginecologia es: " gineco
	Mostrar "El presupuesto asignado para traumatologia es! " trauma
	Mostrar "El presupuesto asignado para pediatria es " pediatria
	
FinAlgoritmo
