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
  return lines
}

function updateGrid(grid, rows, cols, occupied_threshold, search_visible=false) {
  let changed = false

  const updated_grid = []

  for (let i = 0; i < rows; i++) {
    updated_grid.push([...grid[i]])
  }

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < rows; j++) {
      const spot = grid[i][j]

      if (spot != '.') {
        const occupied = getOccupied([i,j], rows, cols, grid, search_visible)
        if (spot == '#' && occupied >= occupied_threshold) {
          updated_grid[i][j] = 'L'
          changed = true
        } 
        else if (spot == 'L' && occupied == 0) {
          updated_grid[i][j] = '#'
          changed = true
        }
      }
    }
  }
  
  return [updated_grid, changed]
}

function inGrid(spot, rows, cols) {
  const i = spot[0]
  const j = spot[1]
  return (i >= 0 && j >= 0 && i < rows && j < cols)
}


function add(u, v) {
  return u.map((u_i, i) => u_i + v[i])
}


function getOccupied(spot, rows, cols, grid, search_visible = false) {
  let occupied = 0

  const directions = [
    [0,1],
    [0,-1],
    [1,0],
    [1,1],
    [1,-1],
    [-1,0],
    [-1,1],
    [-1,-1],
  ]

  for (const direction of directions) {
    let neighbor = add(spot, direction)

    if (!search_visible) {
      if (inGrid(neighbor, rows, cols)) {
        occupied += (grid[neighbor[0]][neighbor[1]]=='#')
      }
    }
    else {
      let searching = true
      
      while (searching) {
        if (inGrid(neighbor,rows,cols)) {
          if (grid[neighbor[0]][neighbor[1]] != '.') {
            occupied += (grid[neighbor[0]][neighbor[1]] == '#')
            searching = false
          }
          else {
            neighbor = add(neighbor,direction)
          }
        }
        else {
          searching = false
        }
      }
    }
  }
  return occupied
}

function partOne(grid) {
  const rows = grid.length
  const cols = grid[0].length
  
  let changed = true
  while (changed) {
    [grid, changed] = updateGrid(grid, rows, cols, 4, false)
  }

  return grid.reduce((occupied, row) => {
    return occupied + row.filter(spot => spot == '#').length
  }, 0);
}

function partTwo(grid) {
  const rows = grid.length
  const cols = grid[0].length
  
  let changed = true
  while (changed) {
    [grid, changed] = updateGrid(grid, rows, cols, 5, true)
  }

  return grid.reduce((occupied, row) => {
    return occupied + row.filter(spot => spot == '#').length
  }, 0);
}

async function main() {
	const start_time = process.hrtime() 
  const lines = await loadInput();

  const grid = lines.map(line => Array.from(line))

  const part_one_ans = partOne(grid)
  const part_two_ans = partTwo(grid)
  
  const diff = process.hrtime(start_time)
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
  
  console.log(`Day 11 (${total_time}s)`)
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}