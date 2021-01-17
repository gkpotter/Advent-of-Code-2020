# -*- coding: utf-8 -*-
import time
import os

def transform(subject, loop):
	value = 1
	modulus = 20201227
	while loop >= 1:
		if loop % 2 == 1:	
			value *= subject
			value %= modulus
		
		subject *= subject
		subject %= modulus

		loop//=2
	return value


def find_loop(key, subject):
	loop = 1
	while transform(subject, loop) != key:
		loop += 1
	return loop


def part_one(card_key, door_key, subject):
	"""
	Using Sympy's discrete log:

	from sympy.ntheory.residue_ntheory import discrete_log

	card_loop = discrete_log(20201227, card_key, subject)
	door_loop = discrete_log(20201227, door_key, subject)
	"""

	card_loop = find_loop(card_key, subject)
	door_loop = find_loop(door_key, subject)

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