# detailpage.py

from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Detailpage(QWidget):
    def __init__(self):
        super().__init__()

        # Create a label to show the detailpage content
        self.label = QLabel('This is the detailpage')

        # Create a vertical layout and add the label to it
        layout = QVBoxLayout()
        layout.addWidget(self.label)

        # Set the layout for the widget
        self.setLayout(layout)
