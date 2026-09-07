function Main(input) {

    input = input.split("\n");
    const n = input[0];
    var a = input[1];
    
    let sum = 0;

    console.log(n, n/2 + 2);
    for (let i = n/2 + 2; i < n; i++) {
        sum += a[i];
        console.log(sum);
    }

    console.log(sum);
}

Main(require("fs").readFileSync("/dev/stdin", "utf-8"));
