function main(input) {
    const args = input.split('\n');
    const nums = args[0].split(' ');
    const a = parseInt(nums[0], 10);
    const b = parseInt(nums[1], 10);

    let x = (a + b) / 2;

    x = Math.ceil(x);

    console.log(x)
}

main(require('fs').readFileSync('/dev/stdin', 'utf-8'));
