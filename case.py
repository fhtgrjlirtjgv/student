import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')
df.info()

print(df.describe())

df['math score  '].plot(kind='hist')
plt.show()