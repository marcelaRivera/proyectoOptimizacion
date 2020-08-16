from lecture import readFile

def main():

	jobs = []
	jobsCalificate = []

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


main()