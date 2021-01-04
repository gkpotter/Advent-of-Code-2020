def wrap(x, n):
	while x < 1:
		x += n
	while x > n:
		x-= n
	return x


def update(current, cups, n):
	picked_up = []
	destination = wrap(current-1, n)

	for i in range(1,4):
		next_index = (cups.index(current)+1) % len(cups)
		
		picked_up.append(cups.pop(next_index))

	while destination in picked_up:
		destination = wrap(destination-1, n)

	dest_index = cups.index(destination)

	for cup in reversed(picked_up):
		cups.insert(dest_index+1,cup)

	return (cups[(cups.index(current)+1) % n], cups)

def part_one(cups):
	n = len(cups)
	current = cups[0]
	
	for i in range(100):
		current, cups = update(current,cups,n)

	one_index = cups.index(1)
	s = ''
	
	for i in range(1, len(cups)):
		s += str(cups[(one_index+i) % len(cups)])
	
	return s


def part_two(cups):
	current = cups[0]

	for i in range(10, 10**6 + 1):
		cups.append(i)

	n = len(cups)

	for i in range(10*7):
			current, cups = update(current, cups, n)

	one_index = cups.index(1)
	total = 1
	
	for i in range(1, 3):
		total *= cups[(one_index+i) % len(cups)]
	
	return total


def main():
	with open('input.txt','r') as data:
		cups = [int(x) for x in data.readline()]

		print('part 1: {}'.format(part_one(cups.copy())))
		print('part 2: {}'.format(part_two(cups.copy())))


if __name__ == "__main__":
		main()