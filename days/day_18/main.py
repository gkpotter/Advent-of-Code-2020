import re
import time
import os


def eval_plus_first(expression):
	while '(' in expression:
		expression = re.sub(r'\(([0-9+* ]+)\)', 
			lambda match: str(eval_plus_first(match.group(1))), 
			expression)

	while '+' in expression:
		expression = re.sub(r'([0-9]+) (\+) ([0-9]+)', eval_operation, expression, 1)
	
	while '*' in expression:
		expression = re.sub(r'([0-9]+) (\*) ([0-9]+)', eval_operation, expression, 1)

	return int(expression)


def eval_left_to_right(expression):
	while '(' in expression:
		expression = re.sub(r'\(([0-9+* ]+)\)', 
			lambda match: str(eval_left_to_right(match.group(1))), 
			expression)

	while '+' in expression or '*' in expression:
		expression = re.sub(r'^([0-9]+) ([+*]) ([0-9]+)', 
			eval_operation, 
			expression)

	return int(expression)


def eval_operation(match):
	x = int(match.group(1))
	y = int(match.group(3))
	oper = match.group(2)
	
	if oper == '+':
		return str(x+y)
	elif oper == '*':
		return str(x*y)
	else:
		return '0'


def part_one(expressions):
	total = 0
	for expression in expressions:
		total += eval_left_to_right(expression)
	return total


def part_two(expressions):
	total = 0
	for expression in expressions:
		total += eval_plus_first(expression)
	return total


def main():
	start_time = time.time()
	
	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		expressions = [line.strip() for line in data.readlines()]

		part_one_ans = part_one(expressions)
		part_two_ans = part_two(expressions)

		print('Day 18 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()