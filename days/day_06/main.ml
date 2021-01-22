open Core

let file = "input.txt"

let unique_chars str =
	let rec unique_chars2 l seen n =
		match l with
		| [] -> seen
		| hd :: tl -> (
			if List.mem seen hd ~equal:(Char.equal)
			then unique_chars2 tl seen n
			else unique_chars2 tl (seen @ [hd]) (n + 1)
		)
	in
	unique_chars2 (String.to_list str) [] 0
;;

let intersection l1 l2 =
	List.filter l1 ~f:(fun x -> (List.mem l2 x ~equal:(Char.equal)))
;;

let part_one groups =
	List.fold groups ~init:0 ~f:(fun total group ->
		let n =
			group
			|> List.fold ~init:("") ~f:(^)
			|> unique_chars
			|> List.length
		in
		total + n
	)
;;

let part_two groups =
	List.fold groups ~init:0 ~f:(fun total group ->
		let n =
			group
			|> List.map ~f:unique_chars
			|> List.fold ~init:(unique_chars (List.hd_exn group)) ~f:intersection
			|> List.length
		in
		total + n
	)
;;

let get_groups l =
	let rec get_groups2 l groups group =
		match l with
		| [] -> (groups @ [group])
		| "" :: tl -> get_groups2 tl (groups @ [group]) []
		| hd :: tl -> get_groups2 tl groups (group @ [hd])
	in 
	get_groups2 l [] []
;;

let () = 
	let start_time = Unix.gettimeofday () in
	let groups =
		get_groups (In_channel.read_lines file)
	in
	let part_one_ans = part_one groups in
	let part_two_ans = part_two groups in
	printf "Day  6 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans;
;;