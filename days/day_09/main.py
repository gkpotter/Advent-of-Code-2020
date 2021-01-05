import time
import os

def part_one(nums):
	i = 25
	
	while i < len(nums):
		current = nums[i]
		found = False
		S = nums[i-25:i]

		for n in S:
			for m in S:
				if n+m == current and n != m:
					found = True
		
		if not found:
			return nums[i]

		i+=1


def part_two(nums, N):
	for i in range(len(nums)):
		k = 0
		
		while sum(S := nums[i:i+k])<N:
			k+=1
		
		if sum(S) == N:
			return min(S) + max(S)


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		nums = [int(line) for line in data.readlines()]
		
		part_one_ans = part_one(nums)
		part_two_ans = part_two(nums, part_one_ans)

		print('day  9 ({:,.3f}s)'.format(time.time()-start_time))
		print('  part 1: {}'.format(part_one_ans))
		print('  part 2: {}'.format(part_two_ans))

if __name__ == "__main__":
		main()