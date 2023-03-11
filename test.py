from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap, QPainter, QPalette
from PySide6.QtCore import Qt, QSize

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个 QVBoxLayout 布局管理器，并将其添加到窗口中
        vbox = QVBoxLayout(self)

        # 创建一个 QLabel 控件，并将其添加到 QVBoxLayout 中
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        # 加载一张图片
        pixmap = QPixmap('images/inside.jpg')

        # 设置 QLabel 的属性，使图片自适应并填充整个控件
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.label.setMinimumSize(1, 1)  # 设置最小大小

        # 设置窗口大小和标题
        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('Example')
        self.show()

    def resizeEvent(self, event):
        # 当窗口大小改变时，调用此函数重新计算 QLabel 的大小和位置
        super().resizeEvent(event)

        # 获取窗口的大小
        size = self.label.size()

        # 使用 QPainter 绘制图片，并设置其缩放属性
        pixmap = QPixmap('images/inside.jpg')
        scaled_pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 使用 QPalette 调整背景颜色，防止缩放后出现黑边
        pal = QPalette()
        pal.setBrush(QPalette.Window, Qt.black)
        self.setPalette(pal)

        # 设置 QLabel 的背景颜色和图片
        self.label.setStyleSheet("background-color: black;")
        self.label.setPixmap(scaled_pixmap)

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()
