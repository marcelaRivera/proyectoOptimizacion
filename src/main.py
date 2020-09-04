from lecture import readFile, writeOutSA, writeOutGoloso, writeAnality
from initialSolution import getHourInit, constructiveO, getEmployersCalificatesInJobs, constructiveHeuristic
from generateNeighborhood import generatingNeighborhood, test
from simuleted import simulatedAnneling, funcionObjetivoWithCost,jobsForEachWoker 
from goloso import goloso
import random
import numpy as np

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
			name = "data_20_99_163_33.dat"
			#name = "data_30_25_219_66.dat" # DB 1
			#name = "data_39_45_351_66.dat" # DB 2
			#name = "data_137_245_2105_33.dat" # DB 2

			jobs, jobsCalificate =  readFile(name)
			S = getHourInit(jobs)
			O = constructiveO(jobs)
			P = getEmployersCalificatesInJobs(jobsCalificate, len(jobs))
			entrada = constructiveHeuristic(S, O, P, R, len(jobsCalificate))
			listWorkerCosto = [random.random() for i in range(len(jobsCalificate))]
			print("Opcion 1")

		elif opcion == "2" and jobs is not None and jobsCalificate is not None:
			costo, solucion, tiempo = goloso(S, O, P, R, len(jobsCalificate), jobsCalificate, listWorkerCosto, iteraciones, len(jobsCalificate))
			writeOutGoloso(costo,solucion,tiempo,name[:8] + "_Goloso")

		elif opcion == "3" and jobs is not None and jobsCalificate is not None:
			minTemp = 0.1
			iteration = 10
			alpha = 0.99
			repeat = 1
			simulatedAnneling(200,minTemp,iteration,alpha,entrada,len(jobsCalificate),jobsCalificate,O,len(jobs),listWorkerCosto,repeat)
			#print(str(costo))
			#input("")
			#globalCostSA, globalTimeSA, mejorSolucionGlobalSA, mejorCostoGlobalSA = simulatedAnneling(maxTemp,minTemp,iteration,alpha,entrada,len(jobsCalificate),jobsCalificate,O,len(jobs),listWorkerCosto,repeat)
			#writeAnality(globalCostSA,globalTimeSA,name[:8])
			#writeOutSA(globalCostSA, globalTimeSA, mejorSolucionGlobalSA, mejorCostoGlobalSA, name[:8] + str(iteration) + "_" + str(alpha) + "" + str(iteration) + "_SA")
		
		elif opcion == "4":
			print("Opcion 4")
			opcion = 4

		elif jobs is None or jobsCalificate is None:
			print("Primero debe cargar un archivo ")

		else:
			print("Ingrese una opcion valida")

		print("\n\n")

main()