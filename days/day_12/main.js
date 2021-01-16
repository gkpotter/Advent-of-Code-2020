const fs = require('fs');
const readline = require('readline');

const compass = {
	'N' : [0,1],
	'E' : [1,0],
	'S' : [0,-1],
	'W' : [-1,0]
}
const directions = Object.keys(compass)

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

function add(u, v) {
	return u.map((u_i, i) => u_i + v[i])
}

function mult(k, u) {
	return u.map(u_i => k * u_i)
}

function rotateCCW(u, deg) {
	const [x, y] = u;
	
	while (deg < 0) {
		deg += 360;
	}

	switch (deg) {
		case 90:
			return [-y,x];
		case 180:
			return [-x,-y];
		case 270:
			return [y, -x];
		default:
			return [x, y];
	}

}


function partOne(instructions) {
	let direction = [1,0]
	let pos = [0,0]

	for (const [letter, num] of instructions) {
		if (directions.includes(letter)) {
			pos = add(pos, mult(num, compass[letter]))
		}
		else if (letter == 'F') {
			pos = add(pos, mult(num, direction))
		}
		else {
			deg = num

			if (letter == 'R') {
				deg *= -1
			}

			direction = rotateCCW(direction, deg)
		}
	}

	return pos.reduce((total, p) => total + Math.abs(p), 0);
}

function partTwo(instructions) {
	let pos = [0,0]
	let waypoint = [10,1]

	for (const [letter, num] of instructions) {
		if (directions.includes(letter)) {
			waypoint = add(waypoint, mult(num, compass[letter]))
		}
		else if (letter == 'F') {
			pos = add(pos, mult(num, waypoint))
		}
		else {
			deg = num

			if (letter == 'R') {
				deg *= -1
			}

			waypoint = rotateCCW(waypoint, deg)
		}
	}

	return pos.reduce((total, p) => total + Math.abs(p), 0);
}


async function main() {
	const start_time = process.hrtime() 
	const lines = await loadInput();

	const instructions = lines.map(line => [line[0],Number(line.substring(1))])

	const part_one_ans = partOne(instructions)
	const part_two_ans = partTwo(instructions)
	
	const diff = process.hrtime(start_time)
	const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
	
	console.log(`Day 12 (${total_time}s)`)
	console.log(`  Part 1: ${part_one_ans}`);
	console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
	main();
}