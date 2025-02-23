import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from pretreatment import fill_nan, str2code
from pretreatment import drop_str

train = pd.read_csv('../datas/train.csv')
test = pd.read_csv('../datas/test.csv')
pred = pd.read_csv('../datas/sample_submission.csv')

# 学習データと訓練データを結合する(特徴量エンジニアリングの為)
data = pd.concat([train, test], sort=False)

data = str2code(data)

print(data.head())
data = drop_str(data)
data = fill_nan(data)
print(data.head())
print(data.isnull().sum().to_string())


# 訓練データとテストデータを前処理を行ったデータに置き換える
train = data[:len(train)]
test = data[len(train):]

# 学習データを入力値(x_train)と出力値(y_train)にわける
y_train = train['SalePrice']
X_train = train.drop('SalePrice', axis=1)
X_test = test.drop('SalePrice', axis=1)

# 学習
clf = LogisticRegression(penalty='l2', solver="sag", random_state=0, max_iter=1000)
print("LogsticRegression()")
clf.fit(X_train, y_train)
print("fit()")
pred['SalePrice'] = clf.predict(X_test)

pred.to_csv('sample_out', index=False)
