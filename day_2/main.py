def part_one(pw_data):
	total_valid = 0

	for datum in pw_data:
		count = datum['password'].count(datum['letter'])
		[m,M] = datum['range']
		total_valid += count in range(m,M+1)

	return total_valid
  			
def part_two(pw_data):
	total_valid = 0

	for datum in pw_data:
		[a,b] = datum['range']
		l = datum['letter']
		pw = datum['password']
		total_valid += (pw[a-1]==l)^(pw[b-1]==l)

	return total_valid
	  			
def main():
  with open('data_2.txt','r') as data:
  	raw_pw_data = [line.split(' ') for line in data.readlines()]
  	pw_data = []
  	
  	for raw_datum in raw_pw_data:
  		datum = {}
  		datum['range']= [int(x) for x in raw_datum[0].split('-')]
  		datum['letter'] = raw_datum[1].strip(':')
  		datum['password'] = raw_datum[2].strip('\n')
  		pw_data.append(datum)

  	print('part 1: {}'.format(part_one(pw_data)))
  	print('part 2: {}'.format(part_two(pw_data)))
  	

if __name__ == "__main__":
    main()