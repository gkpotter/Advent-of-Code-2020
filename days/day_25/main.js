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

function transform(subject, loop) {
  let value = 1;
  const modulus = 20201227;

  while (loop >= 1) {
    if (loop % 2 == 1) { 
      value *= subject;
      value %= modulus;
    }
    
    subject *= subject;
    subject %= modulus;

    loop = Math.floor(loop/2);
  }
  return value;
}


function find_loop(key, subject) {
  let loop = 1;
  while (transform(subject, loop) != key) {
    loop += 1;
  }

  return loop;
}

function partOne(card_key, door_key, subject) {
  const card_loop = find_loop(card_key, subject);
  const door_loop = find_loop(door_key, subject);

  return transform(transform(subject, door_loop), card_loop);
}


async function main() {
	const start_time = process.hrtime();
  
  const lines = await loadInput();
  const [card_key, door_key] = lines.map(line => Number(line));

  const part_one_ans = partOne(card_key, door_key, 7);
  const part_two_ans = '⭐️';
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day 25 (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}