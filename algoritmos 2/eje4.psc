Algoritmo eje4
	//Rendimiento de Combustible: Un conductor desea saber cuántos litros de gasolina consume su vehículo por cada kilómetro recorrido. El algoritmo debe solicitar el kilometraje inicial, el kilometraje final y la cantidad de litros surtidos para dar el resultado.
	
	
	Escribir "Ingresa kilometro_inicial"
	Leer kilometro_inicial
	
	Escribir  "Ingresa kilometro_final"
	Leer kilometro_final
	
	Escribir "Ingrese cantidad de litros cargados"
	Leer cantidad_litros
	
	kilometros_recorridos<- kilometro_final-kilometro_inicial
	
	rendimiento<-cantidad_litros/kilometros_recorridos
	
	Mostrar "Usted recorrio " kilometros_recorridos " kilometros recorridos" " y " "Su vehiculo consume " rendimiento " litros por cada kilometro recorrido"

FinAlgoritmo
