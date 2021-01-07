import time
import os

class Cup:
	def __init__(self, num):
		self.num = num
		self.right = None

	def __str__(self):
		return str(self.num)

	def __repr__(self):
		return str(self.num)


def create_cups(nums):
	n = len(nums)
	
	cups = { nums[i]: Cup(nums[i]) for i in range(n)}

	for i in range(0,len(nums)):
		cups[nums[i]].right = cups[nums[(i+1)%n]]

	return cups


def update(current, cups, n):
	picked_up = []

	j = current.right
	for i in range(1,4):
		picked_up.append(j.num)
		j = j.right

	current.right = j

	dest = current.num - 1 if current.num > 1 else n

	while dest in picked_up:
		dest = dest - 1 if dest > 1 else n

	tmp = cups[dest].right
	cups[dest].right = cups[picked_up[0]]
	cups[picked_up[2]].right = tmp

	return (cups[current.right.num], cups)

def part_one(nums):
	cups = create_cups(nums)
	n = len(cups)
	current = cups[1]

	for i in range(100):
		current, cups = update(current, cups, n)

	j = cups[1].right
	s = ''
	
	for i in range(1, len(cups)):
		s += str(j.num)
		j = j.right
	
	return s


def part_two(nums):
	nums.extend([*range(10, 10**6 + 1)])
	cups = create_cups(nums)
	current = cups[nums[0]]
	n = len(cups)

	for i in range(10**7):
		current, cups = update(current, cups, n)

	total = 1
	j = cups[1].right
	for i in range(1, 3):
		total *= j.num
		j = j.right
	
	return total


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		nums = [int(x) for x in data.readline()]

		part_one_ans = part_one(nums)
		part_two_ans = part_two(nums)

		print('day 23  ({:,.3f}s)'.format(time.time()-start_time))
		print('  part 1: {}'.format(part_one_ans))
		print('  part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()