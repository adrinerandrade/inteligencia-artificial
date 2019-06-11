import scipy.io as scipy

from knn import doKnn

mat = scipy.loadmat('./data/grupoDados1.mat')
grupoTrain = mat['grupoTrain']
grupoTest = mat['grupoTest']
trainRotulos = mat['trainRots']
testRotulos = mat['testRots']

rotulos_previstos = doKnn(grupoTrain, trainRotulos, grupoTest, 1)
total_test = len(testRotulos)
total_corretos = 0
for i in range(total_test):
  train_rotulo = testRotulos[i][0]
  if train_rotulo == rotulos_previstos[i]:
    total_corretos += 1

print("Acurácia: {}", total_corretos / total_test)
print(rotulos_previstos)