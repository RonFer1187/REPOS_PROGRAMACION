Algoritmo eje15
	//Índice de Masa Corporal (IMC): Desarrolle un algoritmo que calcule el IMC de una persona. Para ello, debe solicitar el peso en kilogramos y la estatura en metros, aplicando la fórmula: $IMC = peso / (estatura)^2$.
	
	definir estatura, peso, imc como real
	
	Escribir "Ingrese su estatura"
	Leer estatura
	
	Escribir "Ingrese su peso"
	Leer peso
	
	imc<-peso/(estatura*estatura) 
	imc_ok<-REDON(imc*100)/100
	
	Mostrar "El IMC de usted es : " imc_ok
	
	
FinAlgoritmo
