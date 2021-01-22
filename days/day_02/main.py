import time
import os


def part_one(pw_data):
	total_valid = 0

	for entry in pw_data:
		count = entry['password'].count(entry['letter'])
		[m, M] = entry['range']
		total_valid += count in range(m, M+1)

	return total_valid
		

def part_two(pw_data):
	total_valid = 0

	for entry in pw_data:
		[a,b] = entry['range']
		l = entry['letter']
		pw = entry['password']
		total_valid += (pw[a-1] == l)^(pw[b-1] == l)

	return total_valid
		

def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		raw_pw_data = [line.split(' ') for line in data.readlines()]
		pw_data = []
		
		for raw_entry in raw_pw_data:
			entry = {}
			entry['range'] = [int(x) for x in raw_entry[0].split('-')]
			entry['letter'] = raw_entry[1].strip(':')
			entry['password'] = raw_entry[2].strip('\n')
			pw_data.append(entry)

		part_one_ans = part_one(pw_data)
		part_two_ans = part_two(pw_data)

		print('Day  2 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))
		

if __name__ == "__main__":
		main()