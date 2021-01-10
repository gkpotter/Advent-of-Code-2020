# -*- coding: utf-8 -*-
import time
import os

sympy_available = False
try:
	from sympy.ntheory.residue_ntheory import discrete_log
	sympy_available = True
except:
	print('Sympy not available. Brute forcing...')


def transform(subject, loop):
	value = 1
	while loop >= 1:
		if loop % 2 == 1:	
			value *= subject
			value %= 20201227
		
		subject *= subject
		subject %= 20201227

		loop//=2
	return value


def part_one(card_key, door_key, subject):
	if sympy_available:
		card_loop = discrete_log(20201227, card_key, 7)
		door_loop = discrete_log(20201227, door_key, 7)
	else:
		card_loop = 1
		while transform(subject, card_loop) != card_key:
			card_loop += 1
		
		door_loop = 1
		while transform(subject, door_loop) != door_key:
			door_loop += 1

	return transform(transform(subject, door_loop), card_loop)


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		card_key = int(data.readline())
		door_key = int(data.readline())

		part_one_ans = part_one(card_key, door_key, 7)
		part_two_ans = '⭐️'

		print('Day 25  ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()