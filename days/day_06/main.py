import time
import os

def part_one(groups):
	total = 0
	for group in groups:
		group_str = ''
		for person in group:
			group_str += person
		total += len(set(list(group_str)))
	return total


def part_two(groups):
	total = 0
	for group in groups:
		first = set(list(group[0]))
		total += len(first.intersection(*[set(list(person)) for person in group[1:]]))

	return total


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		groups = []

		group = []
		for line in data.readlines():
			if line == '\n':
				groups.append(group)
				group = []
			else:
				group.append(line.strip())
		groups.append(group)
		
		part_one_ans = part_one(groups)
		part_two_ans = part_two(groups)

		print('Day  6 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))
		

if __name__ == "__main__":
		main()