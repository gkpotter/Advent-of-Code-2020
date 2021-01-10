open Core
open Core_kernel

let file = "input.txt"

let part_one nums =
	List.fold_until nums
		~init:[] 
		~f:(fun prev x -> 
			if (List.length prev) < 25 
			then Continue (prev @ [x])	
			else 
				if List.for_all prev ~f:(fun n ->
						match 
							List.find prev ~f:(fun m -> n + m = x && not (n = m)) 
						with
						| Some _m -> false
						| None -> true )
				then Stop x
				else Continue ((List.tl_exn prev) @ [x]))
		~finish:(fun _prev -> 0)
;;

let part_two nums n =
	let rec search remainder summands total =
	if total < n then
		match remainder with
		| hd :: tl -> 
			search 
				tl 
				(Fdeque.enqueue summands `back hd) 
				(total + hd)
		| [] -> []
	else if total > n then 
		match (Fdeque.dequeue summands `front) with
		| Some (hd, tl) -> 
			search
				remainder 
				tl
				(total - hd)
		| None -> []
	else
		Fdeque.to_list summands
	in
	let summands =  (search nums Fdeque.empty 0) in
	let compare = (-) in
	match (
		List.max_elt summands ~compare, 
		List.min_elt summands ~compare) 
	with
		| (Some max, Some min) -> max + min
		| _ -> 0
;;

let () = 
	let start_time = Core.Unix.gettimeofday () in
	let nums = file
		|> In_channel.read_lines
		|> List.map ~f:int_of_string
	in
	let n = (part_one nums) in
	printf "day  9 (%.3fs)\n" ((Core.Unix.gettimeofday ()) -. start_time);
	printf "  part 1: %d\n" n;
	printf "  part 2: %d\n" (part_two nums n)
;;
