
import matplotlib.pyplot as plt

def graficoComparative(valueObjectMean,theBestObjectValue,timeMean,theBestTime,instances):
	# x = Tamaño de la instancia

	# valor objetivo medio 
	for aux in valueObjectMean:
		plt.scatter(aux,instances,label="Tiempo",s=15)
	plt.title("Valor objetivo Medio")
	plt.ylabel("Valor objetivo")
	plt.xlabel("Tamaño de la instancia")
	plt.legend(loc='best')
	plt.show()

	# Minimo valor 
	for aux in theBestObjectValue:
		plt.scatter(aux,instances,label="Tiempo",s=15)
	plt.title("Valores minimos")
	plt.ylabel("Valor objetivo mínimo")
	plt.xlabel("Tamaño de la instancia")
	plt.legend(loc='best')
	plt.show()

	# Timepos promedios
	for aux in timeMean:
		plt.scatter(aux,instances,label="Tiempo",s=15)
	plt.title("Tiempos promedio de ejecución")
	plt.ylabel("Tiempo de ejecución")
	plt.xlabel("Tamaño de la instancia")
	plt.legend(loc='best')
	plt.show()
	
	# Timepos minimos
	for aux in theBestTime:
		plt.scatter(aux,instances,label="Tiempo",s=15)
	plt.title("Tiempos mínimos de ejecución de las instancias")
	plt.ylabel("Tiempo de mínimos de ejecución")
	plt.xlabel("Tamaño de la instancia")
	plt.legend(loc='best')
	plt.show()

def graficarStatics(globalBetterSolution,globalTime,repeat):
	dateComplete = []
	for aux in range(len(globalBetterSolution)):
		listAux = []
		listAux.append(globalBetterSolution[aux])
		listAux.append(globalTime[aux])
		dateComplete.append(listAux)
	print(dateComplete)
	input("")
	dateComplete.sort(key = lambda x : x[0][len(x[0])-1])

	colors = ['black','red','gray','orange','gold','yellow','green','aqua','blue','indigo','pink']
	count = 0
	generation = list(range(1,len(globalBetterSolution[0])+1))
	indexForTime = list(range(1,repeat+1))

	#####
	for instancia in dateComplete:
		plt.scatter(generation,instancia[0],s=15)
	plt.title("Totalidad de ejecuciones")
	plt.ylabel("Cantidad de trabajadores normalizado")
	plt.xlabel("Iteraciones")
	plt.legend(loc='best')
	plt.show()


	for instancia in dateComplete[:11]:
		plt.scatter(generation,instancia[0],c=colors[count],label="Iteración" + str(count+1),s=15)
		count = count + 1
	plt.title("Los 11 mejores resultados")
	plt.ylabel("Cantidad de trabajadores normalizado")
	plt.xlabel("Iteraciones")
	plt.legend(loc='best')
	plt.show()

	count = 0
	for instancia in dateComplete[len(dateComplete[0])-13:]:
		plt.scatter(generation,instancia[0],c=colors[count],label="Iteración" + str(count+1),s=15)
		count = count + 1
	plt.title("Los 11 peores resultados")
	plt.ylabel("Cantidad de trabajadores normalizado")
	plt.xlabel("Iteraciones")
	plt.legend(loc='best')
	plt.show()

	count = 0
	for instancia in dateComplete[:3]:
		plt.scatter(generation,instancia[0],c=colors[count],label="Iteración" + str(count+1),s=15)
		count = count + 1
	plt.title("Los 3 mejores resultados")
	plt.ylabel("Cantidad de trabajadores normalizado")
	plt.xlabel("Iteraciones")
	plt.legend(loc='best')
	plt.show()

	count = 0
	for instancia in dateComplete[len(dateComplete[0])-5:]:
		plt.scatter(generation,instancia[0],c=colors[count],label="Iteración" + str(count+1),s=15)
		count = count + 1
	plt.title("Los 3 peores resultados")
	plt.ylabel("Cantidad de trabajadores normalizado")
	plt.xlabel("Iteraciones")
	plt.legend(loc='best')
	plt.show()

	auxTimeOrder = []
	for auxTime in dateComplete:
		auxTimeOrder.append(auxTime[1])
	plt.scatter(indexForTime,auxTimeOrder,label="Tiempo",s=15)
	plt.title("Tiempos de ejecución")
	plt.ylabel("Tiempo de ejecución de las instancias")
	plt.xlabel("Repetición")
	plt.legend(loc='best')
	plt.show()	
	