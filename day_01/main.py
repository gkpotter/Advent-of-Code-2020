def part_one(nums):
	for x in nums:
		for y in nums:
			if x+y == 2020:
				return x*y
  			
def part_two(nums):
	for x in nums:
		for y in nums:
			for z in nums:
				if x+y+z == 2020:
					return x*y*z
	  			
def main():
  with open('input.txt','r') as data:
  	nums = [int(line) for line in data.readlines()]
  	
  	print('part 1: {}'.format(part_one(nums)))
  	print('part 2: {}'.format(part_two(nums)))
  	

if __name__ == "__main__":
    main()