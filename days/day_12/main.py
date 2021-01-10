import time
import os

compass = {
	'N' : [0,1],
	'E' : [1,0],
	'S' : [0,-1],
	'W' : [-1,0]
}


def add(u, v):
	return [u[i]+v[i] for i in range(len(u))]


def mult(k, u):
	return [k*u[i] for i in range(len(u))]


def rotate_left(u, deg):
	x, y = u
	while deg < 0:
		deg += 360

	if deg == 90:
		return [-y,x]
	elif deg == 180:
		return [-x,-y]
	elif deg == 270:
		return [y, -x]
	else:
		return [x, y]


def part_one(instructions):
	direction = [1,0]
	pos = [0,0]

	for i in range(len(instructions)):
		letter, num = instructions[i]

		if letter in compass:
			pos = add(pos, mult(num, compass[letter]))
		elif letter == 'F':
			pos = add(pos, mult(num, direction))
		else:
			deg = num

			if letter == 'R':
				deg *= -1

			direction = rotate_left(direction, deg)

	return sum(abs(x) for x in pos) 


def part_two(instructions):
	pos = [0,0]
	waypoint = [10,1]

	for i in range(len(instructions)):
		letter, num = instructions[i]

		if letter in compass:
			waypoint = add(waypoint, mult(num, compass[letter]))
		elif letter == 'F':
			pos = add(pos, mult(num, waypoint))
		else:
			deg = num

			if letter == 'R':
				deg *= -1

			waypoint = rotate_left(waypoint, deg)

	return sum(abs(x) for x in pos)


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		instructions = [[line[0],int(line[1:])] for line in data.readlines()]
		
		part_one_ans = part_one(instructions)
		part_two_ans = part_two(instructions)

		print('Day 12 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()