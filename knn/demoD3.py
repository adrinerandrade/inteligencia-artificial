# Adriner Maranho de Andrade
# Fabio Luiz Fischer
# Jorge Guilherme Kohn

from execution import execute_scenario

print('Dados já normalizados')
execute_scenario('grupoDados3', 1)
execute_scenario('grupoDados3', 7)
execute_scenario('grupoDados3', 26)

# ---------------------------------------------------------------------------------
# Q3.1: Aplique o kNN ao problema usando k = 1. Qual é a acurácia na classificação?
#       R.: A acurácia foi de 70%
# ---------------------------------------------------------------------------------
# Q3.2: A acurácia pode ser igual a 92% com o kNN. 
#       Descubra por que o resultado atual é muito menor.
#       Ajuste o conjunto de dados ou k de tal forma que a acurácia se torne 92% e explique o que você fez e por quê.
#       R.: Os dados já estão normalizados, com isso não foi preciso ajustar os dados.
#           Ajustando o valor de k para 7, foi possível chegar a 92%, mas executando o algoritmo
#           Com k = 26, podemos chegar no máximo que é 96% de acurácia.