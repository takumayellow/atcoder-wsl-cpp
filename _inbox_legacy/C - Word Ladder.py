from collections import deque

def find_min_operations(S, T):
    n = len(S)
    
    # 初期設定
    queue = deque([(S, [S])])  # (現在の文字列, 現在までの配列X)
    visited = set()
    visited.add(S)
    
    while queue:
        current, path = queue.popleft()
        
        if current == T:
            return path
        
        # 現在の文字列から1文字を変更して次の文字列を生成
        next_strings = []
        for i in range(n):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if current[i] != c:
                    next_str = current[:i] + c + current[i+1:]
                    if next_str not in visited:
                        next_strings.append(next_str)
        
        # 辞書順でソートしてから追加する
        next_strings.sort()
        for next_str in next_strings:
            visited.add(next_str)
            queue.append((next_str, path + [next_str]))
    
    return []

# 入力の受け取り
S = input().strip()
T = input().strip()

# 結果の取得
result = find_min_operations(S, T)

# 出力
print(len(result))
for s in result:
    print(s)