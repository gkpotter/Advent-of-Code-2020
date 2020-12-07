def part_one(passports):
	total_valid = 0
	for passport in passports:
		total_valid += all_fields_present(passport)
	return total_valid
  			
def part_two(passports):
	total_valid = 0
	for passport in passports:
		total_valid += validate(passport)
	return total_valid

def all_fields_present(passport):
	fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
	for field in fields:
		if field not in passport:
			return False
	return True

def validate(passport):
	if not all_fields_present(passport):
		return False

	byr = passport['byr']
	if not (is_year(byr) and int(byr) in range(1920,2003)):
		return False

	iyr = passport['iyr']
	if not (is_year(iyr) and int(iyr) in range(2010,2021)):
		return False

	eyr = passport['eyr']
	if not (is_year(eyr) and int(eyr) in range(2020,2031)):
		return False

	hgt = passport['hgt']
	if not valid_height(hgt):
		return False

	hcl = passport['hcl']
	if not(hcl[0]=='#' and len(hcl)==7 and 
		all(is_digit(x) or x in ['a','b','c','d','e','f'] for x in hcl[1:])):
		return False

	ecl = passport['ecl']
	if ecl not in ['amb','blu','brn','gry','grn','hzl','oth']:
		return False

	pid = passport['pid']
	if not(len(pid)== 9 and all(is_digit(x) for x in pid)):
		return False

	return True

def is_year(y):
	return len(y) == 4 and all(is_digit(x) for x in y)

def is_digit(x):
	try:
		return int(x) in range(0,10)
	except:
		return False

def valid_height(hgt):
	try:
		if hgt[2:] == 'in' and int(hgt[:2]) in range(59,77):
			return True
		if hgt[3:] == 'cm' and int(hgt[:3]) in range(150,194):
			return True
		return False
	except:
		return False
	
def str_to_passport(s):
	passport = {}
	items = [x.split(':') for x in s.strip().split(' ')]
	for item in items:
		passport[item[0]] = item[1]
	return passport

def main():
  with open('data_4.txt','r') as data:
  	passports = []

  	s = ''
  	for line in data.readlines():
  		if line == '\n':
  			passports.append(str_to_passport(s))
  			s = ''
  		else:
  			s += line.strip()+' '
  	passports.append(str_to_passport(s))

  	print('part 1: {}'.format(part_one(passports)))
  	print('part 2: {}'.format(part_two(passports)))
  	

if __name__ == "__main__":
    main()