open Core

let file = "input.txt"

let score d =
	let l = List.length d in
	List.foldi d ~init:0 ~f:(fun i total card ->
		total + (l - i) * card	
	)
;;

let rec list_equals l1 l2 = 
	match (l1, l2) with
	| (hd1 :: tl1, hd2 :: tl2) ->
		if hd1 = hd2 then list_equals tl1 tl2
		else false	
	| ([], []) -> true
	| (_,_) -> false
;;

let part_one d1 d2 =
	let rec combat d1 d2 =
		match (d1, d2) with
		| (c1 :: tl1, c2 :: tl2) -> 
			if c1 > c2 
			then combat (tl1 @ [c1; c2]) tl2
			else combat tl1 (tl2 @ [c2; c1])
		| (_ :: _, []) -> score d1
		| ([], _ :: _) -> score d2
		| ([], []) -> failwith "nope"
	in
	combat d1 d2
;;

let part_two d1 d2 =
	let rec rec_combat d1 d2 prev =
		if List.mem prev (d1, d2) ~equal:(fun (p1, q1) (p2, q2) ->
			(list_equals p1 p2) && (list_equals q1 q2)
		)
		then (1, d1)
		else 
			match (d1, d2) with
			| (c1 :: tl1, c2 :: tl2) -> 
				if c1 <= (List.length tl1) && c2 <= (List.length tl2)
				then 
					let sub_winner, _ = 
						rec_combat (List.take tl1 c1) (List.take tl2 c2) []
					in
					if sub_winner = 1
					then rec_combat (tl1 @ [c1; c2]) tl2 (prev @ [(d1,d2)])
					else rec_combat tl1 (tl2 @ [c2; c1]) (prev @ [(d1,d2)])
				else
					if c1 > c2 
					then rec_combat (tl1 @ [c1; c2]) tl2 (prev @ [(d1,d2)])
					else rec_combat tl1 (tl2 @ [c2; c1]) (prev @ [(d1,d2)])
			| (_ :: _, []) -> (1, d1)
			| ([], _ :: _) -> (2, d2)
			| ([], []) -> failwith "nope"
	in
	let _, d = rec_combat d1 d2 [] in
	score d
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let (i, _) = input
		|> List.findi ~f:(fun _ line -> String.(=) line "Player 2:")
		|> Option.value_exn
	in
	let d1 = List.drop ( List.take input (i - 1) ) 1
		|> List.map ~f:int_of_string
	in
	let d2 = List.drop input (i + 1) 
		|> List.map ~f:int_of_string
	in
	let part_one_ans = part_one d1 d2 in
	let part_two_ans = part_two d1 d2 in
	printf "Day 22 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
