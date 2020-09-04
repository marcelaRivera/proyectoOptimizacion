import random
import numpy as np
import copy
from time import time
from grafico import graficarStatics
from generateNeighborhood import generatingNeighborhood, jobsForEachWoker
import matplotlib.pyplot as plt
import math

def simulatedAnneling(Tmax, Tmin, iteracionesInternas, alpha, initial, totalWorker, LTC, O,totalJobs,costWorks,repeat):
    
    globalCost = []
    globalTime = []
    mejorSolucionGlobal = []
    mejorCostoGlobal = None

    for count in range(repeat):
        #solucion initial aleatoria
        start_time = time()
        costos = []
        listWorkerCosto = copy.copy(costWorks)
        mejorCostoGlobal = funcionObjetivoWithoutCost(jobsForEachWoker(initial,totalWorker),O)
        mejorCosto = funcionObjetivoWithoutCost(jobsForEachWoker(initial,totalWorker),O)
        costoActual = funcionObjetivoWithoutCost(jobsForEachWoker(initial,totalWorker),O)
        mejorSolucion = copy.copy(initial)
        actualSolucion = copy.copy(initial)
        mejorSolucionGlobal = copy.copy(initial)
        Tact = copy.copy(Tmax)
        count = 0
        while(Tact > Tmin):
            if count % 10 == 0:
                print(count)
            count = count + 1
            for i in range(iteracionesInternas):
                initial_prima = copy.copy(generatingNeighborhood(actualSolucion, LTC, totalJobs, O))
                #costoNew = copy.copy(funcionObjetivoWithCost(jobsForEachWoker(initial_prima,totalWorker),listWorkerCosto))
                costoNew = copy.copy(funcionObjetivoWithoutCost(jobsForEachWoker(initial,totalWorker),O))
                error = costoNew - costoActual
                if error < 0:
                    costoActual = copy.copy(costoNew)
                    actualSolucion = copy.copy(initial_prima)
                    if (mejorCosto > costoNew):
                        mejorSolucionGlobal = copy.copy(initial_prima)
                        mejorCostoGlobal = copy.copy(costoNew)
                        mejorCosto = copy.copy(costoNew)
                        mejorSolucion = copy.copy(initial_prima)
                elif random.random() < (math.e**(-(error)/Tact)):
                    costoActual = copy.copy(costoNew)
                    actualSolucion = copy.copy(initial_prima)
                costos.append(costoActual)
            Tact = alpha*Tact
        elapsed_time = time() - start_time
        globalCost.append(costos)
        globalTime.append(elapsed_time)
    print(mejorSolucionGlobal)
    print("\n")
    aux1 = jobsForEachWoker(initial,totalWorker)
    print(aux1)
    print("La cantidad de trabajadores es: ")
    print(str(funcionObjetivoWithoutCostFinal(aux1)))
    input("")
    graficarStatics(globalCost,globalTime,repeat)
    return globalCost, globalTime, mejorSolucionGlobal, mejorCostoGlobal

def funcionObjetivoWithCost(workersWithJobs,costoWork):
    result = 0
    aux = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0:
            result = result + len(listElement)*costoWork[aux]
        aux = aux + 1
    return result


def funcionObjetivoWithoutCostFinal(workersWithJobs):
    result = 0
    aux = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0:
            result = result + 1
        aux = aux + 1
    return result

def funcionObjetivoWithoutCost(workersWithJobs, O):
    result = 0
    aux = 0
    for listElement in workersWithJobs:
        if len(listElement) != 0:
            result = result + (len(listElement)/len(O[aux]))
        aux = aux + 1
    return result
"""

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
"""