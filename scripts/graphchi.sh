#!/bin/bash
FILE_PATH=$1
NUM_VERTICES=$2
ITERATIONS=$3
ALGORITHM=$4
SOURCE_NODE=$5
 # Add source node as an argument

# Extract the file name from the path
FILE_NAME=$(basename $FILE_PATH)

# Start the Docker container
docker run -itd --name ligra --hostname ligra faroukdrira/ligra:1.1

# Copy the input file to the container
docker cp $FILE_PATH ligra:/$FILE_NAME

# Copy the run script to the container
docker cp scripts/run_ligra.sh ligra:/run_ligra.sh

# Make the run script executable
docker exec ligra chmod +x /run_ligra.sh

# Execute the run script inside the container
docker exec ligra /run_ligra.sh $FILE_NAME $NUM_VERTICES $ITERATIONS $ALGORITHM $SOURCE_NODE  # Add source node to the command

# Copy the output file from the container to the host
docker cp ligra:/output_ligra.txt docker_manager/output/

# Stop and remove the container
docker stop ligra
docker rm ligra
