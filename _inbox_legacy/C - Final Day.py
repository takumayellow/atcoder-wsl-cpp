def sort_with_original_index(data):
  """
  元のラベル付きのリストをソートし、ソート後のインデックスを保持する関数。

  Args:
    data: ソート対象のリスト。

  Returns:
    ソートされたリストと元のインデックスのリストのタプルのリスト。
  """
  indexed_data = list(enumerate(data))
  sorted_data = sorted(indexed_data, key=reversed)
  return sorted_data

n,k=map(int,input().split())
l=[]
for _ in range(n):
    l.append(sum(map(int,input().split())))
l=sort_with_original_index(l)
print(l)
a=[]*n
""" for m in range(n):
    if l[k-1]-l[m]<=300:a[("Yes")
    else:print("No")
print(*a) """