import random
import numpy as np
import copy
from time import time
from generateNeighborhood import generatingNeighborhood, jobsForEachWoker
import matplotlib.pyplot as plt

def simulatedAnneling2(Tmax, Tmin, iteracionesInternas, alpha, initial, totalWorker, LTC, O,totalJobs):
    #solucion initial aleatoria
    start_time = time()
    listWorkerCosto = [random.random() for i in range(len(LTC))]
    costos = []
    initialAux = copy.copy(initial)
    mejorCosto = funcionObjetivoWithCost(jobsForEachWoker(initial,totalWorker),listWorkerCosto)
    print("el costo es:",mejorCosto)
    print("los costos son:",listWorkerCosto)
    input()
    mejorSolucion = copy.copy(initial)
    auxiiii = 0

    while(Tmax > Tmin):

        for i in range(iteracionesInternas):
            if (auxiiii % 10) == 0 :
                print("Vamos en la itaracion: " + str(auxiiii))
            auxiiii = auxiiii + 1
            costoOld = funcionObjetivoWithCost(jobsForEachWoker(initial,totalWorker),listWorkerCosto)
            initial_prima = generatingNeighborhood(initial, LTC, totalJobs, O)
            costoNew = funcionObjetivoWithCost(jobsForEachWoker(initial_prima,totalWorker),listWorkerCosto)
            error = costoNew - costoOld

            if(error < 0):
                initial = copy.copy(initial_prima)
                if (mejorCosto > costoNew):
                    mejorCosto = costoNew
                    mejorSolucion = copy.copy(initial)
                costos.append(costoNew)
                
            elif(random.random() < np.exp(-float(error)/Tmax)):
                initial = copy.copy(initial_prima)
                costos.append(costoNew)
            else:
                costos.append(costoOld)
        
        Tmax = alpha*Tmax

    elapsed_time = time() - start_time
    print("Tiempo de respuesta: ", elapsed_time)
    print("La inicial")
    print(jobsForEachWoker(initialAux,totalWorker))
    print("La mejorada")
    print(jobsForEachWoker(mejorSolucion,totalWorker))
    print("costo")
    print(costos)
    print("Costo de la mejor slucion es: ")
    print(funcionObjetivoWithCost(jobsForEachWoker(mejorSolucion,totalWorker),listWorkerCosto))
    print("Los costos de los trabajdores ")
    print(listWorkerCosto)

    plt.plot(costos)
    plt.ylabel("Costos")
    plt.xlabel("Iteracion")
    plt.show()

def funcionObjetivoWithCost(workersWithJobs,costoWork):
    result = 0
    aux = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0:
            result = result + len(listElement)*costoWork[aux]
        aux = aux + 1
    return result

def funcionObjetivoWithoutCost(workersWithJobs, LTC):
    result = 0
    aux = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0: # [ [3] , []]
            result = result + (1/len(LTC[aux]))
        aux = aux + 1
    return result


def simulatedAnneling(Tmax, Tmin, iteracionesInternas, alpha, initial, totalWorker, LTC, O,totalJobs):
    #solucion initial aleatoria
    start_time = time()

    costos = []
    initialStart = copy.copy(initial)
    mejorCosto = funcionObjetivoWithoutCost(jobsForEachWoker(initial,totalWorker),LTC)
    print("el costo es:",mejorCosto)
    input()
    mejorSolucion = copy.copy(initial)
    auxiiii = 0
    while(Tmax > Tmin):

        for i in range(iteracionesInternas):
            if (auxiiii % 100) == 0 :
                print("Vamos en la itaracion: " + str(auxiiii))

            initialAux = copy.copy(initial)
            auxiiii = auxiiii + 1
            costoOld = funcionObjetivoWithoutCost(jobsForEachWoker(initial,totalWorker),LTC)
            initial_prima = generatingNeighborhood(initial, LTC, totalJobs, O)
            costoNew = funcionObjetivoWithoutCost(jobsForEachWoker(initial_prima,totalWorker),LTC)
            error = costoNew - costoOld 

            if(error < 0):
                #print(initial)
                #print(initial_prima)
                #input("")
                initial = copy.copy(initial_prima) 
                if (mejorCosto > costoNew):
                    mejorCosto = copy.copy(costoNew) 
                    mejorSolucion = copy.copy(initial)
                costos.append(costoNew)
                
            elif(random.random() < random.random()):
                #print("aca")
                #print(initial)
                #print(initial_prima)
                #input("")
                #print("********")
                initial = copy.copy(initial_prima) 
                #print(initial)
                #print(initial_prima)
                #input("")
                #print("EL costo es: " + str(costoNew))
                costos.append(costoNew)
            else: 
                costos.append(costoOld)
            
        Tmax = alpha*Tmax
    
    elapsed_time = time() - start_time
    print("Tiempo de respuesta: ", elapsed_time)
    print("La inicial")
    print(jobsForEachWoker(initialStart,totalWorker))
    print("La mejorada")
    print(jobsForEachWoker(mejorSolucion,totalWorker))
    print("Cantidad de trabajadores")
    print(costos)
    print("Cantidad de trabajdores de la mejor solucion es: ")
    print(mejorCosto)
    print("Y son: ")
    print(mejorSolucion)

    plt.plot(costos)
    plt.ylabel("Trabajdores")
    plt.xlabel("Número de Iteracion")
    plt.show()