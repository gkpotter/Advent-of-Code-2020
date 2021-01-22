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

function getTile(x1, x2, x3) {
  const x = 2*x1 - x2 + x3;
  const y =        x2 + x3;
  return [x,y];
}

function getNeighbors(x, y) {
  neighbors = [
    [x+2,y],
    [x-2,y],
    [x-1,y+1],
    [x-1,y-1],
    [x+1,y+1],
    [x+1,y-1]
  ];

  return neighbors;
}

function partOne(directions) {
  const tiles = new Set();

  for (const d of directions) {
    const coords = d.reduce(([x1,x2,x3], i) => {
      switch (i) {
        case 'e':
          return [x1+1,x2,x3];
        case 'w':
          return [x1-1,x2,x3];
        case 'n':
          return [x1,x2+1,x3];
        case 's':
          return [x1,x2-1,x3];
        case 'N':
          return [x1,x2,x3+1];
        case 'S':
          return [x1,x2,x3-1];
        default:
          return [x1,x2,x3];
      }
    },
    [0,0,0]);
    
    const tile = String(getTile(...coords));
    
    if (tiles.has(tile)) {
      tiles.delete(tile);
    }
    else {
      tiles.add(tile);
    }
  }

  return [tiles.size, tiles];
}

function partTwo(tiles) {
  for (let i = 0; i < 100; i++) {
    const updated_tiles = new Set();
    const adjacent = {};

    for (const tile of tiles) {
      const [x,y] = tile.split(',');
      const neighbors = getNeighbors(Number(x), Number(y));
      let b = 0;
      
      for (neighbor of neighbors) {
        s = String(neighbor);
        if (!tiles.has(s)) {
          if (adjacent[s] == undefined){
            adjacent[s] = 1;
          }
          else {
            adjacent[s] += 1;
          }
        }
        else {
          b += 1;
        }
      }
      
      if ([1,2].includes(b)) {
        updated_tiles.add(tile);
      }
    }

    for (const tile of Object.keys(adjacent)) {
      if (adjacent[tile] == 2){
        updated_tiles.add(tile);
      }
    }

    tiles = updated_tiles;
  }

  return tiles.size;
}

async function main() {
	const start_time = process.hrtime();
  
  const lines = await loadInput();
  const directions = lines.map(line => 
    line.replace(/ne/g,'N')
        .replace(/nw/g,'n')
        .replace(/sw/g,'S')
        .replace(/se/g,'s')
        .split('')
  );

  const [part_one_ans, tiles] = partOne(directions);
  const part_two_ans = partTwo(tiles);
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day 24 (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}