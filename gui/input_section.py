from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QButtonGroup, QFormLayout, QComboBox, QLineEdit, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QFont

class InputSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        self.instruction_label = QLabel("Please upload the edgelist you want to process")
        self.instruction_label.setFont(QFont("Helvetica", 14))
        self.layout.addWidget(self.instruction_label)

        self.upload_button = QPushButton("Upload Edgelist File")
        self.upload_button.setFont(QFont("Helvetica", 14))
        self.layout.addWidget(self.upload_button)

        self.file_label = QLabel("No file uploaded")
        self.file_label.setFont(QFont("Helvetica", 12))
        self.layout.addWidget(self.file_label)

        self.info_label = QLabel("Do you know your graph's information?")
        self.info_label.setFont(QFont("Helvetica", 14))
        self.layout.addWidget(self.info_label)

        self.info_group = QButtonGroup(self)
        self.info_yes = QRadioButton("Yes")
        self.info_no = QRadioButton("No")
        self.info_yes.setFont(QFont("Helvetica", 14))
        self.info_no.setFont(QFont("Helvetica", 14))
        self.info_group.addButton(self.info_yes)
        self.info_group.addButton(self.info_no)
        self.layout.addWidget(self.info_yes)
        self.layout.addWidget(self.info_no)

        self.algorithm_label = QLabel("Select Algorithm:")
        self.algorithm_label.setFont(QFont("Helvetica", 14))
        self.layout.addWidget(self.algorithm_label)

        self.algorithm_combo = QComboBox()
        self.algorithm_combo.setFont(QFont("Helvetica", 14))
        self.algorithm_combo.addItems([
            "Select", 
            "Connected Components",
            "Page Rank",
            "Triangle Counting",
            "Minimum Spanning Forest",
            "Community Detection",
            "BFS",
            "Approximate Diameter",
            "Betweenness Centrality",
            "Maximal Independent Set",
            "Radii Estimation"
        ])
        self.layout.addWidget(self.algorithm_combo)

        self.parameter_layout = QFormLayout()
        self.layout.addLayout(self.parameter_layout)

        self.run_button = QPushButton("Run")
        self.run_button.setFont(QFont("Helvetica", 14))
        self.run_button.setStyleSheet("background-color: blue; color: white;")
        self.layout.addWidget(self.run_button)

        self.layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def reset_parameters(self):
        while self.parameter_layout.rowCount() > 0:
            self.parameter_layout.removeRow(0)

    def add_parameter(self, label, widget):
        self.parameter_layout.addRow(label, widget)
