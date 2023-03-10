# homepage.py

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal

class Homepage(QWidget):
    line_signal = Signal(str)
    def __init__(self):
        super().__init__()

        # Create a label to show the homepage content
        self.label = QLabel('This is the homepage')

        # Create a vertical layout and add the label to it
        layout = QVBoxLayout()
        btn11 = QPushButton("按钮")
        layout.addWidget(btn11)
        layout.addWidget(self.label)

        btn11.clicked.connect(self.get_coordinate)

        # Set the layout for the widget
        self.setLayout(layout)

    def get_coordinate(self):
        self.line_signal.emit("1")
