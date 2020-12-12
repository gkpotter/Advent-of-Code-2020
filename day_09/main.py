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
  with open('input.txt','r') as data:
  	nums = [int(line) for line in data.readlines()]
  	
  	print('part 1: {}'.format(N := part_one(nums)))
  	print('part 2: {}'.format(part_two(nums, N)))

if __name__ == "__main__":
    main()