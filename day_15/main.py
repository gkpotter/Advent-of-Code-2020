def part_one(nums, k):
	spoken = {}
	for i in range(len(nums)):
		spoken[nums[i]] = (i, i)

	i = len(nums)
	while(i<k):
		recent = nums[-1]
		prev, prevprev = spoken[recent]

		if prev == prevprev:
			num = 0
		else:
			num = prev - prevprev
		
		if num in spoken:
			spoken[num] = (i, spoken[num][0])
		else:
			spoken[num] = (i,i)
		
		nums.append(num)
		i+=1

	return nums[k-1]


def main():
	with open('input.txt','r') as data:
		nums = [int(item) for item in data.readline().strip().split(',')]

		print('part 1: {}'.format(part_one(nums, 2020)))
		print('part 2: {}'.format(part_one(nums, 30000000)))

if __name__ == "__main__":
    main()