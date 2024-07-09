#!/bin/bash

# Arguments
FILE_NAME=$1
NUM_VERTICES=$2
ITERATIONS=$3
ALGORITHM=$4

# Echo the parameters to check if they are passed correctly


# Conversion step
java -jar mmap.jar Convert $FILE_NAME

# Run the appropriate algorithm
case $ALGORITHM in
    "ConnectedComponent")
        java -jar mmap.jar ConnectedComponent ${FILE_NAME}.bin $NUM_VERTICES > output_mmap.txt
        ;;
    "PageRank10")
        java -jar mmap.jar PageRank ${FILE_NAME}.bin $NUM_VERTICES 10 > output_mmap.txt
        ;;
    "PageRank20")
        java -jar mmap.jar PageRank ${FILE_NAME}.bin $NUM_VERTICES 20 > output_mmap.txt
        ;;
    "TriangleCounting")
        java -jar mmap.jar TriangleCounting ${FILE_NAME}.bin $NUM_VERTICES > output_mmap.txt
        ;;
    *)
        echo "Unknown algorithm: $ALGORITHM" > output_mmap.txt
        ;;
esac
