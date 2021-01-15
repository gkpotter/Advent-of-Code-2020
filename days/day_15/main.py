import time
import os


def part_one(nums, k):
	spoken = {}
	for i in range(len(nums)):
		spoken[nums[i]] = (i, i)

	i = len(nums)
	recent = nums[-1]
	
	while(i<k):
		prev, prevprev = spoken[recent]

		if prev == prevprev:
			recent = 0
		else:
			recent = prev - prevprev
		
		if recent in spoken:
			spoken[recent] = (i, spoken[recent][0])
		else:
			spoken[recent] = (i,i)
		
		i+=1

	return recent


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		nums = [int(item) for item in data.readline().strip().split(',')]

		part_one_ans = part_one(nums, 2020)
		part_two_ans = part_one(nums, 30000000)

		print('Day 15 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))

if __name__ == "__main__":
		main()