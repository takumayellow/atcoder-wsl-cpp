function Main(input) {
    input = input.split("\n");

    const tmp = input[0].split(" ");
    const n = Number(tmp[0]);
    const k = Number(tmp[1]);

    console.log(n-k+1);

}

Main(require("fs").readFileSync("/dev/stdin", "utf-8"));
