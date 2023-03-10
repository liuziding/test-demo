from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建水平布局并设置间距为10像素
        hbox = QHBoxLayout()
        hbox.setSpacing(10)

        # 创建3个按钮并将其添加到水平布局中
        for i in range(3):
            button = QPushButton(f"Button {i+1}")
            hbox.addWidget(button)

        # 将水平布局设置为主窗口的布局
        self.setLayout(hbox)

        # 设置主窗口的固定宽度和高度
        self.setFixedSize(300, 50)

        # 设置主窗口的底部边框颜色为红色
        self.setStyleSheet("QWidget { border-bottom: 2px solid red; }")

if __name__ == '__main__':
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec()
