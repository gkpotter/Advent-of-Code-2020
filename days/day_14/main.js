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

function bitmask(value, mask) {
	const b = (value >>> 0).toString(2).padStart(36, '0')
	const masked_b = b.split('')
										.map((b_i, i) => mask[i] == 'X' ? b_i : mask[i])
										.join('')
	const masked_value = parseInt(masked_b, 2)
	
	return masked_value
}

function floatingBitmask(value, mask) {
	const b = (value >>> 0).toString(2).padStart(36, '0')
	const floating_b = b.split('')
											.map((b_i, i) => mask[i] == '0' ? b_i : mask[i])
											.join('')
	const masked_addresses = resolveFloating(floating_b,[])

	return masked_addresses
}

function resolveFloating(floating_b, b_list) {
	let branched = false

	for (let i = 0; i < floating_b.length; i++) {
		if (floating_b[i] == 'X') {
			const decide_0 = floating_b.substring(0,i) + '0' + floating_b.substring(i+1)
			const decide_1 = floating_b.substring(0,i) + '1' + floating_b.substring(i+1)
			
			resolveFloating(decide_0, b_list)
			resolveFloating(decide_1, b_list)
			
			branched = true
			break
		}
	}

	if (!branched) {
		b_list.push(parseInt(floating_b,2))
	}
	
	return b_list
}

function partOne(instructions) {
	const mem = {}
	let mask = 'X'.repeat(36)
	
	for (const instr of instructions) {
		if (instr[0] == 'mask') {
			mask = instr[1];
		}
		else {
			const address = Number(instr[0].match(/mem\[(\d*)\]/)[1])
			const value = Number(instr[1])

			const masked_value = bitmask(value, mask)
			
			mem[address] = masked_value
		}
	}

	return Object.values(mem)
						   .reduce((total,address)=>total+Number(address), 0)
}

function partTwo(instructions) {
	const mem = {}
	let mask = 'X'.repeat(36)
	
	for (const instr of instructions) {
		if (instr[0] == 'mask') {
			mask = instr[1];
		}
		else {
			const address = Number(instr[0].match(/mem\[(\d*)\]/)[1])
			const value = Number(instr[1])

			const masked_addresses = floatingBitmask(address, mask)
			
			for (const masked_address of masked_addresses){
				mem[masked_address] = value
			}
		}
	}

	return Object.values(mem)
							 .reduce((total,address)=>total+Number(address), 0)
}


async function main() {
	const start_time = process.hrtime() 
	const lines = await loadInput();

	const instructions = lines.map(line => line.split(' = '))

	const part_one_ans = partOne(instructions)
	const part_two_ans = partTwo(instructions)
	
	const diff = process.hrtime(start_time)
	const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
	
	console.log(`Day 14 (${total_time}s)`)
	console.log(`  Part 1: ${part_one_ans}`);
	console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
	main();
}