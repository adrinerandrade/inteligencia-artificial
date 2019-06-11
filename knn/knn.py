def knn(dadosTrain, rotuloTrain, dadosTeste, k):
  qtdeTeste = len(dadosTeste)
  qtdeTrain = len(dadosTrain)

  matriz_distancia = [[0 for x in range(qtdeTeste)] for y in range(qtdeTrain)]
  for i in range(len(dadosTeste)):
    matriz_distancia[i] = calc_distancia(dadosTeste[i], vetor_train)


def calc_distancia(elem_teste, vetor_train):
