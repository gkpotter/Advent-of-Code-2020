import time
import os

def part_one(fields, tickets):
	total = 0
	for ticket in tickets:
		for x in ticket:
			entry_valid = False
			
			for field in fields:
				if x in fields[field]:
					entry_valid = True
					break
			
			if not entry_valid:
				total += x
	
	return total


def part_two(fields, tickets, my_ticket):
	valid_tickets = []

	for ticket in tickets:
		ticket_valid = True

		for x in ticket:
			entry_valid = False
			
			for field in fields:
				if x in fields[field]:
					entry_valid = True
					break
			
			if not entry_valid:
				ticket_valid = False
				break
		
		if ticket_valid:
			valid_tickets.append(ticket)

	possible_fields = []

	for entry_num in range(len(my_ticket)):
		entries = []
		for ticket in valid_tickets:
			entries.append(ticket[entry_num])

		possible_fields.append([])
		
		for field in fields:
			valid = True
			for entry in entries:
				if entry not in fields[field]:
					valid = False
					break
			if valid:
				possible_fields[entry_num].append(field)

	while not all(len(field_list)==1 for field_list in possible_fields):
		for field_list in possible_fields:
			if len(field_list)==1:
				for other in possible_fields:
					if len(other) != 1 and field_list[0] in other:
						other.remove(field_list[0])

	field_order = [field_list[0] for field_list in possible_fields]

	prod = 1
	for i in range(len(my_ticket)):
		if 'departure' in field_order[i]:
			prod *= my_ticket[i]
	
	return prod



def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = [line.strip() for line in data.readlines()]
		i = 0
		fields = {}
		my_ticket = []
		tickets = []

		while lines[i] != '':
			items = lines[i].split(':');
			field = items[0]
			ranges = [[int(x) for x in item.split('-')] for item in items[1].split(' or ')]
			
			fields[field] = []
			for r in ranges:
				for x in range(r[0],r[1]+1):
					fields[field].append(x)

			i+=1

		i+=2
		my_ticket = [int(x) for x in lines[i].strip().split(',')]

		i+=3
		while i < len(lines):
			tickets.append([int(x) for x in lines[i].strip().split(',')])
			i+=1

		part_one_ans = part_one(fields, tickets)
		part_two_ans = part_two(fields, tickets, my_ticket)

		print('Day 16 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))

if __name__ == "__main__":
		main()