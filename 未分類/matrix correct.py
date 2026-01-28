import numpy as np

# ランダムな行列をQR分解して正規直交基底 Q を得る
A = np.random.randn(5, 5)
Q, R = np.linalg.qr(A)

# Q の列ベクトルは正規直交基底
# 内積を確かめてみよう
print(Q.T @ Q)  # 単位行列に近い
