import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset_df = pd.read_csv("../datas/train.csv")
dataset_df = dataset_df.drop('Id', axis=1)
print(dataset_df.isnull().sum().to_string())

df_num = dataset_df.select_dtypes(include = ['float64', 'int64'])
print(df_num.head())
# 各データの分布の表示
df_num.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8);
plt.show()

