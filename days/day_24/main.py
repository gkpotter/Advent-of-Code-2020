import time
import os

def get_tile(coords):
	x = 2*coords[0] - coords[1] + coords[2]
	y =               coords[1] + coords[2]
	return (x,y)


def get_neighbors(tile):
	(x,y) = tile

	neighbors = [
		(x+2,y),
		(x-2,y),
		(x-1,y+1),
		(x-1,y-1),
		(x+1,y+1),
		(x+1,y-1),
	]

	return neighbors

def part_one(directions):
	tiles = []

	for d in directions:
		coords = [0,0,0]
		for i in d:
			if i == 'e':
				coords[0] += 1
			elif i == 'w':
				coords[0] -= 1
			
			elif i == 'n':
				coords[1] += 1
			elif i == 's':
				coords[1] -= 1
			
			elif i == 'N':
				coords[2] += 1
			elif i == 'S':
				coords[2] -= 1
			
		tile = get_tile(coords)

		if tile in tiles:
			tiles.remove(tile)
		else:
			tiles.append(tile)

	return (len(tiles),tiles)


def part_two(tiles):
	grid = {}
	for tile in tiles:
		grid[tile] = True

	for i in range(100):
		updated_grid = {}
		adjacent = {}

		for tile in grid:
			neighbors = get_neighbors(tile)
			b = 0
			
			for neighbor in neighbors:
				if neighbor not in grid:
					if neighbor in adjacent:
						adjacent[neighbor] += 1
					else:
						adjacent[neighbor] = 1
				else:
					b += 1
			
			if b in [1,2]:
				updated_grid[tile] = True

		for tile in adjacent:
			if adjacent[tile] == 2:
				updated_grid[tile] = True

		grid = updated_grid

	return len(grid)


def main():
	start_time = time.time()
	
	with open(os.path.dirname(__file__) + '/input.txt', 'r') as data:
		lines = [line.strip() for line in data.readlines()]

		directions = []

		for line in lines:
			directions.append(line.replace('ne','N').replace('nw','n').replace('se','s').replace('sw','S'))

		part_one_ans, tiles = part_one(directions)
		part_two_ans = part_two(tiles)

		print('day 24  ({:,.3f}s)'.format(time.time()-start_time))
		print('  part 1: {}'.format(part_one_ans))
		print('  part 2: {}'.format(part_two_ans))


if __name__ == "__main__":
		main()