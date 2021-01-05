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
	for i in range(100):
		checked = []
		updated_tiles = []

		for tile in tiles:
			neighbors = get_neighbors(tile)
			b = 0
			
			for neighbor in neighbors:
				b += tiles.count(neighbor)
				if b > 2:
					break
			
			if b in [1,2]:
				updated_tiles.append(tile)

			for neighbor in neighbors:
				if neighbor not in tiles and neighbor not in checked:
					b = 0
					for other in get_neighbors(neighbor):
						b += tiles.count(other)
						if b>2:
							break

					if b == 2:
						updated_tiles.append(neighbor)
				checked.append(neighbor)


		tiles = updated_tiles

		# print('Day {}: {}'.format(i+1,len(tiles)))

	return len(tiles)


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