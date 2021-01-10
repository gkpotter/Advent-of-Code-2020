#!/bin/bash

tmp="test.tmp"

echo "Advent of Code 2020" | tee ${tmp}
echo "" | tee ${tmp}
echo "Python" | tee ${tmp}
echo "-------------------------" | tee -a ${tmp}

for i in $(seq -f "%02g" 1 25)
do
	python3 "days/day_${i}/main.py" | tee -a  ${tmp}
	echo "-------------------------" | tee -a  ${tmp}
done

echo "" | tee -a ${tmp}
echo "OCaml" | tee -a ${tmp}
echo "-------------------------" | tee -a  ${tmp}
for i in "01" "05" "06" "09" "10" "13"
do
	cd "days/day_${i}/"
	corebuild main.native -quiet
	./main.native | tee -a  "../../${tmp}"
	corebuild -clean -quiet
	cd ../..
	echo "-------------------------" | tee -a  ${tmp}
done

mv ${tmp} test.log