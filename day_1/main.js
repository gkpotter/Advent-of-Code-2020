const fs = require('fs');
const readline = require('readline');

async function loadData() {
  const rl = readline.createInterface({
    input: fs.createReadStream('data.txt')
  });

  const data = [];
  for await (const line of rl) {
    data.push(Number(line));
  }
  return data
}

function partOne(nums) {
  for(let x of nums) {
    for (let y of nums) {
      if (x+y == 2020) {
        return x*y
      }
    }
  }
}

function partTwo(nums) {
  for(let x of nums) {
    for (let y of nums) {
      for (let z of nums) {
        if (x+y+z == 2020) {
          return x*y*z
        }
      }
    }
  }
}

async function main() {
  const nums = await loadData();
  console.log(`part 1: ${partOne(nums)}`);
  console.log(`part 2: ${partTwo(nums)}`);
}

if (require.main === module) {
  main();
}