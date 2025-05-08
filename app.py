# test_visualize.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib  # 日本語表示対応

st.title("データ可視化アプリ")

# CSVファイルをアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type="csv")

if uploaded_file is not None:
    # データを読み込む
    df = pd.read_csv(uploaded_file)
    st.success("データを読み込みました！")

    # データのプレビュー
    st.subheader("データプレビュー")
    st.dataframe(df.head())

    # 数値データを含む列を抽出
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if numeric_columns:
        st.subheader("データ分布の可視化")
        
        # ユーザーに可視化する列を選択させる
        selected_column = st.selectbox("可視化する列を選択してください", numeric_columns)
        
        # 選択された列の基本統計量を表示
        st.write(f"**{selected_column}の基本統計量**")
        st.write(df[selected_column].describe())
        
        # ヒストグラムを表示
        st.write(f"**{selected_column}の分布**")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(df[selected_column], kde=True, ax=ax)
        plt.title(f"{selected_column}の分布")
        plt.xlabel(selected_column)
        plt.ylabel("頻度")
        st.pyplot(fig)
        
        # 箱ひげ図を表示
        st.write(f"**{selected_column}の箱ひげ図**")
        fig, ax = plt.subplots(figsize=(10, 4))
        sns.boxplot(x=df[selected_column], ax=ax)
        plt.title(f"{selected_column}の箱ひげ図")
        st.pyplot(fig)
    else:
        st.warning("数値データを含む列が見つかりませんでした。")
