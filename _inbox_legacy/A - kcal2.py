from decimal import Decimal, getcontext, ROUND_DOWN

# 入力の読み込みと計算
a, b = map(int, input().split())
result = Decimal(a) * Decimal(b) / Decimal(100)

# 通常の表示に切り替えるための量子化
# 1桁の精度まで表示し、小数点以下のゼロを削除
formatted_result = result.quantize(Decimal('1.0000000000'), rounding=ROUND_DOWN)

# 不要なゼロや小数点を削除
print(f"{formatted_result:f}".rstrip('0').rstrip('.'))