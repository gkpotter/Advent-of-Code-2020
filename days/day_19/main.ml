open Core

let file = "input.txt"

let check alphabet grammar word start_symbol =
	let rec check alphabet grammar word stack i =
		let word_length = List.length word in
		if (List.length stack) > word_length
		then false
		else
			match stack with 
			| top :: rest ->
			if List.mem alphabet top ~equal:(String.(=))
			then
				if i >= word_length then false
				else if String.(=) top (List.nth_exn word i) 
				then check alphabet grammar word rest (i+1)
				else false 
			else
				List.fold_until (Map.find_exn grammar top) ~init:false
				~f:(fun _ subrules -> 
					if check alphabet grammar word (subrules@rest) i 
					then Stop true
					else Continue false 
				) 
				~finish:(fun _ -> false)
			| [] -> i = word_length
	in 
	check alphabet grammar word [start_symbol] 0
;;

let part_one (alphabet : string list) (grammar : (string, string list list , 'a) Map.t ) (words : string list list) (start_symbol : string) =
	List.fold words ~init:0 ~f:(fun total word ->
 		if check alphabet grammar word start_symbol
 		then total + 1
 		else total
 	)
;;

let part_two alphabet grammar words start_symbol =
	let updated_grammar = 
		Map.update 
			(Map.update grammar 
			"8" 
			~f:(function
				| _ -> [["42"];["42"; "8"]]
			))
		"11" 
		~f:(function
			| _ -> [["42"; "31"];["42"; "11"; "31"]]
		)
	in
	List.fold words ~init:0 ~f:(fun total word ->
 		if check alphabet updated_grammar word start_symbol
 		then total + 1
 		else total
 	)
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let grammar_alist, words, _ = List.fold input ~init:([],[],false) 
		~f:(fun (grammar, words, grammar_done) line ->
			if grammar_done then
				(grammar, (words@[List.map (String.to_list line) ~f:(String.of_char)]), grammar_done)
			else
				if String.(=) line "" then 
					(grammar, words, true)
				else
					match String.split line ~on:':' with
					| rule :: b :: [] -> 
						let subrules = b
							|> String.split ~on:'|'
							|> List.map ~f:(fun item ->
								item
								|> String.strip
								|> String.strip ~drop:(Char.(=)'\"')
								|> String.split ~on:' '
							)
						in
						((grammar@[(rule, subrules)]), words, grammar_done)
					| _ -> failwith "nope"
	) 	
	in
	let grammar = Map.of_alist_exn (module String) grammar_alist in
	let alphabet = ["a"; "b"] in
	let start_symbol = "0" in
	let part_one_ans = part_one alphabet grammar words start_symbol in
	let part_two_ans = part_two alphabet grammar words start_symbol in
	printf "Day 19 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans
;;
