import time
import os

# need to check each branch in parallel to avoid infinite loop
def check(alphabet, grammar, word, start_symbol):
	stack = [start_symbol]
	return _check(alphabet, grammar, word, stack, 0)


def _check(alphabet, grammar, word, stack, i):
	if stack != [] and len(stack) <= len(word):
		top = stack.pop(0)

		if top in alphabet:
			if i>=len(word):
				return False

			if top == word[i]:
				return _check(alphabet, grammar, word, stack, i+1)
			else:
				return False
		else:
			for match in grammar[top]:
				if _check(alphabet, grammar, word, match+stack, i):
					return True
			
			return False
				
	return i == len(word)


def part_one(alphabet, grammar, words, start_symbol):
	total = 0
	
	for word in words:
		total += check(alphabet, grammar, word, start_symbol)
	
	return total


def part_two(alphabet, grammar, words, start_symbol):
	grammar['8'] = [['42'], ['42', '8']]
	grammar['11'] = [['42', '31'], ['42', '11', '31']]

	total = 0
	
	for word in words:
		total += check(alphabet, grammar, word, start_symbol)
	
	return total


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = [line.strip() for line in data.readlines()]
		
		grammar = {}

		i = 0
		while lines[i] != '':
			items = lines[i].split(':')

			grammar[items[0]] = [match.strip().replace('"','').split(' ') 
				for match in items[1].split('|')]

			i+=1

		words = lines[i+1:]
		alphabet = ['a', 'b']
		start_symbol = '0'

		part_one_ans = part_one(alphabet, grammar, words, start_symbol)
		part_two_ans = part_two(alphabet, grammar, words, start_symbol)

		print('Day 19 ({:,.3f}s)'.format(time.time() - start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()