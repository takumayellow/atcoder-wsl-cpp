---
name: solve-retro
description: 問題を解いた過程を、録画の独り言・vim の undo の履歴（変更ごとのコードと時刻）・tmux ペインに残った実行の記録・Claude との会話から再構成し、軌跡（trajectory.md）・発言録（minutes.md）・振り返りページ（retrospective.html）にまとめる。「解いた過程を振り返りたい」「録画から振り返り作って」「どこで詰まったかまとめて」「議事録から流れを整理して」等で使う。解く前に「録画して解く」準備を聞かれたときもこれ
---

# solve-retro

1 問を解いた過程を、**何を考えて、どこで詰まり、どう抜けたか**が後から読める形にする。
画面だけを見ず、**独り言（録画の音声）から考えの流れを取る**のが中心。
完成形の例は ICPC 練習 JAG 2026 C「有給」の回で、`~/dev/icpc-team-2026/contest/2026/JAG/c/` にある
（`trajectory.md` `minutes.md` `retrospective.html`）。迷ったらこれを写して直す。
icpc-team-2026 は非公開、このリポジトリは公開なので、例をこちらに写してコミットしない。

解法そのものの解説（explanation.md・スライド）は `/atcoder-explain` が作る。このスキルは**過程**を扱い、解説へはリンクで繋ぐ。

## 材料と、それぞれから取るもの

| 材料 | 取れるもの | 道具 |
|------|-----------|------|
| 録画の音声（独り言） | 考えていたこと・迷い・気づいた瞬間 | `tools/retro/transcribe_rec.py` |
| vim の undo の履歴 | 変更ごと（1 回の入力・1 つのコマンドごと）のコードと秒単位の時刻。保存しなかった途中の変更も入る | `tools/retro/undo_versions.py` |
| 解いた tmux ペインのスクロールバック | 打ったコマンドと出力（デバッグ表示・サンプルの結果）が順番どおり全部 | `tmux capture-pane`（手順 1） |
| 録画の画面 | 見ていたもの（問題文・解説・図） | `tools/retro/frames.py` |
| Claude Code の会話ログ | 何を聞き、何と答えられたか | `tools/retro/claude_log.py` |
| `.snap/`（あれば） | 保存ごと・テストごとのソース | `actest`（自動）/ `tools/retro/watch_src.py`（任意） |
| 途中の版 × 愚直解 | 各版が何件落ちるか、最初の反例 | `tools/retro/verify_versions.py` |

**コードと時刻は undo の履歴、考えは独り言、実行の結果はスクロールバック**から取る。
undo の履歴と独り言はどちらも時刻つきなので、時刻で並べるだけで「この 1 行を書き換えたとき何を言っていたか」が対応する。
スクロールバックには時刻が無いので、実行の直前の保存（`changes.txt` の「保存N」）と出力の内容で位置を合わせる。
コードを録画の画面から読み起こすのは、undo の履歴が無いときだけにする（手間も誤りも多い）。

## 解く前（ユーザーに勧めること）

1. **OBS で録画して、考えを声に出しながら解く。** 独り言が一番の材料。黙って解くと「なぜその行を書き換えたか」が残らない。
2. **マイクを別トラックにする**（一度設定すれば以後ずっと効く。OBS の設定変更はユーザーに確認してから）:
   - 設定 → 出力 → 出力モード「詳細」→ 録画タブの「音声トラック」で 1 と 2 にチェック
   - 音声ミキサーの歯車 →「オーディオの詳細プロパティ」で、デスクトップ音声はトラック 1 だけ、マイクはトラック 1 と 2
   - するとトラック 2（`--track 1`）がマイクだけになり、声の分離（`--separate`）が要らなくなる
   - マイクの入力が小さいと拾い漏れる。フィルタの「ゲイン」で +10 dB ほど上げる
3. 録画のファイル名は OBS の既定（`2026-09-30 19-21-27.mp4`）のままにする。開始時刻をここから読む。
4. **解いた tmux ペインは、振り返りが済むまで閉じない。** スクロールバックはペインを閉じると消える
   （`clear` では消えない。保持は `history-limit 100000` 行）。
5. **コードは vim で書く。** undo の履歴は dotfiles の `_vimrc` で `~/.vim/undo/` に残るので、ほかの準備は要らない。
   vim の外（Claude の Edit・別のエディタ）で同じファイルを書き換えると、そのファイルの履歴は読めなくなる。
   解いている途中で Claude に直させたいときは、別のファイルに書かせる。

