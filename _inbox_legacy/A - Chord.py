s = input().strip()
valid_chords = {"ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"}

# `s` が `valid_chords` のいずれかに含まれているかチェック
if s in valid_chords:
    print('Yes')
else:
    print('No')  # `s` がいずれにも一致しない場合は空文字を出力