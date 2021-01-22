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

function partOne(ingredient_lists, allergen_lists) {
  const all_allergens = new Set([].concat(...allergen_lists));
  const bad_foods = {};
  
  for (const allergen of all_allergens) {
    for (let k = 0; k < ingredient_lists.length; k++) {
      if (allergen_lists[k].includes(allergen)) {
        const foods = ingredient_lists[k];
        
        if (bad_foods[allergen] == undefined) {
          bad_foods[allergen] = [...foods];
        }
        else {
          bad_foods[allergen] = foods.filter(food => 
          	bad_foods[allergen].includes(food));
        }
      }
    }  
  }

  let done = false;
  while (!done) {
    done = true;

    for (const allergen of all_allergens) {
      if (bad_foods[allergen].length == 1) {
        for (const other of all_allergens) {
          if (other != allergen) {
            bad_foods[other] = [...bad_foods[other]].filter(food => 
            	!bad_foods[allergen].includes(food));
          }
        }
      }
      else {
        done = false
      }
    }
  }

  const all_bad_foods = [].concat(...Object.values(bad_foods));

  let good_count = 0;

  for (const i of ingredient_lists) {
    good_count += i.reduce((total, food) => total+!all_bad_foods.includes(food),0);
  }

  return [good_count, bad_foods]
}

function partTwo(bad_foods) {
  const ordered_bad_foods = [...Object.keys(bad_foods)];
  ordered_bad_foods.sort();

  let bad_food_list = '';
  for (const allergen of ordered_bad_foods) {
    bad_food_list += bad_foods[allergen].pop() + ',';
  }
  bad_food_list = bad_food_list.substring(0,bad_food_list.length-1);
  
  return bad_food_list;
}

async function main() {
	const start_time = process.hrtime();
  
  const lines = await loadInput();

  const ingredient_lists = [];
  const allergen_lists = [];

  for (const line of lines) {
    const items = line.replace(')','').split(' (contains ');
    const i = items[0].split(' ');
    const a = items[1].split(', ');
    
    ingredient_lists.push(i);
    allergen_lists.push(a);
  }
  const [part_one_ans, bad_foods] = partOne(ingredient_lists, allergen_lists);
  const part_two_ans = partTwo(bad_foods);
  
  const diff = process.hrtime(start_time);
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3);
  
  console.log(`Day 21  (${total_time}s)`);
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}