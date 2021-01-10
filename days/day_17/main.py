import time
import os

directions_4d = []
directions_3d = []
offsets = [-1,0,1]

for i in offsets:
	for j in offsets:
		for k in offsets:
			for m in offsets:
				if i == 0:
					directions_3d.append([i,j,k,m])
				directions_4d.append([i,j,k,m])

directions_3d.remove([0,0,0,0])
directions_4d.remove([0,0,0,0])


def update_grid(grid, four_dim):
	d, h, l, w = grid_size(grid)
	expanded_grid = empty_grid(d+2,h+2,l+2,w+2)
	new_grid = empty_grid(d+2,h+2,l+2,w+2)

	# expand 'infinite' grid
	for t in range(d):
		for z in range(h):
			for x in range(l):
				for y in range(w):
					expanded_grid[t+1][z+1][x+1][y+1] = grid[t][z][x][y]

	# update grid
	for t in range(d+2):
		for z in range(h+2):
			for x in range(l+2):
				for y in range(w+2):
					pos = [t,z,x,y]
					neighbors = get_neighbors(expanded_grid, pos, four_dim)
					
					if expanded_grid[t][z][x][y] == 1:
						new_grid[t][z][x][y] = (neighbors in [2,3])
					else:
						new_grid[t][z][x][y] = (neighbors == 3)
					
	return new_grid


def empty_grid(d, h,l,w):
	return [[[[0 for y in range(w)] 
		for x in range(l)] 
		for z in range(h)] 
		for t in range(d)]


def in_grid(grid, pos):
	d, h, l, w = grid_size(grid)
	t, z, x, y = pos

	return ((t >= 0 and t < d) 
		and (z >= 0 and z < h) 
		and (x >= 0 and x < l) 
		and (y >= 0 and y < w))


def get_neighbors(grid, pos, four_dim):
	neighbors = 0

	directions = directions_4d if four_dim else directions_3d

	for direction in directions:
		neighbor = add(pos, direction)
		if in_grid(grid, neighbor):
			t,z,x,y = neighbor
			if grid[t][z][x][y] == 1:
				neighbors += 1

	return neighbors


def add(u,v):
	return [u[i]+v[i] for i in range(len(u))]


def grid_size(grid):
	d = len(grid)
	h = len(grid[0])
	l = len(grid[0][0])
	w = len(grid[0][0][0])

	return (d, h, l, w)


def print_grid(grid):
	d, h, l, w = grid_size(grid)
	for t in range(d):
		for z in range(h):
			print('z = {}, t = {}'.format(z-h//2, t-d//2))
			for x in range(l):
				print(''.join(['#' if point == 1 else '.' for point in grid[t][z][x]]))


def count_active(grid):
	count = 0
	d, h, l, w = grid_size(grid)

	for t in range(d):
		for z in range(h):
			for x in range(l):
				count += sum(grid[t][z][x])
	
	return count


def part_one(grid):
	for i in range(6):
		grid = update_grid(grid, four_dim = False)

	return count_active(grid)


def part_two(grid):
	for i in range(6):
		grid = update_grid(grid, four_dim = True)

	return count_active(grid)


def main():
	start_time = time.time()

	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = [line.strip() for line in data.readlines()]
		grid = []
		initial_layer = []
		
		for line in lines:
			initial_layer.append([1 if i == '#' else 0 for i in line.strip()])

		grid.append([initial_layer])

		part_one_ans = part_one(grid)
		part_two_ans = part_two(grid)

		print('Day 17 ({:,.3f}s)'.format(time.time()-start_time))
		print('  Part 1: {}'.format(part_one_ans))
		print('  Part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()