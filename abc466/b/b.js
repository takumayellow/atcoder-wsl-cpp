const input = require("fs").readFileSync(0, "utf8");
const tokens = input.trim().split(/\s+/);
let idx = 0;
const next = () => tokens[idx++];
const nextInt = () => Number(next());
const results = [];
main();
console.log(results.join(" "));

function main() {
    const N = nextInt();
    const M = nextInt();
    const C = new Array();
    for (let i = 0; i < N; i++) {
        const c = nextInt()
        const s = nextInt()
        C[c] = [...(C[c] ?? []), s]
    }

    for (let i = 1; i <= M; i++) {
        if (C[i] !== undefined && C[i].length > 0) {
            results.push(Math.max(...C[i]))
            continue
        }

     results.push(-1)
    }
}
