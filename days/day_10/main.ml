open Core

let file = "input.txt"

let part_one diffs =
	let ones = List.count diffs ~f:(fun d -> d = 1) in
	let threes = List.count diffs ~f:(fun d -> d = 3) in
	ones*threes
;;

let part_two diffs =
	let factor = [1;1;2;4;7;13] in
	let total, _ = List.fold diffs ~init:(1,0) ~f:(fun (total, streak) d ->
		if d = 1 then (total, streak+1)
		else (total*(List.nth_exn factor streak),0))
	in
	total
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let adapters =
		let middle = file
			|> In_channel.read_lines
			|> List.map ~f:int_of_string
			|> List.sort ~compare:(-)
		in
	([0] @ middle) @ [(List.last_exn middle)+3]
	in
	let diffs = adapters
		|> List.mapi ~f:(fun i a ->
			let prev = match (List.nth adapters (i-1)) with
				| Some x -> x
				| None -> 0
			in
			a-prev)
	in
	let part_one_ans = part_one diffs in
	let part_two_ans = part_two diffs in
	printf "Day 10 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
