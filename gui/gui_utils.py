# Placeholder for any GUI-specific utility functions if needed in the future
from PyQt5.QtWidgets import QMessageBox

def show_message_box(title, message):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()
