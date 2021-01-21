open Core

let file = "input.txt"

let string_to_passport s =
	let items = s
		|> String.strip 
		|> String.split ~on:' '
		|> List.map ~f:(fun item ->
			match String.split item ~on:':' with
			| a :: b :: [] -> (a, b)
			| _ -> failwith "nope"
		)
	in
	Map.of_alist_exn (module String) items
;;

let all_fields_present passport =
  let rec check passport fields =
  	match fields with
  	| field :: tl ->
  		if (Map.mem passport field) then check passport tl
  		else false
  	| [] -> true
  in
  check passport ["byr";"iyr";"eyr";"hgt";"hcl";"ecl";"pid"]
;;

let is_valid passport = 
	if not (all_fields_present passport) then false
	else if 
		let byr = Map.find_exn passport "byr" in
		not (Str.string_match (Str.regexp "^\\(19[2-9][0-9]\\|200[0-2]\\)$") byr 0)
		then false
	else if 
		let iyr = Map.find_exn passport "iyr" in
		not (Str.string_match (Str.regexp "^\\(201[0-9]\\|2020\\)$") iyr 0)
		then false
	else if 
		let eyr = Map.find_exn passport "eyr" in
		not (Str.string_match (Str.regexp "^\\(202[0-9]\\|2030\\)$") eyr 0)
		then false
	else if 
		let hgt = Map.find_exn passport "hgt" in
		not (Str.string_match (Str.regexp "^\\(1[5-8][0-9]\\|19[0-3]\\)cm$") hgt 0)
		&& not  (Str.string_match (Str.regexp "^\\(59\\|6[0-9]\\|7[0-6]\\)in$") hgt 0)
		then false
	else if 
		let hcl = Map.find_exn passport "hcl" in
		not (Str.string_match (Str.regexp "^#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]$") hcl 0)
		then false
	else if 
		let ecl = Map.find_exn passport "ecl" in
		not (List.mem ["amb"; "blu"; "brn"; "gry"; "grn"; "hzl"; "oth"] ecl ~equal:String.(=))
		then false
	else if 
		let pid = Map.find_exn passport "pid" in
		not (Str.string_match (Str.regexp "^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$") pid 0)
		then false
	else
		true
;;

let part_one passports =
	List.fold passports ~init:0 ~f:(fun total passport ->
		if (all_fields_present passport) then (total+1)
		else total
	)
;;

let part_two passports =
	List.fold passports ~init:0 ~f:(fun total passport ->
		if (is_valid passport) then (total+1)
		else total
	)
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let passports =
		let rec parse_input lines passports s = 
			match lines with
			| line :: tl -> 
				if String.(=) line "" 
				then parse_input 
					tl
					(passports @ [(string_to_passport s)])
					""
				else
					parse_input tl passports (String.concat [s; line; " "])
			| [] -> passports @ [(string_to_passport s)]
		in
		parse_input input [] ""
	in
	let part_one_ans = part_one passports in
	let part_two_ans = part_two passports in
	printf "Day  4 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
