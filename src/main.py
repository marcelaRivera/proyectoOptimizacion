from lecture import readFile
from initialSolution import getHourInit, constructiveO, getEmployersCalificatesInJobs, constructiveHeuristic
from generateNeighborhood import generatingNeighborhood
from simuleted import simulatedAnneling, simulatedAnneling2

def main():

	jobs = [] # Lista que almacenara a las tareas 
	jobsCalificate = [] # Trabajos que puede hacer cada trabajador

	# Realizando lectura de archivo de entrada
	jobs, jobsCalificate =  readFile() 

	O = [] #vector con las tareas superpuestas
	P = [] #empleados calificados para hacer la tarea i
	R = [] #trabajos asignados al trabajador w
	S = [] #horas de inicio de cada trabajo 
	
	S = getHourInit(jobs)
	O = constructiveO(jobs)
	#print(O)
	P = getEmployersCalificatesInJobs(jobsCalificate, len(jobs))
	entrada = constructiveHeuristic(S, O, P, R, len(jobsCalificate))
	#print(entrada)
	#print("Largo maximo" + str(len(entrada)))
	#print("NUmero maximo es: " + str(max(entrada)))
	#print("NUmero minimo es: " + str(min(entrada)))
	input("al fin ")
	salida = generatingNeighborhood(entrada, jobsCalificate,len(jobs),O) # len(jobs) solo para generar la solucion
	#print(salida)
	#input("stop")
	# simuleted

	input("simuleted")
	salidaSimuleted = simulatedAnneling2(100,1,10,2,0.99,salida,len(jobsCalificate),jobsCalificate,O,len(jobs))
	#print(salidaSimuleted)
main()