from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QFont

class OutputSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        self.result_label = QLabel("Algorithm Output:")
        self.result_label.setFont(QFont("Helvetica", 14))
        self.layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.result_text.setFont(QFont("Helvetica", 12))
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

    def set_result(self, message):
        self.result_text.setText(message)
