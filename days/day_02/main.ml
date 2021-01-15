open Core

type entry = {range: int*int; letter: char; password: string}
[@@deriving sexp_of]

let file = "input.txt"

let part_one entries =
	List.fold entries ~init:0 ~f:(fun total entry ->
		let count = 
			String.count entry.password ~f:(Char.(=) entry.letter)
		in
		let (min, max) = entry.range in
		if (count >= min) && (count <= max)
		then total+1
		else total
	)
;;


let part_two entries =
	List.fold entries ~init:0 ~f:(fun total entry ->
		let (a, b) = entry.range in
		let pw_list = String.to_list entry.password in
		if Bool.(<>)
			(Char.(=) (List.nth_exn pw_list (a-1)) entry.letter)
			(Char.(=) (List.nth_exn pw_list (b-1)) entry.letter)
		then total+1
		else total
	)
;;


let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let entries = 
		input
		|> List.map ~f:(String.split ~on:' ')
		|> List.map ~f:(function
			| r :: l :: password :: [] ->
				let range_list = r
					|> String.split ~on:'-'
					|> List.map ~f:int_of_string
				in
				let range = (List.nth_exn range_list 0, List.nth_exn range_list 1) in
				let letter = Char.of_string (String.strip l ~drop:(Char.(=) ':')) in
				{range; letter; password}
			| _ -> failwith "nope"
		)
	in
	let part_one_ans = part_one entries in
	let part_two_ans = part_two entries in
	printf "Day  2 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
