def update_grid(grid, rows, cols, occupied_threshold, search_visible=False):
	changed = True

	while changed:
		changed = False

		updated_grid = []
		for i in range(rows):
			updated_grid.append(grid[i].copy())

		for i in range(rows):
			for j in range(cols):
				spot = grid[i][j]

				if spot != '.':
					occupied = get_occupied([i,j], rows, cols, grid, search_visible)

					if spot == '#' and occupied >= occupied_threshold:
						updated_grid[i][j] = 'L'
						changed = True
					elif spot == 'L' and occupied == 0:
						updated_grid[i][j] = '#'
						changed = True
		
		return [updated_grid, changed]


def in_grid(spot, rows, cols):
	i = spot[0]
	j = spot[1]
	return i >= 0 and j >= 0 and i < rows and j < cols


def add(u, v):
	return [u[i]+v[i] for i in range(len(u))]


def get_occupied(spot, rows, cols, grid, search_visible = False):
	occupied = 0

	directions = [
		[0,1],
		[0,-1],
		[1,0],
		[1,1],
		[1,-1],
		[-1,0],
		[-1,1],
		[-1,-1],
	]

	for direction in directions:
		neighbor = add(spot,direction)

		if not search_visible:
			if in_grid(neighbor,rows,cols):
				occupied += (grid[neighbor[0]][neighbor[1]]=='#')
		else:
			searching = True
			
			while searching:
				if in_grid(neighbor,rows,cols):
					if grid[neighbor[0]][neighbor[1]] != '.':
						occupied += (grid[neighbor[0]][neighbor[1]] == '#')
						searching = False
					else:
						neighbor = add(neighbor,direction)
				else:
					searching = False
		
	return occupied


def part_one(grid):
	rows = len(grid)
	cols = len(grid[0])
	
	changed = True
	while changed:
		grid, changed = update_grid(grid, rows, cols, 4, False)

	occupied = 0

	for i in range(rows):
		for j in range(cols):
			occupied += (grid[i][j] == '#')

	return occupied


def part_two(grid):
	rows = len(grid)
	cols = len(grid[0])
	
	changed = True
	while changed:
		grid, changed = update_grid(grid, rows, cols, 5, True)

	occupied = 0

	for i in range(rows):
		for j in range(cols):
			occupied += (grid[i][j] == '#')

	return occupied


def main():
  with open('input.txt','r') as data:
  	grid = [list(line.strip()) for line in data.readlines()]
  	
  	print('part 1: {}'.format(part_one(grid)))
  	print('part 2: {}'.format(part_two(grid)))

if __name__ == "__main__":
    main()