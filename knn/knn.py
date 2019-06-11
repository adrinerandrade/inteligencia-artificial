import math as math
import numpy as numpy

# Executa o knn a partir de dados de treinamento, os rotulos desses dados
# os dados de teste e um valor de k.
# O retorno da função é um array contendo a classificação dos elementos de teste
def do_knn(dadosTrain, rotuloTrain, dadosTeste, k):
  # Quantidade de elementos de teste
  qtdeTeste = len(dadosTeste)
  # Quantidade de elementos de treinamento
  qtdeTrain = len(dadosTrain)

  # Formação da matriz contendo a distância de cada elemento de teste com
  # os elementos de treino
  matriz_distancia = [[0 for x in range(qtdeTrain)] for y in range(qtdeTeste)]
  for i in range(len(dadosTeste)):
    matriz_distancia[i] = calc_distancia(dadosTeste[i], dadosTrain, rotuloTrain)
  
  # Monta o array contendo a classificação de cada elemento de teste em cima do index
  rotulos_previstos = [0 for x in range(len(dadosTeste))]
  for i in range(len(matriz_distancia)):
    # Ordenando a tupla contendo a distancia e a classificação para as menores distâncias
    distanciaOrdenada = sorted(matriz_distancia[i], key=lambda distancia: distancia[0])
    # Obtem somente os rótulos mais próximos
    rotulos_ordenados = list(map(lambda x: x[1], distanciaOrdenada))
    # calculando a moda para obter a classificação
    classificacao = numpy.argmax(numpy.bincount(rotulos_ordenados[0:k]))
    rotulos_previstos[i] = classificacao

  return rotulos_previstos

# Calcula a distância euclidiana entre um elemento de teste e os dados de treinamento
def calc_distancia(elem_teste, vetor_train, rotulos_train):
  distancia = [0 for i in range(len(vetor_train))]
  for i in range(len(vetor_train)):
    distancia_elemento = numpy.subtract(elem_teste, vetor_train[i])
    distancia_calc = math.sqrt(numpy.sum(numpy.power(distancia_elemento, 2)))
    # Já armazena qual o rotulo do elemento para ser possível recuperar posteriormente
    # na ordenação das distâncias e pegar os vizinhos mais próximos
    distancia[i] = (distancia_calc, rotulos_train[i][0])
  return distancia