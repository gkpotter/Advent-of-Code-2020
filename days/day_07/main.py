import re
import time
import os


def search(bag, rules):
	others = rules[bag]

	if others == {}:
		return False
	else:
		for other in others:
			if other == "shiny gold bag":
				return True
		
		return any(search(other,rules) for other in others)


def count(bag, rules):
	others= rules[bag]

	if others == {}:
		return 0
	else:
		return sum(rules[bag][other]*(1+count(other,rules)) for other in others)


def part_one(rules):
	total = 0

	for bag in rules:
		total += search(bag, rules)
		
	return total


def part_two(rules):
	return count("shiny gold bag", rules)


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = data.readlines()
		rules = {}

		for line in lines:
			bag = re.findall(r'^.*?bag', line)[0]
			rules[bag] = {}

			for item in re.findall(r'[1-9].*?\ bag', line):
				l = item.split(' ')
				num = int(l[0])
				other = ' '.join(l[1:])
				rules[bag][other] = num

		part_one_ans = part_one(rules)
		part_two_ans = part_two(rules)

		print('Day  7 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))
		

if __name__ == "__main__":
		main()