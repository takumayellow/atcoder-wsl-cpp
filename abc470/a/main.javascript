function main(input) {
    const N = Number(input.trim());
    
    const ans = [];
    
    for (let i = 1; i <= N; i++) {
        if (i % 3 === 0) {
            ans.push('Fizz');
        } else {
            ans.push(i);
        }
    }
    
    console.log(ans.join('\n'));
    
}

main(require('fs').readFileSync('/dev/stdin', 'utf-8'));
