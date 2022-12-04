from numpy import random
import numpy as np
import time

def MontyHallSimulation (N):
    NoCambia=[]
    Cambia=[]
    for i in range(0,N):
        puertaGanadora=random.choice(['Puerta 1', 'Puerta 2', 'Puerta 3'])
        primeraEleccion=random.choice(['Puerta 1', 'Puerta 2', 'Puerta 3'])
        puertaAbierta=list(set(['Puerta 1', 'Puerta 2', 'Puerta 3'])-set([primeraEleccion,puertaGanadora]))[0]
        otraPuerta=list(set(['Puerta 1', 'Puerta 2', 'Puerta 3'])-set([primeraEleccion,puertaAbierta]))[0]
        NoCambia.append(primeraEleccion==puertaGanadora)
        Cambia.append(otraPuerta==puertaGanadora)
        
    print(f'\n\
    {N:,} simulaciones realizadas \n\
    Porcentaje de ganar basado en estrategia:\n\
    Mantener eleccion: {"{:.1%}".format(sum(NoCambia)/N)}\n\
    Cambiar puerta: {"{:.1%}".format(sum(Cambia)/N)}')
            

Start_time = time.time()
MontyHallSimulation(N=100000)         
print(f'\nTiempo total:: {round(time.time()-Start_time,2)} Segundos')