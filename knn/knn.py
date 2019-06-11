import math as math
import numpy as numpy

def doKnn(dadosTrain, rotuloTrain, dadosTeste, k):
  qtdeTeste = len(dadosTeste)
  qtdeTrain = len(dadosTrain)

  matriz_distancia = [[0 for x in range(qtdeTrain)] for y in range(qtdeTeste)]
  for i in range(len(dadosTeste)):
    matriz_distancia[i] = calc_distancia(dadosTeste[i], dadosTrain, rotuloTrain)
  
  rotulos_previstos = [0 for x in range(len(dadosTeste))]
  for i in range(len(matriz_distancia)):
    distanciaOrdenada = sorted(matriz_distancia[i], key=lambda distancia: distancia[0])
    rotulos_ordenados = list(map(lambda x: x[1], distanciaOrdenada))
    # calculando a moda para obter a classificação
    classificacao = numpy.argmax(numpy.bincount(rotulos_ordenados[0:k]))
    rotulos_previstos[i] = classificacao

  return rotulos_previstos

def calc_distancia(elem_teste, vetor_train, rotulos_train):
  distancia = [0 for i in range(len(vetor_train))]
  for i in range(len(vetor_train)):
    distancia_elemento = numpy.subtract(elem_teste, vetor_train[i])
    distancia_calc = math.sqrt(numpy.sum(numpy.power(distancia_elemento, 2)))
    distancia[i] = (distancia_calc, rotulos_train[i][0])
  return distancia