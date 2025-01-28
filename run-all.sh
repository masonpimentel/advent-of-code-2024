#!/bin/bash

# Loop from 10 to 10 (single iteration)
for i in $(seq "$1" "$2");
do
    # Navigate into the folder
    cd "$i"
    
    # Run the Python script
    echo "Day $i"
    python "$i.py"
    echo "---"
    
    # Navigate back to the parent directory
    cd ..
done