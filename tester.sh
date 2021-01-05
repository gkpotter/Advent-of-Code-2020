#!/bin/bash

log="test.log"
echo "Advent of Code 2020 (using Python)"
echo "-------------------------" | tee ${log}

for i in $(seq -f "%02g" 1 25)
do
	python3 "day_${i}/main.py" | tee -a  ${log}
	echo "-------------------------" | tee -a  ${log}
done

# echo "Test saved to: ./${log}"