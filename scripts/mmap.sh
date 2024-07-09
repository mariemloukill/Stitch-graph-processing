FILE_PATH=$1
NUM_VERTICES=$2
ITERATIONS=$3
ALGORITHM=$4
SOURCE_NODE=$5
# Extract the file name from the path
FILE_NAME=$(basename $FILE_PATH)

# Start the Docker container
docker run -itd --name mmap --hostname mmap racembenrhayem/mmap:latest

# Copy the input file to the container
docker cp $FILE_PATH mmap:/root/$FILE_NAME

# Copy the run script to the container
docker cp scripts/run_mmap.sh mmap:/root/run_mmap.sh

# Make the run script executable
docker exec mmap chmod +x /root/run_mmap.sh

# Execute the run script inside the container
docker exec mmap /root/run_mmap.sh $FILE_NAME $NUM_VERTICES $ITERATIONS $ALGORITHM

# Copy the output file from the container to the host
docker cp mmap:/root/output_mmap.txt docker_manager/output/

# Stop and remove the container
docker stop mmap
docker rm mmap