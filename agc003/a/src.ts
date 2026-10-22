import * as fs from "fs";

// 今回は連続文字列が与えられるのでtrimは不要？
const s = fs.readFileSync("dev/stdin", "utf-8").trim();

// この記法もよくわからない
const paired = (a, b) => s.includes(a) === s.includes(b);

console.log(paired("N", "S") && paired("E", "W") ? """"""""Ye   

