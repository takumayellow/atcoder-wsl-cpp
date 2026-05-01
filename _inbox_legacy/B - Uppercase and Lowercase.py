s = input()
lower_count = sum(1 for char in s if char.islower())
upper_count = len(s) - lower_count  # 総数から小文字の数を引いて大文字の数を得る

if upper_count > lower_count:
    # 大文字が多いので小文字に変換
    result = s.upper()
else:
    # 小文字が多いか同数なので大文字に変換
    result = s.lower()

print(result)
