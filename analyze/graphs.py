import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataset_df = pd.read_csv("../datas/train.csv")
dataset_df = dataset_df.drop('Id', axis=1)

# print(dataset_df.dtypes.to_string())
fig = plt.figure()

# MSSubClass
## 各値ごとに統計を出す
## 最大値順にソートして表示してみたけど平均値に影響してないしあまり特徴のある指標ではなさそう
dataset_df['MSSubClass'] = dataset_df['MSSubClass'].astype('string')
stats = dataset_df.groupby('MSSubClass')['SalePrice'].agg(['mean', 'median', 'max', 'min']).astype(int).reset_index()
print(stats)
stats.sort_values(by = 'max', ascending=True, inplace=True)
ax = fig.add_subplot(111)
ax.bar(stats["MSSubClass"], stats["median"])
# ax.bar(stats["MSSubClass"], stats["mean"])
ax.scatter(stats["MSSubClass"], stats["max"])
ax.scatter(stats["MSSubClass"], stats["min"])
plt.show()


