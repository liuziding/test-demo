import sys

from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication

from homePage import HomePage
from detailPage import DetailPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(1200, 800) # 设置窗口大小
        self.setup_ui()

    def setup_ui(self):
        self.my_function("1", "2")

    def my_function(self, param1, param2):
        print(param1)
        print(param2)
        print("213423")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())