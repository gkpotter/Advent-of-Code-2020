const fs = require('fs');
const readline = require('readline');

async function loadInput() {
  const rl = readline.createInterface({
    input: fs.createReadStream(__dirname + '/input.txt')
  });

  const lines = [];
  for await (const line of rl) {
    lines.push(line);
  }
  return lines;
}

class Piece {
  constructor(num, grid) {
    this.num = num;
    this.grid = grid;
    this.d = grid.length;
  }

  top() {
    return this.grid[0];
  }

  bot() {
    return this.grid[this.d-1];
  }

  left() {
    return this.grid.map(row => row[0]);
  }

  right() {
    return this.grid.map(row => row[this.d-1]);
  }
  
  flip() {
    for (const row of this.grid) {
      row.reverse();
    }
  }

  rotate() {
    this.grid = this.grid[0].map((_, i) => this.grid.map(row => row[this.d-1-i]));
  }


  toString() {
    return String(this.num);
  }
}


function solve(board, pieces, n, row, col) {
  if ((col + n*row) < n*n) { 
    if (col == n) {
      row += 1;
      col = 0;
    }
    
    for (const piece of pieces) {
      board[row][col] = piece;
      const others = [...pieces].filter(other => other.num != piece.num);

      // check all orientations
      for (let i = 0; i < 4; i++) {
        board[row][col].rotate();
        if (check(board, row, col)) {
          if (solve(board, others, n, row, col+1)) {
            return true;
          }
        }
      }  
      
      board[row][col].flip();

      for (let i = 0; i < 4; i++) {
        board[row][col].rotate();
        if (check(board, row, col)) {
          if (solve(board, others, n, row, col+1)) {
            return true;
          }
        }
      }

      // backtrack
      board[row][col] = 0;
    }
    
    //no solution
    return false;
  }
  else {
    return true;
  }
}

function arrayEquals(a, b) {
  for (let i = 0; i < a.length; ++i) {
    if (a[i] !== b[i]) {
      return false;
    }
  }
  return true;
}

function check(board, row, col) {
  if (row > 0) {
    if (!arrayEquals(board[row][col].top(), board[row-1][col].bot())) {
      return false;
    }
  }
  if (col > 0) {
    if (!arrayEquals(board[row][col].left(), board[row][col-1].right())) {
      return false;
    }
  }
  return true;
}

function getImage(board) {
  const img = [];
  const n = board.length;
  const d = board[0][0].d;

  let line = [];
  let i = 0;

  while (i < n*d) {
    if (![0,d-1].includes(i%d)) {  
      for (const piece of board[Math.floor(i/d)]) {
        line.push(...piece.grid[i%d].slice(1, -1));
      }

      img.push([...line]);
      line = [];
    }
    i += 1;
  }

  return img;
}

function flipped(grid) {
  return grid.map(row => row.slice().reverse());
}

function rotated(grid) {
  const d = grid[0].length;
  return grid[0].map((_, i) => grid.map(row => row[d-1-i]));
}

function getOrientations(grid) {
  const grids = [];

  grids.push(grid);

  for (let i = 0; i < 3; i++) {
    grids.push(rotated(grids[i]));
  }
  
  grids.push(flipped(grids[0]));

  for (let i = 0; i < 3; i++) {
    grids.push(rotated(grids[i+4]));
  }

  return grids;
}

function partOne(pieces) {
  const n = Math.sqrt(pieces.length);
  const board = [...Array(n)].map(row => Array(n).fill(0));

  solve(board, pieces, n, 0, 0);

  return [Number(board[0][0].num)
          * Number(board[n-1][0].num)
          * Number(board[0][n-1].num)
          * Number(board[n-1][n-1].num),
          board];
}

function partTwo(board) {
  const img = getImage(board);
  const monsters = getOrientations(['                  # '.split(''),
                                    '#    ##    ##    ###'.split(''),
                                    ' #  #  #  #  #  #   '.split('')]);

  for (const monster of monsters) {
    h = monster.length;
    w = monster[0].length;
    
    for (let x = 0; x < img.length - w; x++) {
      for (let y = 0; y < img.length - h; y++) {
        let found = true;
        
        for (let i = 0; i < w; i++) {
          if (!found) {
            break;
          }
      
          for (let j = 0; j < h; j++) {
            if (![' ', img[y+j][x+i]].includes(monster[j][i])) {
              if (img[y+j][x+i] != 'O') {
                found = false;
              }
            }
          }
        }
        // mark monster
        if (found) {
          for (let i = 0; i < w; i++) {
            for(let j = 0; j < h; j++) {
              if (monster[j][i] != ' ') {
                img[y+j][x+i] = 'O';
              }
            }
          }
        }
      }
    }
  }

  let count = 0;
  for (const line of img) {
    for (const x of line) {
      if (x == '#') {
        count += 1;
      }
    }
  }

  return count;
}

async function main() {
	const start_time = process.hrtime();
  
  const lines = await loadInput();

  const pieces = [];

  let num = -1;
  let grid = [];
  
  for (line of lines) {
    if (line == '') {
      pieces.push(new Piece(num, grid));
      num = -1;
      grid = [];
    }
    else {
      if (num == -1) {
        num = Number(line.substring(5).replace(':',''));
      }
      else {
        grid.push(line.split(''));
      }
    }
  }
  
  pieces.push(new Piece(num, grid));

  const [part_one_ans, board] = partOne(pieces);
  const part_two_ans = partTwo(board);
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day 20 (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}