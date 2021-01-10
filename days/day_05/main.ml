open Core

let file = "input.txt"

let dec_to_bin str =
	let l = String.length str in
	str
	|> String.to_list
	|> List.mapi ~f:(fun i c ->
		if Char.equal c '1'
		then Int.pow 2 (l-i-1)
		else 0
	)
	|> List.fold ~init:(0) ~f:(+)
;;

let get_id seat = 
	let seat_bin = 
		seat
		|> String.to_list
		|> List.map  ~f:(fun letter -> 
			if (Char.equal letter 'B') || (Char.equal letter 'R')
			then '1' 
			else '0'
		)
	in
	let row_bin, col_bin = List.split_n seat_bin 7
	in
	(dec_to_bin (String.of_char_list row_bin))*8 
		+ (dec_to_bin (String.of_char_list col_bin))
;;

let part_one seats =
	let max = seats
		|> List.map ~f:(get_id)
		|> List.max_elt ~compare:(-)
	in
	match max with
	| Some max -> max
	| None -> 0
;;

let part_two seats =
	let ids = List.map seats ~f:(get_id) in
	let my_seat = ids
		|> List.find ~f:(fun id ->
			not (List.mem ids (id+1) ~equal:(=)) && (List.mem ids (id+2) ~equal:(=))
		)
	in
	match my_seat with
	| Some seat -> seat
	| None -> 0
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let seats = 
		(In_channel.read_lines file) 
	in
	printf "day  5 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  part 1: %d\n" (part_one seats);
	printf "  part 2: %d\n" (part_two seats)
;;