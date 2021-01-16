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

function partOne(tickets,fields) {
	const ticket_reducer = (ticket_total, x) => {
		for (const field of Object.keys(fields)) {
			if (fields[field].includes(x)) {
				return ticket_total;
			}
		}
		return ticket_total + x;
	}

	const total = tickets.reduce((total, ticket) => {
		return total + ticket.reduce(ticket_reducer, 0)
	}, 0);

	return total;
}

function partTwo(tickets, my_ticket, fields) {
	let total = 0

	const valid_tickets = tickets.filter(ticket => {
		return !ticket.some(entry => {
			for (const field of Object.keys(fields)) {
				if (fields[field].includes(entry)) {
					return false
				}
			}
			return true
		})
	});

	const possible_fields = []

	for (let entry_num = 0; entry_num < my_ticket.length; entry_num++) {
		let entries = valid_tickets.map(ticket => ticket[entry_num])

		const possible_fields_for_entry = Object.keys(fields).filter(field => {
			for (const entry of entries) {
				if (!fields[field].includes(entry)){
					return false
				}
			}
			return true
		})

		possible_fields.push(possible_fields_for_entry)
		
	}

	while (possible_fields.some(field_list => field_list.length > 1)) {
		for (const field_list of possible_fields) {
			if (field_list.length == 1) {
				for (let j = 0; j < possible_fields.length; j++) {
					const index = possible_fields[j].indexOf(field_list[0])
					if (possible_fields[j].length != 1 && index>=0) {
						possible_fields[j].splice(index,1)
					}
				}
			}
		}
	}

	const field_order = possible_fields.map(field_list => field_list[0])

	const prod = field_order.reduce((total, field, i) => {
		if (field.includes('departure')) {
			return total * my_ticket[i]
		}
		return total
	}, 1)

	
	return prod
}

async function main() {
	const start_time = process.hrtime() 
	const lines = await loadInput();

	let i = 0
	const fields = {}
	const tickets = []

	while (lines[i] != '') {
		items = lines[i].split(':');
		field = items[0]
		ranges = items[1].split(' or ')
										 .map(item => item.split('-').map(Number))

		fields[field] = []
		for (const r of ranges) {
			for (let x = r[0]; x <= r[1]; x++) {
				fields[field].push(x)
			}
		}

		i+=1
	}

	i+=2
	const my_ticket = lines[i].split(',').map(Number)


	i+=3
	while (i < lines.length) {
		tickets.push(lines[i].split(',').map(Number))
		i+=1
	}

	const part_one_ans = partOne(tickets, fields)
	const part_two_ans = partTwo(tickets, my_ticket, fields)
	
	const diff = process.hrtime(start_time)
	const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
	
	console.log(`Day 16 (${total_time}s)`)
	console.log(`  Part 1: ${part_one_ans}`);
	console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
	main();
}