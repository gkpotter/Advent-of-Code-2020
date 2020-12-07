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
  with open('data_3.txt','r') as data:
  	rows =  [line.strip() for line in data.readlines()]
  	
  	print('part 1: {}'.format(part_one(rows)))
  	print('part 2: {}'.format(part_two(rows)))
  	

if __name__ == "__main__":
    main()