# Adriner Maranho de Andrade
# Fabio Luiz Fischer
# Jorge Guilherme Kohn

from execution import execute_scenario, execute_scenario_filtering_attributes

execute_scenario('grupoDados1', 1)
execute_scenario('grupoDados1', 5)
execute_scenario('grupoDados1', 10)

print()
attrs_description = ['sepal length', 'sepal width', 'petal length', 'petal width']
execute_scenario_filtering_attributes('grupoDados1', 1, [0, 1, 2], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [0, 1, 3], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [0, 2, 3], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [1, 2, 3], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [1, 2], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [1, 3], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [2, 3], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [0, 1], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [0, 2], attrs_description)
execute_scenario_filtering_attributes('grupoDados1', 1, [0, 3], attrs_description)

#---------------------------------------------------
# Q1.1. Qual é a acurácia máxima que você consegue da classificação?
#
#       R.: 96%, sendo k = 1 ou k = 5.
#---------------------------------------------------
# Q1.2. É necessário ter todas as características (atributos) para obter a acurácia máxima para esta classificação? 
#
#       R.: Não. Executando somente com as características ['sepal length', 'sepal width', 'petal width']
#           (ou em indexes [0, 1, 3]), conseguimos chegar na mesma acurácia de 96%.