保存ごとの版まで確実に残したい回だけ、裏のウィンドウで `watch_src.py` を動かしてもよい（`.snap/<日時>_save-<名前>` が残る）:
`tmux new-window -d -n snap "python3 /mnt/c/Users/takum/dev/atcoder/atcoder-wsl-cpp/tools/retro/watch_src.py '$PWD'"`、
終わったら `tmux kill-window -t snap`。

## 解いた後の手順

作業ファイル（TSV・コマ画像・音声）はすべて scratchpad に置き、**リポジトリに入れない**。

### 1. 材料を集める

- 録画: `ls -t ~/Videos/*.mp4`。解いた時間帯のものを特定し、`ffprobe` で長さとトラック数を見る。
- 解いたペイン: 今いる場所か、スクロールバックに問題フォルダが出てくるペインを探して、丸ごと scratchpad に書き出す。
  Git Bash の `tmux` は `wsl.exe tmux` で、`-F '#{pane_id}'` のような書式だけの引数は壊れるので、`id=` を前に付けて剥がす:

  ```bash
  DIR=contest/2026/JAG/c        # 問題フォルダのパスの一部
  for p in $(tmux list-panes -a -F 'id=#{pane_id}' | sed 's/^id=//'); do
    n=$(tmux capture-pane -p -J -S - -t "$p" | grep -c "$DIR")
    [ "$n" -gt 0 ] && echo "$p $n"
  done                                                   # ヒット数の多いペインが本命
  tmux capture-pane -p -J -S - -t <ペイン> > <scratchpad>/retro/pane.txt
  ```

  `<プロンプト>$ python3 main.py < input.txt` の行で区切ると、試行ごとの出力の列になる。
  デバッグ表示（`l=-1,r=0のときcountの値は0` など）は、そのとき何を疑っていたかの証拠になる。
- コードの変更: 解いたファイルごとに、編集した環境（WSL）の `python3` で取り出す:

  ```bash
  python3 /mnt/c/Users/takum/dev/atcoder/atcoder-wsl-cpp/tools/retro/undo_versions.py main.py --out <scratchpad>/retro
  ```

  `changes.txt` に「時刻・番号・保存したか・差分の行」が変更ごとに並び、各変更の直後の中身が
  `<日時>_u<番号>[_s<保存番号>].py` で残る。「履歴がありません」と出たら、`.snap/` か録画の画面から版を読む
  （全部は読まず、スクロールバックで出力が変わった所の前後に絞る）。
- Claude との会話:

  ```bash
  py -3.13 tools/retro/claude_log.py --since "2026-09-30 19:00" --until "2026-10-01 00:00" --cwd atcoder-wsl-cpp
  ```

### 2. 独り言を文字起こしする（Groq Whisper）

```bash
py -3.13 tools/retro/transcribe_rec.py "C:/Users/takum/Videos/<録画>.mp4" --out <scratchpad>/retro --track 1   # マイクが別トラックのとき
py -3.13 tools/retro/transcribe_rec.py "C:/Users/takum/Videos/<録画>.mp4" --out <scratchpad>/retro --separate  # 混ざっているとき
```

- GROQ_API_KEY は `~/dev/tus-tools/.env` から読む。**キーを表示・コミットしない。**
- 出力は 1 行 1 発話の TSV（時刻 / 秒数 / no_speech_prob / 本文）。途中で止まっても同じコマンドで続きから再開する。
- 拾い漏れが多ければ `--vad-threshold 0.3`。区間だけやり直すなら `--from 23:40 --to 23:50`。
- 処理の速さの目安: 2 分ぶんが 30 秒ほど（`--separate` 込み）。
- 誤認識は文脈で直してから引用する。前回の例: 「サタン／ウタン」→ 左端／右端、「アンス」→ ans、「半壊区間」→ 半開区間、「ワイルループ」→ while ループ。

### 3. 画面を確かめる（必要な所だけ）

```bash
py -3.13 tools/retro/frames.py "<録画>.mp4" --out <scratchpad>/retro --every 60                       # 全体を粗く
py -3.13 tools/retro/frames.py "<録画>.mp4" --out <scratchpad>/retro --from 23:44 --to 23:48 --every 5  # 気になる区間
```

一覧画像（`sheet_*.jpg`）を Read で見る。各コマに実時刻が入っている。
独り言が「これ」「ここ」と指しているものを特定するのに使う。

### 4. 年表を作る

