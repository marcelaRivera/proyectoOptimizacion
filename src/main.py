from lecture import readFile



def getNumberEmployesCalificatesInJobs(jobsCalificate, jobs):
	numberEmployes = []
	cont = 0
	for e in range(jobs):
		cont = 0
		for i in jobsCalificate:
			for j in i:
				if e == int(j):
					cont = cont + 1
		numberEmployes.append(cont)
	return numberEmployes


def orderList(jobs, jobsOrder):
	hoursInit = []
	j = 0
	for i in jobs:
		print(int(i[0]))
		print(jobsOrder[j])
		print(int(i[0]) + jobsOrder[j])
		hoursInit.append(int(i[0]) + jobsOrder[j])
		j = j + 1
	hoursInit.sort()
	print(hoursInit)


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
	jobsOrder = getNumberEmployesCalificatesInJobs(jobsCalificate, len(jobs))
	print(jobsOrder)
	orderList(jobs, jobsOrder)


main()