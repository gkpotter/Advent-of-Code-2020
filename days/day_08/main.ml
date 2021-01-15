open Core

let file = "input.txt"

let attempt instructions = 
	let length = List.length instructions in
	let rec run steps acc i =
		if steps > length  then -1
		else if (i >= length) then acc
		else match List.nth_exn instructions i with
		| ("nop",_) -> run (steps+1)  acc    (i+1)
		| ("jmp",n) -> run (steps+1)  acc    (i+n)
		| ("acc",n) -> run (steps+1) (acc+n) (i+1)
		| (_,_) -> failwith "nope"
	in
	run 0 0 0
;;

let part_one instructions =
	let rec run seen acc i =
		if List.exists seen ~f:((=) i) then acc
		else match List.nth_exn instructions i with
		| ("nop",_) -> run (seen@[i])  acc    (i+1)
		| ("jmp",n) -> run (seen@[i])  acc    (i+n)
		| ("acc",n) -> run (seen@[i]) (acc+n) (i+1)
		| (_,_) -> failwith "nope"
	in
	run [] 0 0
;;

let part_two instructions =
	let rec fix front back =
		match back with 
		| (instr, num) :: tl ->
			let x = match instr with
				| "jmp" -> ("nop", num)
				| "nop" -> ("jmp", num)
				| _ -> (instr, num)
			in
			let acc = attempt (front@[x]@tl) in
			if acc > 0 then acc
			else fix (front@[(instr,num)]) tl
		| [] -> 0
	in
	fix [] instructions
;;


let () = 
	let start_time = Unix.gettimeofday () in
	let input = In_channel.read_lines file in
	let instructions = input
		|> List.map ~f:(fun line -> 
			match String.split line ~on:' ' with
			| instr :: num :: [] -> (instr, int_of_string num)
			| _ -> failwith "nope"
		)
	in
	let part_one_ans = part_one instructions in
	let part_two_ans = part_two instructions in
	printf "Day  8 (%.3fs)\n" ((Unix.gettimeofday ()) -. start_time);
	printf "  Part 1: %d\n" part_one_ans;
	printf "  Part 2: %d\n" part_two_ans;
;;