時刻はどれも日本時間にそろっている（録画名・`changes.txt`・`.snap` の名前・`claude_log.py` の出力）。
スクロールバックの各実行は、その直前の保存の時刻に置く（迷ったら録画の画面で同じ出力が映ったコマを見る）。
発言・実行・版・会話を 1 本の時刻順に並べ、**考えが切り替わった所**で段階に区切る
（方針を決めた／サンプルが通った／ランダム比較で崩れた／書き直した／解説を読んだ、など）。

### 5. 途中の版を検証する

意味のある版（各段階の最後・バグを入れた版・直した版）を `undo_versions.py` の出力（無ければ `.snap/` か画面）から選び、
`<問題フォルダ>/history/NN_<何をした版か>.<拡張子>` に写す（`.snap/` はコミットしないので、残す版はここに入れる）。

愚直解と入力の生成を `gen.py`（scratchpad）に書き、全版をまとめて突き合わせる:

```python
# gen.py
import itertools
def cases():                      # 小さい入力の全通り（またはランダム）
    for n in range(1, 8):
        for t in itertools.product("o_x", repeat=n):
            for k in range(n + 1):
                yield f"{n} {k}\n{''.join(t)}\n"
def solve(inp):                   # 愚直解。正しさが自明な書き方にする
    ...
```

```bash
py -3.13 tools/retro/verify_versions.py --gen <scratchpad>/gen.py history/*.py main.py
```

「不一致 9454 / 24603、最初の反例 `2 0 / _o` → 正解 1 / この版 0」のような行が出る。
この数字と反例を軌跡とページにそのまま使う。C++ の版は 1 件ずつ別プロセスなので遅い（1 件 20ms ほど）。`--limit` で絞る。

### 6. 書く（`<問題フォルダ>/` に置く）

- **`trajectory.md`（軌跡）**: 冒頭に全体の流れの表 → 段階ごとの節（時刻の範囲を見出しに入れる）→
  詰まり方の型 → つまずいたバグ（版・症状・最初の反例・直し方）→ 分かったこと → ファイルとの対応 → 残っていること。
  例は JAG C の `trajectory.md`。
- **`minutes.md`（発言録）**: 独り言の引用を話題ごとに時刻つきで並べる。「そのときの画面」を添える。
  引用は聞き取りを直したものと断り、補った語は〔 〕で示す。例は JAG C の `minutes.md`。
- 段階の区切りと「詰まり方の型」は、独り言の中の迷い（「なんで continue なんだろう」「あれ？」）を根拠にする。
  画面の変化だけで推測しない。

### 7. 振り返りページを作る（`retrospective.html`）

`artifact-design` スキルを読んでから書く。構成は JAG C の `retrospective.html` に合わせる:

- 時刻の物差し（段階を色分けし、長さを実時間に比例させる）
- 段階ごとの節（独り言の引用を時刻つきで、そのときの版と結果）
- 版の見比べ（タブで版を切り替え、バグの行を強調し、不一致件数を出す）
- つまずいたバグの表、詰まり方の型、次にやること

同じ問題の解説ページ（`/atcoder-explain` の出力や、別に公開した解説の Artifact）があれば、互いにリンクする。
Artifact として公開し（アイコンは `timeline`）、URL を `trajectory.md` の冒頭に書く。

### 8. 確かめてからコミットする

- ページと md に書いた数字（不一致件数・反例・時刻）が、手順 5 の出力・`changes.txt`・スクロールバック・TSV に一致するか見直す。
  事実と合わない記述は残さない（`report-review.md` の考え方。必要なら `report-reviewer` を回す）。
- コミットするのは `trajectory.md` `minutes.md` `retrospective.html` `history/`。
  **録画・音声・TSV・コマ画像・`.snap/` は入れない。**
- ブランチを切って PR を作り、マージする。

## 道具の置き場所

- `tools/retro/`: 上の道具と共通部品 `rectime.py`。`undo_versions.py` と任意の `watch_src.py` は WSL の `python3`（標準ライブラリだけ）で動かす。
  ほかは Windows の `py -3.13` で動かす（faster-whisper・openai・python-dotenv・soundfile・Pillow が入っている）。
  `verify_versions.py` は WSL の `python3` でも動く。
- 声の分離: `~/dev/voice-lab/.venv/Scripts/audio-separator.exe`（モデル `UVR-MDX-NET-Voc_FT`）。
  場所が変わったら `RETRO_SEPARATOR` / `RETRO_SEPARATOR_MODELS` で指定する。
- dotfiles からはジャンクション `~/dotfiles/claude/skills/solve-retro` で参照している（正本はこのリポジトリ）。
