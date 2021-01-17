open Core

let file = "input.txt"

let transform subject loop =
	let modulus = 20201227 in
	let rec transform subject loop value =
		if loop = 0 
		then value
		else if loop mod 2 = 1 
		then transform ((subject * subject) mod modulus)
									 (loop / 2)
									 ((value * subject) mod modulus)
		else transform ((subject * subject) mod modulus)
									 (loop / 2)
									 value
	in
	transform subject loop 1
;;

let find_loop key subject =
	let rec check loop =
		if transform subject loop = key then loop
		else check (loop+1)
	in
	check 1
;;

let part_one card_key door_key subject =
	let card_loop = find_loop card_key subject in
	let door_loop = find_loop door_key subject in
	transform (transform subject door_loop) card_loop
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.create file in
	let card_key = int_of_string (Option.value_exn (In_channel.input_line input)) in
	let door_key = int_of_string (Option.value_exn (In_channel.input_line input)) in
	let part_one_ans = part_one card_key door_key 7 in
	let part_two_ans = "⭐️" in
	printf "Day 25 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %s\n" part_two_ans
;;
