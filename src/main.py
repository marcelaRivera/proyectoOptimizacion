from lecture import readFile



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


#Descripcion: vector que ordena de manera ascendente las tareas según el criterio: Sj+Pj.
#Donde Sj corresponde a la hora de inicio de la tarea j y Pj indica la cantidad de personas que pueden hacr la tarea j
#Entrada: vector con hora de inicio y fin de la tarea i. Vector con la cantidad de trabajadores que pueden hacer la tarea j
#Salida: vector con trabajos ordenados segun el criterio Sj+Pj. En cada posicion del arreglo se tiene el 
#identificador #de la tarea
def orderList(jobs, jobsOrder):
	hoursInitTuple = []  #vector que contiene la suma Sj+Pj, Identificdor de la tarea (j)
	hourInitId = []  #vector que contiene la suma Sj + Pj, este es el vector que se ordena de forma ascendente
	hourInitIdFinal = []  #vector que contiene los identificadores ordenados de forma ascendente según Sj+Pj
	j = 0
	for i in jobs:
		hoursInitTuple.append([int(i[0]) + jobsOrder[j], j])
		hourInitId.append(int(i[0]) + jobsOrder[j])
		j = j + 1
	hourInitId.sort()
	for i in hourInitId:
		for j in hoursInitTuple:
			if i == j[0]:
				hourInitIdFinal.append(j[1])
	print('tareas ordenadas: \n')
	print(hourInitIdFinal)
	return hourInitIdFinal

def main():

	jobs = []
	jobsCalificate = []
	jobsOrder = []
	jobs, jobsCalificate =  readFile()

	print("La cantidad de tareas es: \n")
	print(str(len(jobs)))
	print("\n")

	print("Los tiempos de los trabajos son: \n")
	print(jobs)
	print("\n")

	print("La cantidad de trabajores es: \n")
	print(str(len(jobsCalificate)))
	print("\n")

	print("Los trabajos calificados de cada trabajador son: \n")
	print(jobsCalificate)
	print("\n")
	jobsOrder = getNumberEmployersCalificatesInJobs(jobsCalificate, len(jobs))
	print('cantidad de personas aptas para la tarea i')
	print(jobsOrder)
	orderList(jobs, jobsOrder)

main()