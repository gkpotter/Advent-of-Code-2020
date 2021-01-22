open Core

let file = "input.txt";;

let part_one nums k =
	let spoken = Int.Table.create () ~size:k in
	List.iteri nums ~f:(fun i num -> 
		Hashtbl.set spoken ~key:num ~data:(i, i)); 
	let rec take_turn i recent = 
		if i = k then recent
		else
			let (p, pp) = Hashtbl.find_exn spoken recent in
			let new_recent = (p - pp) in
			Hashtbl.update spoken new_recent ~f:(function
				| Some (prev, _) -> (i, prev)
				| None -> (i, i)
			);
			take_turn (i + 1) new_recent
	in
	take_turn (List.length nums) (List.nth_exn nums ((List.length nums) - 1))
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.create file in
	let nums = 
		input
		|> In_channel.input_line
		|> Option.value_exn 
		|> String.split ~on:','
		|> List.map ~f:int_of_string
	in
	let part_one_ans = part_one nums 2020 in
	let part_two_ans = part_one nums 30000000 in
	printf "Day 15 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
