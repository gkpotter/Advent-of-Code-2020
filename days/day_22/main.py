import time
import os


def score_deck(d):
	score = 0
	l = len(d)
	for i in range(len(d)):
		score += (l-i)*d[i]

	return score


def part_one(d1, d2):
	while len(d1)!=0 and len(d2)!=0:
		c1 = d1.pop(0)
		c2 = d2.pop(0)

		if c1 > c2:
			d1.extend([c1,c2])
		else:
			d2.extend([c2,c1])
	
	score = 0
	if len(d2) == 0:
		score = score_deck(d1)
	else:
		score = score_deck(d2)
	
	return score


def recursive_combat(d1, d2, previous_states):
	while len(d1)!=0 and len(d2)!=0:
		if (tuple(d1),tuple(d2)) in previous_states:
			return (1, d1)
		else:
			previous_states.append((tuple(d1),tuple(d2)))
			c1 = d1.pop(0)
			c2 = d2.pop(0)

			if c1 <= len(d1) and c2 <= len(d2):
				if recursive_combat(d1[:c1], d2[:c2], [])[0] == 1:
					d1.extend([c1,c2])
				else:
					d2.extend([c2,c1])
			else:
				if c1 > c2:
					d1.extend([c1,c2])
				else:
					d2.extend([c2,c1])
	
	if len(d2) == 0:
		return (1, d1)
	else:
		return (2, d2)


def part_two(d1, d2):
	_, d = recursive_combat(d1,d2,[])

	return score_deck(d)


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = [line.strip(')\n') for line in data.readlines()]

		i = lines.index('Player 2:')
		
		d1 = [int(x) for x in lines[1 : i-1]]
		d2 = [int(x) for x in lines[i+1 : ]]

		part_one_ans = part_one(d1.copy(),d2.copy())
		part_two_ans = part_two(d1.copy(),d2.copy())

		print('Day 22  ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()