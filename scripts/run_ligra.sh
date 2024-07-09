#!/bin/bash

# Arguments
FILE_NAME=$1
NUM_VERTICES=$2
ITERATIONS=$3
ALGORITHM=$4
SOURCE_NODE=$5  # Add source node as an argument

# Conversion step
./SNAPtoAdj $FILE_NAME ${FILE_NAME}.adj
echo $FILE_NAME > output_ligra.txt
# Run the appropriate algorithm
case $ALGORITHM in
    "CC")
       ./algorithms/Components -rounds 0 ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    "MIS")
       ./algorithms/MIS -rounds 1 ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    "PR10")
        ./algorithms/PageRank -maxiters 10 -rounds 1 ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    "PR20")
        ./algorithms/PageRank -maxiters 20 -rounds 1 ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    "TC")
       ./algorithms/Triangle -rounds 1 ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    "BFS")
       ./algorithms/BFS -r $SOURCE_NODE -rounds 1  ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    "BC")
       ./algorithms/BC r $SOURCE_NODE -rounds 1  ${FILE_NAME}.adj >> output_ligra.txt
        ;;
    *)
        echo "Unknown algorithm: $ALGORITHM" >> output_ligra.txt
        ;;
esac
