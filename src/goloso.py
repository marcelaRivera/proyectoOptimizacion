import random
import copy
from generateNeighborhood import test
from initialSolution import orderList, addingNewElement

#Descripcion: funcion que permite construir una solucion factible utilizando un criterio goloso
#Entrada: S vector con las horas de inicio, O vector con las tareas superpuestas de j,
#P vector con los empleados calificados para trabajo j, R vector con los trabajos asignados al trabajador w
#Salida: vector con una solucion factible
def goloso(S, O, P, R, E, LTC):
	jobsOrders = orderList(S, P)
	jobsOrdersAux = orderList(S, P)
	print(jobsOrders)
	listWorkerCost = [random.random() for i in range(len(LTC))]
	costWorkersCalificates = []
	totalCostWorkersCalificates = []
	totalCostWorkersCalificatesOrder = []
	jobsAux = []
	workers = []
	costCurrent = []
	verificar = 0
	costMin = 0.0
	rAux = list()
	rAux2 = list()
	pos = 0
	
	for i in range(E):
		rAux.append(list())
	while len(jobsOrdersAux) > 0:
		isPossible = -1 
		contAux = 0
		verificar = -1
		elementNow = jobsOrdersAux[0]
		for worker in P[elementNow]:
			costWorkersCalificates.append(listWorkerCost[worker])
			rAux2.append(rAux[worker])
			workers.append(worker)
			#print('los trabajadores calificados son: ', P[elementNow])
			#input()
		totalCostWorkersCalificatesOrder = minCost(rAux2, costWorkersCalificates, workers)
		#print('todos los costos son: ', listWorkerCost)
		for worker in totalCostWorkersCalificatesOrder:
			if len(rAux[worker[2]]) == 0:
				rAux[worker[2]].append(elementNow)
				#print('Raux es: ', rAux)
				#input()
				jobsOrdersAux.pop(0)
				break
				
			else:
				isPossible = addingNewElement(rAux[worker[2]],elementNow,O,jobsOrders)
				if isPossible == 1:
					rAux[worker[2]].append(elementNow)
					jobsOrdersAux.pop(0)
					break
				else:
					verificar = 0

		#if verificar == 0:
		print('Raux es: ', rAux)

				

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