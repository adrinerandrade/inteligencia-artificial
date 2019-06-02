import matplotlib.pyplot as plt
from dataset import Dataset
from correlation import Correlation

selected_datase = int(input('Informe o dataset:'))
data = Dataset(selected_datase).get_dataset()
correlation_value = Correlation(data).calc()
print('Correlação')
print(correlation_value)
plt.scatter(data[0], data[1])
plt.show()