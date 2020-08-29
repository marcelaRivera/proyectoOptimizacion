import random

def generatingNeighborhood(initialSolution, LTC, total, O):
	initialSolution1 = initialSolution
	listCantWorkerSelect = []
	listCantWorkerNotSelect = []
	cantWorkerSelect = random.randint(0,len(LTC)-1)
	cantWorkerNotSelect = len(LTC) - cantWorkerSelect
	
	listWorker = [i for i in range(len(LTC))]

	listCantWorkerSelect = selectWorkerEmpty(cantWorkerSelect,initialSolution,len(LTC))
	listCantWorkerNotSelect = list(set(listWorker)-set(listCantWorkerSelect))
	listJobsForEachWoker = jobsForEachWoker(initialSolution,len(LTC))
	isPossible = 0
	contItera = 0
	for worker in listCantWorkerSelect:
		for jobs in listJobsForEachWoker[worker]:
			for workerAux in listCantWorkerNotSelect:
				for jobsAux in listJobsForEachWoker[workerAux]:
					if jobs not in O[jobsAux]:
						isPossible = 1
					else:
						isPossible = 0
						break
				if isPossible == 1:
					initialSolution[jobs] = workerAux
					listJobsForEachWoker = jobsForEachWoker(initialSolution,len(LTC))
					isPossible = 0
	return initialSolution

def selectWorker(cantWorkerSelect, initialSolution, large):
	result = []
	cont = 0
	while cont < cantWorkerSelect:
		aux = random.randint(0,large-1)
		result.append(aux)
		cont = cont + 1
	return result

def selectWorkerEmpty(cantWorkerSelect, initialSolution, large):
	#input("")
	result = []
	cont = 0
	listWorker = jobsForEachWoker(initialSolution,large)
	listAuxFinal = []
	for listElement in listWorker:
		listAux = []
		listAux.append(len(listElement))
		listAux.append(cont)
		listAux.append(listElement)
		cont = cont + 1
		listAuxFinal.append(listAux)
	cont = 0
	listAuxFinal.sort(key = lambda x : x[0])
	while cont < cantWorkerSelect:
		auxRandom = random.randint(0,len(listAuxFinal)-1)
		result.append(listAuxFinal[auxRandom][1])
		cont = cont + 1
		listAuxFinal.remove(listAuxFinal[auxRandom])
	return result

def test (listEntry, total):
	initial = [-1 for i in range(total)]
	worker = 0
	for aux in listEntry:
		for jobs in aux:
			initial[jobs] = worker
		worker = worker + 1
	return initial

# Entrada: Solución inicial y cantidad de trabajadores
# Procesamiento: Se encarga de realizar la agrupacion de las tareas de cada uno de los trabajadores
# Salida: Entrega una lista de lista, en donde se identifica claramente la distintas tareas que tiene cada trabajador.

def jobsForEachWoker(listEntry,totalWoker):
	listWorker = [[] for i in range(totalWoker)]
	jobs = 0
	for aux in listEntry:
		listWorker[aux].append(jobs)
		jobs = jobs + 1
	return listWorker

def funcionObjetivo(workersWithJobs):
    result = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0:
            result = result + 1
    return result