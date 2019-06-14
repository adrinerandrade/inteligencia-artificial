# Adriner Maranho de Andrade
# Fabio Luiz Fischer
# Jorge Guilherme Kohn

from execution import execute_scenario

print('Sem normalização')
execute_scenario('grupoDados2', 1, False, True)
print('--------------------------------')

print('Com normalização')
execute_scenario('grupoDados2', 1)
execute_scenario('grupoDados2', 3)
execute_scenario('grupoDados2', 10)

#---------------------------------------------------
# Q2.1: Aplique seu kNN a este problema. Qual é a sua acurácia de classificação? 
#
#       R.: A acurácia inicial foi de 68,3%, com k = 1.

#---------------------------------------------------
# Q2.2: A acurácia pode ser igual a 98% com o kNN. 
#       Descubra por que o resultado atual é muito menor. 
#       Ajuste o conjunto de dados ou k de tal forma que a acurácia se torne 98% e explique o que você fez e por quê

#       R.: Os dados não estão normalizados, por isso a acurácia baixa.
#           Para aumentar a acurácia os dados foram normalizados pois assim trabalhamos somente com a proporção
#           que existe entre os valores de uma mesma característica. Isso faz com que todas as características
#           tenham um mesmo valor máximo e valor mínimo, impedindo que uma característica específica domine o cálculo.
#           Executando com k = 3, chegamos a 98%, porem com k=10, podemos chegar a 100% de acurácia.
