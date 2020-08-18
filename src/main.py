from lecture import readFile
from initialSolution import getHourInit, constructiveO, getEmployersCalificatesInJobs, constructiveHeuristic


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
	P = getEmployersCalificatesInJobs(jobsCalificate, len(jobs))
	constructiveHeuristic(S, O, P, R, len(jobsCalificate))


	

main()