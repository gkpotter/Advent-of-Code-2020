import time
import os


def part_one(adapters):
	ones = 0
	threes = 0

	for i in range(1,len(adapters)):
		diff = adapters[i] - adapters[i - 1]

		if diff == 1:
			ones+=1
		elif diff == 3:
			threes+=1
	
	return ones*threes
	

def part_two(adapters):
	total = 1
	streak = 0

	# tribonacci numbers?
	factor = [1, 1, 2, 4, 7, 13]

	for i in range(1,len(adapters)):
		diff = adapters[i] - adapters[i - 1]

		if diff == 1:
			streak += 1
		else:
			total *= factor[streak]
			streak = 0
	
	return total


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		adapters = [int(line) for line in data.readlines()]
		adapters.append(0)
		adapters.sort()
		adapters.append(adapters[-1] + 3)
		
		part_one_ans = part_one(adapters)
		part_two_ans = part_two(adapters)

		print('Day 10 ({:,.3f}s)'.format(time.time() - start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))

if __name__ == "__main__":
		main()