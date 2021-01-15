open Core

let file = "input.txt"

let check_rows rows (r, d) = 
	let width = List.length (List.hd_exn rows) in
	let rec check_rows trees (x, y) =
		match List.nth rows y with
		| None -> trees
		| Some row -> 
			let new_pos = ( (x+r) mod width, y+d) in
			match List.nth row x with
			| Some c -> check_rows (trees + (Bool.to_int (Char.(=) c '#'))) new_pos
			| None -> failwith "nope"
	in
	check_rows 0 (0, 0)
;;

let part_one rows =
	check_rows rows (3, 1)
;;


let part_two rows =
	let slopes = [(1,1); (3,1); (5,1); (7,1); (1,2)] in
	List.fold slopes ~init:1 ~f:(fun prod slope ->
		prod * (check_rows rows slope)
	)
;;


let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let rows = 
		input
		|> List.map ~f:(String.to_list)
	in
	let part_one_ans = part_one rows in
	let part_two_ans = part_two rows in
	printf "Day  3 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
