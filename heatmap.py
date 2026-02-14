import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("dataset_correlation.csv", delimiter=",")
df.drop('Index', axis=1, inplace=True)
df.dropna(inplace=True)
df = df.reset_index()
df.drop('index', axis=1, inplace=True)
df_corr = df.corr(method='pearson')
sns.heatmap(df_corr, annot=True)
plt.show()