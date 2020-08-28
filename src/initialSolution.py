import random
from generateNeighborhood import test

#Descripcion: funcion que permite calcular la cantidad de trabajadores que pueden realizar
#el trabajo i. Con i = 0,...., cantidad de trabajos totales
#Entrada: vector que contiene los trabajos que puede realizar el trabajador i. Con i = 0,..., cantidad de trabajadores. 
#Segundo parametro corresponde a la cantidad de trabajos totales
#Salida: vector que contiene la cantidad de personas que pueden realizar el trabajo i.
#Es decir, en la posicion 0 se tiene la cantidad de personas que pueden hacer la tarea 0, pos 1 cant de personas 
#que pueden hacer la tarea 1 y asi sucesivamente
def getNumberEmployersCalificatesInJobs(jobsCalificate, jobs):
	numberEmployers = []
	cont = 0
	for e in range(jobs):
		cont = 0
		for i in jobsCalificate:
			for j in i:
				if e == int(j):
					cont = cont + 1
		numberEmployers.append(cont)
	return numberEmployers


#descripcion: permite conocer los trabajadores que pueden realizar la tarea j
#Entrada: matriz con las tareas que realiza cada trabajador, cantidad de trabajos
#Salida: matriz con los trabajadores que pueden hacer el trabajo i
def getEmployersCalificatesInJobs(jobsCalificate, jobs):
	workers = []
	for t in range(jobs):
		cont = 0
		workersAux = []
		for i in jobsCalificate:
			for j in i:
				if t == int(j):
					workersAux.append(cont)
			cont = cont + 1
		workers.append(workersAux)
	return workers

#Descripcion: vector que ordena de manera ascendente las tareas según el criterio: Sj+Pj.
#Donde Sj corresponde a la hora de inicio de la tarea j y Pj indica la cantidad de personas que pueden hacr la tarea j
#Entrada: vector con hora de inicio y fin de la tarea i. Vector con los trabajadores que pueden hacer la tarea j
#Salida: vector con trabajos ordenados segun el criterio Sj+Pj. En cada posicion del arreglo se tiene el 
#identificador de la tarea
def orderList(jobs, jobsOrder):
	hoursInitTuple = []  #vector que contiene la suma Sj+Pj, Identificdor de la tarea (j)
	hourInitIdFinal = []  #vector que contiene los identificadores ordenados de forma ascendente según Sj+Pj
	j = 0
	for i in jobs:
		hoursInitTuple.append([i + len(jobsOrder[j]), j])
		j = j + 1
	hoursInitTuple.sort(key = lambda x : x[0])
	for element in hoursInitTuple:
		hourInitIdFinal.append(element[1])
				
	return hourInitIdFinal

#Descripcion: vector que ordena de manera ascendente las tareas según el criterio: Sj+Pj.
#Donde Sj corresponde a la hora de inicio de la tarea j y Pj indica la cantidad de personas que pueden hacr la tarea j
#Entrada: vector con hora de inicio y fin de la tarea i. Vector con la cantidad de trabajadores que pueden hacer la tarea j
#Salida: vector con trabajos ordenados segun el criterio Sj+Pj. En cada posicion del arreglo se tiene el 
#identificador #de la tarea
def getHourInit(jobs):
	hourInitForJob = [] #vector con horas de inicio
	for i in jobs:
		hourInitForJob.append(int(i[0]))	
	return hourInitForJob

#Descripcion: funcion que permite construir una solucion inicial factible
#Entrada: S vector con las horas de inicio, O vector con las tareas superpuestas de j,
#P vector con los empleados calificados para trabajo j, R vector con los trabajos asignados al trabajador w
#Salida: vector con una solucion factible
def constructiveHeuristic(S, O, P, R, E):
	jobsOrders = orderList(S, P)
	jobsOrdersAux = orderList(S, P)
	jobsAux = []
	contJob = 0
	rAux = list()
	
	for i in range(E):
		rAux.append(list())

	while len(jobsOrdersAux) > 0:
		isPossible = -1 
		elementNow = jobsOrdersAux[0]
		for worker in P[elementNow]:
			if len(rAux[worker]) == 0:
				rAux[worker].append([jobsOrders[elementNow],elementNow])
				jobsOrdersAux.pop(0)
				break
			else:
				auxRandom = random.randint(0,len(P[elementNow])-1)
				worker = P[elementNow][auxRandom]
				isPossible = addingNewElement(rAux[worker],elementNow,O,jobsOrders)

				if isPossible == 1:
					rAux[worker].append([jobsOrders[elementNow],elementNow])
					jobsOrdersAux.pop(0)
					break
				else:
					listOldRAux = rAux[worker]
					listNew = []
					listNew.append(elementNow)
					jobsOrdersAux.pop(0)
					rAux[worker] = []
					rAux[worker].append([jobsOrders[elementNow],elementNow])

					for x in listOldRAux:
						isPossible = addingNewElement(rAux[worker],x[1],O,jobsOrders)
						if isPossible == 1:
							rAux[worker].append([x[0],x[1]])
						else:
							jobsOrdersAux.append(x[1])
					break
	return test(rAux,len(S))   

"""
def addingNewElementWhenHaveConflict(listOld, rAux, O,jobsOrdersAux):

	isPossible = 0
	if len(listOld) == 0:
		return 1
	for elementAux in listOld:
		isPossible = addingNewElementWithConflict(rAux,elementAux,O)
		if isPossible == 1:
			rAux.append(elementAux)
		else:
			jobsOrdersAux.append(elementAux)
	return rAux, jobsOrdersAux, 0
"""

def addingNewElement(listActual, elementToAdd,O,jobsOrders):
	isPossible = 0
	if len(listActual) == 0:
		return 1
	for job in listActual:
		isPossible = isPossibleToAdd(job,O[elementToAdd])
		if isPossible == 0:
			break
	if isPossible == 1:
		return 1
	else:
		return 0
"""
def addingNewElementWithConflict(listActual, elementToAdd,O):
	isPossible = 0
	for job in listActual:
		isPossible = isPossibleToAdd(job,O[elementToAdd])
	if isPossible == 1:
		return 1
	else:
		return 0
"""

def isPossibleToAdd(elementToAdd, listReadyToCompare):
	if elementToAdd in listReadyToCompare:
		return 0
	return 1


#Descripcion: permite obtener los trabajos superpuestos entre si
#entrada: matriz con los horarios de inicio y fin de cada trabajo
#Salida: matriz que indica para cada trabajo (fila), el conjunto de trabajos que topa con sus horarios
#y por lo tanto, el trabajador no podra tener asignada dos tareas del mismo conjunto.
#ejemplo: [[0,1,2],[3,6,7]] esto implica que un trabajador no puede tener asignada la tarea 0,1 y 2 al mismo tiempo
#tampoco se puede asignar al mismo trabajador las tareas 3,6,7. Es decir, estas tareas deben ser hechar por
#diferentes trabajadores
def constructiveO(jobs):
	C = []
	cAux = []
	verificador = 0
	for i in jobs:
		cont = 0
		cAux = []
		verificador = 0
		for j in jobs:
			if j != i:
				if int(j[0]) < int(i[1]) and int(j[1]) > int(i[0]):
					cAux.append(cont)
					verificador = 1
			cont = cont + 1
		if(verificador == 1):
			C.append(cAux)
	return C