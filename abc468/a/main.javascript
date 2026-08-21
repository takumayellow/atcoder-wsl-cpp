function Main (input){
    input = input.split("\n");
    const n = Number(input[0]);
    const tmp = input[1].split(" ").map(Number);
    let result = 0;
    for (let i = 0; i< n-2; i++){
        if(tmp[i]<tmp[i-1] && tmp[i+1]>tmp[i+2]){
            result += 1;
        }
    }
    console.log(result);
}

Main(require("fs").readFileSync(0, "utf8"));
