import scipy.io as scipy
import numpy as numpy
import copy as copy

from knn import do_knn
from normalization import Normalize

# Executa um knn dado o endereço do caminho dos dados e um valor de K.
def execute_scenario(dados, k):
  mat = scipy.loadmat('./data/%s.mat' % dados)
  grupoTrain = normalize_function(copy.copy(mat['grupoTrain']), copy.copy(mat['grupoTrain']))
  grupoTest = normalize_function(copy.copy(mat['grupoTrain']), copy.copy(mat['grupoTest']))
  trainRotulos = mat['trainRots']
  testRotulos = mat['testRots']

  # Realizando a classificação dos elementos de teste
  rotulos_previstos = do_knn(grupoTrain, trainRotulos, grupoTest, k)
  # Verificando quantos elementos estão corretos com base nos rótulos dos elementos de teste
  total_test = len(testRotulos)
  total_corretos = 0
  for i in range(total_test):
    train_rotulo = testRotulos[i][0]
    if train_rotulo == rotulos_previstos[i]:
      total_corretos += 1
  print('Acurácia sendo k = %s: %s%%' % (k, (total_corretos / total_test) * 100))

# Normaliza os dados 
def normalize_function(train, dados):
  train = numpy.transpose(train)
  dados = numpy.transpose(dados)
  for i in range(len(train)):
    dados[i] = Normalize(train[i]).normalizeData(dados[i])
  return numpy.transpose(dados)