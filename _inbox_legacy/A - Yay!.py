s = input()

# 最初に 0 番目と 1 番目をチェックして、必要ならそのまま返す
if s[0] != s[1] and s[1] == s[2]:
    print(1)  # `s[0]` がユニーク
elif s[0] == s[1] and s[1] != s[2]:
    print(3)  # `s[2]` がユニーク

# 中央部分をループでチェック
else:
    for i in range(1, len(s) - 2):
        # 前後の文字と違うか確認
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            print(i + 1)  # i + 1 の位置がユニーク
            break
    else:
        # ループで何も見つからない場合は最後の文字を確認
        if s[-1] != s[-2]==s[-3]:
            print(len(s))  # 最後の文字がユニーク
        else:print(len(s)-1)