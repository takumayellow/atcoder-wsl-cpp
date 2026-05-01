import numpy as np

# 式を計算
term1 = (5 * np.sqrt(3) - 9) / 15
term2 = (31 - 15 * np.sqrt(3)) / 45
result = 2 * (np.arctan(term1) + term2)

# 結果を表示
print(f"計算結果: {result:.4f}")
