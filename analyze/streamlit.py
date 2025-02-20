import streamlit as st
import pandas as pd
import plotly.express as px

# 📌 タイトル
st.title("📊 Kaggle データ可視化ツール")

# 📌 CSVアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

if uploaded_file is not None:
    # CSV読み込み
    df = pd.read_csv(uploaded_file)
    st.write("データのプレビュー:")
    st.dataframe(df.head())

    # ==========================
    #  カラム選択
    # ==========================
    all_cols = df.columns

    x_col = st.selectbox("X軸のカラム", all_cols)
    y_col = st.selectbox("Y軸のカラム", all_cols)

    # ==========================
    #  集計方法
    # ==========================
    agg_method = st.selectbox("集計方法", ["平均", "中央値", "最頻値", "最大値", "最小値", "合計", "なし"])

    # ==========================
    #  集計関数の定義
    # ==========================
    def mode_agg(x):
        """最頻値を計算する簡易関数 (空の場合は None を返す)"""
        vc = x.value_counts()
        return vc.index[0] if not vc.empty else None

    # ==========================
    #  GroupBy + Aggregation
    # ==========================
    if agg_method != "なし":
        if agg_method == "平均":
            df_agg = df.groupby(x_col, as_index=False)[y_col].mean()
        elif agg_method == "中央値":
            df_agg = df.groupby(x_col, as_index=False)[y_col].median()
        elif agg_method == "最頻値":
            df_agg = df.groupby(x_col, as_index=False)[y_col].agg(mode_agg)
        elif agg_method == "最大値":
            df_agg = df.groupby(x_col, as_index=False)[y_col].max()
        elif agg_method == "最小値":
            df_agg = df.groupby(x_col, as_index=False)[y_col].min()
        elif agg_method == "合計":
            df_agg = df.groupby(x_col, as_index=False)[y_col].sum()
    else:
        # 集計しない場合はそのまま使う
        df_agg = df.copy()

    # ==========================
    #  X軸が文字列のとき、カテゴリ名にサンプル数を付ける
    # ==========================
    # 「object」や「category」型かどうかで判定（簡易判定）
    if pd.api.types.is_object_dtype(df[x_col]) or pd.api.types.is_categorical_dtype(df[x_col]):
        # 元データ df からカテゴリのサンプル数を取得
        cat_counts = df[x_col].value_counts(dropna=False)

        # 置換用の辞書を作成: "A" -> "A (2)"
        def label_with_counts(cat):
            # cat が NaN (欠損) の場合の表示
            if pd.isna(cat):
                return f"NaN ({cat_counts[cat]})"
            else:
                return f"{cat} ({cat_counts[cat]})"

        mapping_dict = {cat: label_with_counts(cat) for cat in cat_counts.index}

        # df_agg の x_col を置換
        # agg_method="なし" の場合は単に df そのままなので注意
        # 既に groupby 済みでも x_col が残っていれば置換できる
        if x_col in df_agg.columns:
            df_agg[x_col] = df_agg[x_col].map(mapping_dict)

    # ==========================
    #  グラフの種類
    # ==========================
    chart_type = st.selectbox("グラフの種類", ["散布図", "棒グラフ", "折れ線グラフ", "ヒートマップ"])

    # ==========================
    #  ヒートマップ用の aggfunc を用意
    # ==========================
    aggregator_map = {
        "平均": "mean",
        "中央値": "median",
        "最大値": "max",
        "最小値": "min",
        "合計": "sum"
    }
    pivot_aggfunc = aggregator_map.get(agg_method, "mean")

    # ==========================
    #  グラフ描画
    # ==========================
    if chart_type == "散布図":
        fig = px.scatter(df_agg, x=x_col, y=y_col)
    elif chart_type == "棒グラフ":
        fig = px.bar(df_agg, x=x_col, y=y_col)
    elif chart_type == "折れ線グラフ":
        fig = px.line(df_agg, x=x_col, y=y_col)
    elif chart_type == "ヒートマップ":
        # 1次元の pivot_table のままでも OK
        df_pivot = df.pivot_table(index=x_col, values=y_col, aggfunc=pivot_aggfunc)
        fig = px.imshow(df_pivot, aspect="auto", color_continuous_scale="viridis")

    st.plotly_chart(fig)
