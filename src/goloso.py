import random
import copy
from time import time
from generateNeighborhood import test, jobsForEachWoker
from initialSolution import orderList, addingNewElement
from simuleted import funcionObjetivoWithCost, jobsForEachWoker
#Descripcion: funcion que permite construir una solucion factible utilizando un criterio goloso
#Entrada: S vector con las horas de inicio, O vector con las tareas superpuestas de j,
#P vector con los empleados calificados para trabajo j, R vector con los trabajos asignados al trabajador w
#Salida: vector con una solucion factible
def goloso(S, O, P, R, E, LTC, listWorkerCost, repeat, totalWorker):

	jobsOrders = orderList(S, P)
	jobsOrdersAux = orderList(S, P)
	print(jobsOrders)
	costWorkersCalificates = []
	totalCostWorkersCalificatesOrder = []
	jobsAux = []
	workers = []
	costCurrent = []
	verificar = 0
	costMin = 0.0
	rAux2 = list()
	pos = 0
	globalCost = 0
	globalTime = 0
	mejorSolucionGlobal = 0

	for count in range(repeat):
		start_time = time()
		costos = []
		cantTrabajadores = 0
		jobsOrdersAux = orderList(S, P)
		rAux = list()
		for i in range(E):
			rAux.append(list())
		while len(jobsOrdersAux) > 0:
			isPossible = -1 
			contAux = 0
			verificar = -1
			elementNow = jobsOrdersAux[0]
			costWorkersCalificates = []
			rAux2 = []
			for worker in P[elementNow]:
				costWorkersCalificates.append(listWorkerCost[worker])
				rAux2.append(rAux[worker])
				workers.append(worker)
				verificar = 1
			totalCostWorkersCalificatesOrder = minCost(rAux2, costWorkersCalificates, P[elementNow])
			for worker2 in totalCostWorkersCalificatesOrder:
				if len(rAux[worker2[2]]) == 0:
					rAux[worker2[2]].append(elementNow)
					verificar = 1
					cantTrabajadores = cantTrabajadores + 1
					jobsOrdersAux.pop(0)
					break				
				else:
					isPossible = addingNewElement(rAux[worker2[2]],elementNow,O,jobsOrders)
					if isPossible == 1:
						rAux[worker2[2]].append(elementNow)
						jobsOrdersAux.pop(0)
						verificar = 1
						break
					else:
						verificar = 0
			if verificar == 0:
				print('trabajo sin asignar', elementNow)

		globalTime = time() - start_time
		mejorSolucionGlobal = test(rAux, len(S))
		globalCost = funcionObjetivoWithCost(jobsForEachWoker(mejorSolucionGlobal, totalWorker), listWorkerCost)
		print('r aux es del goloso: ', rAux)
	return globalCost, mejorSolucionGlobal, globalTime, cantTrabajadores
				

def minCost(workersWithJobs,costWork, workers):
    result = []
    result2 = []
    aux = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0:
        	if(costWork != 10):
        		result.append([len(listElement)*costWork[aux],aux, workers[aux]])
        else:
        	#print('aux es: ', aux)
        	result.append([costWork[aux],aux, workers[aux]])
        aux = aux + 1
    result.sort(key = lambda x : x[0])
    #for element in hoursInitTuple:
	#	hourInitIdFinal.append(element[1])
    #print('la pos es: ', pos)
    #print('la lista de costos ordenada es: ', result  )
    return result