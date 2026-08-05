import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('pokemon.csv')
data.plot(kind='scatter', x='Attack', y='Defense', alpha=0.5, color='red')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.show()