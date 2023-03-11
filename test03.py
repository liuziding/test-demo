import sys
from PySide6.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建上下布局管理器
        vbox = QVBoxLayout()
        self.setLayout(vbox)

        # 创建上面的QWidget对象
        top_widget = QWidget()
        top_widget.setStyleSheet("border: 2px solid black;")
        top_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        vbox.addWidget(top_widget, stretch=2)

        # 创建下面的QWidget对象
        bottom_widget = QWidget()
        bottom_widget.setStyleSheet("border: 1px solid black;")
        bottom_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        vbox.addWidget(bottom_widget, stretch=1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
