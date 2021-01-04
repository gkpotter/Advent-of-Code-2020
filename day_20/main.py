import math

class Piece:
	def __init__(self, num, grid):
		self.num = num
		self.grid = grid
		self.d = len(grid)

	def top(self):
		return self.grid[0]

	def bot(self):
		return self.grid[self.d-1]

	def left(self):
		return [row[0] for row in self.grid]

	def right(self):
		return [row[self.d-1] for row in self.grid]

	# flip along vertical axis
	def flip(self):
		for row in self.grid:
			row.reverse()

	# rotate 90 degrees clockwise
	def rotate(self):
		self.grid = [list(row) for row in zip(*reversed(self.grid))]

	def __str__(self):
		return str(self.grid)

	def __repr__(self):
		return str(self.num)

def solve(board, pieces, n, row, col):
	if col + n*row < n*n:	
		if col == n:
			row += 1
			col = 0
		
		for piece in pieces:
			board[row][col] = piece
			others = pieces.copy()
			others.remove(piece)

			# check all orientations
			for i in range(4):
				board[row][col].rotate()
				if check(board, row, col):
					if solve(board, others, n, row, col+1):
						return True
			
			board[row][col].flip()

			for i in range(4):
				board[row][col].rotate()
				if check(board, row, col):
					if solve(board, others, n, row, col+1):
						return True

			# backtrack
			board[row][col] = 0
		
		# no solution
		return False

	else:
		return True

def check(board, row, col):
	if row > 0:
		if board[row][col].top() != board[row-1][col].bot():
			return False
	if col > 0:
		if board[row][col].left() != board[row][col-1].right():
			return False
	return True


def part_one(pieces):
	n = int(math.sqrt(len(pieces)))
	board = [[0 for i in range(n)] for j in range(n)]

	solve(board, pieces, n, 0, 0)

	for row in board:
		print(row)

	return (int(board[0][0].num)
				* int(board[n-1][0].num)
				* int(board[0][n-1].num)
				* int(board[n-1][n-1].num))

def part_two():
	return


def main():
  with open('input.txt','r') as data:
  	lines = [line.strip() for line in data.readlines()]

  	pieces = []

  	i = 0
  	num = -1
  	grid = []
  	
  	while i < len(lines):
  		line = lines[i]

  		if line == '':
  			pieces.append(Piece(num, grid))
  			num = -1
  			grid = []
  		else:
	  		if num == -1:
	  			num = int(line[5:].strip(':'))
	  		else:
	  			grid.append(list(line))

	  	i += 1
  	
  	pieces.append(Piece(num, grid))

  	print('part 1: {}'.format(part_one(pieces)))
  	print('part 2: {}'.format(part_two()))



if __name__ == "__main__":
    main()