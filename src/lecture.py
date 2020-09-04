def readFile(name):
	
	contJobs = -1
	contCalificate = -1
	jobs = []
	jobsCalificate = []

	file = open("../dataset/" + name, 'r')
	
	for aux in file:
		if ("Jobs" in aux):
			contJobs = int(aux.replace("Jobs","").replace(" ","").replace("=","").replace("\n",""))
		elif (contJobs > 0):
			listAux = []
			aux = aux.replace("\n","").split(" ")
			for element in aux:
				if (element.isdigit()):
					listAux.append(element)
			jobs.append(listAux)
			listAux = []
			contJobs = contJobs - 1
		elif ("Qualifications" in aux):
			contCalificate = int(aux.replace("Qualifications","").replace(" ","").replace("=","").replace("\n",""))
		elif (contCalificate > 0):
			listAux = []
			aux = aux.replace("\n","").split(":")[1].split(" ")
			for element in aux:
				if (element.isdigit()):
					listAux.append(element)
			jobsCalificate.append(listAux)
			contCalificate = contCalificate - 1
	
	return jobs , jobsCalificate

def writeOutSA(globalCost, globalTime, mejorSolucionGlobal, mejorCostoGlobal, name):
    file = open ( "Ejecución/SA/" + name + "_out.txt",'w')
    file.write("\n******************* Inicio de inserción ******************\n\n")
    file.write("Los elementos son del archivo: " + name)
    file.write("\n\nLos costos globales son: \n")
    for aux in globalCost:
        file.write(str(aux) + " ")
    file.write("\n\nLos tiempos globales son: \n\n")
    count = 1
    for aux in globalTime:
        file.write("Iteración " + str(count) + ": " + str(aux) + " \n")
        count = count + 1
    file.write("\nLa mejor solución global es: ")
    for aux in mejorSolucionGlobal:
        file.write(str(aux) + " ")
    file.write("\n\nEl mejor costo es: : ")
    file.write(str(mejorCostoGlobal) + " ")
    file.write("\n\n")
    file.write("******************* Termino de inserción ******************")
    file.write("\n")
    file.close()

def writeOutGoloso(globalCost, solution, globalTime,name):
    file = open ("Ejecución/Goloso/" + name + "_out.txt",'w')
    file.write("\n******************* Inicio de inserción ******************\n\n")
    file.write("Los elementos son del archivo: " + name)
    file.write("\n\nEl costo global es de: " + str(globalCost) + "\n")
    file.write("\n\nEl tiempo global es de:" + str(globalTime) + "\n\n")
    file.write("\nLa mejor solución global es: \n")
    for aux in solution:
        file.write(str(aux) + " ")
    file.write("\n\n")
    file.write("******************* Termino de inserción ******************")
    file.write("\n")
    file.close()

def writeAnality(globalCostSA,globalTimeSA,name):
	file = open ( "Costos/" + name + "_globlaCost.txt",'w')
	for aux in globalCostSA:
		file.write(str(aux) + " ")
	file.close()

	file = open ( "Tiempos/" + name + "_time.txt",'w')
	count = 1
	for aux in globalTimeSA:
		file.write( "Tiempos/" + "Iteración " + str(count) + ": " + str(aux))
		count = count + 1
	file.close()

"""
def writeOutCost(globalCost,name):
	file = open ( "Costos/Trabajadores/" + name + "_globlaCostWorkers.txt",'w')
	for aux in globalCost:
		file.write(str(aux) + " ")
	file.close()
"""