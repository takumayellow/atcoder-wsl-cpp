"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
// ============================================================
// import 文: 他のモジュール（ここでは Node.js 標準の "fs" = File System）を読み込む。
// `import * as fs from "fs"` は「"fs" モジュールが export しているもの全部を
// `fs` という名前のオブジイクトにまとめて import する」という書き方（namespace import）。
// これにより fs.readFileSync のように「名前空間.関数名」の形で呼び出せる。
// ============================================================
const fs = __importStar(require("fs"));
// ------------------------------------------------------------
// fs.readFileSync(fd, encoding)
//   - 第1引数 0 は「ファイルディスクリプタ 0」＝標準入力(stdin)を表す特別な数値。
//     （1=標準出力, 2=標準エラー出力 という OS 共通の約束事。0 を渡すと
//      「ファイルではなく標準入力から同期的に全部読む」という意味になる）
//   - 第2引数 "utf-8" はエンコーディング指定。これを付けないと Buffer 型（バイト列）が
//     返るが、"utf-8" を指定すると最初から string 型で返ってくる。
//   - readFileSync は「同期」関数なので、読み終わるまで次の行に進まない
//     （非同期の readFile と違い await/コールバック不要でそのまま使える）。
//
// .trim() : String.prototype のメソッド。文字列の「先頭と末尾」の空白文字
//   （スペース・タブ・改行など）を取り除いた新しい文字列を返す（元の文字列は変更しない＝
//   イミュータブル）。入力末尾の改行コードを消すためによく使う。
//
// .split(区切り) : 文字列をある基準で分割して配列にするメソッド。
//   ここでは区切りに正規表現リテラル /\s+/ を渡している。
//     - `/ ... /` はスラッシュで囲んだ正規表現リテラルの書き方。
//     - `\s` は「空白文字1つ」（スペース・タブ・改行など）を表すメタ文字。
//     - `+` は直前のパターン（\s）の「1回以上の繰り返し」を表す量指定子。
//   つまり /\s+/ は「1文字以上連続する空白のかたまり」にマッチする正規表現で、
//   これで区切ることで「改行区切り」でも「スペース区切り」でも「両方混在」でも
//   一律にトークン単位へバラせる。
//
// メソッドチェーン: readFileSync(...).trim().split(...) のように、ある関数/メソッドの
//   戻り値に対してすぐ次のメソッドを "." でつなげて呼び出す書き方。
//   1. readFileSync が返した string に対して
//   2. .trim() を呼んでまた string を受け取り
//   3. その string に .split() を呼んで string[] を得る
//   という流れが1行で表現されている。
//
// const tokens = ... : `const` は再代入不可の変数宣言。tokens という名前に
//   string[]（文字列の配列）が束縛される。型注釈を書いていないが、TypeScript の
//   型推論により右辺の型（string[]）が自動的に tokens の型になる。
const tokens = fs.readFileSync(0, "utf-8").trim().split(/\s+/);
// let ptr = 0;
//   `let` は再代入可能な変数宣言（`const` と違い後で ptr = ... で書き換えられる）。
//   型注釈なしだが、初期値 0 (number) から型推論されて ptr: number 扱いになる。
//   tokens 配列の「次に読むべきインデックス位置」を保持するカーソル役。
let ptr = 0;
// const Str = (): string => tokens[ptr++];
//   これはアロー関数（arrow function）という関数定義の書き方。
//     - `()` : 引数なし（丸括弧の中に仮引数を書く。今回は空）。
//     - `: string` : このアロー関数の「戻り値の型」がstringであるという型注釈
//       （引数リストの直後、`=>` の直前に書く）。
//     - `=>` : アロー関数の本体につなぐ記号。
//     - `tokens[ptr++]` : 本体が波括弧 `{ }` で囲まれていない「式本体（expression body）」。
//       この場合、`return` を書かなくても式の評価結果がそのまま戻り値になる（暗黙の return）。
//   `tokens[ptr++]` の中身:
//     - `tokens[ptr]` で配列 tokens の ptr 番目の要素（string）を取り出す。
//     - `ptr++` は後置インクリメント演算子。「今の ptr の値を式全体の値として使ってから、
//       ptr 自身を +1 する」という意味。つまり「今指している要素を返しつつ、
//       次回に備えてポインタを1つ進める」という、入力読み取りでは定番の書き方。
//   `const Str = ...` なので Str という名前の「関数」を保持する定数（関数を値として
//   変数に代入する、という JS/TS ではおなじみの発想＝関数は第一級オブジェクト）。
//   呼び出すときは `Str()` のように丸括弧を付けて呼ぶ。
const Str = () => tokens[ptr++];
// const Num = (): number => Number(Str());
//   同じくアロー関数。戻り値の型注釈は `: number`。
//   本体は `Number(Str())` という「関数呼び出しの入れ子（合成）」:
//     1. まず Str() を呼んで文字列トークンを1つ取り出す（副作用として ptr が進む）。
//     2. その文字列を組み込み関数 `Number(...)` に渡して数値へ変換する。
//   `Number("123")` は 123 (number) を返す、JS 標準のグローバル関数。
//   このファイルでは a, b, c は文字列のまま使いたいので Num() は実際には
//   呼び出されていないが、数値入力問題にもそのまま使い回せる汎用ヘルパーとして
//   テンプレートに常備されている。
const Num = () => Number(Str());
// const n_out = (n?: number): void => { ... };
//   今度は本体が `{ }` で囲まれた「ブロック本体（block body）」のアロー関数。
//   ブロック本体では自動 return はされないので、値を返したいときは明示的に
//   `return` を書く必要がある（このヘルパーは何も return していないので戻り値は undefined）。
//   引数 `n?: number` の `?` はオプショナルパラメータ（省略可能な引数）を表す記法。
//     - `?` があると、その引数を渡さずに呼び出しても TypeScript の型チェックでエラーにならない。
//     - 内部的には型が `number | undefined`（number か undefined のどちらか）として扱われる。
//   戻り値型注釈 `: void` は「意味のある値を返さない関数」であることを示す型。
//   `console.log(n)` は標準出力へ1行出力する組み込み関数呼び出し。
const n_out = (n) => {
    console.log(n);
};
// const s_out = (s?: string): void => { ... };
//   n_out と同じ形の関数で、対象が string である版。
//   このファイルの解法本体では、最終的な答え "YES" / "NO" を出力するのに使われている。
const s_out = (s) => {
    console.log(s);
};
// const s_len = (s?: string): void => { ... };
//   文字列 s の「長さ」だけを出力するヘルパー。
//   `s?.length` はオプショナルチェイニング演算子 `?.` を使った書き方:
//     - もし s が undefined（または null）なら、その場で全体の評価を undefined にして
//       止まる（.length へのアクセスを試みず、実行時エラーを避ける）。
//     - s に値が入っていれば普通に s.length（文字列の文字数）にアクセスする。
//   引数 s がオプショナル（`?`）なので、呼び出し時に何も渡さない可能性があり、
//   その安全対策として `?.` が使われている。
//   ※ このファイルの解法ロジックからは呼び出されていない（未使用のテンプレ関数）。
const s_len = (s) => {
    console.log(s === null || s === void 0 ? void 0 : s.length);
};
// const create2dArray = <T>(rows: number, cols: number, initialValue: T): T[][] => { ... };
//   ジェネリクス（generics）を使った関数定義。
//     - `<T>` は「この関数を呼ぶときに具体的な型が決まる、型のプレースホルダー」を宣言している。
//       T は number でも string でも boolean でも、呼び出し側が渡した initialValue の型に
//       応じて自動的に決まる（型推論される）。
//     - 引数 `rows: number, cols: number` は普通の数値引数（行数・列数）。
//     - `initialValue: T` は「各マスを埋める初期値」で、その型が T。
//     - 戻り値型 `T[][]` は「T の配列の配列」＝2次元配列という意味
//       （`T[]` が1次元配列、それをさらに配列にしたのが `T[][]`）。
//   本体:
//     `Array.from({ length: rows }, () => Array.from({ length: cols }, () => initialValue))`
//     - `Array.from(arrayLike, mapFn)` は「配列っぽいもの」から新しい配列を作る組み込み関数。
//     - `{ length: rows }` は本物の配列ではないが `length` プロパティだけを持つ
//       「配列に似たオブジェクト（array-like）」。Array.from はこれを「要素数 rows 個の
//       配列」として扱ってくれる（中身は最初 undefined の連続として扱われる）。
//     - 第2引数の `() => ...` はマッパー関数。Array.from は要素数ぶん、このマッパーを
//       呼び出してその戻り値を新しい配列の各要素にする。
//     - 外側の `Array.from` のマッパーの中でさらに `Array.from({ length: cols }, () => initialValue)`
//       を呼んでいる＝「rows 個の、それぞれが cols 個の initialValue で埋まった配列」を
//       作っている、つまり rows × cols の2次元配列ができあがる。
//     - 内側のマッパーが `() => initialValue` になっている理由:
//       もし単純に `Array(cols).fill(initialValue)` のようにすると、initialValue が
//       オブジェクト（配列など参照型）の場合に「全マスが同じ1個のオブジェクトへの参照」を
//       共有してしまい、1マス書き換えると全マスが変わってしまうバグになりやすい。
//       毎回コールバックを呼ぶ Array.from 方式なら、呼び出しごとに新しい値を生成する
//       実装にもできて安全（ここでは initialValue をそのまま返しているので参照共有には
//       なるが、値型 number/string/boolean などプリミティブなら問題にならない）。
//   ※ このファイルの解法ロジックからは呼び出されていない（DP・グリッド問題向けの
//     汎用テンプレ関数として常備されている）。
const create2dArray = (rows, cols, initialValue) => {
    return Array.from({ length: rows }, () => Array.from({ length: cols }, () => initialValue));
};
// ============================================================
// ここから ABC060 A「Shiritori（しりとり）」の実際の解法ロジック。
//
// 問題: 半角スペース区切りで3つの文字列 a, b, c が与えられる。
//   「a の最後の文字」と「b の最初の文字」が一致し、かつ
//   「b の最後の文字」と「c の最初の文字」も一致するなら "YES" を、
//   そうでなければ "NO" を出力する（＝ a→b→c がしりとりとして繋がっているか判定）。
// ============================================================
// const a: string = Str();
//   `Str()` を呼び出して tokens の先頭（ptr=0 の位置）から1トークンを取得し、
//   ptr を 1 に進める。取得した値を `a` という定数に代入。
//   `: string` は右辺の推論結果と一致する明示的な型注釈（無くても動くが、
//   「この変数は string のはず」という意図を明示するために書かれている）。
const a = Str();
// const b: string = Str();
//   2回目の Str() 呼び出し。ptr は 1→2 に進み、tokens[1] を取得する。
const b = Str();
// const c: string = Str();
//   3回目の Str() 呼び出し。ptr は 2→3 に進み、tokens[2] を取得する。
//   これで入力の3トークン全部（a, b, c）を読み終えたことになる。
const c = Str();
// if (条件式) { ... } else { ... }
//   TypeScript/JavaScript の基本的な条件分岐構文。条件式が truthy（真として扱われる値）
//   なら if ブロック、そうでなければ else ブロックが実行される。
//
// 条件式: a[a.length - 1] == b[0] && b[b.length - 1] == c[0]
//   - `a.length` : 文字列 a の文字数（string の組み込みプロパティ）。
//   - `a.length - 1` : 最後の文字のインデックス（配列/文字列は 0 始まりなので、
//     長さから 1 引いた位置が末尾になる）。
//   - `a[a.length - 1]` : 文字列に対する角括弧インデックスアクセス。JS の string は
//     配列のように `[]` で1文字ずつ取り出せる（内部的には charAt と同等）。
//     これで「a の最後の1文字」が得られる。
//   - `b[0]` : b の先頭（インデックス0）の1文字＝「b の最初の文字」。
//   - `==` : 等価演算子（緩い比較）。両辺の型を必要なら暗黙変換してから比較する。
//     ここでは両辺とも文字列（string 型の1文字）同士の比較なので、`===`（厳密等価）
//     を使っても結果は変わらない。TypeScript/ESLint の流儀としては `===` を推奨する
//     ことが多いが、このファイルは `==` を使っている。
//   - `&&` : 論理積（AND）演算子。左右どちらも true のときだけ全体が true になる。
//     JS は短絡評価（left-to-right, short-circuit）なので、左側
//     `a[a.length-1] == b[0]` が false ならその時点で右側は評価されず全体が false になる。
//   まとめると: 「a の末尾文字 == b の先頭文字」かつ「b の末尾文字 == c の先頭文字」
//   の両方が成り立つときだけ if の中に入る。
if (a[a.length - 1] == b[0] && b[b.length - 1] == c[0]) {
    // 条件成立＝しりとりが a→b→c と正しく繋がっている場合。
    s_out("YES");
}
else {
    // 条件不成立＝どちらか一方でも文字が繋がっていない場合。
    s_out("NO");
}
