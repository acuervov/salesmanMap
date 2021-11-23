import random
import math

# cantidadPuntos = input('escribe un numero: ') # el usuario me dice la cantidad de puntos

coordenadas = [] # arreglo donde voy a guardar las cordenadas

class Punto: # Este objeto sera el que guarda la pareja ordenada de las coordenadas
    def __init__(self, x, y, pais):
        self.x = x
        self.y = y 
        self.pais = pais
    def __repr__(self):
        return str(self.__dict__)


with open("/Users/mac/Desktop/Programacion/python/salesmanMap/puntos.txt","r") as archivo: #esto toma los puntos del archivo puntos.txt, si lo implementa es su computador tendra que ajustar  esta linea para que coincida con el path en que aloje el archivo
    for linea in archivo:
        pareja = linea.split(',')
        coordenadas.append(Punto(float(pareja[0]), float(pareja[1]), pareja[2]))

print(coordenadas)

path = coordenadas # este sera el path inicial

def generarPath (coordenadas): #Esta funcion es la que genera aleatoreamente el path; 
    parcial = coordenadas[1:len(coordenadas) -1]
    nuevo =  random.sample(parcial, len(parcial))
    return [coordenadas[0]] + nuevo + [coordenadas[len(coordenadas)-1]]

initialTemp = 100 # Este es el estado de la temperatura inicial
finalTemp = 0.2 #Este es el estado de la temperatura final
r = 0.999 # Este es el ratio de enfriamiento. 

def aRadianes (angulo):
    return angulo * (math.pi/180)
    
def distanciaPuntos (punto1,punto2):
    R = 6378 #radio de la tierra; 
    DLat = aRadianes(punto2.y - punto1.y)
    Dlon = aRadianes(punto2.x - punto1.x)
    a = ((math.sin(DLat/2)) ** 2) + (math.cos(punto1.y)*math.cos(punto2.y)*((math.sin(Dlon/2)) ** 2))
    c = 2*(math.atan2((math.sqrt(a)),(math.sqrt(1-a))))
    return c*R

def distanciaRutas (path): #Esta ruta calcula la distancia total de cada path
    sum = 0
    for ii in range(len(path)-1): 
       sum+= distanciaPuntos(path[ii], path[ii+1])
    return sum

Temp = initialTemp
distancia = 0

while Temp > finalTemp: # En este ciclo while se genera toda la magia
    newPath = generarPath(coordenadas)
    diferencia = distanciaRutas(newPath) - distanciaRutas(path)
    if (diferencia < 0 or math.exp(-diferencia/Temp) > random.uniform(0,1)):
        path = newPath
    Temp = r*Temp


for ii in path: 
    print(ii.pais)

print("distancia total: ",distanciaRutas(path))








    

