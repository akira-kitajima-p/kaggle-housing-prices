from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split

def train_predict(X_train: pd.DataFrame , y_train, X_test: pd.DataFrame, model_type="lr", categorical_features=[]):
    """
    指定されたカラムを削除したデータでモデルを学習し、予測を行う
    Args:
        X_train (pd.DataFrame): 学習用の特徴量データ
        y_train (pd.Series): 学習用のラベルデータ
        X_test (pd.DataFrame): テストデータ
        model_type (str): "lr"（ロジスティック回帰）or "rf"（ランダムフォレスト）or "lgbm"（LightGBM）
        drop_columns (list): 学習前に削除するカラムのリスト
    Returns:
        np.array: 予測結果
    """

    if model_type == "lr":
        clf = LogisticRegression(penalty='l2', solver="sag", random_state=0, max_iter=10000)
    elif model_type == "rf":
        clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
    elif model_type == "lgbm":
        return lightgbm_predict(X_train, y_train, X_test, categorical_features)
    else:
        raise ValueError("model_type must be 'lr', 'rf', or 'lgbm'.")

    clf.fit(X_train, y_train)
    return clf.predict(X_test).astype(int)

def lightgbm_predict(X_train: pd.DataFrame, y_train: pd.Series, X_test: pd.DataFrame, categorical_features):
    """
    LightGBMによる学習と予測
    """
    X_train, X_valid, y_train, y_valid = train_test_split(
        X_train, y_train, test_size=0.3, random_state=0
    )

    for col in categorical_features:
        X_train[col] = X_train[col].astype('category')
        X_valid[col] = X_valid[col].astype('category')
        X_test[col] = X_test[col].astype('category')

    lgb_train = lgb.Dataset(X_train, y_train, categorical_feature=categorical_features)
    lgb_eval = lgb.Dataset(X_valid, y_valid, reference=lgb_train, categorical_feature=categorical_features)

    params = {
        'objective': 'regression',
        'metric' : 'rmse',
        'learning_rate': 0.01,
        'num_leaves': 43,
        'max_depth': -1
    }

    model = lgb.train(
        params, lgb_train,
        valid_sets=[lgb_train, lgb_eval],
        num_boost_round=1000,
        callbacks=[lgb.early_stopping(10)]
    )

    return model.predict(X_test, num_iteration=model.best_iteration)
