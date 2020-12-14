def part_one(start, bus_ids):
	time = start-1
	earliest_bus_id = 0

	while earliest_bus_id == 0:
		time += 1
		for bus_id in bus_ids:
			if time % bus_id == 0:
				earliest_bus_id = bus_id
				break	

	return earliest_bus_id * (time - start)


def part_two(start, bus_ids, offsets):
	sorted_ids = sorted(bus_ids, reverse = True)
	
	x = 0
	k = 0
	step = 1
	current_id = sorted_ids[0]
	
	# solve x = -offset (mod id) by sieving
	while k < len(sorted_ids):
		if (x + offsets[current_id]) % current_id == 0:
			step *= sorted_ids[k]
			k+=1
			if k < len(sorted_ids):
				current_id = sorted_ids[k]
		else:
			x += step

	return x


def main():
  with open('input.txt','r') as data:
  	lines = data.readlines()
  	start = int(lines[0])
  	bus_ids = []
  	offsets = {}
  	offset = 0

  	for item in lines[1].split(','):
  		if item != 'x':
  			bus_id = int(item)
  			bus_ids.append(bus_id)
  			offsets[bus_id] = offset
  			
  		offset+=1

  	print('part 1: {}'.format(part_one(start, bus_ids)))
  	print('part 2: {}'.format(part_two(start, bus_ids, offsets)))


if __name__ == "__main__":
    main()