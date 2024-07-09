import subprocess
import os

def run_docker_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def run_docker_container(system, algorithm, file_path, num_vertices, iterations=None, source_node=None):
    file_name = os.path.basename(file_path)
    local_dir = os.path.dirname(file_path)
    script_path = f'scripts/run_{system}.sh'
    main_script_path = f'scripts/{system}.sh'

    # Prepare the docker command with an optional source node parameter
    docker_command = f'bash {main_script_path} {file_path} {num_vertices} {iterations} {algorithm} {source_node}'
    stdout, stderr = run_docker_command(docker_command)
    
    # Copy the output file from the container to the local machine
    output_file = f'docker_manager/output/output_{system}.txt'
    
    return stdout, stderr
