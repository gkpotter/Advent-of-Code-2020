import re
import time
import os


def attempt(instructions):
	acc = 0
	i = 0
	steps = 0
	
	while(i < len(instructions)):
		steps += 1
		if steps>len(instructions):
			return -1
		
		instr = instructions[i]
		
		if instr[0] == 'nop':
			i+=1
		elif instr[0] == 'jmp':
			i += int(instr[1])
		elif instr[0] == 'acc':
			acc += int(instr[1])
			i+=1

	return acc


def part_one(instructions):
	seen = []
	acc = 0
	i = 0
	
	while(i not in seen):
		instr = instructions[i]
		seen.append(i)
		
		if instr[0] == 'nop':
			i+=1
		elif instr[0] == 'jmp':
			i += int(instr[1])
		elif instr[0] == 'acc':
			acc += int(instr[1])
			i+=1

	return acc


def part_two(instructions):
	for i in range(len(instructions)):
		prev = instructions[i][0]
		
		if prev == 'jmp':
			instructions[i][0] = 'nop'
		elif prev == 'nop':
			instructions[i][0] = 'jmp'
		
		acc = attempt(instructions)
		if acc > 0:
			return acc
		
		instructions[i][0] = prev


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = data.readlines()
		instructions = []

		for line in lines:
			instructions.append(line.strip().split(' '))
		
		part_one_ans = part_one(instructions)
		part_two_ans = part_two(instructions)

		print('Day  8 ({:,.3f}s)'.format(time.time() - start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))

if __name__ == "__main__":
		main()