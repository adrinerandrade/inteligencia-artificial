# Adriner Maranho de Andrade
# Fabio Luiz Fischer
# Jorge Guilherme Kohn

import scipy.io as scipy
import numpy as numpy
import copy as copy
import matplotlib.pyplot as plt

from knn import do_knn
from normalization import Normalize

# Executa um knn dado o endereço do caminho dos dados e um valor de K.
def execute_scenario(dados, k, normalizar = True):
  mat = scipy.loadmat('./data/%s.mat' % dados)
  if (normalizar):
    normalize_function(copy.copy(mat['grupoTrain']), mat['grupoTrain'], mat['grupoTest'])
  grupoTrain = mat['grupoTrain']
  grupoTest = mat['grupoTest']
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
  index,sub_plot = plt.subplots()
  sub_plot.scatter(getDadosRotulo(grupoTrain, trainRotulos, 1, 0), getDadosRotulo(grupoTrain, trainRotulos, 1, 1), c='red'  , marker='^')
  sub_plot.scatter(getDadosRotulo(grupoTrain, trainRotulos, 2, 0), getDadosRotulo(grupoTrain, trainRotulos, 2, 1), c='blue' , marker='+')
  sub_plot.scatter(getDadosRotulo(grupoTrain, trainRotulos, 3, 0), getDadosRotulo(grupoTrain, trainRotulos, 3, 1), c='green', marker='.')
  plt.show()

def getDadosRotulo(dados, rotulos, rotulo, indice):
  ret = []
  for idx in range(0, len(dados)):
    if(rotulos[idx] == rotulo):
      ret.append(dados[idx][indice])
          
  return ret

# Normaliza os dados com base no valor do train
def normalize_function(dados, train, test):
  dados = numpy.transpose(dados)
  train = numpy.transpose(train)
  test = numpy.transpose(test)
  for i in range(len(train)):
    # normaliza os dados
    normalize_instance = Normalize(dados[i])
    # normaliza os dados do train com base no train
    train[i] = normalize_instance.normalize_array(train[i])
    # normaliza os dados do test com base no train
    test[i] = normalize_instance.normalize_array(test[i])