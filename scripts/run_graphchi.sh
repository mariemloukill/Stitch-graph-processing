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
        ./graphChi-binaries/connectedcomponenents filetype edgelist file ${FILE_NAME} >> output_graphchi.txt
        ;;
    "CommunityDetection")
       ./graphChi-binaries/communitydetection filetype edgelist file ${FILE_NAME} >> output_graphchi.txt
        ;;
    "PR10")
        ./graphChi-binaries/pagerank filetype edgelist file ${FILE_NAME} niters 10 >> output_graphchi.txt
        ;;
    "PR20")
        ./graphChi-binaries/pagerank filetype edgelist file ${FILE_NAME} niters 20 >> output_graphchi.txt
        ;;
    "TC")
       ./graphChi-binaries/TriangleCounting filetype edgelist file ${FILE_NAME} niters 10 >> output_graphchi.txt
        ;;
    "MinimumSpanningForest")
        ./graphChi-binaries/MinimumSpanningForest filetype edgelist file ${FILE_NAME} >> output_graphchi.txt
        ;;
    
    *)
        echo "Unknown algorithm: $ALGORITHM" >> output_graphchi.txt
        ;;
esac
