# Stitch Graph Processing Interface

Welcome to the **Stitch Graph Processing Interface**! This desktop application provides an intuitive way to upload an edgelist file, choose a graph algorithm to execute on the file, and input relevant parameters. The interface is designed using PyQt to ensure a seamless user experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Graph Algorithms Supported](#graph-algorithms-supported)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **User-Friendly Interface**: An easy-to-navigate GUI for uploading edgelists and running graph algorithms.
- **AI-Driven System Selection**: A customized KNN model predicts the best system to run the chosen algorithm on the given graph, considering five existing systems: GraphChi, Ligra, Mmap, GridGraph, and GPOP.
- **Context-Aware and Adaptive**: Chooses the optimal system based on the graph characteristics and the desired algorithm, supporting in-memory, out-of-core, and hybrid systems.
- **Automated Execution**: Runs a Docker container of the designated system to execute the chosen algorithm, returns the result, and then kills the container to prevent technical hassles for the user.
- **Progress Tracking**: A progress section to display real-time messages during the algorithm's execution.
- **Parameter Input**: Input fields for algorithm parameters with validation to ensure correctness.
- **Aesthetic Design**: A visually appealing layout divided into input and output sections.

## Installation

### Prerequisites

- Python 3.7+
- PyQt5 or PySide2
- Docker
- Required Python packages (specified in `requirements.txt`)

### Steps

1. **Clone the Repository**
    ```bash
    git clone https://github.com/mariemloukill/Stitch-graph-processing.git
    cd Stitch-graph-processing
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**
    ```bash
    python main.py
    ```

## Usage

1. **Launch the Application**:
    Run the `main.py` script to start the interface.

2. **Upload Edgelist**:
    Click on the "Upload Edgelist" button and select your edgelist file. Ensure the file is in the correct format.

3. **Select Algorithm and Parameters**:
    Choose the graph algorithm from the dropdown menu and input any required parameters.

4. **Run the Algorithm**:
    Click on the "Run" button to execute the selected algorithm. The KNN model will predict the best system for execution. A Docker container of the designated system will be run, the algorithm will be executed, and the results will be returned to the user. Monitor the progress in the "Progress" section and view the results in the output section.

## Graph Algorithms Supported

- **Connected Components (CC)**
- **Page Rank (PR10, PR20)**
- **Triangle Counting (TC)**
- **Minimum Spanning Forest (MinimumSpanningForest)**
- **Community Detection (CommunityDetection)**
- **BFS (BFS)**
- **Approximate Diameter (appr)**
- **Betweenness Centrality (BC)**
- **Maximal Independent Set (MIS)**
- **Radii Estimation (Radii)**

## Project Structure

Stitch-graph-processing/
* main.py # Entry point for the application
* requirements.txt # Required Python packages
* ui/
    * main_window.ui # UI design file
    * ... # Other UI related files
* algorithms/
    *connected_components.py
    *page_rank.py
    * ... # Other algorithm implementations
* utils/
    * file_validation.py # File validation utilities
    * ... # Other utility scripts
* models/
     * knn_model.pkl # Pre-trained KNN model
     * scaler.pkl # Scaler for input features
     * label_encoder_workload.pkl # Label encoder for workloads
     * ... # Other model-related files
* docker/
    * Dockerfile.graphchi # Dockerfile for GraphChi
    * Dockerfile.ligra # Dockerfile for Ligra
    * ... # Dockerfiles for other systems
* README.md # This file

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code adheres to the project's coding standards and includes relevant tests.

## Acknowledgements

- Thanks to all contributors for their support and collaboration.
- Special thanks to the PyQt communities for their excellent tools and resources.
