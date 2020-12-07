import re

def part_one(rules):
	total = 0

	for bag in rules:
		total += search(bag, rules)
		
	return total

def search(bag, rules):
	others = rules[bag]

	if others == {}:
		return False
	else:
		for other in others:
			if other == "shiny gold bag":
				return True
		
		return any(search(other,rules) for other in others)

def part_two(rules):
	return count("shiny gold bag", rules)

def count(bag, rules):
	others= rules[bag]

	if others == {}:
		return 0
	else:
		return sum(rules[bag][other]*(1+count(other,rules)) for other in others)
		
def main():
  with open('data_7.txt','r') as data:
  	lines = data.readlines()
  	rules = {}

  	for line in lines:
  		bag = re.findall(r'^.*?bag', line)[0]
  		rules[bag] = {}

  		for item in re.findall(r'[1-9].*?\ bag', line):
  			l = item.split(' ')
  			num = int(l[0])
  			other = ' '.join(l[1:])
  			rules[bag][other] = num

  	print('part 1: {}'.format(part_one(rules)))
  	print('part 2: {}'.format(part_two(rules)))
		

if __name__ == "__main__":
    main()