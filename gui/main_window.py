from PyQt5.QtWidgets import QMainWindow, QSplitter, QVBoxLayout, QWidget, QFileDialog, QLineEdit
from PyQt5.QtCore import Qt
from gui.input_section import InputSection
from gui.progress_section import ProgressSection
from gui.output_section import OutputSection
from utils.file_utils import verify_edgelist
from ml.model import predict_best_system, extract_graph_features
from docker_manager.docker_utils import run_docker_container
from gui.gui_utils import show_message_box

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stitch graph processing interface")
        self.setGeometry(100, 100, 1000, 600)  # Updated the window size

        self.setup_ui()
    
    def setup_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.splitter = QSplitter(Qt.Horizontal)
        self.layout.addWidget(self.splitter)

        self.input_section = InputSection(self)
        self.progress_section = ProgressSection(self)
        self.output_section = OutputSection(self)
        self.splitter.addWidget(self.input_section)
        self.splitter.addWidget(self.progress_section)
        self.splitter.addWidget(self.output_section)

        self.connect_signals()

    def connect_signals(self):
        self.input_section.upload_button.clicked.connect(self.upload_file)
        self.input_section.info_yes.toggled.connect(self.info_toggled)
        self.input_section.info_no.toggled.connect(self.info_toggled)
        self.input_section.algorithm_combo.currentIndexChanged.connect(self.algorithm_selected)
        self.input_section.run_button.clicked.connect(self.run_algorithm)

    def upload_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Upload Edgelist File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if file_name:
            self.input_section.file_label.setText(f"File: {file_name}")
            self.progress_section.append_progress(f"File {file_name} uploaded successfully.")
            if not verify_edgelist(file_name):
                show_message_box("Error", "The uploaded file is not a valid edgelist.")
                self.input_section.file_label.setText("No file uploaded")
                self.progress_section.append_progress("Invalid edgelist file uploaded.")

    def info_toggled(self):
        self.input_section.reset_parameters()
        if self.input_section.info_yes.isChecked():
            self.edges_input = QLineEdit()
            self.nodes_input = QLineEdit()
            self.size_input = QLineEdit()
            self.input_section.add_parameter("Number of Edges:", self.edges_input)
            self.input_section.add_parameter("Number of Nodes:", self.nodes_input)
            self.input_section.add_parameter("Size in GB:", self.size_input)
        elif self.input_section.info_no.isChecked():
            self.progress_section.append_progress("It's fine, we'll do the calculations for you.")
            self.calculate_graph_info()

    def calculate_graph_info(self):
        file_path = self.input_section.file_label.text().split(":", 1)[-1].strip()
        self.progress_section.append_progress("Calculating graph's information...")
        num_edges, num_nodes, size_gb = extract_graph_features(file_path)
        self.progress_section.append_progress(f"Calculated values - Edges: {num_edges}, Nodes: {num_nodes}, Size: {size_gb:.2f} GB")
        self.num_edges = num_edges
        self.num_nodes = num_nodes
        self.size_gb = size_gb

    def algorithm_selected(self):
        self.input_section.reset_parameters()
        index = self.input_section.algorithm_combo.currentIndex()
        if index == 2:  # Page Rank
            self.iterations_input = QLineEdit()
            self.input_section.add_parameter("Number of Iterations:", self.iterations_input)
        elif index in [6, 8]:  # BFS or Betweenness Centrality
            self.source_node_input = QLineEdit()
            self.input_section.add_parameter("Source Node:", self.source_node_input)


    def run_algorithm(self):
        file_path = self.input_section.file_label.text().split(":", 1)[-1].strip()
        num_vertices = self.num_nodes  # Dynamic parameter
        source_node = None  # Initialize source node

        selected_algorithm = self.input_section.algorithm_combo.currentText()
        iterations = None

        if selected_algorithm == "Page Rank":
            if not self.iterations_input.text().isdigit():
                show_message_box("Error", "Number of Iterations should be a valid number.")
                return
            iterations = int(self.iterations_input.text())
            if abs(iterations - 10) < abs(iterations - 20):
                selected_algorithm = "PageRank10"
            else:
                selected_algorithm = "PageRank20"
        elif selected_algorithm == "Connected Components":
            selected_algorithm = "ConnectedComponent"
        elif selected_algorithm == "Triangle Counting":
            selected_algorithm = "TriangleCounting"
        elif selected_algorithm == "BFS":
            if not self.source_node_input.text().isdigit():
                show_message_box("Error", "Source Node should be a valid number.")
                return
            source_node = self.source_node_input.text()
        elif selected_algorithm == "Betweenness Centrality":
            if not self.source_node_input.text().isdigit():
                show_message_box("Error", "Source Node should be a valid number.")
                return
            source_node = self.source_node_input.text()
            selected_algorithm = "BC"
        elif selected_algorithm == "Approximate Diameter":
            selected_algorithm = "appr"
        elif selected_algorithm == "Community Detection":
            selected_algorithm = "CommunityDetection"
        elif selected_algorithm == "Minimum Spanning Forest":
            selected_algorithm = "MinimumSpanningForest"
        elif selected_algorithm == "Maximal Independent Set":
            selected_algorithm = "MIS"
        elif selected_algorithm == "Radii Estimation":
            selected_algorithm = "Radii"

        self.progress_section.append_progress(f"Running {selected_algorithm} algorithm...")

        if self.input_section.info_yes.isChecked():
            try:
                num_edges = int(self.edges_input.text())
                num_nodes = int(self.nodes_input.text())
                size_gb = float(self.size_input.text())
                self.progress_section.append_progress(f"Using provided values - Edges: {num_edges}, Nodes: {num_nodes}, Size: {size_gb} GB")
                self.progress_section.append_progress("<font color='red'>Warning: Incorrect values may cause model errors or graph processing issues.</font>")
            except ValueError:
                show_message_box("Error", "Please enter valid numbers for edges, nodes, and size.")
                return
        else:
            num_edges = self.num_edges
            num_nodes = self.num_nodes
            size_gb = self.size_gb

        self.progress_section.append_progress("Selecting the best graph processing system...")
        system = predict_best_system(selected_algorithm, num_edges, num_nodes, size_gb)
        self.progress_section.append_progress(f"Chosen system: {system}")
        
        self.progress_section.append_progress("Starting Docker container...")
        stdout, stderr = run_docker_container(system, selected_algorithm, file_path, num_nodes, iterations, source_node)
        self.progress_section.append_progress("Docker container finished execution.")

        if stderr:
            self.progress_section.append_progress(f"Error: {stderr}")
        else:
            self.progress_section.append_progress(f"Result: {stdout}")

        # Assuming the output file is named consistently
        output_file_path = f"docker_manager/output/output_{system.lower()}.txt"
        with open(output_file_path, "r") as output_file:
            result = output_file.read()
        self.output_section.set_result(result)
