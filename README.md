# Stitch Graph Processing Interface

Welcome to the **Stitch Graph Processing Interface**! This desktop application provides an intuitive way to upload an edgelist file, choose a graph algorithm to execute on the file, and input relevant parameters. The interface is designed using PyQt/PySide to ensure a seamless user experience.

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
- **Progress Tracking**: A progress section to display real-time messages during the algorithm's execution.
- **Parameter Input**: Input fields for algorithm parameters with validation to ensure correctness.
- **Aesthetic Design**: A visually appealing layout divided into input and output sections.

## Installation

### Prerequisites

- Python 3.7+
- PyQt5
- 
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
    Click on the "Run" button to execute the selected algorithm. Monitor the progress in the "Progress" section and view the results in the output section.

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

