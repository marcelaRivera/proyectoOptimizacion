def readFile():
	
	contJobs = -1
	contCalificate = -1
	jobs = []
	jobsCalificate = []

	#file = open("../dataset/data_1_23_40_66.dat", 'r')
	file = open("../dataset/data_21_93_175_33.dat", 'r')
	#file = open("../dataset/data_124_198_1383_33.dat", 'r')
	
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