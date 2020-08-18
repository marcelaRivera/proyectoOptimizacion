import random

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
#identificador #de la tarea
def orderList(jobs, jobsOrder):
	hoursInitTuple = []  #vector que contiene la suma Sj+Pj, Identificdor de la tarea (j)
	hourInitId = []  #vector que contiene la suma Sj + Pj, este es el vector que se ordena de forma ascendente
	hourInitIdFinal = []  #vector que contiene los identificadores ordenados de forma ascendente según Sj+Pj
	j = 0
	for i in jobs:
		hoursInitTuple.append([i + len(jobsOrder[j]), j, i, len(jobsOrder[j])])
		hourInitId.append(i + len(jobsOrder[j]))
		j = j + 1
	hourInitId.sort()
	for i in hourInitId:
		for j in hoursInitTuple:
			if i == j[0] and (i-j[3]) == j[2]:
				if j[1] not in hourInitIdFinal:
					hourInitIdFinal.append(j[1])
				
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
def constructiveHeuristic(S, O, P, R):
	jobsOrders = orderList(S, P)
	jobsOrdersAux = orderList(S, P)
	jobsAux = []
	print('lista ordenada', jobsOrders)
	contJob = 0
	rAux = list()
	for i in range(len(P)):
		rAux.append(list())
	#print('P es: ', P)
	#print('O es: ', O)
	while len(jobsOrdersAux) > 0:
		jobsOrdersAux.pop(0)
		sePuede = -1
		for worker in P[jobsOrders[contJob]]:
			if len(rAux[worker]) == 0:
				rAux[worker].append(jobsOrders[contJob])
				sePuede = 1
				break
			else:
				for worker2 in rAux[worker]:
					if worker2 not in O[jobsOrders[contJob]]:
						sePuede = 1	
					else:
						sePuede = 0
						break
				if sePuede == 1:
					rAux[worker].append(jobsOrders[contJob])
					break
		print('RAUX ES: ', rAux)
		if sePuede == 0:
			jobsAux.append(jobsOrders[contJob])
			employerRandom = random.randrange(len(P[jobsOrders[contJob]]))
			print(employerRandom)
		


			#if jobsOrders[contJob] not in rAux[worker] and worker in P[jobsOrders[contJob]]:
				#print('entro aca?')
			#	if len(rAux[worker]) == 0:
					#print('el job es:', jobsOrders[contJob])
					#print('O es:', O[jobsOrders[contJob]])
			#		rAux[worker].append(jobsOrders[contJob])
					#print('R1 es', rAux)
			#		break
			#	else:
					#print('el job es:', jobsOrders[contJob])
					#print('O es:', O[jobsOrders[contJob]])
			#		for job in rAux[worker]:
			#			if jobsOrders[contJob] not in O[worker]:
			#				rAux[worker].append(jobsOrders[contJob])
						#print('R2 es ', rAux, 'cont es:', contJob)
			#				break
		
		contJob = contJob + 1
		
		#print(rAux)
	


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