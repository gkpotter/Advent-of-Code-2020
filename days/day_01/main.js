const fs = require('fs');
const readline = require('readline');

async function loadInput() {
  const rl = readline.createInterface({
    input: fs.createReadStream(__dirname + '/input.txt')
  });

  const lines = [];
  for await (const line of rl) {
    lines.push(line);
  }
  return lines;
}

function partOne(nums) {
  for (const x of nums) {
    for (const y of nums) {
      if (x + y == 2020) {
        return x * y;
      }
    }
  }
}

function partTwo(nums) {
  for (const x of nums) {
    for (const y of nums) {
      for (const z of nums) {
        if (x + y + z == 2020) {
          return x * y * z;
        }
      }
    }
  }
}

async function main() {
	const start_time = process.hrtime() ;
  
  const lines = await loadInput();
  const nums = lines.map(line => Number(line));

  const part_one_ans = partOne(nums);
  const part_two_ans = partTwo(nums);
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day  1 (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}