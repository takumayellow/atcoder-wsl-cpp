import * as fs from "fs";

const S = fs.readFileSync("/dev/stdin", "utf-8");

let n = 0, w = 0, s = 0, e = 0;

for (let i = 0; i < S.length; i++) {
    switch (S[i]) {
        case "N": n++; break;
        case "W": w++; break;
        case "S": s++; break;
        case "E": e++; break;
    }
}

if (((n===0 && s===0) || (n>0 && s>0)) && ((w===0 && e===0) || (w>0 && e>0))) { console.log("Yes"); }
else { console.log("No"); }



