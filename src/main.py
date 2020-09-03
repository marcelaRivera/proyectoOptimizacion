from lecture import readFile
from initialSolution import getHourInit, constructiveO, getEmployersCalificatesInJobs, constructiveHeuristic
from generateNeighborhood import generatingNeighborhood, test
from simuleted import simulatedAnneling, funcionObjetivoWithCost,jobsForEachWoker 
from goloso import goloso, minCost
import random

def main():

	opcion = 0
	jobs = None # Lista que almacenara a las tareas
	jobsCalificate = None # Trabajos que puede hacer cada trabajador
	O = None #vector con las tareas superpuestas
	P = None #empleados calificados para hacer la tarea i
	R = [] #trabajos asignados al trabajador w
	S = None #horas de inicio de cada trabajo 
	entrada = None
	listOfCost = None
	listWorkerCosto = None
	iteraciones = 11

	while opcion != 4:

		print("1. Ingresar archivo")
		print("2. Realizar análisis con método Goloso")
		print("3. Realizar análisis con metaheuristica SA")
		print("4. Salir")

		opcion = input("Ingrese la opción: ")
		print(opcion)
		if opcion == "1":
			jobs, jobsCalificate =  readFile()
			S = getHourInit(jobs)
			O = constructiveO(jobs)
			P = getEmployersCalificatesInJobs(jobsCalificate, len(jobs))
			entrada = constructiveHeuristic(S, O, P, R, len(jobsCalificate))
			listWorkerCosto = [random.random() for i in range(len(jobsCalificate))]
			print("Opcion 1")

		elif opcion == "2" and jobs is not None and jobsCalificate is not None:
			costo,solucion, tiempo = goloso(S, O, P, R, len(jobsCalificate), jobsCalificate, listWorkerCosto, iteraciones, len(jobsCalificate))
			print("Opcion 2", '\ncosto: ', costo, '\n solucion: ', solucion, '\n tiempo: ', tiempo)

		elif opcion == "3" and jobs is not None and jobsCalificate is not None:
			print(funcionObjetivoWithCost(jobsForEachWoker(entrada,len(jobsCalificate)),listWorkerCosto))
			globalCostSA, globalTimeSA, mejorSolucionGlobalSA, mejorCostoGlobalSA = simulatedAnneling(int(funcionObjetivoWithCost(jobsForEachWoker(entrada,len(jobsCalificate)),listWorkerCosto)/2),10,100,0.99,entrada,len(jobsCalificate),jobsCalificate,O,len(jobs),listWorkerCosto,1)
			print("Opcion 3")
		
		elif opcion == "4":
			print("Opcion 4")
			opcion = 4

		elif jobs is None or jobsCalificate is None:
			print("Primero debe cargar un archivo ")

		else:
			print("Ingrese una opcion valida")

		print("\n\n")

main()