const fs = require('fs');
const readline = require('readline');

async function loadInput() {
  const rl = readline.createInterface({
    input: fs.createReadStream('input.txt')
  });

  const lines = [];
  for await (const line of rl) {
    lines.push(line);
  }
  return lines
}

function stringToPassport(s) {
  const passport = {}
  const items = s.trim(' ').split(' ').map(x => x.split(':'))
  
  for (const item of items) {
    passport[item[0]] = item[1]
  }

  return passport
}

function allFieldsPresent(passport) {
  const fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid'];
  for (const field of fields){
    if (passport[field] == undefined) {
      return false;
    }
  }
  return true;
}

function validate(passport) {
  if (!allFieldsPresent(passport)) {
    return false
  }

  byr = passport['byr']
  if (!/^(19[2-9]\d|200[0-2])$/g.test(byr)) {
    return false
  }

  iyr = passport['iyr']
  if (!/^(201\d|2020)$/.test(iyr)) {
    return false
  }

  eyr = passport['eyr']
  if (!/^(202\d|2030)$/.test(eyr)) {
    return false
  }

  hgt = passport['hgt']
  if (!/^(1[5-8]\d|19[0-3])cm$/.test(hgt) && !/^(59|6\d|7[0-6])in$/.test(hgt)) {
    return false
  }

  hcl = passport['hcl']
  if (!/^#[0-9a-f]{6}$/.test(hcl)) {
    return false
  }

  ecl = passport['ecl']
  if (!['amb','blu','brn','gry','grn','hzl','oth'].includes(ecl)) {
    return false
  }

  pid = passport['pid']
  if (!/^\d{9}$/.test(pid)) {
    return false
  }

  return true
}

function partOne(passports) {
  let total_valid = 0
  for (const passport of passports){
    total_valid += allFieldsPresent(passport);
  }
  return total_valid
}

function partTwo(passports) {
 let total_valid = 0
  for (const passport of passports){
    total_valid += validate(passport);
  }
  return total_valid
}

async function main() {
  const start_time = process.hrtime() 
  
  const lines = await loadInput();

  const passports = []

  let s = ''
  for (const line of lines) {
    if (line == ''){
      passports.push(stringToPassport(s))
      s = ''
    }
    else {
      s += line + ' '
    }
  }
  passports.push(stringToPassport(s))

  const part_one_ans = partOne(passports)
  const part_two_ans = partTwo(passports)
  
  const diff = process.hrtime(start_time)
  const total_time = (diff[0] + diff[1]/1e9).toFixed(3)
  
  console.log(`Day  1 (${total_time}s)`)
  console.log(`  Part 1: ${part_one_ans}`);
  console.log(`  Part 2: ${part_two_ans}`);
}

if (require.main === module) {
  main();
}