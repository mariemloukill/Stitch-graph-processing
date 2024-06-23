import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QLabel, QComboBox, QFileDialog, QLineEdit, QFormLayout, QSplitter, QTextEdit, QSpacerItem, QSizePolicy, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor
from utils.file_utils import verify_edgelist
from ml.model import choose_graph_system
from docker_manager.docker_utils import run_docker_container

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stitch graph processing interface")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.splitter = QSplitter(Qt.Horizontal)
        self.layout.addWidget(self.splitter)

        self.input_widget = QWidget()
        self.input_layout = QVBoxLayout(self.input_widget)
        self.splitter.addWidget(self.input_widget)

        self.instruction_label = QLabel("Please upload the edgelist you want to process")
        self.instruction_label.setFont(QFont("Helvetica", 14))
        self.input_layout.addWidget(self.instruction_label)

        self.upload_button = QPushButton("Upload Edgelist File")
        self.upload_button.setFont(QFont("Helvetica", 14))
        self.upload_button.clicked.connect(self.upload_file)
        self.input_layout.addWidget(self.upload_button)

        self.file_label = QLabel("No file uploaded")
        self.file_label.setFont(QFont("Helvetica", 12))
        self.input_layout.addWidget(self.file_label)

        self.algorithm_label = QLabel("Select Algorithm:")
        self.algorithm_label.setFont(QFont("Helvetica", 14))
        self.input_layout.addWidget(self.algorithm_label)

        self.algorithm_combo = QComboBox()
        self.algorithm_combo.setFont(QFont("Helvetica", 14))
        self.algorithm_combo.addItems(["Select", "PageRank", "BFS", "DFS"])
        self.algorithm_combo.currentIndexChanged.connect(self.algorithm_selected)
        self.input_layout.addWidget(self.algorithm_combo)

        self.parameter_layout = QFormLayout()
        self.input_layout.addLayout(self.parameter_layout)

        self.run_button = QPushButton("Run")
        self.run_button.setFont(QFont("Helvetica", 14))
        self.run_button.setStyleSheet("background-color: blue; color: white;")
        self.run_button.clicked.connect(self.run_algorithm)
        self.input_layout.addWidget(self.run_button)

        self.input_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.output_widget = QWidget()
        self.output_layout = QVBoxLayout(self.output_widget)
        self.splitter.addWidget(self.output_widget)

        self.progress_label = QLabel("Progress:")
        self.progress_label.setFont(QFont("Helvetica", 14))
        self.output_layout.addWidget(self.progress_label)

        self.progress_text = QTextEdit()
        self.progress_text.setFont(QFont("Helvetica", 12))
        self.progress_text.setReadOnly(True)
        self.output_layout.addWidget(self.progress_text)

        self.result_label = QLabel("Algorithm Output:")
        self.result_label.setFont(QFont("Helvetica", 14))
        self.output_layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.result_text.setFont(QFont("Helvetica", 12))
        self.result_text.setReadOnly(True)
        self.output_layout.addWidget(self.result_text)

    def upload_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Upload Edgelist File", "", "All Files (*);;Text Files (*.txt)", options=options
        )
        if file_name:
            self.file_label.setText(f"File: {file_name}")
            self.progress_text.append(f"File {file_name} uploaded successfully.")
            if not verify_edgelist(file_name):
                QMessageBox.critical(self, "Error", "The uploaded file is not a valid edgelist.")
                self.file_label.setText("No file uploaded")
                self.progress_text.append("Invalid edgelist file uploaded.")

    def algorithm_selected(self, index):
        while self.parameter_layout.rowCount() > 0:
            self.parameter_layout.removeRow(0)

        if index == 1:
            self.iterations_input = QLineEdit()
            self.parameter_layout.addRow("Number of Iterations:", self.iterations_input)
        elif index == 2:
            self.source_node_input = QLineEdit()
            self.parameter_layout.addRow("Source Node:", self.source_node_input)
        elif index == 3:
            self.source_node_input = QLineEdit()
            self.parameter_layout.addRow("Source Node:", self.source_node_input)

    def run_algorithm(self):
        if self.algorithm_combo.currentIndex() == 1 and not self.iterations_input.text().isdigit():
            QMessageBox.critical(self, "Error", "Number of Iterations should be a valid number.")
            return
        if (self.algorithm_combo.currentIndex() in [2, 3] and not self.source_node_input.text().isdigit()):
            QMessageBox.critical(self, "Error", "Source Node should be a valid number.")
            return

        selected_algorithm = self.algorithm_combo.currentText()
        self.progress_text.append(f"Running {selected_algorithm} algorithm...")

        self.progress_text.append("Selecting the best graph processing system...")
        system = choose_graph_system()
        self.progress_text.append(f"Chosen system: {system}")

        self.progress_text.append("Starting Docker container...")
        result = run_docker_container(system, selected_algorithm)
        self.progress_text.append("Docker container finished execution.")

        self.result_text.setText(result)
