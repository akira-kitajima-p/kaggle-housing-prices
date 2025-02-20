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
    # 数値列のみを Y の候補にする (平均・中央値などを正常に計算するため)
    numeric_cols = df.select_dtypes(include=["int", "float"]).columns
    all_cols = df.columns

    x_col = st.selectbox("X軸のカラム", all_cols)
    # "最頻値" を使う場合は文字列でも集計できるので、ここでは全列を候補にしてもOKです。
    # ただし、最大値・最小値・合計・平均・中央値をとる場合は数値列である必要があるため、
    # そうでない場合はエラーになる可能性があります。
    # 簡単な対策として、数値列から選んでほしいときは下記のようにします:
    # y_col = st.selectbox("Y軸のカラム", numeric_cols)
    # 今回はあえてすべての列を選択できるように設定。
    y_col = st.selectbox("Y軸のカラム", all_cols)

    # ==========================
    #  集計方法
    # ==========================
    agg_method = st.selectbox("集計方法", ["平均", "中央値", "最頻値", "最大値", "最小値", "合計", "なし"])

    # 集計を実行
    if agg_method != "なし":
        if agg_method == "平均":
            df_agg = df.groupby(x_col)[y_col].mean().reset_index()
        elif agg_method == "中央値":
            df_agg = df.groupby(x_col)[y_col].median().reset_index()
        elif agg_method == "最頻値":
            # value_counts() の結果が空になる場合に備えて一応対策
            df_agg = df.groupby(x_col)[y_col].agg(
                lambda x: x.value_counts().index[0] if not x.value_counts().empty else None
            ).reset_index()
        elif agg_method == "最大値":
            df_agg = df.groupby(x_col)[y_col].max().reset_index()
        elif agg_method == "最小値":
            df_agg = df.groupby(x_col)[y_col].min().reset_index()
        elif agg_method == "合計":
            df_agg = df.groupby(x_col)[y_col].sum().reset_index()
    else:
        # 集計しない場合はそのまま
        df_agg = df.copy()

    # ==========================
    #  グラフの種類
    # ==========================
    chart_type = st.selectbox("グラフの種類", ["散布図", "棒グラフ", "折れ線グラフ", "ヒートマップ"])

    # ==========================
    #  ヒートマップ用の集計設定 (デモ用)
    # ==========================
    # pivot_table で使える文字列の集計関数を dict で用意
    aggregator_map = {
        "平均": "mean",
        "中央値": "median",
        "最大値": "max",
        "最小値": "min",
        "合計": "sum"
    }
    # "最頻値" や "なし" の場合は pivot_table では直接扱いづらいので、とりあえず "mean" にしておく
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
        # 2D ヒートマップを描画したい場合は、
        #   pivot_table(index=..., columns=..., values=..., aggfunc=...)
        # という形でX軸・Y軸に別々のカラムを使うのが一般的です。
        # ここでは元のコードに合わせて単純に index=x_col, values=y_col で pivot
        df_pivot = df.pivot_table(index=x_col, values=y_col, aggfunc=pivot_aggfunc)
        # aspect="auto" でデータ量に応じてアスペクト比を調整
        fig = px.imshow(df_pivot, aspect="auto", color_continuous_scale="viridis")

    st.plotly_chart(fig)
