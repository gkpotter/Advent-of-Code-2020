import time
import os

class Cup:
	def __init__(self, num):
		self.num = num
		self.left = None
		self.right = None

	def show(self):
		print('('+str(self.num)+')',end='')
		self._show(self)

	def _show(self, first):
		if self.right == first:
			print('')
			return
		else:
			print(self.right.num,end='')
			self.right._show(first)

	def __str__(self):
		return str(self.num)

	def __repr__(self):
		return str(self.num)


def create_cups(nums):
	cups = { nums[i]: Cup(nums[i]) for i in range(len(nums))}

	cups[nums[0]].left = cups[nums[-1]]
	cups[nums[0]].right = cups[nums[1]]
	
	for i in range(1,len(nums)-1):
		cups[nums[i]].left = cups[nums[i-1]]
		cups[nums[i]].right = cups[nums[i+1]]

	cups[nums[-1]].left = cups[nums[-2]]
	cups[nums[-1]].right = cups[nums[0]]

	return cups


def update(current, cups, n):
	picked_up = []

	j = current.right
	for i in range(1,4):
		picked_up.append(j.num)
		j = j.right

	current.right = j
	j.left = current

	destination_num = current.num-1

	if destination_num < 1:
		destination_num += n

	while destination_num in picked_up:
		destination_num -= 1
		if destination_num < 1:
			destination_num += n

	tmp = cups[destination_num].right
	cups[destination_num].right.left = cups[picked_up[2]]

	cups[destination_num].right = cups[picked_up[0]]
	cups[picked_up[0]].left = cups[destination_num]
	
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
	cups = create_cups(nums)
	current = cups[1]

	for i in range(10, 10**6 + 1):
		cups[i] = Cup(i)

	for i in range(11, 10**6):
		cups[i].right = cups[i+1]
		cups[i].left = cups[i-1]

	cups[2].right = cups[10]
	cups[10].left = cups[2]
	cups[10].right = cups[11]
	cups[1].left = cups[10**6]
	cups[10**6].right = cups[1]
	cups[10**6].left = cups[10**6-1]

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