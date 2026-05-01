S = input()  # 入力された文字列
n = len(S)  # 文字列の長さ

# 各文字のインデックスを保存する辞書
indices = {}
for idx, char in enumerate(S):
    if char not in indices:
        indices[char] = []
    indices[char].append(idx)

count = 0

# 各文字について回文を作るための組を数える
for char, idx_list in indices.items():
    # idx_list に含まれるインデックスを使用
    m = len(idx_list)
    # (i, k) の組を選ぶためのループ
    for i in range(m):
        for k in range(i + 1, m):
            # i < k なので、j の位置は idx_list[i] と idx_list[k] の間のすべてのインデックスが可能
            j_start = idx_list[i] + 1
            j_end = idx_list[k]
            if j_start < j_end:  # j が存在する範囲かチェック
                count += (j_end - j_start)  # j の選択肢の数を加算

print(count)  # 結果を出力
