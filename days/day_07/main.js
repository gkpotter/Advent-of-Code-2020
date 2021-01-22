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

function search(bag, rules) {
  const others = Object.keys(rules[bag]);

  if (others == []) {
    return false;
  }
  else {
    return (others.some(other => other == "shiny gold bag") 
      || others.some(other => search(other, rules)));
  }

}

function count(bag, rules) {
  const others = Object.keys(rules[bag]);

  if (others.length == 0) {
    return 0;
  }
  else {
    return others.reduce((total, other) => {
     return total + rules[bag][other]*(1+count(other,rules));
    }, 0);
  }
}

function partOne(rules) {
  return Object.keys(rules).reduce((total, bag) => {
    return total + search(bag, rules);
  }, 0);
}

function partTwo(rules) {
  return count("shiny gold bag", rules);
}

async function main() {
	const start_time = process.hrtime();
  const lines = await loadInput();

  const rules = {};
  for (const line of lines){
    const bag = line.match(/^.*?bag/)[0];
    rules[bag] = {};

    for (const item of line.matchAll(/[1-9].*?\ bag/g)) {
      l = item[0].split(' ');
      num = Number(l.shift());
      other = l.join(' ');
      rules[bag][other] = num;
    }
  }

  const part_one_ans = partOne(rules);
  const part_two_ans = partTwo(rules);
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day  7 (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}