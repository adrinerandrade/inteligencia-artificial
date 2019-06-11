import scipy.io as scipy

from knn import doKnn

mat = scipy.loadmat('./data/grupoDados1.mat')
grupoTrain = mat['grupoTrain']
grupoTest = mat['grupoTest']
testRotulos = mat['testRots']
trainRotulos = mat['trainRots']

rotulos_previstos = doKnn(grupoTrain, trainRotulos, grupoTest, 1)
print(rotulos_previstos)