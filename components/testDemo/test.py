from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.detail_btn = QPushButton("Details")
        self.detail_btn.clicked.connect(self.show_detail)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is the main page"))
        layout.addWidget(self.detail_btn)
        self.setLayout(layout)

    def show_detail(self):
        stacked_widget.setCurrentIndex(0)

class DetailWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.back_btn = QPushButton("Back")
        self.back_btn.clicked.connect(self.show_main)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("This is the detail page"))
        layout.addWidget(self.back_btn)
        self.setLayout(layout)

    def show_main(self):
        stacked_widget.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication([])
    
    stacked_widget = QStackedWidget()
    
    stacked_widget.addWidget(DetailWindow())
    stacked_widget.addWidget(MainWindow())
    
    stacked_widget.show()
    app.exec_()
