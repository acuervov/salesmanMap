import random
import math


# cantidadPuntos = input('escribe un numero: ') # el usuario me dice la cantidad de puntos

coordenadas = [] # arreglo donde voy a guardar las cordenadas

class Punto: # Este objeto sera el que guarda la pareja ordenada de las coordenadas
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    def __repr__(self):
        return str(self.__dict__)


with open("/Users/mac/Desktop/Programacion/python/salesmanMap/puntos.txt","r") as archivo:
    for linea in archivo:
        pareja = linea.split(',')
        coordenadas.append(Punto(int(pareja[0]), int(pareja[1])))

print(coordenadas)


path = coordenadas # este sera el path inicial

def generarPath (coordenadas):
    parcial = coordenadas[1:len(coordenadas) -1]
    nuevo =  random.sample(parcial, len(parcial))
    return [coordenadas[0]] + nuevo + [coordenadas[len(coordenadas)-1]]

initialTemp = 100
finalTemp = 0.2
r = 0.9

def distanciaRutas (path):
    sum = 0
    for ii in range(len(path)-1): 
       xSum = math.pow((path[ii+1].x)-(path[ii].x),2)
       ySum = math.pow((path[ii+1].y)-(path[ii].y),2)
       sum+= math.sqrt(xSum+ySum)
    return sum

Temp = initialTemp
distancia = 0

while Temp > finalTemp:
    newPath = generarPath(coordenadas)
    diferencia = distanciaRutas(newPath) - distanciaRutas(path)
    if (diferencia < 0 or math.exp(-diferencia/Temp) > random.uniform(0,1)):
        path = newPath
    Temp = r*Temp


for ii in path: 
    print(ii.x,ii.y)









    

