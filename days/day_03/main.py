import time
import os

def part_one(rows):
	return check_trees(rows, 3, 1)
	

def part_two(rows):
	slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	prod = 1
	for slope in slopes:
		prod *= check_trees(rows,*slope)
	return prod


def check_trees(rows, right, down):
	total_trees = 0
	x = 0
	y = 0
	width = len(rows[0])
	
	while(y<len(rows)):
		total_trees += (rows[y][x] == '#')
		x = (x + right) % width
		y += down
	
	return total_trees
	
					
def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		rows =  [line.strip() for line in data.readlines()]
		
		part_one_ans = part_one(rows)
		part_two_ans = part_two(rows)

		print('Day  3 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))
		

if __name__ == "__main__":
		main()