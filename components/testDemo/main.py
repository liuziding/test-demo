# main.py

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from homepage import Homepage
from detailpage import Detailpage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a stacked widget
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Create the homepage and detail page
        self.homepage = Homepage()
        self.detailpage = Detailpage()

        # Add the pages to the stacked widget
        self.stacked_widget.addWidget(self.homepage)
        self.stacked_widget.addWidget(self.detailpage)

        self.homepage.line_signal.connect(self.set_line_text)

        # Create a button to switch between pages
        self.button = QPushButton('Switch')
        self.button.clicked.connect(self.switch_page)
        self.homepage.layout().addWidget(self.button)

    def set_line_text(self, param):
        print("111111")
        self.stacked_widget.setCurrentWidget(self.detailpage)

    def switch_page(self):
        # Switch between the pages
        if self.stacked_widget.currentWidget() == self.homepage:
            self.stacked_widget.setCurrentWidget(self.detailpage)
        else:
            self.stacked_widget.setCurrentWidget(self.homepage)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
