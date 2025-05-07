import pymc as pm
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import arviz as az
import seaborn as sns

# データ作成
np.random.seed(1)
x = np.linspace(0, 1, 100)
y = 2 * x + 1 + np.random.normal(scale=0.1, size=100)

# モデル定義
with pm.Model() as model:
    a = pm.Normal('a', mu=0, sigma=10)
    b = pm.Normal('b', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=1)
    
    mu = a * x + b
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y)
    
    trace = pm.sample(1000, tune=1000, return_inferencedata=True)


# Streamlit表示
st.title("ベイズ線形回帰モデル")

# 事後分布をプロット
st.subheader("パラメータの事後分布")
fig, ax = plt.subplots(figsize=(10,5))
az.plot_posterior(trace, var_names=['a', 'b', 'sigma'], ax=ax)
st.pyplot(fig)

# トレースプロット
st.subheader("トレースプロット（サンプルの推移）")
fig2, ax2 = plt.subplots(figsize=(10,5))
az.plot_trace(trace, var_names=['a', 'b', 'sigma'], ax=ax2)
st.pyplot(fig2)

# 推定された回帰線を表示
st.subheader("データと予測回帰線")
a_mean = trace.posterior['a'].mean().item()
b_mean = trace.posterior['b'].mean().item()

fig3, ax3 = plt.subplots()
ax3.scatter(x, y, label='観測データ')
ax3.plot(x, a_mean * x + b_mean, color='red', label='推定回帰線')
ax3.legend()
st.pyplot(fig3)
