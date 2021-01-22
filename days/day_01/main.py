import time
import os

def part_one(nums):
	for x in nums:
		for y in nums:
			if x + y == 2020:
				return x * y

				
def part_two(nums):
	for x in nums:
		for y in nums:
			for z in nums:
				if x + y + z == 2020:
					return x * y * z

					
def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		nums = [int(line) for line in data.readlines()]
		
		part_one_ans = part_one(nums)
		part_two_ans = part_two(nums)

		print('Day  1 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))
		

if __name__ == "__main__":
		main()