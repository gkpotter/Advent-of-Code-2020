open Core

let file = "input.txt"

let part_one start bus_ids =
	0
;;

(* let part_two nums =

;; *)

let () = 
	let input = In_channel.create file in
	let start = int_of_string (Option.value_exn (In_channel.input_line input)) in
	let bus_ids = 
		input
		|> In_channel.input_line
		|> Option.value_exn 
		|> String.split ~on:','
		|> List.filter ~f:(String.(<>) "x")
		|> List.map ~f:int_of_string
		|> List.sort ~compare:(fun a b -> b - a)
	in
	print_s [%sexp (bus_ids: int list)];
	printf "part 1: %d\n" (part_one start bus_ids);
	(* printf "part 2: %d\n" (part_two nums) *)
;;
