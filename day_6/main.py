def part_one(groups):
  total = 0
  for group in groups:
    group_str = ''
    for person in group:
      group_str += person
    total += len(set(list(group_str)))
  return total

def part_two(groups):
  total = 0
  for group in groups:
    first = set(list(group[0]))
    total += len(first.intersection(*[set(list(person)) for person in group[1:]]))

  return total

def main():
  with open('data_6.txt','r') as data:
  	groups = []

  	group = []
  	for line in data.readlines():
  		if line == '\n':
  			groups.append(group)
  			group = []
  		else:
  			group.append(line.strip())
  	groups.append(group)

  	print('part 1: {}'.format(part_one(groups)))
  	print('part 2: {}'.format(part_two(groups)))
  	

if __name__ == "__main__":
    main()