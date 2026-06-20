# ICPC 国内予選 入力テンプレート

## 要点

ICPC 国内予選は **AtCoder と違い「1ファイルに複数データセットが連結」** されている。
1本のプログラムが全データセットをループ処理し、各データセットを1行ずつ出力する。

- 単発の `n = int(input())` だけだと**最初のデータセットしか処理されず WA**。必ずループ。
- 終端は問題ごとに違うので Input を必ず読む。**最頻出は「先頭の値が 0」で終端**
  （終端行は `0` / `0 0` / `0 0 0` … データセット先頭行の整数の個数に一致）。
- 入力は `input()` で素直に読めば十分（AtCoder と同じ感覚。`sys.stdin` のトークン読みは不要）。

## 雛形（`main.py` / `main.cpp`）

書き換えるのは **「先頭の読み方」と「番兵の条件」の2か所だけ**。

```python
while True:
    n = int(input())     # 先頭を読む
    if n == 0: break     # 番兵
    ...
    print(ans)           # 1データセット=1行
```

### よくある変種

| 入力の形 | 先頭の読み方 | 番兵 |
|---|---|---|
| 単一値・0終端（最頻出） | `n = int(input())` | `if n == 0: break` |
| 先頭が複数値・"0 0.." 終端 | `a, b, s = map(int, input().split())` | `if a == b == s == 0: break` |
| 個数T先頭・番兵なし | `for _ in range(int(input())):` | （ループ回数で制御） |

1行に n 個並ぶ行は `a = list(map(int, input().split()))`。

## 起動

`tools/icpc <year> <problem> [py|cpp]` で `icpc/practice/<year>/<problem>/` を作成し、
この雛形を `main.py`（または `main.cpp`）としてコピー、自動 `cd`＋エディタで開く。

## 補足

- Python は NumPy 不可前提（素の Python3）。
- C++ で ACL を使うなら `library/cpp/` の該当ヘッダを貼り付ける。
- ローカルテスト: bash/WSL は `python main.py < input.txt`、
  PowerShell は `Get-Content input.txt | python main.py`（PowerShell は `<` 不可）。
