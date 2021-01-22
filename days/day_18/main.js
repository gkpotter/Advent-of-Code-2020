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

function evalLeftToRight(expression) {
  while (expression.includes('(')) {
    expression = expression.replace(/\(([0-9+* ]+)\)/, 
      (match, p1) => String(evalLeftToRight(p1)));
  }

  while (expression.includes('+') || expression.includes('*')) {
    expression = expression.replace(/^([0-9]+) ([+*]) ([0-9]+)/, 
      (match, p1, p2, p3) => eval_operation(p1, p2, p3));
  }

  return Number(expression);
}

function evalPlusFirst(expression) {
  while (expression.includes('(')) {
    expression = expression.replace(/\(([0-9+* ]+)\)/, 
      (match, p1) => String(evalPlusFirst(p1)));
  }

  while (expression.includes('+')) {
    expression = expression.replace(/([0-9]+) (\+) ([0-9]+)/, 
      (match, p1, p2, p3) => eval_operation(p1, p2, p3));
  }

  while (expression.includes('*')) {
    expression = expression.replace(/([0-9]+) (\*) ([0-9]+)/, 
      (match, p1, p2, p3) => eval_operation(p1, p2, p3));
  }

  return Number(expression);
}


function eval_operation(x, oper, y) {
  if (oper == '+') {
    return String(Number(x) + Number(y));
  }
  else if (oper == '*') {
    return String(Number(x) * Number(y));
  }
  else {
    throw 'nope';
  }
}

function partOne(expressions) {
  return expressions.reduce((total, expression) => total + evalLeftToRight(expression), 0);
}

function partTwo(expressions) {
  return expressions.reduce((total, expression) => total + evalPlusFirst(expression), 0);
}

async function main() {
	const start_time = process.hrtime();
  
  const expressions = await loadInput();
  
  const part_one_ans = partOne(expressions);
  const part_two_ans = partTwo(expressions);
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day 18 (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}