#!/bin/bash

tmp="test.tmp"

echo "Advent of Code 2020 (using Python)" | tee ${tmp}
echo "-------------------------" | tee -a ${tmp}

for i in $(seq -f "%02g" 1 25)
do
	python3 "days/day_${i}/main.py" | tee -a  ${tmp}
	echo "-------------------------" | tee -a  ${tmp}
done

mv ${tmp} test.log