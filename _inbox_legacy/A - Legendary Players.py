# データの文字列
data_str = """
tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481
"""

# 文字列を行ごとに分割し、各行を名前とレートに分ける
names = []
ratings = []

for line in data_str.strip().split('\n'):
    name, rating = line.split()
    names.append(name)
    ratings.append(int(rating))  # レートは整数に変換

# 名前とレートが対応するように辞書を作成する
data_dict = dict(zip(names, ratings))

# ユーザーから名前を入力してレーティングを取得
input_name = input().strip()

# レーティングを出力（名前は必ず存在する前提）
print(data_dict[input_name])
