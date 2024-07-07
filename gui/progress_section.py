from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QFont

class ProgressSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout(self)

        self.progress_label = QLabel("Progress:")
        self.progress_label.setFont(QFont("Helvetica", 14))
        self.layout.addWidget(self.progress_label)

        self.progress_text = QTextEdit()
        self.progress_text.setFont(QFont("Helvetica", 14))
        self.progress_text.setReadOnly(True)
        self.layout.addWidget(self.progress_text)

    def append_progress(self, message):
        self.progress_text.append(message + "\n")
