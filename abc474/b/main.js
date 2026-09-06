function main(input) {
    const args = input.split("\n");
    const n = parseInt(args[0], 10);
    const p = args[1].split(" ").map((n) => parseInt(n, 10));
    
    let flag = true;
    
    for (let i = 0; i < Math.floor(n/10); i++) {
        for (let j = 0; j < 10; j++) {
            let x = p[10*i+j];
            console.log("インデックス" + (10*i+j));
            console.log("値"+x);
            console.log("区間左"+10*i);
            console.log("区間右"+10*(i+1));
            if (10*i <= x && x <= 10*(i+1)) { console.log("通過"); continue; }
            else { flag = false; console.log("falseは"+flag); break; }
        }
    }

    if (n%10 != 0) {
        let i = Math.floor((n/10));
        console.log(10*i)
        for (let s = 10*i; s < n; s++) {
            let x = p[s];
            console.log("インデックスl"+s);
            console.log("値"+x);
            console.log("区間左"+10*i);
            console.log("区間右"+10*(i+1));
            if (10*i <= x && x <= 10*(i+1)) { console.log("通過"); continue; }
            else { flag = false; break; }
        }
    }

    if (flag === true) {
        console.log("Yes");
    }
    else { console.log("No"); }
     

}

main(require("fs").readFileSync("/dev/stdin", "utf-8"));
