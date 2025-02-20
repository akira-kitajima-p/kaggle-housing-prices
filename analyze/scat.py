import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset_df = pd.read_csv("../datas/train.csv")
dataset_df = dataset_df.drop('Id', axis=1)
print(dataset_df.isnull().sum().to_string())

df_num = dataset_df.select_dtypes(include = ['float64', 'int64'])

for col in df_num.columns.drop('SalePrice', errors='ignore'):
    plt.figure(figsize=(6, 4))
    # 横軸に該当のカラム、縦軸にSalePriceの散布図
    sns.scatterplot(data=dataset_df, x=col, y='SalePrice')
    # 回帰線を重ねるなら regplot でも良い (散布図と同時に回帰線を表示)
    # sns.regplot(data=dataset_df, x=col, y='SalePrice', scatter=True, ci=None)
    
    plt.title(f"{col} vs. SalePrice (Scatter)")
    plt.show()
