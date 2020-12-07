def part_one(seats):
	return max(get_id(seat) for seat in seats)

def part_two(seats):
	available = list(range(1,127*44+7+1))
	for seat in seats:
		available.remove(get_id(seat))
	for seat in available:
		if seat+1 not in available and seat-1 not in available:
			return seat

def get_id(seat):
	row_bin = seat[0].replace('B','1').replace('F','0')
	col_bin = seat[1].replace('R','1').replace('L','0')

	row = bin_to_dec(row_bin)
	col = bin_to_dec(col_bin)

 	return row * 8 + col

def bin_to_dec(b):
	b = str(b)
	l = len(b)
	d = 0
	for i in range(l):
		if b[i] == '1':
			d += 2**(l-i-1) 
	return d
	  			
def main():
	with open('data_5.txt','r') as data:
		seats = [ [line[:7], line[7:].strip()] 
  		for line in data.readlines()]
  	print('part 1: {}'.format(part_one(seats)))
  	print('part 2: {}'.format(part_two(seats)))
  	

if __name__ == "__main__":
    main()