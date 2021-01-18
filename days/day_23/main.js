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
  return lines
}

class Cup {
	constructor(num) {
		this.num = num
		this.right = null
	}

	toString() {
		return String(this.num)
	}
}

function createCups(nums) {
	const n = nums.length

	const cups = {}
	for (let i = 0; i < n; i++) {
		cups[nums[i]] = new Cup(nums[i])
	}
	for (let i = 0; i < n; i++) {
		cups[nums[i]].right = cups[nums[(i+1)%n]]
	}

	return cups
}

function update(current, cups, n) {
	const picked_up = []

	let j = current.right
	for (let i = 0; i < 3; i++) {
		picked_up.push(j.num)
		j = j.right
	}

	current.right = j

	let dest = current.num > 1 ? current.num - 1 : n

	while (picked_up.includes(dest)) {
		dest = (dest > 1 ? dest - 1 : n)
	}

	const tmp = cups[dest].right
	cups[dest].right = cups[picked_up[0]]
	cups[picked_up[2]].right = tmp

	return [cups[current.right.num], cups]
}


function partOne(nums) {
	const n = nums.length
	let cups = createCups(nums)
	let current = cups[nums[0]]

	for (let i = 0; i < 100; i++) {
		[current, cups] = update(current, cups, n)
	}

	let j = cups[1].right
	let s = ''
	
	for (let i = 1; i < Object.keys(cups).length; i++) {
		s += String(j.num)
		j = j.right
	}
	
	return s
}

function partTwo(nums) {
	for (let i = 10; i < (10**6+1); i++) {
		nums.push(i)
	}
	const n = nums.length
	const start = nums[0]
	let cups = createCups(nums)
	let current = cups[start]

	for (let i = 0; i < 10**7; i++) {
		[current, cups] = update(current, cups, n)
	}

	let total = 1
	let j = cups[start].right
	for (let i = 0; i < 2; i++) {
		total *= j.num
		j = j.right
	}
	
	return total
}

async function main() {
	const start_time = process.hrtime() 
  
  const lines = await loadInput();
  const nums = lines[0].split('').map(x => Number(x))

  const part_one_ans = partOne(nums)
  const part_two_ans = partTwo(nums)
  
  const diff = process.hrtime(start_time)
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
  
  console.log(`Day  1 (${total_time}s)`)
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}