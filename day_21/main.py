def part_one(ingredient_lists, allergen_lists):
	all_allergens = set.union(*[set(a) for a in allergen_lists])
	
	bad_foods = {}
	
	for allergen in all_allergens:
		foods = []
		
		for k in range(len(ingredient_lists)):
			if allergen in allergen_lists[k]:
				foods.append(set(ingredient_lists[k]))

		bad_foods[allergen] = set.intersection(*foods)
	
	
	done = False
	while not done:
		done = True
		
		for allergen in all_allergens:
			if len(bad_foods[allergen]) == 1:
				for other in all_allergens:
					if other != allergen:
						bad_foods[other] = bad_foods[other].difference(bad_foods[allergen])
			else:
				done = False
	
	all_bad_foods = set.union(*bad_foods.values())

	good_count = 0

	for i in ingredient_lists:
		good_count += len(i)
		for bad_food in all_bad_foods:
			good_count -= i.count(bad_food)

	return (good_count, bad_foods)


def part_two(bad_foods):
	bad_food_list = ''
	
	for allergen in sorted(bad_foods.keys()):
		bad_food_list += bad_foods[allergen].pop() + ','
	bad_food_list = bad_food_list[:-1]
	
	return bad_food_list


def main():
	with open('input.txt','r') as data:
		lines = [line.strip(')\n') for line in data.readlines()]
		
		ingredient_lists = []
		allergen_lists = []

		for line in lines:
			items = line.split(' (contains ')
			i = items[0].split(' ')
			a = items[1].split(', ')

			ingredient_lists.append(i)
			allergen_lists.append(a)

		part_one_ans, bad_foods = part_one(ingredient_lists, allergen_lists)
		print('part 1: {}'.format(part_one_ans))
		print('part 2: {}'.format(part_two(bad_foods)))



if __name__ == "__main__":
		main()