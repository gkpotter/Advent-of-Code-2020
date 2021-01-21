const fs = require('fs');
const readline = require('readline');


const directions_4d = []
const directions_3d = []
const offsets = [-1,0,1]

for (i of offsets) {
  for (j of offsets) {
    for (k of offsets) {
      for (m of offsets) {
        if (i!=0 || j!=0 || k!=0 || m!=0){
          if (i == 0) {
            directions_3d.push([i,j,k,m])
          }
          directions_4d.push([i,j,k,m])

        }
      }
    }
  }
}


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

function updateGrid(grid, four_dim) {
  const [d, h, l, w] = gridSize(grid)
  const expanded_grid = emptyGrid(d+2,h+2,l+2,w+2)
  const new_grid = emptyGrid(d+2,h+2,l+2,w+2)

  // expand 'infinite' grid
  for (let t = 0; t < d; t++) {
    for (let z = 0; z < h; z++) {
      for (let x = 0; x < l; x++) {
        for (let y = 0; y < w; y++) {
          expanded_grid[t+1][z+1][x+1][y+1] = grid[t][z][x][y]
        }
      }
    }
  }

  // update grid
  for (let t = 0; t < d+2; t++) {
    for (let z = 0; z < h+2; z++) {
      for (let x = 0; x < l+2; x++) {
        for (let y = 0; y < w+2; y++) {
          const pos = [t,z,x,y]
          const neighbors = getNeighbors(expanded_grid, pos, four_dim)
          if (expanded_grid[t][z][x][y] == 1) {
            new_grid[t][z][x][y] = Number([2,3].includes(neighbors))
          }
          else {
            new_grid[t][z][x][y] = Number(neighbors == 3)
          }
        }
      }
    }
  }
        
  return new_grid
}

function emptyGrid(d, h,l,w) {
  return [...Array(d)].map(
    t => [...Array(h)].map(
      z => [...Array(l)].map(
        x => Array(w).fill(0)
      )
    )
  )
}

function inGrid(grid, pos) {
  const [d, h, l, w] = gridSize(grid)
  const [t, z, x, y] = pos

  return ((t >= 0 && t < d) 
    && (z >= 0 && z < h) 
    && (x >= 0 && x < l) 
    && (y >= 0 && y < w))
}

function add(u,v) {
  return u.map((u_i,i) => u_i + v[i])
}

function gridSize(grid) {
  const d = grid.length
  const h = grid[0].length
  const l = grid[0][0].length
  const w = grid[0][0][0].length

  return [d, h, l, w]
}

function getNeighbors(grid, pos, four_dim) {
  let neighbors = 0

  const directions = (four_dim ? directions_4d : directions_3d)
  
  for (direction of directions) {
    const neighbor = add(pos, direction)
    if (inGrid(grid, neighbor)) {
      const [t,z,x,y] = neighbor
      if (grid[t][z][x][y] == 1) {
        neighbors += 1
      }
    }
  }

  return neighbors
}

function countActive(grid) {
  let count = 0
  const [d, h, l, w] = gridSize(grid)

  for (let t = 0; t < d; t++) {
    for (let z = 0; z < h; z++) {
      for (let x = 0; x < l; x++) {
        for (let y = 0; y < w; y++) {
          count += grid[t][z][x][y]
        }
      }
    }
  }
  
  return count
}

function printGrid(grid) {
  const [d, h, l, w] = gridSize(grid)
  for (let t = 0; t < d; t++) {
    for (let z = 0; z < h; z ++) {
      console.log(`z = ${z-h/2}, t = ${t-d/2}`)
      for (let x = 0; x < l; x++) {
        console.log(grid[t][z][x].map(p => p == 1 ? '#': '.').join(''))
      }
    }
  }
}

function partOne(grid) {
  for (let i = 0; i < 6; i++) {
    grid = updateGrid(grid, four_dim = false)
  }

  return countActive(grid)
}

function partTwo(grid) {
  for (let i = 0; i < 6; i++) {
    grid = updateGrid(grid, four_dim = true)
  }

  return countActive(grid)
}

async function main() {
	const start_time = process.hrtime() 
  
  const lines = await loadInput();
  const initial_layer = lines.map(line => 
    line.split('').map(c => c == '#' ? 1 : 0)
  );

  const grid = [[initial_layer]]

  const part_one_ans = partOne(grid)
  const part_two_ans = partTwo(grid)
  
  const diff = process.hrtime(start_time)
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
  
  console.log(`Day 17 (${total_time}s)`)
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}