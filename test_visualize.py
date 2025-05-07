# test_visualize.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("簡単な可視化テスト")

# CSVファイルをアップロード
uploaded_file = st.file_uploader("hs_all.csvをアップロードしてください", type="csv")

if uploaded_file is not None:
    # データを読み込む
    df = pd.read_csv(uploaded_file)
    st.success("データを読み込みました！")

    # データのプレビュー
    st.subheader("データプレビュー")
    st.dataframe(df.head())

    # 推定退職率のヒストグラムを表示する
    if "estimated_retire_rate_normalized" in df.columns:
        st.subheader("推定退職率の分布")

        fig, ax = plt.subplots()
        sns.histplot(df["estimated_retire_rate_normalized"], kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.warning("推定退職率のカラムが見つかりませんでした。")
