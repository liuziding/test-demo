# homepage.py

from PySide6.QtWidgets import *
from PySide6.QtCore import *

class DetailPage(QWidget):
    detail_signal = Signal(str)
    def __init__(self):
        super().__init__()

        # Create a label to show the detailpage content
        self.label = QLabel('This is the detailpage')

        # Create a vertical layout and add the label to it
        layout = QVBoxLayout()
        layout = QVBoxLayout()
        btn111 = QPushButton("按钮2")
        layout.addWidget(btn111)
        layout.addWidget(self.label)

        # Set the layout for the widget
        self.setLayout(layout)

        btn111.clicked.connect(self.switch_detail_page)

    def switch_detail_page(self):
        self.detail_signal.emit("detailPage")
