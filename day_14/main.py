def bitmask(value, mask):
	b = str(bin(value))[2:].zfill(len(mask))
	masked_b = [b[i] if mask[i]=='X' else mask[i] for i in range(len(mask))]
	masked_value = int(''.join(masked_b), 2)
	return masked_value


def floating_bitmask(value, mask):
	b = str(bin(value))[2:].zfill(len(mask))
	masked_b = [b[i] if mask[i]=='0' else mask[i] for i in range(len(mask))]
	floating_b = ''.join(masked_b)
	
	return resolve_floating(floating_b,[])

def resolve_floating(floating_b, b_list):
	branched = False

	for i in range(len(floating_b)):
		if floating_b[i] == 'X':
			decide_0 = floating_b[:i] + '0' + floating_b[i+1:]
			decide_1 = floating_b[:i] + '1' + floating_b[i+1:]
			resolve_floating(decide_0,b_list)
			resolve_floating(decide_1,b_list)
			branched = True
			break

	if not branched:
		b_list.append(int(floating_b,2))
	
	return b_list

def part_one(instructions):
	mem = {}
	mask = 36*'X'
	
	for instr in instructions:
		if instr[0] == 'mask':
			mask = instr[1]
		else:
			address = int(instr[0][4:-1])
			value = int(instr[1])

			masked_value = bitmask(value,mask)
			
			mem[address] = masked_value

	return sum(mem.values())


def part_two(instructions):
	mem = {}
	mask = 36*'0'
	
	for instr in instructions:
		if instr[0] == 'mask':
			mask = instr[1]
		else:
			address = int(instr[0][4:-1])
			value = int(instr[1])

			masked_addresses = floating_bitmask(address,mask)

			for masked_address in masked_addresses:
				mem[masked_address] = value

	return sum(mem.values())


def main():
  with open('input.txt','r') as data:
  	instructions = [line.strip().split(' = ') for line in data.readlines()]

  	print('part 1: {}'.format(part_one(instructions)))
  	print('part 2: {}'.format(part_two(instructions)))


if __name__ == "__main__":
    main()