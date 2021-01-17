open Core

let file = "input.txt"

let part_one nums =
	let num =
	 	List.find nums ~f:(fun x -> 
			List.exists nums ~f:(fun y -> y = 2020 - x)
		)
	in
	match num with
	| Some y -> y*(2020-y)
	| None -> 0
;;

let part_two nums =
	let num =
	 	List.find_map nums ~f:(fun x -> 
			let y = List.find_map nums ~f:(fun z -> 
				List.find nums ~f:(fun w -> w = 2020 - x - z)
			)
			in
			match y with
		 	| Some y -> Some (x*y*(2020-x-y))
		 	| None -> None
	 	)
	in
	match num with
	| Some num -> num
	| None -> 0
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let nums = List.map input ~f:int_of_string in
	let part_one_ans = part_one nums in
	let part_two_ans = part_two nums in
	printf "Day  1 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
