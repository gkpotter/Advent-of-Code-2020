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
	let rec search start stop summands total =
	if total < n then
		match stop with
		| hd :: tl -> 
			search 
				start 
				tl 
				(Fdeque.enqueue_back summands hd) 
				(total + hd)
		| [] -> []
	else if total > n then 
		match start with
		| hd :: tl -> 
			search 
				tl 
				stop 
				(Fdeque.drop_front_exn summands) 
				(total - hd)
		| [] -> []
	else
		summands
	in
	let summands = Fdeque.to_list (search nums nums Fdeque.empty 0) in
	let compare = (-) in
	Option.value_exn(List.max_elt summands ~compare) 
		+ Option.value_exn(List.min_elt summands ~compare)  
;;

let () = 
	let nums = file
		|> In_channel.read_lines
		|> List.map ~f:int_of_string
	in
	let n = (part_one nums) in
	printf "part 1: %d\n" n;
	printf "part 2: %d\n" (part_two nums n)
;;
